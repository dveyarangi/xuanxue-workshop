"""The test base itself: a case that is not marked as proving a process cannot start one, and
the scripts' Git listing it answers from the folder never outlives the case."""

from __future__ import annotations

import subprocess
import sys
import tempfile
import types
import unittest
from pathlib import Path
from unittest import mock

import repository
from repository import RepositoryCase, proves_a_process

import docs_corpus


def outcome(case: type[unittest.TestCase]) -> unittest.TestResult:
    """Runs a planted case on its own and returns what it did."""
    result = unittest.TestResult()
    unittest.TestLoader().loadTestsFromTestCase(case).run(result)
    return result


class TheGuard(unittest.TestCase):
    def test_a_case_not_marked_fails_when_it_starts_a_process_and_names_it(self) -> None:
        class Unmarked(RepositoryCase):
            def test_starts_git(self) -> None:
                subprocess.run(["git", "--version"], capture_output=True)

        result = outcome(Unmarked)

        self.assertEqual(1, len(result.failures))
        self.assertIn("not marked as proving a process", result.failures[0][1])
        self.assertIn("'git', '--version'", result.failures[0][1])

    def test_a_marked_test_may_start_what_it_proves_in_a_real_repository(self) -> None:
        class Marked(RepositoryCase):
            @proves_a_process
            def test_reads_its_repository(self) -> None:
                self.assertTrue((self.root / ".git").is_dir())
                subprocess.run(["git", "status"], cwd=self.root, capture_output=True, check=True)

        result = outcome(Marked)

        self.assertEqual([], result.failures + result.errors)
        self.assertEqual(1, result.testsRun)

    def test_a_case_not_marked_gets_a_plain_folder(self) -> None:
        class Unmarked(RepositoryCase):
            def test_has_no_repository(self) -> None:
                self.assertFalse((self.root / ".git").exists())

        result = outcome(Unmarked)

        self.assertEqual([], result.failures + result.errors)


class TheLiveStoreGuard(unittest.TestCase):
    """A suite run leaves this tree's question store byte-identical: only a session writes it."""

    def setUp(self) -> None:
        workspace = tempfile.TemporaryDirectory()
        self.addCleanup(workspace.cleanup)
        self.store = Path(workspace.name) / "questions"
        self.store.mkdir()
        (self.store / "q-0001-a-question.md").write_text("# q-0001 A question\n", encoding="utf-8")
        patcher = mock.patch.object(repository, "LIVE_STORE", self.store)
        patcher.start()
        self.addCleanup(patcher.stop)

    def test_a_case_that_changes_an_entry_fails_and_names_the_store(self) -> None:
        store = self.store

        class Writer(RepositoryCase):
            def test_writes(self) -> None:
                (store / "q-0001-a-question.md").write_text("# q-0001 Rewritten\n", encoding="utf-8")

        result = outcome(Writer)

        self.assertEqual(1, len(result.failures))
        self.assertIn("question store", result.failures[0][1])

    def test_a_case_that_adds_an_entry_fails_too(self) -> None:
        store = self.store

        class Adder(RepositoryCase):
            def test_adds(self) -> None:
                (store / "q-0002-another.md").write_text("# q-0002 Another\n", encoding="utf-8")

        result = outcome(Adder)

        self.assertEqual(1, len(result.failures))

    def test_a_case_that_only_reads_it_passes(self) -> None:
        store = self.store

        class Reader(RepositoryCase):
            def test_reads(self) -> None:
                (store / "q-0001-a-question.md").read_text(encoding="utf-8")

        result = outcome(Reader)

        self.assertEqual([], result.failures + result.errors)


class TheFolderListing(unittest.TestCase):
    def test_answers_the_scripts_listing_with_every_file_in_gits_order(self) -> None:
        listed: list[str] = []

        class Unmarked(RepositoryCase):
            def test_lists(self) -> None:
                self.write("b.md", "b\n")
                self.write("a/z.md", "z\n")
                self.write("a.md", "a\n")
                listed.extend(docs_corpus.corpus(self.root))

        result = outcome(Unmarked)

        self.assertEqual([], result.failures + result.errors)
        self.assertEqual(["a.md", "a/z.md", "b.md"], listed)

    def test_gives_git_back_when_the_case_ends_even_to_a_module_imported_during_it(self) -> None:
        git_listing = docs_corpus.corpus
        late = types.ModuleType("imported_during_the_case")
        self.addCleanup(sys.modules.pop, late.__name__, None)
        bound: list[object] = []

        class Unmarked(RepositoryCase):
            def test_imports(self) -> None:
                # What an import made inside a case does: the module lands in `sys.modules`
                # and binds the listing `docs_corpus` holds at that moment.
                sys.modules[late.__name__] = late
                late.corpus = docs_corpus.corpus
                bound.append(late.corpus)

        result = outcome(Unmarked)

        self.assertEqual([], result.failures + result.errors)
        self.assertIsNot(git_listing, bound[0])
        self.assertIs(git_listing, docs_corpus.corpus)
        self.assertIs(git_listing, late.corpus)


if __name__ == "__main__":
    unittest.main()
