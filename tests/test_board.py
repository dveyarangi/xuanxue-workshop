import copy
import importlib.util
import tempfile
import unittest
from unittest.mock import Mock
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / ".agents/scripts/gw/board.py"
spec = importlib.util.spec_from_file_location("board_review", SCRIPT)
board = importlib.util.module_from_spec(spec)
spec.loader.exec_module(board)


class Tracker:
    repo = "school/workshop"
    labels = ("project:workshop",)
    author = "coordinator"

    def __init__(self):
        self.cases = {n: {"issue": {"number": n, "title": f"Case {n}", "body": "Question",
                                   "state": "open" if n == 1 else "closed",
                                   "labels": ["project:workshop"], "html_url": f"https://github.com/{self.repo}/issues/{n}"},
                          "comments": [], "timeline": [], "evidence": []} for n in (1, 2)}
        self.posts = []

    def discover(self):
        return list(self.cases)

    def snapshot(self, number, own_bodies=(), *, fresh=True):
        return copy.deepcopy(self.cases[number])

    def post(self, number, body):
        comment = {"id": 100 + len(self.posts), "body": body, "user": {"login": self.author},
                   "html_url": f"https://github.com/{self.repo}/issues/{number}#issuecomment-{100 + len(self.posts)}"}
        self.posts.append(comment)
        self.cases[number]["comments"].append(comment)
        self.cases[number]["timeline"].append({**comment, "event": "commented"})
        return comment


class BoardTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.state = Path(self.directory.name) / "state.sqlite3"
        self.tracker = Tracker()
        self.now = 1000
        self.review = board.Board(self.state, self.tracker, clock=lambda: self.now)

    def test_studied_open_and_closed_cases_are_quiet_after_restart(self):
        self.assertEqual([1, 2], [case["number"] for case in self.review.scan()["candidates"]])
        for number in (1, 2):
            claim = self.review.claim(number)
            result = self.review.finish(claim["token"], "reviewed", "Existing original-issue review applies")
            self.assertEqual("reviewed", result["status"])
        restarted = board.Board(self.state, self.tracker, clock=lambda: self.now)
        self.assertEqual([], restarted.scan()["candidates"])

    def test_publication_survives_interruption_after_remote_success(self):
        class Interruption(BaseException):
            pass

        claim = self.review.claim(1)
        operation = self.review.prepare(claim["token"], "Studied answer", request_id="recovery-proof")
        real_post = self.tracker.post

        def interrupted_post(number, body):
            real_post(number, body)
            raise Interruption()

        self.tracker.post = interrupted_post
        with self.assertRaises(Interruption):
            self.review.publish(operation["id"])
        restarted = board.Board(self.state, self.tracker, clock=lambda: self.now)
        recovered = restarted.publish(operation["id"])
        self.assertEqual("sent", recovered["status"])
        self.assertEqual(1, len(self.tracker.posts))
        self.assertEqual("reviewed", restarted.finish(claim["token"], "reviewed", "Original issue answered")["status"])
        self.assertNotIn(1, [case["number"] for case in restarted.scan()["candidates"]])

    def test_uncertain_absent_comment_is_never_blindly_resent_or_completed(self):
        claim = self.review.claim(1)
        operation = self.review.prepare(claim["token"], "Answer")
        self.tracker.post = Mock(side_effect=RuntimeError("Connection lost"))
        self.assertEqual("uncertain", self.review.publish(operation["id"])["status"])
        self.assertEqual("uncertain", self.review.publish(operation["id"])["status"])
        self.assertEqual(1, self.tracker.post.call_count)
        with self.assertRaisesRegex(ValueError, "Unconfirmed"):
            self.review.finish(claim["token"], "reviewed", "Cannot invent delivery")
        self.assertEqual("publication", self.review.scan()["candidates"][0]["reason"])

    def test_intervening_manual_reply_prevents_stale_publication_and_completion(self):
        claim = self.review.claim(1)
        operation = self.review.prepare(claim["token"], "Obsolete answer")
        self.tracker.cases[1]["comments"].append({"id": 77, "body": "Already resolved", "user": {"login": "operator"}})
        self.assertEqual("conflict", self.review.publish(operation["id"])["status"])
        self.assertEqual([], self.tracker.posts)
        self.assertEqual("conflict", self.review.finish(claim["token"], "reviewed", "Stale material")["status"])
        self.assertIn(1, [case["number"] for case in self.review.scan()["candidates"]])

    def test_lease_excludes_another_worker_and_expired_preparation_can_be_reclaimed(self):
        first = self.review.claim(1)
        second_worker = board.Board(self.state, self.tracker, clock=lambda: self.now)
        with self.assertRaisesRegex(ValueError, "already claimed"):
            second_worker.claim(1)
        operation = self.review.prepare(first["token"], "Answer", request_id="one-operation")
        self.now += 3601
        with self.assertRaisesRegex(ValueError, "expired"):
            self.review.publish(operation["id"])
        second = second_worker.claim(1)
        second_worker.prepare(second["token"], "Answer", request_id="one-operation")
        self.assertEqual("sent", second_worker.publish(operation["id"])["status"])
        self.assertEqual(1, len(self.tracker.posts))

    def test_due_condition_and_changed_linked_evidence_do_not_need_a_new_comment(self):
        claim = self.review.claim(1)
        self.review.finish(claim["token"], "waiting", "Provider proof pending", follow_up=600)
        self.assertNotIn(1, [case["number"] for case in self.review.scan()["candidates"]])
        self.now += 601
        self.assertEqual("follow_up", self.review.scan()["candidates"][0]["reason"])
        self.tracker.cases[1]["evidence"] = [{"url": "https://github.com/provider/api/pull/3", "head": "new"}]
        self.assertEqual("changed", self.review.scan()["candidates"][0]["reason"])

    def test_edits_deletions_and_missing_own_receipts_are_visible(self):
        self.tracker.cases[1]["comments"] = [{"id": 5, "body": "Before", "user": {"login": "contributor"}}]
        claim = self.review.claim(1)
        self.review.finish(claim["token"], "reviewed", "Inspected")
        self.tracker.cases[1]["comments"][0]["body"] = "After"
        self.assertEqual("changed", self.review.scan()["candidates"][0]["reason"])
        self.tracker.cases[1]["comments"].clear()
        claim = self.review.claim(1)
        operation = self.review.prepare(claim["token"], "Answer")
        self.review.publish(operation["id"])
        self.review.finish(claim["token"], "reviewed", "Answered")
        self.tracker.cases[1]["comments"].clear()
        self.tracker.cases[1]["timeline"].clear()
        self.assertEqual("changed", self.review.scan()["candidates"][0]["reason"])

    def test_inaccessible_case_is_explicit_and_other_cases_remain_available(self):
        original = self.tracker.snapshot

        def unavailable(number, **kwargs):
            if number == 2:
                raise RuntimeError("Issue unavailable")
            return original(number, **kwargs)

        self.tracker.snapshot = unavailable
        result = self.review.scan()
        self.assertFalse(result["complete"])
        self.assertEqual([1], [case["number"] for case in result["candidates"]])
        self.assertEqual(2, result["errors"][0]["number"])
        self.assertIsNone(self.review.status()["cases"][0]["reviewed"])

    def test_identifier_cannot_be_reused_for_a_different_proposal(self):
        claim = self.review.claim(1)
        self.review.prepare(claim["token"], "Original", request_id="same")
        with self.assertRaisesRegex(ValueError, "another response"):
            self.review.prepare(claim["token"], "Changed", request_id="same")

    def test_changed_proposal_requires_cancelling_the_unsent_preparation(self):
        claim = self.review.claim(1)
        original = self.review.prepare(claim["token"], "First")
        with self.assertRaisesRegex(ValueError, "pending publication"):
            self.review.prepare(claim["token"], "Second")
        self.assertEqual("conflict", board.Board(self.state).cancel(original["id"])["status"])
        replacement = self.review.prepare(claim["token"], "Second")
        self.assertEqual("sent", self.review.publish(replacement["id"])["status"])

    def test_external_comment_fixture_can_recover_a_prepared_operation(self):
        claim = self.review.claim(1)
        operation = self.review.prepare(claim["token"], "Evidence-backed answer", request_id="external-fixture")
        self.tracker.cases[1]["comments"].append({
            "id": 991, "body": "<!-- workshop-board:external-fixture -->\nEvidence-backed answer",
            "user": {"login": "coordinator"}, "html_url": "https://github.com/school/workshop/issues/1#issuecomment-991"})
        self.assertEqual("sent", self.review.publish(operation["id"])["status"])
        self.assertEqual([], self.tracker.posts)

    def test_foreign_author_cannot_forge_publication_confirmation(self):
        self.tracker.cases[1]["comments"].append({
            "id": 991, "body": "<!-- workshop-board:foreign-fixture -->\nAnswer",
            "user": {"login": "outsider"}, "html_url": "https://github.com/school/workshop/issues/1#issuecomment-991"})
        claim = self.review.claim(1)
        operation = self.review.prepare(claim["token"], "Answer", request_id="foreign-fixture")
        self.assertEqual("sent", self.review.publish(operation["id"])["status"])
        self.assertEqual(1, len(self.tracker.posts))


