import json
import tempfile
import unittest
import threading
from pathlib import Path

from workshop_bot.service import Workshop
from workshop_bot.telegram import Group
from workshop_bot.telegram_api import TelegramError
from workshop_bot.telegram_runtime import serve, receiver_lease


class TelegramPeer:
    def __init__(self, updates=()):
        self.updates = list(updates)
        self.sent = []

    def call(self, method, **parameters):
        if method == "getMe":
            return {"id": 42, "is_bot": True, "username": "workshop_bot", "can_read_all_group_messages": True}
        if method == "getWebhookInfo":
            return {"url": ""}
        if method == "getChat":
            return {"id": -100123, "type": "supergroup"}
        if method == "getChatMember":
            return {"status": "member"}
        if method == "getUpdates":
            result, self.updates = self.updates, []
            return result
        if method == "sendMessage":
            self.sent.append(parameters)
            return {"message_id": 100 + len(self.sent), "chat": {"id": parameters["chat_id"]}}
        raise AssertionError(method)


def message(update=1, text="@workshop_bot Кто владеет проектами?", chat=-100123):
    return {"update_id": update, "message": {
        "message_id": update + 10, "date": 1791780000,
        "chat": {"id": chat, "type": "supergroup"},
        "from": {"id": 7, "first_name": "Anna", "username": "anna"},
        "message_thread_id": 9, "text": text,
        "entities": [{"type": "mention", "offset": 0, "length": 13}]}}


