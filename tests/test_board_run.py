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
    def test_repository_only_push_never_starts_the_reviewer(self):
        import test_board
        runner, report = load('board_run'), load('board_report')
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            tracker = test_board.Tracker()
            reference = {'sha': 'abc', 'repo': {'full_name': 'provider/api', 'pushed_at': 'old'}}
            tracker.cases[1]['evidence'] = [{'data': {'pull': {'head': reference}}}]
            review = test_board.board.Board(root / 'state.sqlite3', tracker)
            for number in (1, 2):
                claim = review.claim(number)
                review.finish(claim['token'], 'reviewed', 'Existing evidence studied')
            path = root / 'report.md'
            report.write_report(path, report.initial_report(), expected='absent')
            before = path.read_bytes()
            reference['repo']['pushed_at'] = 'unrelated-push'
            worker = Mock()
            result = runner.ReviewRun(root, review.state, path, review.scan, worker).run()
            self.assertEqual('quiet', result['status'])
            worker.assert_not_called()
            self.assertEqual(before, path.read_bytes())

    def test_finished_unchanged_review_does_not_require_report_rewrite(self):
        from tests.test_board import Tracker, board
        runner, report = load('board_run'), load('board_report')
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = root / 'report.md'
            report.write_report(path, report.initial_report(), expected='absent')
            prior = report.initial_report().replace('**Reviewed:** none', '**Reviewed:** 2026-10-16T08:00:00+00:00')
            prior = prior.replace('No new result recorded.', 'Existing waiting result: same missing evidence.')
            report.write_report(path, prior, expected=report.version(path))
            before = path.read_bytes()
            review = board.Board(root / 'state.sqlite3', Tracker())
            claim = review.claim(1)
            review.finish(claim['token'], 'waiting', 'Same missing evidence')
            worker = runner.CodexReviewer(root, review.state, path, 'school/workshop',
                                          ['project:workshop'], executable='controlled.exe')
            def completed(*args, **kwargs):
                claim = review.claim(1)
                review.finish(claim['token'], 'waiting', 'Same missing evidence')
                return Mock(returncode=0)
            with patch.object(runner.subprocess, 'run', side_effect=completed):
                worker([{'number': 1}])
            self.assertEqual(before, path.read_bytes())

    def test_changed_report_does_not_establish_finished_review(self):
        from tests.test_board import Tracker, board
        runner, report = load('board_run'), load('board_report')
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory); path = root / 'report.md'
            report.write_report(path, report.initial_report(), expected='absent')
            review = board.Board(root / 'state.sqlite3', Tracker())
            review.claim(1)
            worker = runner.CodexReviewer(root, review.state, path, 'school/workshop',
                                          ['project:workshop'], executable='controlled.exe')
            def incomplete(*args, **kwargs):
                report.operation(path, 'Reviewer wrote a report but did not finish the case')
                return Mock(returncode=0)
            with patch.object(runner.subprocess, 'run', side_effect=incomplete), self.assertRaisesRegex(RuntimeError, 'without completing'):
                worker([{'number': 1}])

    def test_successful_process_without_required_report_is_a_failure(self):
        runner, report = load('board_run'), load('board_report')
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = root / 'report.md'
            report.write_report(path, report.initial_report(), expected='absent')
            worker = runner.CodexReviewer(root, root / 'local/state.sqlite3', path,
                                          'school/workshop', ['project:workshop'], executable='controlled.exe')
            with patch.object(runner.subprocess, 'run', return_value=Mock(returncode=0)), \
                    self.assertRaisesRegex(RuntimeError, 'without completing'):
                worker([{'number': 1}])

    def test_launcher_keeps_credentials_out_of_reviewer_environment(self):
        runner, report = load('board_run'), load('board_report')
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = root / 'report.md'
            report.write_report(path, report.initial_report(), expected='absent')
            worker = runner.CodexReviewer(root, root / 'local/state.sqlite3', path,
                                          'school/workshop', ['project:workshop'], executable='controlled.exe')
            from tests.test_board import Tracker, board
            worker.timeout = 17
            review = board.Board(worker.state, Tracker())
            def complete(*args, **kwargs):
                for number in (1, 2):
                    claim = review.claim(number)
                    review.finish(claim['token'], 'reviewed', 'Controlled evidence checked')
                self.assertNotIn('GH_TOKEN', kwargs['env'])
                self.assertNotIn('GITHUB_TOKEN', kwargs['env'])
                self.assertNotIn('CODEX_THREAD_ID', kwargs['env'])
                self.assertEqual(worker.timeout, kwargs['timeout'])
                self.assertIn('mcp_servers.workshop_review.tool_timeout_sec=' + str(worker.timeout), args[0])
                report.operation(path, 'Controlled completed review')
                return Mock(returncode=0)
            with patch.dict(runner.os.environ, {'GH_TOKEN': 'control-only', 'GITHUB_TOKEN': 'control-only',
                                               'CODEX_THREAD_ID': 'control-only'}), \
                    patch.object(runner.subprocess, 'run', side_effect=complete):
                worker([{'number': 1}, {'number': 2}])

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
        run.worker = lambda cases, **kwargs: observed.append(other.run())
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
            def study(cases, **kwargs):
                calls.append(cases)
                for case in cases:
                    claim = review.claim(case['number'])
                    review.finish(claim['token'], 'reviewed', 'Studied no-response outcome')
            first = runner.ReviewRun(root, state, root / 'report.md', review.scan, study)
            self.assertEqual('completed', first.run()['status'])
            restarted = runner.ReviewRun(root, state, root / 'report.md', board.Board(state, tracker).scan, study)
            self.assertEqual('quiet', restarted.run()['status'])
            self.assertEqual(1, len(calls))

    def test_a_successful_reviewer_cannot_finish_only_part_of_its_batch(self):
        import test_board
        board, runner, report = test_board.board, load('board_run'), load('board_report')
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory); path = root / 'report.md'
            report.write_report(path, report.initial_report(), expected='absent')
            review = board.Board(root / 'state.sqlite3', test_board.Tracker())
            worker = runner.CodexReviewer(root, review.state, path, 'school/workshop',
                                         ['project:workshop'], executable='controlled.exe')
            def partial(*args, **kwargs):
                claim = review.claim(1)
                review.finish(claim['token'], 'reviewed', 'Only first case studied')
                return Mock(returncode=0)
            with patch.object(runner.subprocess, 'run', side_effect=partial):
                with self.assertRaisesRegex(RuntimeError, '"number": 2.*not_reviewed'):
                    worker([{'number': 1}, {'number': 2}])
            self.assertEqual([{'number': 2, 'reasons': ['not_reviewed']}], review.pending([1, 2]))

    def test_every_run_retains_its_result_and_earlier_reviewer_logs(self):
        runner = load('board_run')
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory); state = root / 'state.sqlite3'
            def fail(cases, *, run_directory):
                (run_directory / 'reviewer.jsonl').write_text('partial execution', encoding='utf-8')
                (run_directory / 'reviewer.stderr.log').write_text('retained error', encoding='utf-8')
                raise RuntimeError('Unfinished second case')
            first = runner.ReviewRun(root, state, root / 'report.md',
                lambda: {'complete': True, 'errors': [], 'candidates': [{'number': 1}, {'number': 2}]}, fail).run()
            self.assertEqual('failed', first['status'])
            second = runner.ReviewRun(root, state, root / 'report.md',
                lambda: {'complete': True, 'errors': [], 'candidates': []}, Mock()).run()
            self.assertEqual('quiet', second['status'])
            first_dir, second_dir = Path(first['run_directory']), Path(second['run_directory'])
            self.assertNotEqual(first_dir, second_dir)
            self.assertEqual('partial execution', (first_dir / 'reviewer.jsonl').read_text(encoding='utf-8'))
            self.assertEqual('retained error', (first_dir / 'reviewer.stderr.log').read_text(encoding='utf-8'))
            import json
            self.assertEqual('failed', json.loads((first_dir / 'result.json').read_text())['status'])
            self.assertEqual('quiet', json.loads((second_dir / 'result.json').read_text())['status'])
            self.assertEqual(second, json.loads((root / 'last-run.json').read_text()))

    def test_reviewer_logs_and_publication_mode_belong_to_the_controller_run(self):
        import test_board
        runner, report = load('board_run'), load('board_report')
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory); path = root / 'report.md'
            report.write_report(path, report.initial_report(), expected='absent')
            review = test_board.board.Board(root / 'state.sqlite3', test_board.Tracker())
            worker = runner.CodexReviewer(root, review.state, path, 'school/workshop',
                                         ['project:workshop'], executable='controlled.exe', no_publish=True,
                                         case_timeout=17)
            def complete(*args, **kwargs):
                kwargs['stdout'].write('execution output')
                kwargs['stderr'].write('diagnostic output')
                for number in (1, 2):
                    claim = review.claim(number)
                    review.finish(claim['token'], 'waiting', 'Existing dependency')
                self.assertEqual(34, kwargs['timeout'])
                self.assertIn('mcp_servers.workshop_review.tool_timeout_sec=17', args[0])
                return Mock(returncode=0)
            with patch.object(runner.subprocess, 'run', side_effect=complete):
                result = runner.ReviewRun(root, review.state, path,
                    lambda: {'complete': True, 'errors': [], 'candidates': [{'number': 1}, {'number': 2}]}, worker).run()
            self.assertEqual('completed', result['status'])
            run_dir = Path(result['run_directory'])
            self.assertEqual('execution output', (run_dir / 'reviewer.jsonl').read_text())
            self.assertEqual('diagnostic output', (run_dir / 'reviewer.stderr.log').read_text())
            import json
            self.assertTrue(json.loads((run_dir / 'request.json').read_text())['no_publish'])
            self.assertEqual(34, json.loads((run_dir / 'request.json').read_text())['batch_timeout_seconds'])


if __name__ == "__main__":
    unittest.main()
