"""Listing the straw dogs, guessing where an unwrapped one stands, and taking out the ones that expired."""

from __future__ import annotations

import contextlib
import hashlib
import io
import json
import unittest

from repository import RepositoryCase

import straw_dogs

PACER = "docs/tickets/01-0020-pacer.md"
OWNER = 'ticket="docs/tickets/01-0020-pacer.md"'


class Survey(RepositoryCase):
    def setUp(self) -> None:
        super().setUp()
        self.write(PACER, "# Pacer\n")

    def surveyed(self, *paths: str):
        return straw_dogs.survey(self.root, list(paths or ["docs"]))

    def test_an_operative_statement_is_reported_with_its_condition_and_owner(self) -> None:
        self.write(
            "docs/process.md",
            "# Process\n\n"
            f'<straw-dog until="/pacer is installed" {OWNER}>\n'
            "This document is a suggestion of sequence.\n"
            "</straw-dog>\n\n## Work\n",
        )

        found = self.surveyed().statements

        self.assertEqual(1, len(found))
        self.assertEqual("docs/process.md", found[0].path)
        self.assertEqual(3, found[0].opens)
        self.assertEqual(5, found[0].closes)
        self.assertEqual("/pacer is installed", found[0].until)
        self.assertEqual(PACER, found[0].ticket)
        self.assertEqual(0, found[0].depth)

    def test_an_illustration_of_the_syntax_is_not_a_statement(self) -> None:
        self.write(
            "docs/entry.md",
            "# Entry\n\n"
            'A statement is wrapped in `<straw-dog until="condition" ticket="path">`.\n\n'
            "```md\n"
            '<straw-dog until="x" ticket="y">rule</straw-dog>\n'
            "```\n",
        )

        self.assertEqual([], self.surveyed().statements)

    def test_a_nested_statement_is_reported_and_so_is_the_parent_that_holds_it(self) -> None:
        self.write(
            "docs/process.md",
            "# Process\n\n"
            f'<straw-dog until="/pacer is installed" {OWNER}>\n'
            "Outer rule.\n"
            f'<straw-dog until="/ticket is installed" {OWNER}>\n'
            "Inner rule.\n</straw-dog>\nMore outer.\n</straw-dog>\n",
        )

        outer, inner = self.surveyed().statements

        self.assertEqual((3, 9, 0, 1), (outer.opens, outer.closes, outer.depth, outer.contains))
        self.assertEqual((5, 7, 1, 0), (inner.opens, inner.closes, inner.depth, inner.contains))

    def test_an_opening_tag_wrapped_across_lines_is_one_statement(self) -> None:
        self.write(
            "docs/process.md",
            "# Process\n\n<straw-dog\n"
            '  until="/pacer is installed"\n'
            f"  {OWNER}>\nRule.\n</straw-dog>\n",
        )

        found = self.surveyed().statements

        self.assertEqual(1, len(found))
        self.assertEqual("/pacer is installed", found[0].until)

    def test_a_statement_bound_to_no_ticket_is_a_diagnostic(self) -> None:
        self.write("docs/process.md", '# Process\n\n<straw-dog until="someday">Rule.</straw-dog>\n')

        self.assertEqual(["unbound"], [note.problem for note in self.surveyed().diagnostics])

    def test_a_statement_with_no_condition_is_a_diagnostic(self) -> None:
        self.write("docs/process.md", f"# Process\n\n<straw-dog {OWNER}>Rule.</straw-dog>\n")

        self.assertEqual(["no condition"], [note.problem for note in self.surveyed().diagnostics])

    def test_a_statement_naming_a_ticket_that_is_not_there_is_a_diagnostic(self) -> None:
        self.write(
            "docs/process.md",
            '# Process\n\n<straw-dog until="x" ticket="docs/tickets/absent.md">Rule.</straw-dog>\n',
        )

        self.assertEqual(["unknown owner"], [note.problem for note in self.surveyed().diagnostics])

    def test_a_tag_that_never_closes_stays_visible_as_a_diagnostic(self) -> None:
        self.write("docs/process.md", f'# Process\n\n<straw-dog until="x" {OWNER}>\nRule.\n')

        self.assertEqual(["never closed"], [note.problem for note in self.surveyed().diagnostics])

    def test_a_closing_tag_with_nothing_open_stays_visible_as_a_diagnostic(self) -> None:
        self.write("docs/process.md", "# Process\n\nRule.\n</straw-dog>\n")

        self.assertEqual(["never opened"], [note.problem for note in self.surveyed().diagnostics])

    def test_a_malformed_tag_stays_visible_as_a_diagnostic(self) -> None:
        self.write("docs/process.md", '# Process\n\n<straw-dog until="unterminated\nRule.\n')

        self.assertEqual(["malformed"], [note.problem for note in self.surveyed().diagnostics])

    def test_the_retired_tag_name_is_a_diagnostic_not_an_invisible_statement(self) -> None:
        # The tag was <temporary> until 2026-09-08. One written from habit would otherwise be no
        # statement at all — the defect this tool exists to end, produced by its own rename.
        self.write("docs/process.md", f'# Process\n\n<temporary until="x" {OWNER}>\nRule.\n</temporary>\n')

        problems = [note.problem for note in self.surveyed().diagnostics]

        self.assertEqual(1, len(problems))
        self.assertIn("retired", problems[0])
        self.assertIn("<straw-dog>", problems[0])

    def test_the_retired_tag_name_inside_a_code_span_is_nothing(self) -> None:
        self.write("docs/process.md", "# Process\n\nIt used to be `<temporary>`.\n")

        surveyed = self.surveyed()

        self.assertEqual([], surveyed.statements)
        self.assertEqual([], surveyed.diagnostics)


