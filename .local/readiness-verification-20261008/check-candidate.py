import json
import os
from pathlib import Path
import sys
import unittest
from unittest import mock

root = Path.cwd()
test_dir = root / '.agents/scripts/gw/test'
sys.path.insert(0, str(test_dir))
import test_harness


@test_harness.proves_a_process
def candidate(self):
    if not test_harness.git_checks_ownership():
        self.skipTest('this Git predates the ownership check; the refusal is proved against its message')
    before = self.target_snapshot()
    with mock.patch.dict(os.environ, {'GIT_TEST_ASSUME_DIFFERENT_OWNER': '1'}):
        status, report = self.run_harness('--install')
    self.assertEqual(1, status)
    self.assertEqual(1, len(report['refusals']), report)
    for word in ('target:', 'dubious ownership', 'safe.directory'):
        self.assertIn(word, report['refusals'][0])
    self.assertEqual(before, self.target_snapshot())


test_harness.ARefusal.test_gits_own_ownership_check_is_what_the_refusal_reads = candidate
suite = (
    unittest.defaultTestLoader.loadTestsFromName(
        'test_harness.ARefusal.test_gits_own_ownership_check_is_what_the_refusal_reads'
    )
    if '--targeted' in sys.argv
    else unittest.defaultTestLoader.discover(str(test_dir))
)
result = unittest.TextTestRunner(verbosity=1).run(suite)
summary = {
    'candidate_only': True,
    'repository_source_modified': False,
    'tests': result.testsRun,
    'failures': len(result.failures),
    'errors': len(result.errors),
    'skipped': len(result.skipped),
    'skip_reasons': [reason for _, reason in result.skipped],
    'successful': result.wasSuccessful(),
}
(root / '.local/readiness-verification-20261008/candidate-final-suite.json').write_text(
    json.dumps(summary, indent=2), encoding='utf-8'
)
print(json.dumps(summary, indent=2))
raise SystemExit(0 if result.wasSuccessful() else 1)