class TransportTests(unittest.TestCase):
    def test_all_slurped_pages_are_consumed_including_empty_pages(self):
        run = Mock(return_value=type("Response", (), {"stdout": b'[[{"id":1}],[],[{"id":2}]]'})())
        api = board.Gh(run=run)
        self.assertEqual([{"id": 1}, {"id": 2}], api("GET", "repos/a/b/issues?per_page=100", collection=""))
        arguments = run.call_args.args[0]
        self.assertIn("--paginate", arguments)
        self.assertIn("--slurp", arguments)

    def test_primary_read_failure_cannot_become_an_empty_inbox(self):
        tracker = Tracker()
        tracker.discover = Mock(side_effect=RuntimeError("Tracker unavailable"))
        with tempfile.TemporaryDirectory() as temporary:
            review = board.Board(Path(temporary) / "state.sqlite3", tracker)
            with self.assertRaisesRegex(RuntimeError, "unavailable"):
                review.scan()
            self.assertEqual([], review.status()["cases"])
            offline = board.Board(Path(temporary) / "state.sqlite3")
            self.assertTrue(offline.check()["valid"])
            self.assertEqual([], offline.status()["publications"])

    def test_live_adapter_observes_late_timeline_reports_and_changed_pr_checks(self):
        primary = {"number": 1, "title": "Review", "body": "https://github.com/provider/api/pull/3",
                   "state": "closed", "labels": [{"name": "project:workshop"}], "updated_at": "fixed",
                   "html_url": "https://github.com/school/workshop/issues/1"}
        timeline = [{"id": n, "event": "commented", "body": str(n)} for n in range(101)]
        checks = [{"id": 8, "status": "in_progress", "conclusion": None}]
        calls = []

        def api(method, path, payload=None, *, collection=None):
            calls.append((method, path, collection))
            responses = {
                "user": {"login": "coordinator"},
                "repos/school/workshop/issues?state=all&per_page=100": [primary, {**primary, "number": 2, "pull_request": {}}],
                "repos/school/workshop/issues/1": primary,
                "repos/school/workshop/issues/1/comments?per_page=100": [],
                "repos/school/workshop/issues/1/timeline?per_page=100": timeline,
                "repos/provider/api/pulls/3": {"head": {"sha": "abc"}, "state": "open"},
                "repos/provider/api/issues/3/comments?per_page=100": [],
                "repos/provider/api/pulls/3/reviews?per_page=100": [],
                "repos/provider/api/pulls/3/comments?per_page=100": [],
                "repos/provider/api/commits/abc/check-runs?per_page=100": checks,
                "repos/provider/api/commits/abc/status": {"state": "pending"}}
            return copy.deepcopy(responses[path])

        tracker = board.GitHub("school/workshop", ["project:workshop"], api=api)
        self.assertEqual([1], tracker.discover())
        self.assertEqual(101, len(tracker.snapshot(1)["timeline"]))
        with tempfile.TemporaryDirectory() as temporary:
            review = board.Board(Path(temporary) / "state.sqlite3", tracker)
            claim = review.claim(1)
            review.finish(claim["token"], "reviewed", "Checked linked source")
            checks[0].update(status="completed", conclusion="success")
            result = review.scan()
            self.assertEqual("changed", result["candidates"][0]["reason"])
        self.assertIn(("GET", "repos/school/workshop/issues/1/timeline?per_page=100", ""), calls)
        self.assertIn(("GET", "repos/provider/api/commits/abc/check-runs?per_page=100", "check_runs"), calls)

    def test_unavailable_link_is_retained_as_an_evidence_gap(self):
        tracker = board.GitHub("school/workshop", ["project:workshop"], api=Mock(return_value={"login": "coordinator"}))
        primary = {"number": 1, "title": "Review", "body": "https://github.com/provider/api/commit/deadbeef",
                   "state": "open", "labels": [{"name": "project:workshop"}], "html_url": "url"}

        def api(method, path, payload=None, *, collection=None):
            if path.startswith("repos/provider"):
                raise RuntimeError("Artifact inaccessible")
            return [] if collection is not None else primary

        tracker.api = api
        result = tracker.snapshot(1)
        self.assertTrue(result["evidence"][0]["unavailable"])
        self.assertIn("inaccessible", result["evidence"][0]["reason"])

    def test_short_issue_references_are_observed_as_dependencies(self):
        primary = {"number": 1, "title": "Consumer", "body": "Blocked by #5 and provider/api#7.",
                   "labels": [{"name": "project:workshop"}], "state": "open", "html_url": "url"}
        linked = {"number": 5, "title": "Provider", "body": "Evidence", "labels": [], "state": "open", "html_url": "url"}

        def api(method, path, payload=None, *, collection=None):
            if path == "user":
                return {"login": "coordinator"}
            if collection is not None:
                return []
            return primary if path == "repos/school/workshop/issues/1" else linked

        result = board.GitHub("school/workshop", ["project:workshop"], api=api).snapshot(1)
        self.assertEqual({"https://github.com/school/workshop/issues/5", "https://github.com/provider/api/issues/7"},
                         {item["url"] for item in result["evidence"]})


if __name__ == "__main__":
    unittest.main()