class GroupTests(unittest.TestCase):
    def test_process_interruption_during_send_is_visible_after_restart(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)

            class Interrupted(TelegramPeer):
                def call(self, method, **parameters):
                    if method == "sendMessage":
                        raise SystemExit("Interrupted before local acknowledgement")
                    return super().call(method, **parameters)

            app = Workshop(root, root / "state.sqlite3", lambda context: {
                "disposition": "answer", "answer": "Ответ", "reason": "", "sources": [], "edit": None})
            group = Group(app, Interrupted([message()]), -100123)
            group.start()
            group.poll_once(0)
            with self.assertRaises(SystemExit):
                group.work_once()
            peer = TelegramPeer()
            resumed = Group(app, peer, -100123)
            resumed.start()
            self.assertFalse(resumed.work_once())
            self.assertEqual(resumed.history()[0]["status"], "uncertain")
            self.assertEqual(peer.sent, [])

    def test_polling_retains_the_next_request_while_codex_is_busy(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            entered, received, release, stop = (threading.Event() for _ in range(4))
            errors = []

            def agent(context):
                entered.set()
                self.assertTrue(release.wait(5))
                return {"disposition": "answer", "answer": "Ответ", "reason": "", "sources": [], "edit": None}

            class Arrivals(TelegramPeer):
                polls = 0

                def call(self, method, **parameters):
                    if method == "getUpdates":
                        self.polls += 1
                        if self.polls == 1:
                            return [message()]
                        if self.polls == 2:
                            entered.wait(5)
                            return [message(2)]
                        received.set()
                        stop.wait(0.02)
                        return []
                    return super().call(method, **parameters)

            group = Group(Workshop(root, root / "state.sqlite3", agent), Arrivals(), -100123)

            def run():
                try:
                    serve(group, stop=stop)
                except BaseException as error:
                    errors.append(error)

            worker = threading.Thread(target=run)
            worker.start()
            try:
                self.assertTrue(received.wait(5))
                self.assertEqual(len(group.history()), 2)
                self.assertEqual(group.history()[1]["status"], "queued")
                with self.assertRaises((RuntimeError, OSError)):
                    with receiver_lease(group.workshop.state):
                        self.fail("Second receiver acquired the same history")
            finally:
                stop.set()
                release.set()
                worker.join(6)
            self.assertFalse(worker.is_alive())
            self.assertEqual(errors, [])

    def test_existing_webhook_stops_start_without_deleting_it(self):
        with tempfile.TemporaryDirectory() as temporary:
            class ExistingReceiver(TelegramPeer):
                def call(self, method, **parameters):
                    if method == "getWebhookInfo":
                        return {"url": "https://existing.example/webhook"}
                    return super().call(method, **parameters)

            root = Path(temporary)
            group = Group(Workshop(root, root / "state.sqlite3", None), ExistingReceiver(), -100123)
            with self.assertRaisesRegex(ValueError, "webhook"):
                group.start()

    def test_bare_reference_invites_a_question_without_calling_the_agent(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            app = Workshop(root, root / "state.sqlite3", lambda context: self.fail("No question to answer"))
            peer = TelegramPeer([message(text="@workshop_bot")])
            group = Group(app, peer, -100123)
            group.start()
            group.poll_once(0)
            group.work_once()
            self.assertIn("Задайте", peer.sent[0]["text"])

    def test_long_reply_survives_rate_limit_without_repeating_confirmed_parts(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            answer = "😀" * 2400

            class Limited(TelegramPeer):
                limited = False

                def call(self, method, **parameters):
                    if method == "sendMessage" and len(self.sent) == 1 and not self.limited:
                        self.limited = True
                        raise TelegramError(429, retry_after=0)
                    return super().call(method, **parameters)

            app = Workshop(root, root / "state.sqlite3", lambda context: {
                "disposition": "answer", "answer": answer, "reason": "", "sources": [], "edit": None})
            peer = Limited([message()])
            group = Group(app, peer, -100123)
            group.start()
            group.poll_once(0)
            for _ in range(5):
                group.work_once()
            self.assertEqual(group.history()[0]["status"], "sent")
            self.assertTrue(peer.limited)
            self.assertEqual("".join(item["text"] for item in peer.sent), answer)
            self.assertTrue(all(len(item["text"].encode("utf-16-le")) // 2 <= 4096 for item in peer.sent))

    def test_only_addressed_group_text_is_retained_and_hidden_links_work_after_emoji(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            contexts = []

            def agent(context):
                contexts.append(context)
                return {"disposition": "answer", "answer": "Ответ", "reason": "", "sources": [], "edit": None}

            ordinary = message(1, "PRIVATE ordinary talk")
            ordinary["message"]["entities"] = []
            elsewhere = message(2, "@workshop_bot PRIVATE other group", chat=-100999)
            linked = message(3)
            linked["message"].pop("text")
            linked["message"].pop("entities")
            linked["message"]["caption"] = "😀 бот, что готово?"
            linked["message"]["caption_entities"] = [{"type": "text_link", "offset": 3, "length": 3,
                                                      "url": "https://t.me/workshop_bot"}]
            linked["message"]["reply_to_message"] = {"text": "PRIVATE unrelated quote"}
            spoof = message(4)
            spoof["message"]["entities"] = [{"type": "text_link", "offset": 0, "length": 13,
                                              "url": "https://t.me.evil.example/workshop_bot"}]
            app = Workshop(root, root / "state.sqlite3", agent)
            group = Group(app, TelegramPeer([ordinary, elsewhere, linked, spoof]), -100123)
            group.start()
            group.poll_once(0)
            while group.work_once():
                pass
            self.assertEqual(len(contexts), 1)
            self.assertEqual(len(group.history()), 1)
            self.assertNotIn("PRIVATE", json.dumps([contexts, group.history(), app.history()]))

    def test_uncertain_send_is_not_repeated_after_restart_and_next_request_runs(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            calls = []

            def agent(context):
                calls.append(context)
                return {"disposition": "answer", "answer": "Ответ", "reason": "", "sources": [], "edit": None}

            class LostAcknowledgement(TelegramPeer):
                def call(self, method, **parameters):
                    if method == "sendMessage":
                        self.sent.append(parameters)
                        raise TimeoutError("Response lost")
                    return super().call(method, **parameters)

            app = Workshop(root, root / "state.sqlite3", agent)
            peer = LostAcknowledgement([message()])
            group = Group(app, peer, -100123)
            group.start()
            group.poll_once(0)
            self.assertTrue(group.work_once())
            self.assertEqual(group.history()[0]["status"], "uncertain")
            resumed_peer = TelegramPeer([message(), message(2)])
            resumed = Group(app, resumed_peer, -100123)
            resumed.start()
            resumed.poll_once(0)
            self.assertTrue(resumed.work_once())
            self.assertFalse(resumed.work_once())
            self.assertEqual(len(calls), 2)
            self.assertEqual(len(resumed_peer.sent), 1)
            self.assertEqual([row["status"] for row in resumed.history()], ["uncertain", "sent"])

    def test_group_request_gets_a_reply_and_inspectable_history(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            calls = []

            def agent(context):
                calls.append(context)
                return {"disposition": "answer", "answer": "Проекты отвечают за свою реализацию.",
                        "reason": "", "sources": [], "edit": None}

            app = Workshop(root, root / "state.sqlite3", agent)
            peer = TelegramPeer([message()])
            group = Group(app, peer, -100123)
            group.start()
            group.poll_once(timeout=0)
            self.assertTrue(group.work_once())
            self.assertEqual(len(calls), 1)
            self.assertEqual(peer.sent[0]["reply_parameters"], {"message_id": 11})
            self.assertEqual(peer.sent[0]["message_thread_id"], 9)
            self.assertEqual(peer.sent[0]["chat_id"], -100123)
            history = group.history()
            self.assertEqual(history[0]["status"], "sent")
            self.assertEqual(history[0]["sender"]["id"], 7)
            self.assertEqual(history[0]["message_url"], "https://t.me/c/123/11")
            self.assertIn("Проекты отвечают", history[0]["result"]["answer"])


if __name__ == "__main__":
    unittest.main()
