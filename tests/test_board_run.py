import importlib.util
import tempfile
import unittest
from unittest.mock import Mock, patch
from pathlib import Path


SCRIPTS = Path(__file__).resolve().parents[1] / ".agents/scripts/gw"


def load(name):
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class ReportTests(unittest.TestCase):
    def test_invalid_replacement_cannot_destroy_existing_report(self):
        report = load("board_report")
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "report.md"
            original = report.initial_report()
            report.write_report(path, original, expected="absent")
            with self.assertRaisesRegex(ValueError, "report"):
                report.write_report(path, "# Empty", expected=report.version(path))
            self.assertEqual(original, path.read_text(encoding="utf-8"))

    def test_stale_write_is_refused_and_failure_preserves_review_content(self):
        report = load("board_report")
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "report.md"
            original = report.initial_report().replace("Consult the original assignments and question store.",
                                                       "Operator must decide https://example.org/issue/7")
            old = report.write_report(path, original, expected="absent")
            self.assertTrue(report.operation(path, "Tracker unavailable"))
            first = path.read_bytes()
            self.assertFalse(report.operation(path, "Tracker unavailable"))
            self.assertEqual(first, path.read_bytes())
            self.assertIn("Operator must decide", first.decode())
            with self.assertRaisesRegex(ValueError, "changed"):
                report.write_report(path, original, expected=old)

    def test_report_validator_rejects_missing_empty_and_ambiguous_fields(self):
        report = load("board_report")
        text = report.initial_report()
        invalid = [text.replace('**Reviewed:** none', '**Reviewed:** 2026-10-15T03:00:00'),
                   text.replace('## Results', '## Other'),
                   text.replace('No new result recorded.', ''),
                   text.replace('**Reviewed:** none', '**Reviewed:** none\n- **Reviewed:** none')]
        for value in invalid:
            with self.subTest(value=value), self.assertRaises(ValueError):
                report.validate(value)


class RunTests(unittest.TestCase):
    def test_successful_process_without_required_report_is_a_failure(self):
        runner, report = load('board_run'), load('board_report')
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = root / 'report.md'
            report.write_report(path, report.initial_report(), expected='absent')
            worker = runner.CodexReviewer(root, root / 'local/state.sqlite3', path,
                                          'school/workshop', ['project:workshop'], executable='controlled.exe')
            with patch.object(runner.subprocess, 'run', return_value=Mock(returncode=0)), \
                    self.assertRaisesRegex(RuntimeError, 'without publishing'):
                worker([{'number': 1}])

    def test_launcher_keeps_credentials_out_of_reviewer_environment(self):
        runner, report = load('board_run'), load('board_report')
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = root / 'report.md'
            report.write_report(path, report.initial_report(), expected='absent')
            worker = runner.CodexReviewer(root, root / 'local/state.sqlite3', path,
                                          'school/workshop', ['project:workshop'], executable='controlled.exe')
            def complete(*args, **kwargs):
                self.assertNotIn('GH_TOKEN', kwargs['env'])
                self.assertNotIn('GITHUB_TOKEN', kwargs['env'])
                self.assertNotIn('CODEX_THREAD_ID', kwargs['env'])
                report.operation(path, 'Controlled completed review')
                return Mock(returncode=0)
            with patch.dict(runner.os.environ, {'GH_TOKEN': 'control-only', 'GITHUB_TOKEN': 'control-only',
                                               'CODEX_THREAD_ID': 'control-only'}), \
                    patch.object(runner.subprocess, 'run', side_effect=complete):
                worker([{'number': 1}])

    def test_quiet_scan_calls_no_model_and_leaves_report_unchanged(self):
        runner, report = load("board_run"), load("board_report")
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = root / "report.md"
            report.write_report(path, report.initial_report(), expected="absent")
            before = path.read_bytes()
            worker = Mock()
            run = runner.ReviewRun(root, root / "state.sqlite3", path,
                                   lambda: {"complete": True, "candidates": [], "errors": []}, worker)
            self.assertEqual("quiet", run.run()["status"])
            worker.assert_not_called()
            self.assertEqual(before, path.read_bytes())

    def exercise(self, result, worker=None):
        runner = load("board_run")
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        root = Path(directory.name)
        return runner.ReviewRun(root, root / "state.sqlite3", root / "report.md",
                                lambda: result, worker or Mock())

    def test_only_available_changed_or_due_work_starts_the_reviewer(self):
        worker = Mock()
        run = self.exercise({"complete": True, "errors": [], "candidates": [
            {"number": 1, "reason": "changed", "busy": False},
            {"number": 2, "reason": "new", "busy": True},
            {"number": 3, "reason": "follow_up", "busy": False}]}, worker)
        self.assertEqual([1, 3], run.run()["cases"])
        self.assertEqual([1, 3], [c["number"] for c in worker.call_args.args[0]])

    def test_failed_read_is_not_an_empty_board_and_does_not_start_a_model(self):
        worker = Mock()
        run = self.exercise({"complete": False, "candidates": [],
                             "errors": [{"number": 7, "error": "Access denied"}]}, worker)
        self.assertEqual("failed", run.run()["status"])
        worker.assert_not_called()
        self.assertIn("Access denied", run.report.read_text(encoding="utf-8"))

    def test_competing_controller_cannot_scan_or_start_another_reviewer(self):
        run = self.exercise({"complete": True, "errors": [], "candidates": [{"number": 1}]})
        other = load("board_run").ReviewRun(run.root, run.state, run.report, Mock(), Mock())
        observed = []
        run.worker = lambda cases: observed.append(other.run())
        self.assertEqual("completed", run.run()["status"])
        self.assertEqual("busy", observed[0]["status"])
        other.scan.assert_not_called()
        other.worker.assert_not_called()

    def test_worker_failure_keeps_review_content_and_is_visible(self):
        report = load("board_report")
        run = self.exercise({"complete": True, "errors": [], "candidates": [{"number": 1}]},
                            Mock(side_effect=RuntimeError("Codex failed")))
        report.write_report(run.report, report.initial_report().replace("No new result recorded.",
                            "Existing verified result"), expected="absent")
        self.assertEqual("failed", run.run()["status"])
        text = run.report.read_text(encoding="utf-8")
        self.assertIn("Existing verified result", text)
        self.assertIn("Codex failed", text)

    def test_discovery_only_observes_work_without_starting_or_claiming_review(self):
        run = self.exercise({"complete": True, "errors": [], "candidates": [{"number": 1}]})
        run.discover_only = True
        self.assertEqual("observed", run.run()["status"])
        run.worker.assert_not_called()
        self.assertFalse(run.report.exists())

    def test_completed_cases_remain_quiet_after_controller_restart(self):
        import test_board
        board = test_board.board
        runner = load("board_run")
        tracker = test_board.Tracker()
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            state = root / "state.sqlite3"
            review = board.Board(state, tracker)
            calls = []
            def study(cases):
                calls.append(cases)
                for case in cases:
                    claim = review.claim(case['number'])
                    review.finish(claim['token'], 'reviewed', 'Studied no-response outcome')
            first = runner.ReviewRun(root, state, root / 'report.md', review.scan, study)
            self.assertEqual('completed', first.run()['status'])
            restarted = runner.ReviewRun(root, state, root / 'report.md', board.Board(state, tracker).scan, study)
            self.assertEqual('quiet', restarted.run()['status'])
            self.assertEqual(1, len(calls))


if __name__ == "__main__":
    unittest.main()