class Removal(RepositoryCase):
    """The one mechanical edit this tool makes, and everything it refuses to guess."""

    def setUp(self) -> None:
        super().setUp()
        self.write(PACER, "# Pacer\n")
        self.before = (
            "# Process\r\n\r\n"
            f'<straw-dog until="/pacer is installed" {OWNER}>\r\n'
            "This document is a suggestion of sequence.\r\n"
            "</straw-dog>\r\n\r\n## Work\r\n"
        )
        self.write("docs/process.md", self.before)

    def fingerprint(self) -> str:
        return "sha256:" + hashlib.sha256((self.root / "docs/process.md").read_bytes()).hexdigest()

    def nest_a_statement_inside_the_pacer_block(self) -> None:
        self.write(
            "docs/process.md",
            "# Process\n\n"
            f'<straw-dog until="/pacer is installed" {OWNER}>\n'
            "Outer.\n"
            f'<straw-dog until="/ticket is installed" {OWNER}>\n'
            "Inner.\n</straw-dog>\n</straw-dog>\n",
        )

    def test_removing_an_expired_statement_takes_the_block_and_nothing_else(self) -> None:
        straw_dogs.remove_straw_dog(self.root, "docs/process.md", 3, self.fingerprint())

        self.assertEqual("# Process\r\n\r\n\r\n## Work\r\n", self.read("docs/process.md"))

    def test_a_fingerprint_from_before_someone_elses_edit_removes_nothing(self) -> None:
        stale = self.fingerprint()
        self.write("docs/process.md", self.before + "A note added since.\r\n")
        untouched = self.snapshot()

        with self.assertRaises(straw_dogs.Refused):
            straw_dogs.remove_straw_dog(self.root, "docs/process.md", 3, stale)

        self.assertEqual(untouched, self.snapshot())

    def test_an_outer_statement_is_never_removed_over_a_statement_it_contains(self) -> None:
        self.nest_a_statement_inside_the_pacer_block()
        untouched = self.snapshot()

        with self.assertRaises(straw_dogs.Refused) as refused:
            straw_dogs.remove_straw_dog(self.root, "docs/process.md", 3, self.fingerprint())

        self.assertIn("contains", str(refused.exception))
        self.assertEqual(untouched, self.snapshot())

    def test_the_parent_can_go_only_after_the_child_and_only_on_a_fresh_reading(self) -> None:
        self.nest_a_statement_inside_the_pacer_block()
        before_the_child_went = self.fingerprint()

        straw_dogs.remove_straw_dog(self.root, "docs/process.md", 5, before_the_child_went)
        with self.assertRaises(straw_dogs.Refused):
            straw_dogs.remove_straw_dog(
                self.root, "docs/process.md", 3, before_the_child_went
            )
        rescanned = straw_dogs.survey(self.root, ["docs/process.md"]).statements
        straw_dogs.remove_straw_dog(self.root, "docs/process.md", 3, self.fingerprint())

        self.assertEqual([3], [statement.opens for statement in rescanned])
        self.assertEqual("# Process\n\n", self.read("docs/process.md"))

    def test_a_path_outside_the_repository_is_refused(self) -> None:
        with self.assertRaises(straw_dogs.Refused):
            straw_dogs.remove_straw_dog(self.root, "../elsewhere.md", 3, self.fingerprint())


