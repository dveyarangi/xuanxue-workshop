import json
import tempfile
import unittest
import io
from pathlib import Path
from unittest.mock import patch

from tests.test_board import Tracker, board
from tests.test_telegram import TelegramPeer, message
from workshop_bot.service import Workshop
from workshop_bot.telegram import Group
from workshop_bot.tools import TurnTools, serve
from workshop_bot.telegram_api import TelegramError

NOTICE = "Проверю новый отчёт Daychi о входе через Кабинет."


class ToolTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        self.state = self.root / "private/history.sqlite3"
        self.state.parent.mkdir()
        self.context = {"root": str(self.root), "state": str(self.state), "request_id": "one",
                        "conversation": "group:10", "source": {"sender": "Anna", "message_url": "https://t.me/c/123/11"}}
        self.tools = TurnTools(self.context)
        self.tracker = Tracker()
        self.review = board.Board(self.tools.board_state, self.tracker)
        self.review.scan()

    def test_completed_monitor_review_is_reused_and_changes_are_visible(self):
        claim = self.review.claim(1)
        self.review.finish(claim["token"], "reviewed", "Evidence checked")
        initial = self.tools.board_updates()
        self.assertTrue(initial["cases"][0]["review_current"])
        self.tools.read_issue(1)
        self.tools.review_notice([1], NOTICE)
        self.assertEqual(self.tools.notice(), NOTICE)
        self.tools.finish()
        self.tools = TurnTools({**self.context, "request_id": "two"})
        self.assertEqual(self.tools.review_notice([1], NOTICE), {"status": "unchanged"})
        self.assertIsNone(self.tools.notice())
        self.tracker.cases[1]["issue"]["body"] = "Changed work"
        self.review.scan()
        changed = self.tools.board_updates()["cases"][0]
        self.assertTrue(changed["new_to_conversation"])
        self.assertFalse(changed["review_current"])

    def test_operator_request_is_text_deduplicated_and_keeps_intake_provenance(self):
        result = self.tools.request_operator("Read staging", "Need an account for the sign-in check", "access")
        self.assertEqual(result, self.tools.request_operator("Read staging", "Need an account for the sign-in check", "access"))
        text = (self.root / "docs/requests/telegram.md").read_text(encoding="utf-8")
        self.assertEqual(text.count("## Read staging"), 1)
        self.assertIn("pending", text)
        self.assertIn("https://t.me/c/123/11", text)
        self.assertIn("Anna", text)
        with self.assertRaisesRegex(ValueError, "different content"):
            self.tools.request_operator("Read staging", "Changed request", "access")

    def test_reused_review_notice_is_not_repeated_but_new_conclusion_is_visible(self):
        claim = self.review.claim(1)
        self.review.finish(claim["token"], "reviewed", "Evidence checked")
        self.tools.review_notice([1], NOTICE)
        self.tools.finish()
        other = TurnTools({**self.context, "request_id": "two"})
        self.assertEqual(other.review_notice([1], NOTICE)["status"], "unchanged")
        claim = self.review.claim(1)
        self.review.finish(claim["token"], "reviewed", "Updated conclusion")
        self.assertEqual(other.review_notice([1], "Сверю новое заключение по входу.")["status"], "queued")
        self.assertEqual(other.notice(), "Сверю новое заключение по входу.")

    def test_missing_monitor_uses_existing_discovery_without_claiming_review(self):
        other = TurnTools({**self.context, "root": str(self.root / "other")})
        self.assertFalse(other.board_updates()["monitor_available"])
        with patch.object(other, "tracker", return_value=self.tracker):
            result = other.scan_board()
        self.assertTrue(result["scan"]["complete"])
        self.assertTrue(result["board"]["monitor_available"])
        self.assertFalse(any(row["review_current"] for row in result["board"]["cases"]))

    def test_shared_report_is_supplied_as_dated_context_not_fresh_evidence(self):
        (self.root / "docs").mkdir()
        (self.root / "docs/board-review.md").write_text("# Board review\nReviewed yesterday; one case only.", encoding="utf-8")
        result = self.tools.board_updates()
        self.assertIn("one case only", result["review_report"])
        self.assertIn("not a new GitHub scan", result["source"])

    def test_fresh_read_does_not_make_older_monitor_output_new_again(self):
        self.tracker.cases[1]["issue"]["body"] = "Newer than the monitor"
        with patch.object(self.tools, "tracker", return_value=self.tracker):
            self.tools.read_issue(1, fresh=True)
        self.tools.finish()
        other = TurnTools({**self.context, "request_id": "two"})
        self.assertFalse(other.board_updates()["cases"][0]["new_to_conversation"])
        self.tracker.cases[1]["issue"]["body"] = "Another update"
        with patch.object(other, "tracker", return_value=self.tracker):
            other.read_issue(1, fresh=True)
        self.assertEqual(other.review_notice([1], NOTICE)["status"], "queued")

    def test_fresh_discussion_reads_comments_without_linked_evidence(self):
        calls = []
        def api(method, path, payload=None, **kwargs):
            calls.append(path)
            if path == "user":
                return {"login": "reviewer"}
            if "/comments?" in path:
                return [{"id": 1, "body": "old", "html_url": "https://github.com/school/workshop/issues/1#issuecomment-1"},
                        {"id": 2, "body": "Open https://staging.school.example/?join=sample-invite",
                         "html_url": "https://github.com/school/workshop/issues/1#issuecomment-2"}]
            if path == "repos/school/workshop/issues/1":
                return {"number": 1, "title": "Access", "body": "See https://github.com/school/app/pull/5",
                        "labels": [], "updated_at": "now"}
            raise AssertionError("Discussion must not expand linked evidence: " + path)
        tracker = self.tools.board.GitHub("school/workshop", ["project:workshop"], api=api)
        with patch.object(self.tools, "tracker", return_value=tracker):
            result = self.tools.read_issue(1, section="discussion", fresh=True)
        content = json.loads(result["text"])
        self.assertEqual(content["comments"][0]["id"], 2)
        self.assertIn("?join=sample-invite", content["comments"][0]["body"])
        self.assertEqual(result["source"], "GitHub")
        self.assertIn("checked_at", result)
        self.assertNotIn("version", result)
        self.assertEqual(len(calls), 4)
        self.tools.finish()
        other = TurnTools({**self.context, "request_id": "after-discussion"})
        self.assertFalse(other.board_updates()["cases"][0]["new_to_conversation"])
        with self.assertRaisesRegex(ValueError, "Read the current issue"):
            self.tools.follow_up(1, "not-a-full-evidence-version", "Do work")

    def test_protocol_rejects_unlisted_capability(self):
        incoming = io.StringIO(json.dumps({"jsonrpc": "2.0", "id": 1, "method": "tools/call",
                                          "params": {"name": "connect", "arguments": {}}}) + "\n")
        outgoing = io.StringIO()
        serve(self.context, incoming, outgoing)
        self.assertTrue(json.loads(outgoing.getvalue())["result"]["isError"])

    def test_notice_protocol_preserves_generated_text_and_first_delivery(self):
        for text in (NOTICE, "Проверю другой отчёт."):
            incoming = io.StringIO(json.dumps({'jsonrpc': '2.0', 'id': 1, 'method': 'tools/call',
                'params': {'name': 'review_notice', 'arguments': {'numbers': [1], 'text': text}}}) + '\n')
            outgoing = io.StringIO()
            serve(self.context, incoming, outgoing)
            self.assertNotIn('isError', json.loads(outgoing.getvalue())['result'])
            self.assertEqual(self.tools.notice(), NOTICE)

    def test_notice_requires_brief_nonsecret_model_text(self):
        for text in ('', '   ', 'x' * 321, None, '123456789:' + 'A' * 30):
            with self.subTest(text=text), self.assertRaises(ValueError):
                self.tools.review_notice([1], text)
        self.assertIsNone(self.tools.notice())
        incoming = io.StringIO(json.dumps({'jsonrpc': '2.0', 'id': 1, 'method': 'tools/call',
            'params': {'name': 'review_notice', 'arguments': {'numbers': [1]}}}) + '\n')
        outgoing = io.StringIO()
        serve(self.context, incoming, outgoing)
        self.assertTrue(json.loads(outgoing.getvalue())['result']['isError'])
        self.assertIsNone(self.tools.notice())

    def test_site_check_cannot_target_an_undocumented_host_or_send_credentials(self):
        (self.root / "docs").mkdir()
        (self.root / "docs/current-system.md").write_text("https://school.example/", encoding="utf-8")
        with patch("workshop_bot.tools.socket.getaddrinfo") as dns:
            for url in ("http://school.example/", "https://other.example/", "https://user:pass@school.example/",
                        "https://school.example/?token=secret"):
                with self.assertRaises(ValueError):
                    self.tools.check_site(url)
            dns.assert_not_called()
        with patch("workshop_bot.tools.socket.getaddrinfo", return_value=[(None,None,None,None,("127.0.0.1",443))]):
            with self.assertRaisesRegex(ValueError, "public"):
                self.tools.check_site("https://school.example/")

    def test_documented_hostname_dns_failure_is_a_check_result(self):
        import socket
        (self.root / "docs").mkdir()
        (self.root / "docs/current-system.md").write_text("Staging: `staging.school.example`", encoding="utf-8")
        with patch("workshop_bot.tools.socket.getaddrinfo", side_effect=socket.gaierror()):
            self.assertEqual(self.tools.check_site("https://staging.school.example")["error"], "DNS resolution failed")

    def test_uncertain_notice_is_not_repeated_and_does_not_block_main_answer(self):
        class Peer(TelegramPeer):
            def call(peer, method, **parameters):
                if method == "sendMessage" and parameters["text"] == NOTICE:
                    peer.sent.append(parameters)
                    raise TelegramError()
                return super().call(method, **parameters)

        class Agent:
            tools_enabled = True

            def chat(agent, *args, **kwargs):
                tools = TurnTools(json.loads(Path(kwargs["tool_context"]).read_text(encoding="utf-8")))
                tools.review_notice([1], NOTICE)
                kwargs["on_event"]({})
                kwargs["on_event"]({})
                return {"status": "answered", "answer": "Main answer"}

        peer = Peer([message()])
        group = Group(Workshop(self.root, self.state, Agent()), peer, -100123)
        group.start()
        group.poll_once(0)
        group.work_once()
        self.assertEqual([item["text"] for item in peer.sent], [NOTICE, "Main answer"])
        self.assertEqual(group.history()[0]["notice"]["status"], "uncertain")

    def test_quick_notice_arrives_before_full_work_and_is_not_repeated(self):
        class Agent:
            tools_enabled = True
            quick_enabled = True

            def quick(agent, *args):
                return {"route": "work", "answer": "", "reason": "project work", "notice": NOTICE}

            def chat(agent, *args, **kwargs):
                self.assertEqual([item["text"] for item in peer.sent], [NOTICE])
                self.assertEqual(args[4]["progress_notice"], NOTICE)
                tools = TurnTools(json.loads(Path(kwargs["tool_context"]).read_text(encoding="utf-8")))
                tools.review_notice([1], "A later notice")
                kwargs["on_event"]({})
                return {"status": "answered", "answer": "Main answer"}

        peer = TelegramPeer([message()])
        group = Group(Workshop(self.root, self.state, Agent()), peer, -100123)
        group.start()
        group.poll_once(0)
        group.work_once()
        self.assertEqual([item["text"] for item in peer.sent], [NOTICE, "Main answer"])

    def test_follow_up_reuses_board_publication_and_never_repeats(self):
        version = self.tools.read_issue(1)["version"]
        with patch.object(self.tools, "tracker", return_value=self.tracker):
            first = self.tools.follow_up(1, version, "Please supply the existing conformance evidence.")
            second = self.tools.follow_up(1, version, "Please supply the existing conformance evidence.")
        self.assertEqual(first["url"], second["url"])
        self.assertEqual(first["status"], "sent")
        self.assertEqual(len(self.tracker.posts), 1)

    def test_changed_issue_or_busy_reviewer_prevents_follow_up(self):
        version = self.tools.read_issue(1)["version"]
        self.tracker.cases[1]["issue"]["body"] = "New instruction"
        with patch.object(self.tools, "tracker", return_value=self.tracker):
            with self.assertRaisesRegex(ValueError, "changed"):
                self.tools.follow_up(1, version, "Old action")
        self.review.claim(1)
        with patch.object(self.tools, "tracker", return_value=self.tracker):
            with self.assertRaisesRegex(ValueError, "claimed"):
                self.tools.follow_up(1, version, "Old action")
        self.assertEqual(self.tracker.posts, [])

    def test_progress_is_separate_before_answer_and_survives_restart(self):
        observed = []

        class Agent:
            tools_enabled = True

            def chat(agent, *args, **kwargs):
                tools = TurnTools(json.loads(Path(kwargs["tool_context"]).read_text(encoding="utf-8")))
                tools.review_notice([1], NOTICE)
                kwargs["on_event"]({"type": "item.completed"})
                observed.append(len(peer.sent))
                return {"status": "answered", "answer": "Main answer"}

        app = Workshop(self.root, self.state, Agent())
        peer = TelegramPeer([message()])
        group = Group(app, peer, -100123)
        group.start()
        group.poll_once(0)
        group.work_once()
        self.assertEqual(observed, [1])
        self.assertEqual([item["text"] for item in peer.sent], [NOTICE, "Main answer"])
        reply = message(200, "Continue")
        reply["message"]["entities"] = []
        reply["message"]["reply_to_message"] = {"message_id": 101}
        self.assertEqual(group.select(reply)["conversation_id"], 11)
        group = Group(Workshop(self.root, self.state, Agent()), peer, -100123)
        group.start()
        group.work_once()
        self.assertEqual(len(peer.sent), 2)


if __name__ == "__main__":
    unittest.main()
