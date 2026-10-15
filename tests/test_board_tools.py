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


if __name__ == '__main__':
    unittest.main()