class Guessing(RepositoryCase):
    """Where a straw dog stands unwrapped: a guess from the words a sentence carries, never a verdict."""

    def setUp(self) -> None:
        super().setUp()
        self.write(PACER, "# Pacer\n")

    def guessed(self, *paths: str) -> tuple[int, dict]:
        said = io.StringIO()
        with contextlib.redirect_stdout(said):
            status = straw_dogs.main(["--guess", *(paths or ["docs"])], root=self.root)
        return status, json.loads(said.getvalue())

    def test_a_sentence_carrying_a_listed_word_is_a_candidate_with_its_place_and_word(self) -> None:
        self.write("docs/architecture.md", "# Arch\n\nThe ceiling stays as it is until the operator replaces it.\n")

        status, guessed = self.guessed()

        self.assertEqual(0, status)
        self.assertEqual(1, len(guessed["candidates"]))
        found = guessed["candidates"][0]
        self.assertEqual(("docs/architecture.md", 3, "until"), (found["path"], found["line"], found["word"]))
        self.assertIn("ceiling", found["text"])
        self.assertIn("docs/architecture.md", guessed["scanned"])

    def test_a_tell_inside_code_a_wrapper_or_an_installed_block_is_not_a_candidate(self) -> None:
        self.write(
            "docs/architecture.md",
            "# Arch\n\n"
            "In a span: `until the pacer lands`.\n\n"
            "```md\nfor now, in a fence\n```\n\n"
            f'<straw-dog until="/pacer is installed" {OWNER}>\nWrapped, by hand, until then.\n</straw-dog>\n\n'
            '<installed by="other">\nInstalled: until its source moves.\n</installed>\n',
        )

        self.assertEqual([], self.guessed()[1]["candidates"])

    def test_the_folders_the_harness_imposes_are_skipped_whole_and_a_projects_own_is_read(self) -> None:
        for folder in ("tickets", "rfc", "spec", "sessions"):
            self.write(f"docs/{folder}/one.md", "# One\n\nProvisional until the align.\n")
        self.write("docs/research/one.md", "# Research\n\nHeld for now.\n")

        status, guessed = self.guessed()

        self.assertEqual(0, status)
        self.assertEqual(["docs/research/one.md"], [c["path"] for c in guessed["candidates"]])
        self.assertNotIn("docs/tickets/one.md", guessed["scanned"])

    def test_three_of_the_four_demonstration_sentences_are_found_and_the_fourth_has_no_tell(self) -> None:
        self.write(
            ".agents/mechanisms/keeper/keeper.md",
            "# keeper\n\n"
            "It is installed, and no installer exists yet — that moment is declared.\n\n"
            "| part | where | owner |\n|---|---|---|\n"
            "| reader | `x.py` | same gap; not a live question while nothing installs or extracts |\n",
        )
        self.write(
            ".agents/skills/keeper/SKILL.md",
            "# Keeper\n\nIts own rules reach their readers by hand until the installer lands.\n\n"
            "- `/maintain` applies mechanism rules and owns none.\n",
        )

        found = self.guessed(".agents")[1]["candidates"]

        self.assertEqual(
            {"no installer exists", "nothing installs", "by hand"},
            {c["word"] for c in found} - {"until"},
        )
        self.assertFalse(any("owns none" in c["text"] for c in found))

    def test_a_todo_naming_no_ticket_is_a_candidate_and_a_listed_word_in_code_is_nothing(self) -> None:
        self.write(
            ".agents/scripts/keeper.py",
            "# TODO: tighten this once the harness settles\n"
            "def keep():\n    return 'until'  # placeholder text, not a marking\n",
        )

        found = self.guessed(".agents")[1]["candidates"]

        self.assertEqual([("TODO", 1)], [(c["word"], c["line"]) for c in found])


