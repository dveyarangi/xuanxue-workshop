import importlib.util
import tempfile
import unittest
from pathlib import Path

import test_board


SCRIPT = Path(__file__).resolve().parents[1] / '.agents/scripts/gw/board_tools.py'


class CapabilityTests(unittest.TestCase):
    def setUp(self):
        spec = importlib.util.spec_from_file_location('board_tools_test', SCRIPT)
        self.module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.module)
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.tracker = test_board.Tracker()
        self.review = test_board.board.Board(Path(self.directory.name) / 'state.sqlite3', self.tracker)
        self.tools = self.module.ReviewTools(self.review, allowed_cases=[1], read_repos=['school/workshop'],
                                             read=lambda path, collection=None: {'path': path})

    def test_agent_cannot_claim_an_unassigned_case_or_read_an_unlisted_repository(self):
        with self.assertRaisesRegex(ValueError, 'scope'):
            self.tools.board({'action': 'claim', 'number': 2})
        with self.assertRaisesRegex(ValueError, 'scope'):
            self.tools.read('repos/private/other/issues/1')
        with self.assertRaisesRegex(ValueError, 'scope'):
            self.tools.read('repos/school/workshop/../other/issues/1')
        with self.assertRaisesRegex(ValueError, 'scope'):
            self.tools.read('repos/school/workshop/%2e%2e/other/issues/1')
        self.assertEqual({'author': 'coordinator', 'repo': 'school/workshop'},
                         self.tools.board({'action': 'identity'}))

    def test_authorized_review_publishes_once_and_retains_outcome_without_credentials_in_reply(self):
        claim = self.tools.board({'action': 'claim', 'number': 1})
        prepared = self.tools.board({'action': 'prepare', 'token': claim['token'],
                                     'body': 'Inspected answer', 'request_id': 'scoped-proof'})
        first = self.tools.board({'action': 'publish', 'id': prepared['id']})
        second = self.tools.board({'action': 'publish', 'id': prepared['id']})
        self.assertEqual(first['comment_id'], second['comment_id'])
        self.assertEqual(1, len(self.tracker.posts))
        finished = self.tools.board({'action': 'finish', 'token': claim['token'],
                                     'outcome': 'reviewed', 'note': 'Evidence studied'})
        self.assertEqual('reviewed', finished['status'])

    def test_read_only_proof_cannot_acquire_a_mutating_capability(self):
        self.tools.read_only = True
        with self.assertRaisesRegex(ValueError, 'read-only'):
            self.tools.board({'action': 'claim', 'number': 1})

    def test_preexisting_lease_and_publication_cannot_widen_dispatch_scope(self):
        claim = self.review.claim(1)
        prepared = self.review.prepare(claim['token'], 'Prepared before dispatch')
        self.tools.allowed_cases = {2}
        with self.assertRaisesRegex(ValueError, 'scope'):
            self.tools.board({'action': 'prepare', 'token': claim['token'], 'body': 'Forged scope'})
        with self.assertRaisesRegex(ValueError, 'scope'):
            self.tools.board({'action': 'publish', 'id': prepared['id']})
        self.assertEqual([], self.tracker.posts)

    def test_check_requires_the_whole_assigned_batch_and_ignores_other_cases(self):
        self.tools.allowed_cases = {1, 2}
        first = self.tools.board({'action': 'claim', 'number': 1})
        self.tools.board({'action': 'finish', 'token': first['token'], 'outcome': 'reviewed', 'note': 'First studied'})
        partial = self.tools.board({'action': 'check'})
        self.assertTrue(partial['valid'])
        self.assertFalse(partial['batch_complete'])
        self.assertEqual([{'number': 2, 'reasons': ['not_reviewed']}], partial['pending'])
        second = self.tools.board({'action': 'claim', 'number': 2})
        self.assertIn('active_lease', self.tools.board({'action': 'check'})['pending'][0]['reasons'])
        self.tools.board({'action': 'finish', 'token': second['token'], 'outcome': 'waiting', 'note': 'Owner evidence missing'})
        self.assertTrue(self.tools.board({'action': 'check'})['batch_complete'])

    def test_publication_disabled_still_allows_local_completion(self):
        first = self.review.claim(1)
        prepared = self.review.prepare(first['token'], 'Prepared before proof')
        self.tools.no_publish = True
        with self.assertRaisesRegex(ValueError, 'disabled'):
            self.tools.board({'action': 'prepare', 'token': first['token'], 'body': 'New response'})
        with self.assertRaisesRegex(ValueError, 'disabled'):
            self.tools.board({'action': 'publish', 'id': prepared['id']})
        pending = self.tools.board({'action': 'check'})['pending'][0]
        self.assertIn('unconfirmed_publication', pending['reasons'])
        self.tools.board({'action': 'cancel', 'id': prepared['id']})
        self.tools.board({'action': 'finish', 'token': first['token'], 'outcome': 'operator',
                          'note': 'Publication requires operator authorization'})
        self.assertTrue(self.tools.board({'action': 'check'})['batch_complete'])
        self.assertEqual([], self.tracker.posts)


if __name__ == '__main__':
    unittest.main()
