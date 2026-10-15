import copy
import hashlib
import importlib.util
import json
import sqlite3
from contextlib import closing
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

    def test_unrelated_repository_metadata_does_not_wake_a_studied_pull_request(self):
        pull = {'number': 3, 'body': 'Implementation report', 'state': 'open',
                'head': {'ref': 'feature', 'sha': 'abc',
                         'repo': {'full_name': 'provider/api', 'pushed_at': 'before', 'stargazers_count': 1}},
                'base': {'ref': 'main', 'sha': 'def',
                         'repo': {'full_name': 'provider/api', 'pushed_at': 'before', 'stargazers_count': 1}}}
        self.tracker.cases[1]['evidence'] = [{'url': 'https://github.com/provider/api/pull/3',
                                             'data': {'pull': pull, 'checks': [{'conclusion': 'success'}]}}]
        event = {'event': 'cross-referenced', 'source': {'issue': {
            'number': 9, 'body': 'Related report', 'comments': 1,
            'repository': {'full_name': 'school/workshop', 'pushed_at': 'before', 'updated_at': 'before'}}}}
        self.tracker.cases[1]['timeline'] = [event]
        self.tracker.cases[1]['evidence'][0]['data']['timeline'] = [copy.deepcopy(event)]
        claim = self.review.claim(1)
        self.review.finish(claim['token'], 'reviewed', 'Pinned source and checks studied')
        pull['head']['repo'].update(pushed_at='unrelated push', stargazers_count=2)
        pull['base']['repo']['pushed_at'] = 'unrelated push'
        event['source']['issue']['repository']['pushed_at'] = 'unrelated push'
        self.tracker.cases[1]['evidence'][0]['data']['timeline'][0]['source']['issue']['repository']['updated_at'] = 'unrelated push'
        restarted = board.Board(self.state, self.tracker, clock=lambda: self.now)
        self.assertNotIn(1, [c['number'] for c in restarted.scan()['candidates']])
        event['source']['issue']['comments'] = 2
        self.assertEqual('changed', next(c['reason'] for c in restarted.scan()['candidates'] if c['number'] == 1))
        event['source']['issue']['comments'] = 1
        pull['head']['sha'] = 'new-code'
        self.assertEqual('changed', next(c['reason'] for c in restarted.scan()['candidates'] if c['number'] == 1))

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
        self.review.finish(claim["token"], "waiting", "Provider proof pending", follow_up=21600)
        self.assertNotIn(1, [case["number"] for case in self.review.scan()["candidates"]])
        self.now += 21601
        self.assertEqual("follow_up", self.review.scan()["candidates"][0]["reason"])
        self.tracker.cases[1]["evidence"] = [{"url": "https://github.com/provider/api/pull/3", "head": "new"}]
        self.assertEqual("changed", self.review.scan()["candidates"][0]["reason"])

    def test_waiting_and_operator_follow_ups_cannot_be_shortened_to_one_hour(self):
        for number, outcome in ((1, 'waiting'), (2, 'operator')):
            claim = self.review.claim(number)
            self.review.finish(claim['token'], outcome, 'External action pending', follow_up=3600)
        self.now += 3601
        self.assertEqual([], self.review.scan()['candidates'])
        self.now += 18000
        self.assertEqual(['follow_up', 'follow_up'], [c['reason'] for c in self.review.scan()['candidates']])

    def test_new_evidence_interrupts_the_six_hour_wait(self):
        claim = self.review.claim(1)
        self.review.finish(claim['token'], 'waiting', 'Provider evidence pending', follow_up=3600)
        self.now += 3601
        self.tracker.cases[1]['comments'].append({'id': 99, 'body': 'Provider is ready',
                                                'user': {'login': 'provider'}})
        case = next(c for c in self.review.scan()['candidates'] if c['number'] == 1)
        self.assertEqual('changed', case['reason'])

    def test_legacy_progress_upgrade_preserves_studied_and_unreviewed_material(self):
        self.tracker.cases[1]['evidence'] = [{'data': {'pull': {
            'head': {'sha': 'abc', 'repo': {'full_name': 'provider/api', 'pushed_at': 'old'}},
            'base': {'sha': 'def', 'repo': {'full_name': 'provider/api', 'pushed_at': 'old'}}}}}]
        def legacy_digest(snapshot):
            value = {**snapshot, 'missing_publications': []}
            return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True,
                                              separators=(',', ':')).encode()).hexdigest()
        second_reviewed = legacy_digest(self.tracker.cases[2])
        self.tracker.cases[2]['issue']['body'] = 'A genuinely unreviewed change'
        legacy = Path(self.directory.name) / 'legacy.sqlite3'
        with closing(sqlite3.connect(legacy)) as db, db:
            db.executescript('''
                PRAGMA user_version=1;
                CREATE TABLE meta (name TEXT PRIMARY KEY, value TEXT NOT NULL);
                CREATE TABLE cases (number INTEGER PRIMARY KEY, observed TEXT NOT NULL,
                    reviewed TEXT, snapshot TEXT NOT NULL, due REAL NOT NULL DEFAULT 0,
                    token TEXT UNIQUE, expires REAL, basis TEXT, outcome TEXT, note TEXT);
                CREATE TABLE publications (id TEXT PRIMARY KEY, number INTEGER NOT NULL,
                    token TEXT NOT NULL, basis TEXT NOT NULL, body TEXT NOT NULL, author TEXT NOT NULL,
                    status TEXT NOT NULL CHECK(status IN ('prepared','sending','sent','conflict','uncertain')),
                    comment_id INTEGER, url TEXT);
            ''')
            identity = {'repo': self.tracker.repo, 'labels': list(self.tracker.labels), 'author': self.tracker.author}
            db.execute('INSERT INTO meta VALUES (?,?)', ('identity', board.encoded(identity)))
            for number, snapshot in self.tracker.cases.items():
                observed = legacy_digest(snapshot)
                db.execute('INSERT INTO cases VALUES (?,?,?,?,?,NULL,NULL,?,?,?)',
                           (number, observed, observed if number == 1 else second_reviewed,
                            json.dumps(snapshot), self.now + 3600 if number == 1 else 0,
                            observed, 'waiting' if number == 1 else 'reviewed', 'Retained review'))
        upgraded = board.Board(legacy, self.tracker, clock=lambda: self.now)
        result = upgraded.upgrade(previous_follow_up=3600)
        self.assertEqual(2, result['upgraded'])
        self.now += 3601
        self.assertEqual([2], [c['number'] for c in upgraded.scan()['candidates']])
        first = next(c for c in upgraded.status()['cases'] if c['number'] == 1)
        self.assertEqual(1000 + 21600, first['due'])
        self.assertEqual('Retained review', first['note'])
        self.assertEqual(0, upgraded.upgrade(previous_follow_up=3600)['upgraded'])
        self.assertEqual(first['due'], next(c['due'] for c in upgraded.status()['cases'] if c['number'] == 1))

    def test_progress_upgrade_keeps_a_legacy_preparation_recoverable_once(self):
        snapshot = self.tracker.cases[1]
        snapshot['evidence'] = [{'data': {'pull': {'head': {
            'sha': 'abc', 'repo': {'full_name': 'provider/api', 'pushed_at': 'old'}}}}}]
        old = hashlib.sha256(json.dumps({**snapshot, 'missing_publications': []},
            ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode()).hexdigest()
        body = '<!-- workshop-board:legacy-answer -->\nAnswer'
        with closing(sqlite3.connect(self.state)) as db, db:
            db.execute('INSERT INTO cases VALUES (?,?,?,?,?,?,?,?,?,?)',
                       (1, old, old, json.dumps(snapshot), self.now+3600, 'old-lease', self.now-1,
                        old, 'waiting', 'Retained review'))
            db.execute('INSERT INTO publications VALUES (?,?,?,?,?,?,?,NULL,NULL)',
                       ('legacy-answer', 1, 'old-lease', old, body, self.tracker.author, 'prepared'))
        self.review.upgrade(previous_follow_up=3600)
        claim = self.review.claim(1)
        prepared = self.review.prepare(claim['token'], 'Answer', request_id='legacy-answer')
        self.assertEqual(body, prepared['body'])
        self.assertEqual('sent', self.review.publish('legacy-answer')['status'])
        self.assertEqual('sent', self.review.publish('legacy-answer')['status'])
        self.assertEqual(1, len(self.tracker.posts))

    def test_progress_upgrade_refuses_to_steal_a_live_review(self):
        claim = self.review.claim(1)
        with self.assertRaisesRegex(ValueError, 'active review'):
            self.review.upgrade(previous_follow_up=3600)
        self.assertEqual(claim['token'], self.review.renew(claim['token'])['token'])

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
        timeline[-1]['source'] = {'issue': {'body': 'Related report', 'repository': {
            'full_name': 'provider/api', 'pushed_at': 'unrelated', 'stargazers_count': 100}}}
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
        snapshot = tracker.snapshot(1)
        self.assertEqual(101, len(snapshot["timeline"]))
        linked = snapshot['timeline'][-1]['source']['issue']
        self.assertEqual({'full_name': 'provider/api'}, linked['repository'])
        self.assertEqual('Related report', linked['body'])
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