class Code(RepositoryCase):
    """In code the marking is a TODO naming its ticket."""

    def setUp(self) -> None:
        super().setUp()
        self.write(PACER, "# Pacer\n")

    def surveyed(self):
        return straw_dogs.survey(self.root, [".agents"])

    def test_a_todo_naming_its_ticket_is_a_straw_dog_with_that_owner(self) -> None:
        self.write(".agents/scripts/keeper.py", f"# TODO({PACER}): the pacer takes this over\nx = 1\n")

        found = self.surveyed().statements

        self.assertEqual(1, len(found))
        self.assertEqual((".agents/scripts/keeper.py", 1, PACER), (found[0].path, found[0].opens, found[0].ticket))
        self.assertEqual([], self.surveyed().diagnostics)

    def test_a_todo_naming_a_ticket_that_is_not_there_is_an_unknown_owner(self) -> None:
        self.write(".agents/scripts/keeper.py", "# TODO docs/tickets/absent.md\n")

        self.assertEqual(["unknown owner"], [note.problem for note in self.surveyed().diagnostics])

    def test_a_todo_is_not_removed_by_the_tool(self) -> None:
        self.write(".agents/scripts/keeper.py", f"# TODO({PACER})\n")
        digest = "sha256:" + hashlib.sha256((self.root / ".agents/scripts/keeper.py").read_bytes()).hexdigest()

        with self.assertRaises(straw_dogs.Refused) as refused:
            straw_dogs.remove_straw_dog(self.root, ".agents/scripts/keeper.py", 1, digest)

        self.assertIn("leaves with the code", str(refused.exception))


class CommandLine(RepositoryCase):
    def setUp(self) -> None:
        super().setUp()
        self.write(PACER, "# Pacer\n")
        self.write(
            "docs/process.md",
            f'# Process\n\n<straw-dog until="/pacer is installed" {OWNER}>\nRule.\n</straw-dog>\n',
        )

    def run_tool(self, *argv: str) -> tuple[int, str]:
        said = io.StringIO()
        with contextlib.redirect_stdout(said), contextlib.redirect_stderr(said):
            status = straw_dogs.main(list(argv), root=self.root)
        return status, said.getvalue()

    def test_a_clean_scope_reports_its_statements_as_json_and_succeeds(self) -> None:
        status, said = self.run_tool("docs")

        reported = json.loads(said)
        self.assertEqual(0, status)
        self.assertEqual("/pacer is installed", reported["statements"][0]["until"])
        self.assertEqual([], reported["diagnostics"])
        self.assertNotIn("candidates", reported)

    def test_a_diagnostic_makes_the_run_fail_even_though_it_read_everything(self) -> None:
        self.write("docs/other.md", '# Other\n\n<straw-dog until="x">Rule.</straw-dog>\n')

        status, said = self.run_tool("docs")

        self.assertEqual(1, status)
        self.assertEqual("unbound", json.loads(said)["diagnostics"][0]["problem"])

    def test_a_scope_naming_something_that_is_not_there_is_refused_not_reported_clean(self) -> None:
        status, said = self.run_tool("docs", "docs/typo")

        self.assertEqual(2, status)
        self.assertIn("refused", said)
        self.assertIn("docs/typo", said)
        self.assertNotIn('"statements"', said)

    def test_asking_for_usage_is_answered_not_scanned_as_a_scope(self) -> None:
        status, said = self.run_tool("--help")

        self.assertEqual(0, status)
        self.assertIn("usage", said)
        self.assertNotIn('"scanned"', said)

    def test_an_unknown_flag_is_a_usage_error_rather_than_an_empty_scan(self) -> None:
        status, said = self.run_tool("--recurse")

        self.assertEqual(2, status)
        self.assertIn("usage", said)
        self.assertNotIn('"scanned"', said)

    def test_a_removal_names_its_line_after_the_final_colon_so_drive_letters_survive(self) -> None:
        digest = "sha256:" + hashlib.sha256((self.root / "docs/process.md").read_bytes()).hexdigest()

        status, _ = self.run_tool("--remove", "docs/process.md:3", "--expect", digest)

        self.assertEqual(0, status)
        self.assertEqual("# Process\n\n", self.read("docs/process.md"))


if __name__ == "__main__":
    unittest.main()
