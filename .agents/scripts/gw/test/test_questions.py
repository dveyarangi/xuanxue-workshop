"""The question store read from disk, and the maintainer's verdict on it."""

from __future__ import annotations

import contextlib
import io
import json
import tempfile
import unittest
from datetime import date, datetime, timedelta, timezone
from unittest import mock

from repository import RepositoryCase

import questions

STORE = "docs/questions"


def remember_windows_in_the_case(case: unittest.TestCase) -> None:
    """Keep what `--window` remembers inside the case, never in the machine's temp folder."""
    memory = tempfile.TemporaryDirectory()
    case.addCleanup(memory.cleanup)
    patcher = mock.patch.object(questions, "WINDOW_MEMORY", memory.name)
    patcher.start()
    case.addCleanup(patcher.stop)


def entry(identity: str, question: str, parts: dict[str, str]) -> str:
    """An entry in the store's format: the title line, then one bullet per part, in order given."""
    bullets = [f"- **{name}** {value}" for name, value in parts.items()]
    return "\n".join([f"# {identity} {question}", "", *bullets]) + "\n"


class Store(RepositoryCase):
    """A tree holding a small conforming store: one open root with an open child."""

    def setUp(self) -> None:
        super().setUp()
        remember_windows_in_the_case(self)
        self.seed()

    def seed(self) -> None:
        self.place("q-0001-which-store-holds-the-questions", "Which store holds the questions?", {"state": "open"})
        self.place(
            "q-0001.0001-what-an-entry-holds",
            "What an entry holds?",
            {"part of": "q-0001", "state": "open"},
        )

    def place(self, stem: str, question: str, parts: dict[str, str], folder: str = STORE) -> str:
        """Writes an entry whose id is the stem's own, so the filename agrees with the title."""
        name = f"{folder}/{stem}.md"
        self.write(name, entry(stem[: stem.index("-", 2)], question, parts))
        return name

    def checked(self):
        return questions.check(self.root)

    def problems(self) -> list[str]:
        return [note.problem for note in self.checked().diagnostics]

    def run_check(self) -> tuple[int, dict]:
        said = io.StringIO()
        with contextlib.redirect_stdout(said):
            status = questions.main(["--check"], root=self.root)
        return status, json.loads(said.getvalue())


class AConformingStore(Store):
    def test_checks_clean_and_exits_zero(self) -> None:
        status, report = self.run_check()

        self.assertEqual(0, status)
        self.assertEqual([], report["diagnostics"])
        self.assertEqual(2, report["entries"])


class AMalformedEntry(Store):
    def assertReported(self, text: str, fragment: str) -> None:
        self.write(f"{STORE}/q-0003-a-bad-one.md", text)
        problems = self.problems()
        self.assertEqual(1, len(problems), problems)
        self.assertIn(fragment, problems[0])

    def test_without_a_title_line_naming_its_id(self) -> None:
        self.assertReported("A bad one?\n\n- **state** open\n", "title")

    def test_without_a_state(self) -> None:
        self.assertReported(entry("q-0003", "A bad one?", {"lean": "none"}), "no state")

    def test_with_a_state_outside_the_vocabulary(self) -> None:
        self.assertReported(entry("q-0003", "A bad one?", {"state": "closed:done"}), "state")

    def test_with_a_part_the_format_does_not_have(self) -> None:
        self.assertReported(entry("q-0003", "A bad one?", {"state": "open", "why": "because"}), "why")

    def test_with_a_part_written_twice(self) -> None:
        text = entry("q-0003", "A bad one?", {"state": "open"}) + "- **state** open\n"
        self.assertReported(text, "twice")

    def test_open_but_carrying_an_answer(self) -> None:
        self.assertReported(
            entry("q-0003", "A bad one?", {"state": "open", "answer": "a reason"}), "open"
        )

    def test_every_part_and_the_suspect_flag_are_the_format(self) -> None:
        self.write("docs/record.md", "# A record\n")
        self.place(
            "q-0001.0002-a-full-one",
            "A full one?",
            {
                "part of": "q-0001",
                "depends on": "q-0001, q-0001.0001",
                "state": "closed:decided, suspect",
                "owner": "[the record](../record.md)",
                "answer": "[the record](../record.md) — the user, 2026-09-29",
                "lean": "held loosely",
                "struck": "2, last 2026-10-02T19:40Z",
            },
        )

        self.assertEqual([], self.problems())

    def test_a_strike_without_its_last_time(self) -> None:
        self.assertReported(entry("q-0003", "A bad one?", {"state": "open", "struck": "2"}), "last <YYYY-MM-DDTHH:MMZ>")

    def test_a_strike_whose_time_has_no_zone(self) -> None:
        self.assertReported(
            entry("q-0003", "A bad one?", {"state": "open", "struck": "2, last 2026-10-02T19:40"}), "last <YYYY-MM-DDTHH:MMZ>"
        )

    def test_a_strike_with_a_negative_count(self) -> None:
        self.assertReported(
            entry("q-0003", "A bad one?", {"state": "open", "struck": "-1, last 2026-10-02T19:40Z"}), "last <YYYY-MM-DDTHH:MMZ>"
        )

    def test_a_strike_on_a_day_the_calendar_lacks(self) -> None:
        self.assertReported(
            entry("q-0003", "A bad one?", {"state": "open", "struck": "1, last 2026-13-02T19:40Z"}), "last <YYYY-MM-DDTHH:MMZ>"
        )


ARCHITECTURE = (
    "# Architecture\n\n"
    "## Decisions landed at this ticket's align\n\n"
    "## Impact — 2026-09-28, the inception\n\n"
    "```md\n## Not a heading, an illustration\n```\n"
)


class TheAnswer(Store):
    """A closed question points to its answer and never holds it (decision 43)."""

    def setUp(self) -> None:
        super().setUp()
        self.write("docs/architecture.md", ARCHITECTURE)

    def close(self, kind: str, answer: str | None, folder: str = STORE) -> None:
        parts = {"state": f"closed:{kind}"} | ({"answer": answer} if answer is not None else {})
        self.place("q-0003-a-closed-one", "A closed one?", parts, folder=folder)

    def assertReported(self, fragment: str) -> None:
        problems = self.problems()
        self.assertEqual(1, len(problems), problems)
        self.assertIn(fragment, problems[0])

    def test_is_required_once_the_question_is_closed(self) -> None:
        self.close("pruned", None)
        self.assertReported("no answer")

    def test_decided_is_a_link_not_prose(self) -> None:
        self.close("decided", "we keep the flat directory — the user, 2026-09-29")
        self.assertReported("not a link")

    def test_decided_to_a_file_that_does_not_exist_is_reported(self) -> None:
        self.close("decided", "[the ADR](../adr/0009-never-written.md) — the user, 2026-09-29")
        self.assertReported("does not resolve")

    def test_decided_to_a_heading_that_does_not_exist_is_reported(self) -> None:
        self.close("decided", "[gone](../architecture.md#not-a-heading-an-illustration)")
        self.assertReported("does not resolve")

    def test_decided_to_a_heading_as_written_resolves(self) -> None:
        self.close(
            "decided",
            "[the align](../architecture.md#decisions-landed-at-this-tickets-align), "
            "[the impact](../architecture.md#impact--2026-09-28-the-inception)",
        )
        self.assertEqual([], self.problems())

    def test_decided_elsewhere_on_the_web_is_a_link(self) -> None:
        self.close("decided", "[the RFC](https://example.invalid/rfc) — the user, 2026-09-29")
        self.assertEqual([], self.problems())

    def test_decided_in_done_resolves_from_there(self) -> None:
        self.close(
            "decided",
            "[the align](../../architecture.md#decisions-landed-at-this-tickets-align)",
            folder=f"{STORE}/done",
        )
        self.assertEqual([], self.problems())

    def test_decided_in_done_whose_heading_no_longer_exists_is_reported(self) -> None:
        self.close("decided", "[the align](../../architecture.md#decisions-landed)", folder=f"{STORE}/done")
        self.assertReported("does not resolve")

    def test_deferred_names_its_condition_and_its_default(self) -> None:
        self.close("deferred", "until the listing stops being readable, meanwhile the flat directory")
        self.assertEqual([], self.problems())

    def test_deferred_without_a_default_is_reported(self) -> None:
        self.close("deferred", "until the listing stops being readable")
        self.assertReported("meanwhile")

    def test_merged_points_at_another_question(self) -> None:
        self.close("merged", "q-0001.0001")
        self.assertEqual([], self.problems())

    def test_superseded_by_prose_is_reported(self) -> None:
        self.close("superseded", "the newer one")
        self.assertReported("id")

    def test_moot_gives_its_reason(self) -> None:
        self.close("moot", "the store became the host's")
        self.assertEqual([], self.problems())


class TheFilename(Store):
    def test_whose_id_disagrees_with_the_title_is_reported(self) -> None:
        self.write(f"{STORE}/q-0003-a-question.md", entry("q-0004", "A question?", {"state": "open"}))

        problems = self.problems()

        self.assertEqual(1, len(problems), problems)
        self.assertIn("q-0004", problems[0])

    def test_whose_slug_is_not_the_questions_words_is_reported(self) -> None:
        self.write(f"{STORE}/q-0003-something-else.md", entry("q-0003", "A question?", {"state": "open"}))

        problems = self.problems()

        self.assertEqual(1, len(problems), problems)
        self.assertIn("slug", problems[0])

    def test_holds_every_word_of_the_question_an_apostrophe_dropped(self) -> None:
        self.place("q-0003-what-the-tickets-align-holds", "What the ticket's align holds?", {"state": "open"})

        self.assertEqual([], self.problems())

    def test_that_stops_short_of_the_whole_question_is_reported_with_the_name_it_needs(self) -> None:
        self.place("q-0003-which-package-manager", "Which package manager do we use?", {"state": "open"})

        problems = self.problems()

        self.assertEqual(1, len(problems), problems)
        self.assertIn("q-0003-which-package-manager-do-we-use.md", problems[0])

    def test_that_is_not_an_entrys_name_is_reported(self) -> None:
        self.write(f"{STORE}/notes.md", "# Notes\n")

        problems = self.problems()

        self.assertEqual(1, len(problems), problems)
        self.assertIn("q-NNNN-", problems[0])

    def test_one_id_held_by_two_files_is_reported(self) -> None:
        self.place(
            "q-0001.0001-what-an-entry-holds",
            "What an entry holds?",
            {"part of": "q-0001", "state": "closed:moot", "answer": "gone"},
            folder=f"{STORE}/done",
        )

        problems = self.problems()

        self.assertEqual(1, len(problems), problems)
        self.assertIn("two files", problems[0])


class NestedIds(Store):
    """An id says where its question sits: a root's position, then one per level below it."""

    def test_a_nested_id_reads_in_a_title_a_name_a_relation_and_a_session_line(self) -> None:
        self.place(
            "q-0001.0001.0001-which-parts", "Which parts?", {"part of": "q-0001.0001", "depends on": "q-0001.0001", "state": "open"}
        )
        self.write(f"{STORE}/sessions", "s-alpha running 2026-09-29 q-0001.0001.0001 q-0001.0001,q-0001\n")

        self.assertEqual([], self.problems())

    def test_the_tree_draws_a_child_after_its_parent_and_before_the_next_root(self) -> None:
        self.place("q-0002-a-second-root", "A second root?", {"state": "open"})
        self.place("q-0001.0002-a-second-child", "A second child?", {"part of": "q-0001", "state": "open"})

        self.assertEqual(
            [
                "q-0001 [open] Which store holds the questions?",
                "  q-0001.0001 [open] What an entry holds?",
                "  q-0001.0002 [open] A second child?",
                "q-0002 [open] A second root?",
            ],
            questions.tree(self.root).splitlines(),
        )

    def test_a_child_whose_id_is_not_under_its_parents_is_reported(self) -> None:
        self.place("q-0003-a-flat-child", "A flat child?", {"part of": "q-0001", "state": "open"})

        self.assertEqual(["q-0003 is part of q-0001, so its id is q-0001.NNNN"], self.problems())

    def test_a_root_whose_id_is_nested_is_reported(self) -> None:
        self.place("q-0002.0001-a-lost-one", "A lost one?", {"state": "open"})

        self.assertEqual(["q-0002.0001 is part of nothing, so its id is q-NNNN"], self.problems())

    def test_an_orphans_id_is_not_judged_since_its_parent_is_reported_missing(self) -> None:
        self.place("q-0001.0002-an-orphan", "An orphan?", {"part of": "q-0009", "state": "open"})

        problems = self.problems()

        self.assertEqual(1, len(problems), problems)
        self.assertIn("q-0009, which no entry holds", problems[0])


class TheRelations(Store):
    def assertReported(self, fragment: str) -> None:
        problems = self.problems()
        self.assertEqual(1, len(problems), problems)
        self.assertIn(fragment, problems[0])

    def test_a_parent_that_does_not_exist_is_an_orphan(self) -> None:
        self.place("q-0003-an-orphan", "An orphan?", {"part of": "q-0009", "state": "open"})
        self.assertReported("q-0009")

    def test_a_dependency_that_does_not_exist_is_an_orphan(self) -> None:
        self.place("q-0003-an-orphan", "An orphan?", {"depends on": "q-0001, q-0009", "state": "open"})
        self.assertReported("q-0009")

    def test_a_merge_into_a_question_that_does_not_exist_is_an_orphan(self) -> None:
        self.place("q-0003-an-orphan", "An orphan?", {"state": "closed:merged", "answer": "q-0009"})
        self.assertReported("q-0009")

    def test_a_relation_into_done_resolves(self) -> None:
        self.place(
            "q-0003-an-archived-one",
            "An archived one?",
            {"state": "closed:moot", "answer": "no longer asked"},
            folder=f"{STORE}/done",
        )
        self.place("q-0004-a-later-one", "A later one?", {"depends on": "q-0003", "state": "open"})
        self.assertEqual([], self.problems())

    def test_a_parent_line_naming_two_parents_is_reported(self) -> None:
        self.place("q-0003-two-parents", "Two parents?", {"part of": "q-0001, q-0001.0001", "state": "open"})
        self.assertReported("part of")

    def test_a_cycle_in_part_of_is_reported(self) -> None:
        self.place(
            "q-0001-which-store-holds-the-questions", "Which store holds the questions?", {"part of": "q-0001.0001", "state": "open"}
        )
        self.assertTrue(any("cycle" in problem for problem in self.problems()), self.problems())

    def supersede_the_root_and_close_its_child(self, child_state: str) -> None:
        self.place(
            "q-0001-which-store-holds-the-questions",
            "Which store holds the questions?",
            {"state": "closed:superseded", "answer": "q-0003"},
        )
        self.place(
            "q-0001.0001-what-an-entry-holds",
            "What an entry holds?",
            {"part of": "q-0001", "state": child_state, "answer": "the store changed"},
        )
        self.place("q-0003-which-store-now", "Which store now?", {"state": "open"})

    def test_a_closed_child_under_a_superseded_parent_must_be_suspect(self) -> None:
        self.supersede_the_root_and_close_its_child("closed:moot")
        self.assertReported("superseded")

    def test_a_suspect_child_under_a_superseded_parent_is_already_marked(self) -> None:
        self.supersede_the_root_and_close_its_child("closed:moot, suspect")
        self.assertEqual([], self.problems())

    def decide_early(self, state: str) -> None:
        self.place(
            "q-0003-decided-early",
            "Decided early?",
            {"depends on": "q-0001", "state": state, "answer": "overtaken"},
        )

    def test_a_closed_entry_on_an_open_dependency_must_be_suspect(self) -> None:
        self.decide_early("closed:moot")
        self.assertReported("depends on q-0001")

    def test_a_suspect_entry_on_an_open_dependency_says_so_already(self) -> None:
        self.decide_early("closed:moot, suspect")
        self.assertEqual([], self.problems())


SESSIONS = f"{STORE}/sessions"
TODAY = date(2026, 9, 29)
NOW = datetime(2026, 9, 29, 12, 0, tzinfo=timezone.utc)


class TheSessions(Store):
    """One line per session: its tag, running or ended, the date it last wrote, its current
    question or `-` before it has one, and up to four recent ones."""

    def setUp(self) -> None:
        super().setUp()
        self.write(SESSIONS, "s-alpha running 2026-09-29 q-0001.0001 q-0001\ns-beta ended 2026-09-01 q-0001\n")

    def checked(self):
        return questions.check(self.root, today=TODAY)

    def findings(self) -> list[str]:
        return [note.finding for note in self.checked().findings]

    def assertReported(self, fragment: str) -> None:
        problems = self.problems()
        self.assertEqual(1, len(problems), problems)
        self.assertIn(fragment, problems[0])

    def test_as_written_checks_clean_and_finds_nothing(self) -> None:
        self.assertEqual(([], []), (self.problems(), self.findings()))

    def test_a_session_registered_without_a_position_yet_is_the_form(self) -> None:
        self.write(SESSIONS, "s-alpha running 2026-09-29 -\n")
        self.assertEqual([], self.problems())

    def test_a_line_out_of_the_form_is_reported(self) -> None:
        self.write(SESSIONS, "s-alpha asleep 2026-09-29 q-0001.0001\n")
        self.assertReported("line 1")

    def test_more_than_four_recent_questions_is_out_of_the_form(self) -> None:
        self.write(SESSIONS, "s-alpha running 2026-09-29 q-0001.0001 q-0001,q-0001.0001,q-0001,q-0001.0001,q-0001\n")
        self.assertReported("line 1")

    def test_a_tag_registered_twice_is_reported(self) -> None:
        self.write(SESSIONS, "s-alpha running 2026-09-29 q-0001.0001\ns-alpha ended 2026-09-28 q-0001\n")
        self.assertReported("s-alpha")

    def test_a_position_naming_a_missing_entry_is_reported(self) -> None:
        self.write(SESSIONS, "s-alpha running 2026-09-29 q-0009\n")
        self.assertReported("q-0009")

    def test_a_running_session_on_a_closed_question_is_a_finding_not_a_failure(self) -> None:
        self.place(
            "q-0001.0001-what-an-entry-holds",
            "What an entry holds?",
            {"part of": "q-0001", "state": "closed:moot", "answer": "gone"},
        )

        stranded = [finding for finding in self.findings() if "s-alpha" in finding]

        self.assertEqual([], self.problems())
        self.assertEqual(1, len(stranded), stranded)
        self.assertIn("closed", stranded[0])

    def test_a_running_session_silent_for_over_a_week_is_a_finding(self) -> None:
        self.write(SESSIONS, "s-alpha running 2026-09-21 q-0001.0001\ns-beta running 2026-09-23 q-0001\n")

        found = self.findings()

        self.assertEqual(1, len(found), found)
        self.assertIn("s-alpha", found[0])

    def test_findings_leave_the_exit_status_at_zero(self) -> None:
        self.write(SESSIONS, "s-alpha running 2000-01-01 q-0001.0001\n")

        said = io.StringIO()
        with contextlib.redirect_stdout(said):
            status = questions.main(["--check"], root=self.root, today=TODAY)

        self.assertEqual(0, status)
        self.assertEqual(1, len(json.loads(said.getvalue())["findings"]))


class LikelyTwins(Store):
    def findings(self) -> list[str]:
        return [note.finding for note in questions.check(self.root, today=TODAY).findings]

    def test_two_live_titles_sharing_most_of_their_words_are_a_finding(self) -> None:
        self.place("q-0003-which-package-manager-do-we-use", "Which package manager do we use?", {"state": "open"})
        self.place(
            "q-0004-what-package-manager-should-we-use-for-builds",
            "What package manager should we use for builds?",
            {"state": "open"},
        )

        found = self.findings()

        self.assertEqual(1, len(found), found)
        self.assertIn("q-0003", found[0])
        self.assertIn("q-0004", found[0])
        self.assertEqual([], self.problems())

    def test_titles_sharing_a_word_or_two_are_not(self) -> None:
        self.place("q-0003-which-store-holds-the-drafts", "Which store holds the drafts?", {"state": "open"})

        self.assertEqual([], self.findings())

    def test_an_archived_title_is_searched_by_a_person_not_paired_here(self) -> None:
        self.place("q-0003-which-package-manager-do-we-use", "Which package manager do we use?", {"state": "open"})
        self.place(
            "q-0004-what-package-manager-should-we-use-for-builds",
            "What package manager should we use for builds?",
            {"state": "closed:moot", "answer": "no builds"},
            folder=f"{STORE}/done",
        )

        self.assertEqual([], self.findings())


class ReadyForDone(Store):
    """A wholly closed subtree nothing open depends on is ready to move (parent decision 34); a
    deferred or suspect entry counts as open, since the wake reads it in the live store."""

    def ready(self) -> list[str]:
        return [
            note.finding
            for note in questions.check(self.root, today=TODAY).findings
            if "done/" in note.finding
        ]

    def close(self, stem: str, question: str, state: str = "closed:moot", **parts: str) -> None:
        answer = "until the store grows, meanwhile flat" if "deferred" in state else "overtaken"
        self.place(stem, question, parts | {"state": state, "answer": answer})

    def test_a_closed_subtree_under_an_open_parent_is_ready_at_its_own_root(self) -> None:
        self.close("q-0001.0001-what-an-entry-holds", "What an entry holds?", **{"part of": "q-0001"})
        self.close("q-0001.0001.0001-its-parts", "Its parts?", **{"part of": "q-0001.0001"})

        ready = self.ready()

        self.assertEqual(1, len(ready), ready)
        self.assertIn("q-0001.0001 and", ready[0])

    def test_a_wholly_closed_tree_is_ready_once_at_its_root(self) -> None:
        self.close("q-0001-which-store-holds-the-questions", "Which store holds the questions?")
        self.close("q-0001.0001-what-an-entry-holds", "What an entry holds?", **{"part of": "q-0001"})

        ready = self.ready()

        self.assertEqual(1, len(ready), ready)
        self.assertIn("q-0001 and", ready[0])

    def test_a_deferred_leaf_is_never_ready(self) -> None:
        self.close(
            "q-0001.0001-what-an-entry-holds", "What an entry holds?", "closed:deferred", **{"part of": "q-0001"}
        )

        self.assertEqual([], self.ready())

    def test_a_subtree_holding_a_suspect_entry_is_never_ready(self) -> None:
        self.close("q-0001.0001-what-an-entry-holds", "What an entry holds?", **{"part of": "q-0001"})
        self.close(
            "q-0001.0001.0001-its-parts", "Its parts?", "closed:moot, suspect", **{"part of": "q-0001.0001"}
        )

        self.assertEqual([], self.ready())

    def test_a_subtree_an_open_question_depends_on_is_not_ready(self) -> None:
        self.close("q-0001.0001-what-an-entry-holds", "What an entry holds?", **{"part of": "q-0001"})
        self.place("q-0003-a-later-one", "A later one?", {"depends on": "q-0001.0001", "state": "open"})

        self.assertEqual([], self.ready())

    def test_ready_leaves_the_exit_status_at_zero(self) -> None:
        self.close("q-0001.0001-what-an-entry-holds", "What an entry holds?", **{"part of": "q-0001"})

        status, report = self.run_check()

        self.assertEqual(0, status)
        self.assertEqual(1, len(report["findings"]))


class TheMaintainer(Store):
    def test_leaves_the_tree_byte_identical_even_with_findings_and_diagnostics(self) -> None:
        self.write(SESSIONS, "s-alpha running 2000-01-01 q-0001.0001\n")
        self.place("q-0003-an-orphan", "An orphan?", {"part of": "q-0009", "state": "open"})
        untouched = self.snapshot()

        self.run_check()

        self.assertEqual(untouched, self.snapshot())

    def test_an_entry_it_cannot_read_fails_the_run_and_is_named(self) -> None:
        (self.root / STORE / "q-0003-unreadable.md").write_bytes(b"# q-0003 Unreadable\n\n- **state** \xff\n")

        status, report = self.run_check()

        self.assertEqual(1, status)
        self.assertEqual([f"{STORE}/q-0003-unreadable.md"], [passed.get("record") for passed in report["skipped"]])

    def test_a_call_without_its_mode_is_refused(self) -> None:
        said = io.StringIO()
        with contextlib.redirect_stdout(said):
            status = questions.main([], root=self.root)

        self.assertEqual(2, status)
        self.assertIn("--check", said.getvalue())


class Rendered(Store):
    """A fixed store with two roots of open work, one closed root, and three sessions.

        q-0001 Which store holds the questions?          open
          q-0002 What an entry holds?                    open, lean
            q-0004 Which parts are optional?             open      <- s-alpha
              q-0008 Is the lean optional?               decided, suspect
            q-0005 Is the id a path?                     decided
            q-0006 Is the directory partitioned by root? deferred
          q-0003 How is a subtree archived?              open
            q-0007 Who moves a subtree?                  open
              q-0013 Does the mover repair links?        decided, suspect
            q-0009 Are twins found by embeddings?        deferred
        q-0010 How do sessions reach each other?         open      <- s-beta
        q-0011 Is height depth?                          pruned
        q-0012 (in done/)

    Its children keep the flat ids every store held before an id said where it sits (`.0020`'s
    decision 6): they still read, and a call that opens or renames under them gives nested ones.
    """

    def seed(self) -> None:
        self.place("q-0001-which-store-holds-the-questions", "Which store holds the questions?", {"state": "open"})
        self.write("docs/record.md", "# A record\n")
        decided = "[the record](../record.md) — the user, 2026-09-29"
        self.question("q-0002-what-an-entry-holds", "What an entry holds?", "q-0001", lean="eight parts")
        self.question("q-0003-how-is-a-subtree-archived", "How is a subtree archived?", "q-0001")
        self.question("q-0004-which-parts-are-optional", "Which parts are optional?", "q-0002")
        self.question("q-0005-is-the-id-a-path", "Is the id a path?", "q-0002", "closed:decided", decided)
        self.question(
            "q-0006-is-the-directory-partitioned-by-root",
            "Is the directory partitioned by root?",
            "q-0002",
            "closed:deferred",
            "until a listing is unreadable, meanwhile flat",
        )
        self.question("q-0007-who-moves-a-subtree", "Who moves a subtree?", "q-0003")
        self.question(
            "q-0008-is-the-lean-optional", "Is the lean optional?", "q-0004", "closed:decided, suspect", decided
        )
        self.question(
            "q-0009-are-twins-found-by-embeddings",
            "Are twins found by embeddings?",
            "q-0003",
            "closed:deferred",
            "until a place to run, meanwhile word match",
        )
        self.question("q-0010-how-do-sessions-reach-each-other", "How do sessions reach each other?")
        self.question("q-0011-is-height-depth", "Is height depth?", None, "closed:pruned", "height was abstraction")
        self.question("q-0012-an-archived-one", "An archived one?", None, "closed:moot", "gone", folder=f"{STORE}/done")
        self.question(
            "q-0013-does-the-mover-repair-links",
            "Does the mover repair links?",
            "q-0007",
            "closed:decided, suspect",
            decided,
        )
        self.write(
            SESSIONS,
            "s-alpha running 2026-09-29 q-0004 q-0002,q-0001\n"
            "s-beta running 2026-09-28 q-0010\n"
            "s-gamma ended 2026-09-20 q-0003\n",
        )

    def question(
        self,
        stem: str,
        text: str,
        parent: str | None = None,
        state: str = "open",
        answer: str | None = None,
        lean: str | None = None,
        folder: str = STORE,
    ) -> None:
        parts = {"part of": parent, "state": state, "answer": answer, "lean": lean}
        self.place(stem, text, {name: value for name, value in parts.items() if value is not None}, folder)

    def said(self, *argv: str) -> tuple[int, str]:
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            status = questions.main(list(argv), root=self.root, today=TODAY, now=NOW)
        return status, out.getvalue()

    def section(self, text: str, heading: str) -> str:
        """The lines under one heading of the rendering, up to the next blank line."""
        after = text.split(heading, 1)[1]
        return after.split("\n\n", 1)[0]


class TheWindow(Rendered):
    def test_draws_the_path_from_the_root_to_the_sessions_position(self) -> None:
        status, text = self.said("--window", "--session", "s-alpha")

        path = self.section(text, "path (root to current):")
        self.assertEqual(0, status)
        self.assertEqual(["q-0001", "q-0002", "q-0004"], [line.split()[0] for line in path.strip().splitlines()])
        self.assertIn("<- current", path.splitlines()[-1])

    def test_each_line_carries_its_state_and_its_lean(self) -> None:
        _, text = self.said("--window", "--session", "s-alpha")

        self.assertIn("q-0002 [open] What an entry holds?  ~ eight parts", text)

    def test_the_frontier_holds_every_child_of_the_path_closed_ones_with_their_kind(self) -> None:
        _, text = self.said("--window", "--session", "s-alpha")

        frontier = self.section(text, "frontier (children of each question on the path):")
        self.assertIn("under q-0001: q-0003 [open]", frontier)
        self.assertIn("under q-0002: q-0005 [closed:decided]", frontier)
        self.assertIn("under q-0002: q-0006 [closed:deferred]", frontier)
        self.assertIn("under q-0004: q-0008 [closed:decided, suspect]", frontier)

    def test_lists_the_roots_open_questions_with_their_parents(self) -> None:
        _, text = self.said("--window", "--session", "s-alpha")

        listed = self.section(text, "open questions under this root (q-0001), with their parent:")
        self.assertIn("q-0007 (parent q-0003) Who moves a subtree?", listed)

    def test_shows_a_suspect_anywhere_under_the_root_and_no_other_closed_entry_off_the_path(self) -> None:
        _, text = self.said("--window", "--session", "s-alpha")

        self.assertIn("q-0013 [closed:decided, suspect]", self.section(text, "suspect under this root:"))
        self.assertNotIn("q-0009", text)
        self.assertNotIn("q-0012", text)

    def test_gives_one_line_to_each_other_root(self) -> None:
        _, text = self.said("--window", "--session", "s-alpha")

        roots = self.section(text, "other roots:").strip().splitlines()
        self.assertEqual(["q-0010 [open] How do sessions reach each other?", "q-0011 [closed:pruned] Is height depth?"], [line.strip() for line in roots])

    def test_names_the_recent_positions_and_the_other_running_sessions(self) -> None:
        _, text = self.said("--window", "--session", "s-alpha")

        self.assertIn("recently attached: q-0002, q-0001", text)
        others = self.section(text, "other running sessions:")
        self.assertIn("s-beta at q-0010 (last wrote 2026-09-28)", others)
        self.assertNotIn("s-gamma", others)
        self.assertNotIn("s-alpha", others)
        self.assertNotIn("next free id", text, "the script draws ids, so the agent is not handed one")


class TwoSessions(Rendered):
    def test_each_window_is_drawn_around_its_own_position_and_lists_the_other(self) -> None:
        _, beta = self.said("--window", "--session", "s-beta")

        self.assertIn("current: q-0010", beta)
        self.assertEqual("q-0010", self.section(beta, "path (root to current):").split()[0])
        self.assertIn("q-0001 [open] Which store holds the questions?", self.section(beta, "other roots:"))
        self.assertIn("s-alpha at q-0004", self.section(beta, "other running sessions:"))

    def test_a_session_without_a_position_yet_is_given_the_roots_to_place_itself_among(self) -> None:
        self.write(SESSIONS, "s-alpha running 2026-09-29 -\ns-beta running 2026-09-28 q-0010\n")

        status, text = self.said("--window", "--session", "s-alpha")

        self.assertEqual(0, status)
        self.assertIn("current: none yet", text)
        roots = self.section(text, "roots:")
        self.assertIn("q-0001", roots)
        self.assertIn("q-0010", roots)
        self.assertIn("s-beta at q-0010", text)

    def test_a_session_nobody_registered_is_refused_with_the_way_to_register(self) -> None:
        status, text = self.said("--window", "--session", "s-nobody")

        self.assertEqual(2, status)
        self.assertIn("--wake", text)


class TheCount(Rendered):
    """A struck question carries its count on its line, and the wake reads the most struck first."""

    def strike(self, stem: str, question: str, count: int, parent: str | None = None, state: str = "open",
               folder: str = STORE) -> None:
        parts = {"part of": parent, "state": state, "answer": "gone" if state != "open" else None}
        parts = {name: value for name, value in parts.items() if value is not None}
        self.place(stem, question, parts | {"struck": f"{count}, last 2026-09-29T12:00Z"}, folder)

    def test_a_struck_line_shows_its_count_and_an_unstruck_one_none(self) -> None:
        self.strike("q-0010-how-do-sessions-reach-each-other", "How do sessions reach each other?", 2)

        _, text = self.said("--window", "--session", "s-alpha", "--full")

        roots = self.section(text, "other roots:")
        self.assertIn("q-0010 [open] How do sessions reach each other? (struck 2)", roots)
        self.assertNotIn("struck", roots.split("q-0011")[1])

    def test_the_roots_open_questions_show_their_count(self) -> None:
        self.strike("q-0007-who-moves-a-subtree", "Who moves a subtree?", 1, parent="q-0003")

        _, text = self.said("--window", "--session", "s-alpha", "--full")

        self.assertIn("Who moves a subtree? (struck 1)", self.section(text, "open questions under this root"))

    def test_the_wake_reads_the_most_struck_open_questions_first(self) -> None:
        self.strike("q-0007-who-moves-a-subtree", "Who moves a subtree?", 1, parent="q-0003")
        self.strike("q-0010-how-do-sessions-reach-each-other", "How do sessions reach each other?", 3)
        self.strike("q-0011-is-height-depth", "Is height depth?", 9, state="closed:moot")
        self.strike("q-0012-an-archived-one", "An archived one?", 9, state="closed:moot", folder=f"{STORE}/done")

        _, text = self.said("--wake", "--session", "s-alpha")

        ranked = self.section(text, "most struck, open:").splitlines()[1:]
        self.assertEqual(["q-0010", "q-0007"], [line.split()[0] for line in ranked])
        self.assertTrue(text.index("most struck, open:") < text.index("sessions:"), "it opens the read")


class TheWake(Rendered):
    def registered_tag(self, text: str) -> str:
        return text.splitlines()[0].split()[1].rstrip(",")

    def test_registers_a_new_session_without_a_position_and_prints_its_tag(self) -> None:
        before = self.read(SESSIONS)

        status, text = self.said("--wake")

        tag = self.registered_tag(text)
        self.assertEqual(0, status)
        self.assertEqual(before + f"{tag} running 2026-09-29 -\n", self.read(SESSIONS))
        self.assertIn("registered now", text.splitlines()[0])

    def test_two_wakes_register_two_sessions(self) -> None:
        _, first = self.said("--wake")
        _, second = self.said("--wake")

        self.assertNotEqual(self.registered_tag(first), self.registered_tag(second))
        self.assertEqual(5, len(self.read(SESSIONS).splitlines()))

    def test_reports_the_sessions_first_running_and_ended_with_their_positions(self) -> None:
        _, text = self.said("--wake")

        sessions = self.section(text, "sessions:")
        self.assertIn("s-alpha running, last wrote 2026-09-29, at q-0004", sessions)
        self.assertIn("s-gamma ended, last wrote 2026-09-20, at q-0003", sessions)
        self.assertLess(text.index("sessions:"), text.index("deferred"))

    def test_lists_every_deferral_with_its_condition_and_every_suspect_entry(self) -> None:
        _, text = self.said("--wake")

        deferred = self.section(text, "deferred, to re-check whether each condition is met:")
        self.assertIn("q-0006", deferred)
        self.assertIn("q-0009 [closed:deferred] Are twins found by embeddings? — until a place to run, meanwhile word match", deferred)
        suspect = self.section(text, "suspect, to re-read:")
        self.assertIn("q-0008", suspect)
        self.assertIn("q-0013", suspect)

    def test_a_new_session_is_given_the_roots_to_place_itself_among(self) -> None:
        _, text = self.said("--wake")

        self.assertIn("current: none yet", text)
        self.assertIn("q-0010", self.section(text, "roots:"))

    def test_for_a_registered_session_registers_nothing_and_draws_its_window(self) -> None:
        untouched = self.snapshot()

        status, text = self.said("--wake", "--session", "s-alpha")

        self.assertEqual(0, status)
        self.assertEqual(untouched, self.snapshot())
        self.assertIn("current: q-0004", text)
        self.assertIn("q-0009", self.section(text, "deferred, to re-check whether each condition is met:"))

    def test_for_a_session_nobody_registered_is_refused(self) -> None:
        untouched = self.snapshot()

        status, _ = self.said("--wake", "--session", "s-nobody")

        self.assertEqual(2, status)
        self.assertEqual(untouched, self.snapshot())


class TheEnd(Rendered):
    def test_marks_the_session_ended_keeping_its_position_and_touching_no_other_line(self) -> None:
        status, _ = self.said("--end", "--session", "s-alpha")

        self.assertEqual(0, status)
        self.assertEqual(
            "s-alpha ended 2026-09-29 q-0004 q-0002,q-0001\n"
            "s-beta running 2026-09-28 q-0010\n"
            "s-gamma ended 2026-09-20 q-0003\n",
            self.read(SESSIONS),
        )

    def test_a_later_wake_finds_where_the_ended_session_stopped(self) -> None:
        self.said("--end", "--session", "s-alpha")

        _, text = self.said("--wake")

        self.assertIn("s-alpha ended, last wrote 2026-09-29, at q-0004", self.section(text, "sessions:"))

    def test_a_session_nobody_registered_is_refused_and_nothing_is_written(self) -> None:
        untouched = self.snapshot()

        status, _ = self.said("--end", "--session", "s-nobody")

        self.assertEqual(2, status)
        self.assertEqual(untouched, self.snapshot())


class TheTree(Rendered):
    def test_draws_every_live_root_and_everything_under_it_indented_in_id_order(self) -> None:
        status, text = self.said("--tree")

        self.assertEqual(0, status)
        self.assertEqual(
            [
                "q-0001 [open] Which store holds the questions?",
                "  q-0002 [open] What an entry holds?  ~ eight parts",
                "    q-0004 [open] Which parts are optional?",
                "      q-0008 [closed:decided, suspect] Is the lean optional?",
                "    q-0005 [closed:decided] Is the id a path?",
                "    q-0006 [closed:deferred] Is the directory partitioned by root?",
                "  q-0003 [open] How is a subtree archived?",
                "    q-0007 [open] Who moves a subtree?",
                "      q-0013 [closed:decided, suspect] Does the mover repair links?",
                "    q-0009 [closed:deferred] Are twins found by embeddings?",
                "q-0010 [open] How do sessions reach each other?",
                "q-0011 [closed:pruned] Is height depth?",
            ],
            text.splitlines(),
        )

    def test_under_one_question_draws_that_subtree_alone(self) -> None:
        _, text = self.said("--tree", "q-0003")

        self.assertEqual(
            [
                "q-0003 [open] How is a subtree archived?",
                "  q-0007 [open] Who moves a subtree?",
                "    q-0013 [closed:decided, suspect] Does the mover repair links?",
                "  q-0009 [closed:deferred] Are twins found by embeddings?",
            ],
            text.splitlines(),
        )

    def test_under_a_question_no_live_entry_holds_is_refused(self) -> None:
        status, text = self.said("--tree", "q-0012")

        self.assertEqual(2, status)
        self.assertIn("q-0012", text)


class ItsOutput(Rendered):
    def test_is_utf8_whatever_the_consoles_encoding_so_any_title_prints(self) -> None:
        self.place("q-0010-how-do-sessions-reach-each-other", "How do sessions reach each other → remotely?", {"state": "open"})
        raw = io.BytesIO()
        console = io.TextIOWrapper(raw, encoding="cp1252")

        with contextlib.redirect_stdout(console):
            status = questions.main(["--tree", "q-0010"], root=self.root, today=TODAY)
            console.flush()

        self.assertEqual(0, status)
        self.assertIn("each other → remotely?", raw.getvalue().decode("utf-8"))


class Declared(Rendered):
    """The writer over the fixed store, as s-alpha at q-0004 calls it: written whole, or refused
    with its reason and nothing written."""

    def call(self, *argv: str, session: str | None = "s-alpha", now: datetime = NOW) -> tuple[int, str]:
        said, complained = io.StringIO(), io.StringIO()
        tagged = [*argv, "--session", session] if session else list(argv)
        with contextlib.redirect_stdout(said), contextlib.redirect_stderr(complained):
            status = questions.main(tagged, root=self.root, today=TODAY, now=now)
        return status, said.getvalue() + complained.getvalue()

    def called(self, *argv: str) -> str:
        status, said = self.call(*argv)
        self.assertEqual(0, status, said)
        return said

    def assertRefused(self, reason: str, *argv: str, session: str | None = "s-alpha") -> None:
        untouched = self.snapshot()

        status, said = self.call(*argv, session=session)

        self.assertEqual(2, status, said)
        self.assertIn(reason, said)
        self.assertEqual(untouched, self.snapshot())

    def entry_text(self, stem: str) -> str:
        return self.read(f"{STORE}/{stem}.md")

    def part(self, stem: str, name: str) -> str | None:
        found = [line.split("** ", 1)[1] for line in self.entry_text(stem).splitlines() if line.startswith(f"- **{name}** ")]
        return found[0] if found else None

    def own_line(self) -> str:
        return next(line for line in self.read(SESSIONS).splitlines() if line.startswith("s-alpha "))


class TheCalls(Declared):
    """Each event of a turn is its own call."""

    def test_at_places_the_session(self) -> None:
        self.called("at", "q-0010")

        self.assertEqual("s-alpha running 2026-09-29 q-0010 q-0004,q-0002,q-0001", self.own_line())

    def test_at_prints_the_question_it_landed_on_and_the_one_it_left(self) -> None:
        said = self.called("at", "q-0010")

        self.assertIn(
            "at q-0010 How do sessions reach each other? (from q-0004 Which parts are optional?)", said
        )

    def test_at_that_stays_prints_the_question_alone(self) -> None:
        said = self.called("at", "q-0004")

        self.assertIn("at q-0004 Which parts are optional?", said)
        self.assertNotIn("(from", said)

    def test_open_takes_the_next_free_id_under_its_parent_prints_it_and_leaves_the_session_where_it_stands(self) -> None:
        said = self.called("open", "Is the owner optional?", "--under", "q-0004")

        self.assertIn("opened q-0004.0001", said)
        self.assertEqual(
            "# q-0004.0001 Is the owner optional?\n\n- **part of** q-0004\n- **state** open\n"
            "- **struck** 0, last 2026-09-29T12:00Z\n",
            self.read(f"{STORE}/q-0004.0001-is-the-owner-optional.md"),
        )
        self.assertEqual("s-alpha running 2026-09-29 q-0004 q-0002,q-0001", self.own_line())

    def test_open_takes_the_position_after_every_child_live_or_in_done(self) -> None:
        self.called("open", "Is the owner optional?", "--under", "q-0004")
        self.question("q-0004.0003-an-archived-child", "An archived child?", "q-0004", "closed:moot", "gone", folder=f"{STORE}/done")

        said = self.called("open", "Is the owner required?", "--under", "q-0004")

        self.assertIn("opened q-0004.0004", said)

    def test_open_a_root_takes_the_position_after_every_root_level_id(self) -> None:
        said = self.called("open", "Is there a third root?")

        self.assertIn("opened q-0014", said)
        self.assertIsNone(self.part("q-0014-is-there-a-third-root", "part of"))

    def test_open_where_no_four_digit_position_is_left_is_refused(self) -> None:
        self.question("q-0004.9999-the-last-child", "The last child?", "q-0004")

        self.assertRefused("no free position under q-0004", "open", "One more?", "--under", "q-0004")

    def test_open_between_two_questions_reparents_the_lower(self) -> None:
        self.called("open", "What must an entry hold?", "--between", "q-0002", "q-0004")

        self.assertEqual("q-0002", self.part("q-0002.0001-what-must-an-entry-hold", "part of"))
        self.assertEqual("q-0002.0001", self.part("q-0002.0001.0001-which-parts-are-optional", "part of"))

    def test_move_under_another_and_to_root(self) -> None:
        self.called("move", "q-0007", "--under", "q-0002")
        self.assertEqual("q-0002", self.part("q-0002.0001-who-moves-a-subtree", "part of"))

        self.called("move", "q-0002.0001", "--to-root")
        self.assertIsNone(self.part("q-0013-who-moves-a-subtree", "part of"), "q-0013 went with the first move, freed")

    def test_depend_on_another(self) -> None:
        self.called("depend", "q-0004", "--on", "q-0010")

        self.assertEqual("q-0010", self.part("q-0004-which-parts-are-optional", "depends on"))

    def test_undepend_removes_one_of_two(self) -> None:
        self.called("depend", "q-0004", "--on", "q-0010")
        self.called("depend", "q-0004", "--on", "q-0003")

        self.called("undepend", "q-0004", "--on", "q-0010")

        self.assertEqual("q-0003", self.part("q-0004-which-parts-are-optional", "depends on"))

    def test_undepend_the_last_removes_the_part(self) -> None:
        self.called("depend", "q-0004", "--on", "q-0010")

        self.called("undepend", "q-0004", "--on", "q-0010")

        self.assertIsNone(self.part("q-0004-which-parts-are-optional", "depends on"))

    def test_undepend_on_one_not_awaited_is_refused(self) -> None:
        self.assertRefused("does not depend on q-0010", "undepend", "q-0004", "--on", "q-0010")

    def test_close_with_its_kind_and_pointer(self) -> None:
        self.called("close", "q-0007", "decided", "[the record](../record.md) — the user, 2026-09-29")

        self.assertEqual("closed:decided", self.part("q-0007-who-moves-a-subtree", "state"))
        self.assertEqual("[the record](../record.md) — the user, 2026-09-29", self.part("q-0007-who-moves-a-subtree", "answer"))

    def test_suspect_and_clear(self) -> None:
        self.called("suspect", "q-0007")
        self.assertEqual("open, suspect", self.part("q-0007-who-moves-a-subtree", "state"))

        self.called("clear", "q-0007")
        self.assertEqual("open", self.part("q-0007-who-moves-a-subtree", "state"))

    def test_lean_takes_any_text_a_semicolon_included(self) -> None:
        self.called("lean", "q-0007", "the mover; never by hand")

        self.assertEqual("the mover; never by hand", self.part("q-0007-who-moves-a-subtree", "lean"))

    def test_assign_links_the_owner(self) -> None:
        self.called("assign", "q-0007", "docs/record.md")

        self.assertEqual("[record](../record.md)", self.part("q-0007-who-moves-a-subtree", "owner"))

    def test_a_call_without_its_session_is_refused_with_its_usage(self) -> None:
        self.assertRefused("--session", "at", "q-0010", session=None)

    def test_a_malformed_id_is_refused(self) -> None:
        self.assertRefused("not a question id", "at", "q-12")

    def test_a_kind_outside_the_vocabulary_is_refused(self) -> None:
        self.assertRefused("invalid choice", "close", "q-0007", "done")

    def test_at_a_closed_question_is_refused(self) -> None:
        self.assertRefused("a position is an open question", "at", "q-0005")

    def test_open_raced_by_another_session_takes_the_id_after_theirs(self) -> None:
        theirs = entry("q-0004.0001", "Their question?", {"part of": "q-0004", "state": "open"})

        written = questions.declare(
            self.root,
            "s-alpha",
            [questions.Clause("opens", other="q-0004", text="My question?")],
            TODAY,
            between=lambda: self.write(f"{STORE}/q-0004.0001-their-question.md", theirs),
        )

        self.assertEqual(["q-0004.0002"], written.opened)
        self.assertEqual(theirs, self.read(f"{STORE}/q-0004.0001-their-question.md"))
        self.assertTrue((self.root / STORE / "q-0004.0002-my-question.md").is_file())


class Renaming(Declared):
    """A re-parent renames the subtree that moves, so every id keeps saying where its question
    sits (`.0020`'s decision 6): files, links, relations, session lines and bare ids follow."""

    def stems(self, folder: str = STORE) -> set[str]:
        return {path.stem for path in (self.root / folder).glob("q-*.md")}

    def test_a_move_renames_its_subtree_keeping_nested_positions_and_seating_flat_ones_after_them(self) -> None:
        self.called("open", "Who runs the mover?", "--under", "q-0007")
        self.question("q-0007.0002-is-it-archived", "Is it archived?", "q-0007", "closed:moot", "gone", folder=f"{STORE}/done")

        said = self.called("move", "q-0007", "--under", "q-0002")

        self.assertIn("renamed q-0007 → q-0002.0001", said)
        live, archived = self.stems(), self.stems(f"{STORE}/done")
        self.assertLessEqual(
            {
                "q-0002.0001-who-moves-a-subtree",
                "q-0002.0001.0001-who-runs-the-mover",
                "q-0002.0001.0003-does-the-mover-repair-links",
            },
            live,
        )
        self.assertIn("q-0002.0001.0002-is-it-archived", archived)
        self.assertEqual([], [stem for stem in live | archived if stem.startswith("q-0007") or stem.startswith("q-0013")])
        self.assertEqual("q-0002.0001", self.part("q-0002.0001.0003-does-the-mover-repair-links", "part of"))

    def test_links_and_bare_ids_across_the_docs_follow_the_rename_and_nothing_longer_is_touched(self) -> None:
        self.called("open", "Who runs the mover?", "--under", "q-0007")
        self.write(
            "docs/notes.md",
            "See [the subtree](questions/q-0007-who-moves-a-subtree.md), q-0007 and `q-0007.0001`,\n"
            "not q-00070, faq-0007 or q-0070.\n",
        )

        self.called("move", "q-0007", "--under", "q-0002")

        self.assertEqual(
            "See [the subtree](questions/q-0002.0001-who-moves-a-subtree.md), q-0002.0001 and `q-0002.0001.0001`,\n"
            "not q-00070, faq-0007 or q-0070.\n",
            self.read("docs/notes.md"),
        )

    def test_an_id_inside_a_fenced_block_is_an_example_and_is_left_as_written(self) -> None:
        sample = "Before.\n\n```md\n# q-0041 A sample\n\n- **part of** q-0007\n```\n\nAfter q-0007.\n"
        self.write("docs/sample.md", sample)

        self.called("move", "q-0007", "--under", "q-0002")

        self.assertEqual(sample.replace("After q-0007.", "After q-0002.0001."), self.read("docs/sample.md"))

    def test_relations_and_every_sessions_line_name_the_new_ids(self) -> None:
        self.called("depend", "q-0004", "--on", "q-0007")
        self.write(
            SESSIONS,
            self.read(SESSIONS).replace("s-beta running 2026-09-28 q-0010", "s-beta running 2026-09-28 q-0007 q-0013,q-0010"),
        )

        self.called("move", "q-0007", "--under", "q-0002")

        self.assertEqual("q-0002.0001", self.part("q-0004-which-parts-are-optional", "depends on"))
        self.assertEqual(
            "s-alpha running 2026-09-29 q-0004 q-0002,q-0001\n"
            "s-beta running 2026-09-28 q-0002.0001 q-0002.0001.0001,q-0010\n"
            "s-gamma ended 2026-09-20 q-0003\n",
            self.read(SESSIONS),
        )

    def test_between_renames_the_lower_subtree_under_the_new_question(self) -> None:
        self.called("open", "What must an entry hold?", "--between", "q-0002", "q-0004")

        self.assertLessEqual(
            {
                "q-0002.0001-what-must-an-entry-hold",
                "q-0002.0001.0001-which-parts-are-optional",
                "q-0002.0001.0001.0001-is-the-lean-optional",
            },
            self.stems(),
        )
        self.assertEqual("s-alpha running 2026-09-29 q-0002.0001.0001 q-0002,q-0001", self.own_line())

    def test_a_move_to_the_parent_a_fitting_question_already_has_writes_nothing(self) -> None:
        self.called("open", "Is the owner optional?", "--under", "q-0002")
        untouched = self.snapshot()

        self.called("move", "q-0002.0001", "--under", "q-0002")

        self.assertEqual(untouched, self.snapshot())

    def test_a_move_to_its_own_parent_seats_a_flat_id(self) -> None:
        self.called("move", "q-0004", "--under", "q-0002")

        self.assertIn("q-0002.0001-which-parts-are-optional", self.stems())
        self.assertIn("q-0002.0001.0001-is-the-lean-optional", self.stems())

    def test_a_rename_the_mover_refuses_writes_nothing(self) -> None:
        (self.root / "docs" / "unreadable.md").write_bytes(b"\xff\xfe not utf-8\n")

        self.assertRefused("not UTF-8", "move", "q-0007", "--under", "q-0002")

    def test_a_later_clause_naming_an_id_the_rename_changed_refuses_the_declaration(self) -> None:
        untouched = self.snapshot()

        with self.assertRaises(questions.Refused) as refused:
            questions.declare(
                self.root,
                "s-alpha",
                [questions.Clause("moves", "q-0007", other="q-0002"), questions.Clause("leans", "q-0007", text="late")],
                TODAY,
            )

        self.assertIn("no entry holds q-0007", str(refused.exception))
        self.assertEqual(untouched, self.snapshot())


class TheBody(Declared):
    """An entry holds its own argument after its parts, written by hand and kept by every call as
    it found it (`.0020`'s decision 3)."""

    BODY = "The argument, with `code` and\n\n- **lean** a line shaped like a part.\n"

    def argue(self, stem: str, body: str = BODY) -> None:
        self.write(f"{STORE}/{stem}.md", self.entry_text(stem) + "\n" + body)

    def body_of(self, stem: str) -> str:
        return self.entry_text(stem).split("\n\n", 2)[2]

    def test_survives_every_call_that_rewrites_the_entry(self) -> None:
        self.argue("q-0007-who-moves-a-subtree")

        for call in (
            ("lean", "q-0007", "a lean"),
            ("suspect", "q-0007"),
            ("clear", "q-0007"),
            ("assign", "q-0007", "docs/record.md"),
            ("at", "q-0007"),
            ("close", "q-0007", "moot", "the mover does it"),
        ):
            self.called(*call)
            self.assertEqual(self.BODY, self.body_of("q-0007-who-moves-a-subtree"), call)

    def test_survives_a_strike(self) -> None:
        self.argue("q-0007-who-moves-a-subtree")
        self.call("at", "q-0007")

        self.call("at", "q-0007", now=NOW + timedelta(hours=13))

        self.assertIn("- **struck** 1,", self.entry_text("q-0007-who-moves-a-subtree"))
        self.assertEqual(self.BODY, self.body_of("q-0007-who-moves-a-subtree"))

    def test_survives_a_rename_its_renamed_ids_rewritten_outside_fences(self) -> None:
        self.argue("q-0007-who-moves-a-subtree", "Argued against q-0013.\n\n```\nq-0013 as a sample\n```\n")

        self.called("move", "q-0007", "--under", "q-0002")

        self.assertEqual(
            "Argued against q-0002.0001.0001.\n\n```\nq-0013 as a sample\n```\n",
            self.body_of("q-0002.0001-who-moves-a-subtree"),
        )

    def test_a_line_shaped_like_a_part_in_the_body_is_not_one(self) -> None:
        before = self.problems()
        self.argue("q-0010-how-do-sessions-reach-each-other")

        read = questions.read_store(self.root).index["q-0010"]

        self.assertNotIn("lean", read.parts)
        self.assertEqual(before, self.problems())

    def test_a_line_glued_to_the_parts_is_still_reported(self) -> None:
        self.write(
            f"{STORE}/q-0010-how-do-sessions-reach-each-other.md",
            self.entry_text("q-0010-how-do-sessions-reach-each-other") + "glued to the parts\n",
        )

        self.assertTrue(any("not one of its parts" in problem for problem in self.problems()), self.problems())

    def test_a_hand_edit_to_the_body_meanwhile_refuses_the_call_and_keeps_the_edit(self) -> None:
        self.argue("q-0007-who-moves-a-subtree")
        edited = self.entry_text("q-0007-who-moves-a-subtree") + "One more line.\n"

        with self.assertRaises(questions.Refused) as refused:
            questions.declare(
                self.root,
                "s-alpha",
                [questions.Clause("leans", "q-0007", text="mine")],
                TODAY,
                between=lambda: self.write(f"{STORE}/q-0007-who-moves-a-subtree.md", edited),
            )

        self.assertIn("changed since this call read it", str(refused.exception))
        self.assertEqual(edited, self.entry_text("q-0007-who-moves-a-subtree"))


class ArchivingAtClosure(Declared):
    """A `close` that finishes a subtree moves it to `done/` in the same call; the maintainer's
    move is the sweep for what a closure left behind (parent decision 34, amended)."""

    def archived(self) -> set[str]:
        return {path.stem for path in (self.root / STORE / "done").glob("q-*.md")}

    def test_a_close_that_finishes_a_subtree_moves_it_and_every_link_follows(self) -> None:
        self.write("docs/notes.md", "See [the sessions](questions/q-0010-how-do-sessions-reach-each-other.md).\n")

        said = self.called("close", "q-0010", "moot", "one tree, one directory")

        self.assertIn("moved q-0010 to done/", said)
        self.assertIn("q-0010-how-do-sessions-reach-each-other", self.archived())
        self.assertEqual(
            "See [the sessions](questions/done/q-0010-how-do-sessions-reach-each-other.md).\n", self.read("docs/notes.md")
        )

    def test_a_close_with_an_open_child_moves_nothing_until_the_child_closes_then_both(self) -> None:
        self.called("open", "Across machines?", "--under", "q-0010")

        self.assertNotIn("moved", self.called("close", "q-0010", "moot", "one tree, one directory"))
        said = self.called("close", "q-0010.0001", "moot", "no second machine")

        self.assertIn("moved q-0010, q-0010.0001 to done/", said)
        self.assertLessEqual({"q-0010-how-do-sessions-reach-each-other", "q-0010.0001-across-machines"}, self.archived())

    def test_a_deferred_child_keeps_its_subtree_live(self) -> None:
        self.called("open", "Across machines?", "--under", "q-0010")
        self.called("close", "q-0010.0001", "deferred", "until a second machine, meanwhile one tree")

        said = self.called("close", "q-0010", "moot", "one tree, one directory")

        self.assertNotIn("moved", said)
        self.assertEqual(set(), self.archived() & {"q-0010-how-do-sessions-reach-each-other"})

    def test_a_move_the_mover_refuses_leaves_the_closure_written_and_says_why(self) -> None:
        (self.root / "docs" / "unreadable.md").write_bytes(b"\xff\xfe not utf-8\n")

        status, said = self.call("close", "q-0010", "moot", "one tree, one directory")

        self.assertEqual(1, status, said)
        self.assertIn("not UTF-8", said)
        self.assertEqual("closed:moot", self.part("q-0010-how-do-sessions-reach-each-other", "state"))


class Strikes(Declared):
    """A held question reached again twelve hours or more after its last stamp is struck; any
    other reach writes nothing to it (parent decisions 53 and 54)."""

    def at(self, identity: str, hours: float = 0, session: str = "s-alpha") -> None:
        status, said = self.call("at", identity, session=session, now=NOW + timedelta(hours=hours))
        self.assertEqual(0, status, said)

    def stamped(self, hours: float, count: int = 0) -> str:
        return f"{count}, last {NOW + timedelta(hours=hours):%Y-%m-%dT%H:%M}Z"

    def test_opening_stamps_zero_and_an_at_soon_after_does_not_strike(self) -> None:
        self.called("open", "Is the owner optional?", "--under", "q-0004")
        self.at("q-0004.0001", hours=0.02)

        self.assertEqual(self.stamped(0), self.part("q-0004.0001-is-the-owner-optional", "struck"))

    def test_an_entry_older_than_the_count_is_stamped_at_its_first_reach_and_not_struck(self) -> None:
        self.at("q-0007")

        self.assertEqual(self.stamped(0), self.part("q-0007-who-moves-a-subtree", "struck"))

    def test_a_reach_twelve_hours_on_strikes_once_and_restamps(self) -> None:
        self.at("q-0007")
        self.at("q-0007", hours=12)
        self.at("q-0007", hours=12)

        self.assertEqual(self.stamped(12, count=1), self.part("q-0007-who-moves-a-subtree", "struck"))

    def test_a_reach_short_of_twelve_hours_writes_nothing(self) -> None:
        self.at("q-0007")
        before = self.snapshot()

        self.at("q-0007", hours=11 + 59 / 60)

        self.assertEqual(before, self.snapshot())

    def test_a_stamp_ahead_of_the_clock_does_not_strike(self) -> None:
        self.write(
            f"{STORE}/q-0007-who-moves-a-subtree.md",
            entry("q-0007", "Who moves a subtree?", {"part of": "q-0003", "state": "open", "struck": self.stamped(5)}),
        )

        self.at("q-0007")

        self.assertEqual(self.stamped(5), self.part("q-0007-who-moves-a-subtree", "struck"))

    def test_ordinary_reaches_leave_the_store_as_it_was_and_the_window_unchanged(self) -> None:
        self.at("q-0004")
        self.said("--window", "--session", "s-alpha")
        before = self.snapshot()

        for hours in (1, 3, 5, 8, 11):
            self.at("q-0004", hours=hours)
        _, window = self.said("--window", "--session", "s-alpha")

        self.assertEqual(before, self.snapshot())
        self.assertIn("window unchanged", window)

    def test_a_question_struck_is_not_struck_again_by_another_session_soon_after(self) -> None:
        self.at("q-0007")
        self.at("q-0007", hours=12)

        self.at("q-0007", hours=12.5, session="s-beta")

        self.assertEqual(self.stamped(12, count=1), self.part("q-0007-who-moves-a-subtree", "struck"))

    def test_a_strike_raced_by_another_write_to_the_entry_is_refused_and_keeps_theirs(self) -> None:
        self.at("q-0007")
        theirs = entry("q-0007", "Who moves a subtree?", {"part of": "q-0003", "state": "open", "lean": "theirs"})

        with self.assertRaises(questions.Refused):
            questions.declare(
                self.root,
                "s-alpha",
                [questions.Clause("at", "q-0007")],
                TODAY,
                between=lambda: self.write(f"{STORE}/q-0007-who-moves-a-subtree.md", theirs),
                now=NOW + timedelta(hours=12),
            )

        self.assertEqual(theirs, self.entry_text("q-0007-who-moves-a-subtree"))


class Naming(Declared):
    def test_names_a_long_question_with_every_word(self) -> None:
        question = (
            "Does a question whose words run well past the old forty character cut keep every one "
            "of them in its name when the listing shows it?"
        )
        slug = "-".join(questions._words(question))
        self.assertTrue(120 < len(slug) <= questions.SLUG_LENGTH, len(slug))

        self.called("open", question)

        self.assertTrue((self.root / STORE / f"q-0014-{slug}.md").is_file())

    def test_cuts_a_question_past_the_length_at_a_word_boundary(self) -> None:
        words = [f"word{number:02d}" for number in range(40)]

        self.called("open", f"{' '.join(words)}?")

        [named] = [name.name for name in (self.root / STORE).glob("q-0014-*.md")]
        slug = named[len("q-0014-") : -len(".md")]
        self.assertLessEqual(len(slug), questions.SLUG_LENGTH)
        self.assertGreater(len(slug) + len("-word00"), questions.SLUG_LENGTH, "cut no earlier than it must")
        self.assertEqual(words[: len(slug.split("-"))], slug.split("-"), "whole words, the question's first")


class ThePath(Store):
    """A path that would pass the platform's limit cuts the slug at a word boundary, never the id;
    the limit is measured in `done/`, the longer of an entry's two homes."""

    def seed(self) -> None:
        super().seed()
        self.write(SESSIONS, "s-alpha running 2026-09-29 q-0001\n")

    def called(self, *argv: str) -> None:
        said = io.StringIO()
        with contextlib.redirect_stdout(said):
            status = questions.main([*argv, "--session", "s-alpha"], root=self.root, today=TODAY, now=NOW)
        self.assertEqual(0, status, said.getvalue())

    def limited(self, name: str, slug_room: int):
        prefix = str(self.root / STORE / "done" / f"{name}-")
        return mock.patch.object(questions, "PATH_LIMIT", len(prefix) + slug_room + len(".md"))

    def test_an_opened_question_is_named_with_the_words_that_fit_and_checks_clean(self) -> None:
        with self.limited("q-0002", 10):
            self.called("open", "Does a long question fit?")

            self.assertTrue((self.root / STORE / "q-0002-does-a.md").is_file())
            self.assertEqual([], self.problems())

    def test_a_rename_that_deepens_past_the_limit_cuts_the_same_way(self) -> None:
        self.place("q-0002-who-moves-a-subtree", "Who moves a subtree?", {"state": "open"})

        with self.limited("q-0001.0002", len("who-moves")):
            self.called("move", "q-0002", "--under", "q-0001")

            self.assertTrue((self.root / STORE / "q-0001.0002-who-moves.md").is_file())
            self.assertEqual([], self.problems())


class ClosingByKind(Declared):
    """The kinds `TheCalls` does not close by: each takes its own pointer."""

    def test_deferred_with_its_condition_and_default(self) -> None:
        self.called("close", "q-0007", "deferred", "until the mover exists, meanwhile by hand")

        self.assertEqual("until the mover exists, meanwhile by hand", self.part("q-0007-who-moves-a-subtree", "answer"))

    def test_merged_into_another(self) -> None:
        self.called("close", "q-0007", "merged", "q-0003")

        self.assertEqual("closed:merged", self.part("q-0007-who-moves-a-subtree", "state"))
        self.assertEqual("q-0003", self.part("q-0007-who-moves-a-subtree", "answer"))

    def test_a_suspect_flag_on_a_closed_question_is_set_and_cleared(self) -> None:
        self.called("suspect", "q-0005")
        self.called("clear", "q-0008")

        self.assertEqual("closed:decided, suspect", self.part("q-0005-is-the-id-a-path", "state"))
        self.assertEqual("closed:decided", self.part("q-0008-is-the-lean-optional", "state"))


class Refusals(Declared):
    """What the store refuses whatever form the call takes."""

    def test_an_id_a_rename_took_away_says_to_draw_the_window_again(self) -> None:
        self.called("move", "q-0007", "--under", "q-0002")

        self.assertRefused("draw the window again", "at", "q-0007")

    def test_a_question_nobody_holds(self) -> None:
        self.assertRefused("no entry holds q-0099", "lean", "q-0099", "a lean")

    def test_a_between_whose_lower_is_not_part_of_the_upper(self) -> None:
        self.assertRefused("q-0004 is not part of q-0003", "open", "Misplaced?", "--between", "q-0003", "q-0004")

    def test_a_move_that_makes_a_cycle(self) -> None:
        self.assertRefused("cycle", "move", "q-0002", "--under", "q-0004")

    def test_a_dependency_that_makes_a_cycle(self) -> None:
        self.called("depend", "q-0004", "--on", "q-0003")

        self.assertRefused("cycle", "depend", "q-0003", "--on", "q-0004")

    def test_a_prune_that_leaves_an_open_child(self) -> None:
        self.assertRefused("leaves q-0007 open", "close", "q-0003", "pruned", "not worth holding")

    def test_a_kind_without_its_pointer(self) -> None:
        self.assertRefused("no answer", "close", "q-0004", "decided")

    def test_a_decided_answer_that_does_not_resolve(self) -> None:
        self.assertRefused("does not resolve", "close", "q-0004", "decided", "[gone](../gone.md)")

    def test_a_session_nobody_registered(self) -> None:
        self.assertRefused("no session s-nobody", "at", "q-0004", session="s-nobody")


class Interference(Declared):
    """What another writer does between a call's validation and its write."""

    def declare_with(self, clauses: list[questions.Clause], meanwhile) -> None:
        questions.declare(self.root, "s-alpha", clauses, TODAY, between=meanwhile)

    def test_an_entry_changed_on_disk_refuses_the_call_and_keeps_the_other_writers_text(self) -> None:
        intruder = entry("q-0004", "Which parts are optional?", {"part of": "q-0002", "state": "open", "lean": "theirs"})
        before = self.snapshot()

        with self.assertRaises(questions.Refused) as refused:
            self.declare_with(
                [questions.Clause("leans", "q-0004", text="mine")],
                lambda: self.write(f"{STORE}/q-0004-which-parts-are-optional.md", intruder),
            )

        self.assertIn("changed since this call read it", str(refused.exception))
        self.assertEqual(intruder, self.entry_text("q-0004-which-parts-are-optional"))
        after = self.snapshot()
        del before[f"{STORE}/q-0004-which-parts-are-optional.md"], after[f"{STORE}/q-0004-which-parts-are-optional.md"]
        self.assertEqual(before, after, "nothing else was written")

    def test_an_open_raced_past_its_attempts_is_refused_and_writes_nothing_of_its_own(self) -> None:
        theirs = entry("q-0014", "Their question?", {"state": "open"})

        with mock.patch.object(questions, "OPEN_ATTEMPTS", 1), self.assertRaises(questions.Taken):
            self.declare_with(
                [questions.Clause("opens", text="My question?")],
                lambda: self.write(f"{STORE}/q-0014-their-question.md", theirs),
            )

        self.assertEqual([], list((self.root / STORE).glob("*-my-question.md")))

    def test_a_sessions_at_changes_its_own_line_and_keeps_one_another_session_wrote_meanwhile(self) -> None:
        def beta_moves() -> None:
            self.write(SESSIONS, self.read(SESSIONS).replace("s-beta running 2026-09-28 q-0010", "s-beta running 2026-09-29 q-0001 q-0010"))

        self.declare_with([questions.Clause("at", "q-0002")], beta_moves)

        self.assertEqual(
            "s-alpha running 2026-09-29 q-0002 q-0004,q-0001\n"
            "s-beta running 2026-09-29 q-0001 q-0010\n"
            "s-gamma ended 2026-09-20 q-0003\n",
            self.read(SESSIONS),
        )

    def test_a_write_that_fails_partway_stops_and_reports_what_it_wrote(self) -> None:
        def sessions_file_becomes_a_folder() -> None:
            (self.root / SESSIONS).unlink()
            (self.root / SESSIONS).mkdir()

        with self.assertRaises(questions.WriteInterrupted) as stopped:
            self.declare_with(
                [questions.Clause("at", "q-0004"), questions.Clause("leans", "q-0004", text="written first")],
                sessions_file_becomes_a_folder,
            )

        self.assertEqual([f"{STORE}/q-0004-which-parts-are-optional.md"], stopped.exception.completed)
        self.assertEqual(SESSIONS, stopped.exception.failed)
        self.assertIn("written first", self.entry_text("q-0004-which-parts-are-optional"))


class InOrder(Declared):
    def test_clauses_apply_in_order_and_at_is_checked_against_the_result(self) -> None:
        """The writer's front door takes a list, as a judge's typed value will reach it."""
        written = questions.declare(
            self.root,
            "s-alpha",
            [
                questions.Clause("at", "q-0004.0002"),
                questions.Clause("opens", other="q-0004", text="Is the owner optional?"),
                questions.Clause("opens", other="q-0004", text="Is the owner required at birth?"),
                questions.Clause("closes", "q-0004.0001", other="merged", text="q-0004.0002"),
            ],
            TODAY,
        )

        self.assertEqual(["q-0004.0001", "q-0004.0002"], written.opened)
        self.assertIn(
            "- **state** closed:merged\n- **answer** q-0004.0002",
            self.read(f"{STORE}/done/q-0004.0001-is-the-owner-optional.md"),
            "the merge finished its subtree, so it moved",
        )
        self.assertIn("- **state** open", self.entry_text("q-0004.0002-is-the-owner-required-at-birth"))
        self.assertEqual("q-0004.0002", self.own_line().split()[3])

    def test_a_prune_goes_through_once_the_child_that_stands_alone_is_moved_out_first(self) -> None:
        self.called("move", "q-0007", "--to-root")
        self.called("close", "q-0003", "pruned", "archiving is the mover's")

        self.assertIn("closed:pruned", self.entry_text("q-0003-how-is-a-subtree-archived"))


class ARoundTrip(Declared):
    def test_opens_attaches_closes_and_prunes_and_leaves_no_problem_behind(self) -> None:
        before = self.problems()

        for call in (
            ("open", "Is the owner optional?", "--under", "q-0004"),
            ("at", "q-0004.0001"),
            ("open", "Must an owner exist at birth?", "--under", "q-0004.0001"),
            ("close", "q-0004.0001.0001", "decided", "[the record](../record.md) — the user, 2026-09-29"),
            ("at", "q-0004"),
            ("close", "q-0004.0001", "pruned", "the store keeps no owner rule"),
        ):
            self.called(*call)

        self.assertEqual(before, self.problems(), "the fixture's flat ids are reported as before, and nothing more")
        self.assertIn("closed:pruned", self.read(f"{STORE}/done/q-0004.0001-is-the-owner-optional.md"))
        self.assertNotIn("q-0004.0001", self.said("--tree", "q-0004")[1], "the finished subtree left the live tree")


class Hooked(Rendered):
    """What each host's hook receives and what it gets back."""

    def hook(self, host: str, payload: dict | str) -> tuple[int, str]:
        stdin = io.StringIO(payload if isinstance(payload, str) else json.dumps(payload))
        out = io.StringIO()
        with contextlib.redirect_stdout(out), mock.patch("sys.stdin", stdin):
            status = questions.main(["--hook", host], root=self.root, today=TODAY)
        return status, out.getvalue()

    def context(self, said: str) -> str:
        """The text a host would place in the agent's context from the hook's answer."""
        answer = json.loads(said)
        if "hookSpecificOutput" in answer:
            return answer["hookSpecificOutput"]["additionalContext"]
        return answer["additional_context"]


class TheHook(Hooked):
    def test_claude_code_registers_a_new_session_under_its_own_id_and_injects_the_wake(self) -> None:
        status, said = self.hook("claude-code", {"session_id": "abc-123", "hook_event_name": "SessionStart", "source": "startup"})

        self.assertEqual(0, status)
        self.assertEqual("SessionStart", json.loads(said)["hookSpecificOutput"]["hookEventName"])
        self.assertIn("session: abc-123, registered now", self.context(said))
        self.assertIn("abc-123 running 2026-09-29 -", self.read(SESSIONS))

    def test_a_resumed_session_is_not_registered_twice(self) -> None:
        _, said = self.hook("claude-code", {"session_id": "s-alpha", "hook_event_name": "SessionStart", "source": "resume"})

        self.assertIn("session: s-alpha, already registered", self.context(said))
        self.assertEqual(3, len(self.read(SESSIONS).splitlines()))

    def test_a_message_gets_the_window_and_then_one_line_while_nothing_moved(self) -> None:
        submit = {"session_id": "s-alpha", "hook_event_name": "UserPromptSubmit", "prompt": "next"}

        _, first = self.hook("codex", submit)
        _, second = self.hook("codex", submit)

        self.assertIn("current: q-0004", self.context(first))
        self.assertEqual("UserPromptSubmit", json.loads(first)["hookSpecificOutput"]["hookEventName"])
        self.assertIn("window unchanged since your last one", self.context(second))
        self.assertIn("place this message with `questions.py at q-0004 --session s-alpha`", self.context(second))
        self.assertNotIn("path (root to current):", self.context(second))

    def test_a_moved_position_or_a_changed_entry_draws_the_window_again(self) -> None:
        submit = {"session_id": "s-alpha", "hook_event_name": "UserPromptSubmit", "prompt": "next"}
        self.hook("claude-code", submit)
        self.said("at", "q-0002", "--session", "s-alpha")

        _, moved = self.hook("claude-code", submit)
        self.said("lean", "q-0007", "by hand", "--session", "s-beta")
        _, changed = self.hook("claude-code", submit)

        self.assertIn("current: q-0002", self.context(moved))
        self.assertIn("path (root to current):", self.context(changed))

    def test_another_sessions_move_alone_does_not_redraw_it(self) -> None:
        """q-0007 is stamped first, since the first reach of an entry older than the count writes
        its stamp, which is a change to the entry and so redraws."""
        submit = {"session_id": "s-alpha", "hook_event_name": "UserPromptSubmit", "prompt": "next"}
        self.said("at", "q-0007", "--session", "s-beta")
        self.said("at", "q-0010", "--session", "s-beta")
        self.hook("claude-code", submit)
        self.assertEqual(0, self.said("at", "q-0007", "--session", "s-beta")[0], "the other session moved")

        _, said = self.hook("claude-code", submit)

        self.assertIn("window unchanged", self.context(said))

    def test_a_compaction_makes_the_next_window_whole(self) -> None:
        submit = {"session_id": "s-alpha", "hook_event_name": "UserPromptSubmit", "prompt": "next"}
        self.hook("claude-code", submit)

        _, compacted = self.hook("claude-code", {"session_id": "s-alpha", "hook_event_name": "SessionStart", "source": "compact"})
        self.hook("codex", {"session_id": "s-alpha", "hook_event_name": "UserPromptSubmit", "prompt": "next"})
        _, codex_compacts = self.hook("codex", {"session_id": "s-alpha", "hook_event_name": "PostCompact", "trigger": "auto"})
        _, after = self.hook("codex", submit)

        self.assertIn("path (root to current):", self.context(compacted))
        self.assertEqual("", codex_compacts.strip())
        self.assertIn("path (root to current):", self.context(after))

    def test_cursor_registers_under_its_conversation_id_and_answers_in_its_own_form(self) -> None:
        _, said = self.hook(
            "cursor", {"conversation_id": "conv-9", "session_id": "other", "hook_event_name": "sessionStart"}
        )

        self.assertIn("session: conv-9, registered now", self.context(said))
        self.assertIn("conv-9 running", self.read(SESSIONS))

    def raw_hook(self, host: str, raw: bytes) -> str:
        """The hook fed bytes as a host's pipe carries them, decoded by nothing in between."""
        out = io.StringIO()
        with contextlib.redirect_stdout(out), mock.patch("sys.stdin", io.TextIOWrapper(io.BytesIO(raw))):
            questions.main(["--hook", host], root=self.root, today=TODAY)
        return out.getvalue()

    def test_input_written_as_utf16_with_its_mark_is_read(self) -> None:
        """Cursor on Windows answered "Expecting value: line 1 column 1 (char 0)" to a payload it
        logged as sent: input in another encoding than the code page the pipe was read in."""
        sent = json.dumps({"conversation_id": "conv-16", "hook_event_name": "sessionStart"})

        said = self.raw_hook("cursor", sent.encode("utf-16"))

        self.assertIn("session: conv-16, registered now", self.context(said))

    def test_input_written_as_utf8_with_its_mark_is_read(self) -> None:
        sent = json.dumps({"conversation_id": "conv-8", "hook_event_name": "sessionStart"})

        said = self.raw_hook("cursor", sent.encode("utf-8-sig"))

        self.assertIn("session: conv-8, registered now", self.context(said))

    def test_input_that_is_not_json_is_named_by_its_length_and_how_it_begins(self) -> None:
        said = self.raw_hook("claude-code", b"")

        self.assertIn("the hook's input is not JSON: 0 characters", said)

    def test_cursor_hands_its_session_on_to_later_hooks_and_shells_as_env(self) -> None:
        _, said = self.hook("cursor", {"conversation_id": "conv-9", "hook_event_name": "sessionStart"})

        self.assertEqual({"QUESTIONS_SESSION": "conv-9"}, json.loads(said)["env"])

    def test_cursor_compaction_forgets_the_last_window(self) -> None:
        self.said("--window", "--session", "s-alpha")

        _, said = self.hook("cursor", {"conversation_id": "s-alpha", "hook_event_name": "preCompact"})
        _, window = self.said("--window", "--session", "s-alpha")

        self.assertEqual("{}", said.strip())
        self.assertIn("path (root to current):", window)

    def test_a_session_whose_start_was_never_seen_is_registered_by_its_first_message(self) -> None:
        _, said = self.hook("claude-code", {"session_id": "late-1", "hook_event_name": "UserPromptSubmit", "prompt": "hi"})

        self.assertIn("late-1 running 2026-09-29 -", self.read(SESSIONS))
        self.assertIn("session: late-1", self.context(said))

    def test_an_event_it_has_no_use_for_answers_nothing(self) -> None:
        status, said = self.hook("claude-code", {"session_id": "s-alpha", "hook_event_name": "Stop"})

        self.assertEqual((0, ""), (status, said.strip()))

    def test_a_problem_at_a_known_event_is_answered_in_the_hosts_own_form(self) -> None:
        status, said = self.hook("cursor", {"hook_event_name": "sessionStart"})

        self.assertEqual(0, status)
        self.assertIn("questions hook", self.context(said))

    def test_never_fails_the_host_a_problem_becomes_a_notice_in_context(self) -> None:
        for host, payload in (("claude-code", "not json"), ("nohost", {"session_id": "x", "hook_event_name": "SessionStart"})):
            with self.subTest(host=host):
                status, said = self.hook(host, payload)

                self.assertEqual(0, status)
                self.assertIn("questions hook", said)


class TheAgentsOwnWindow(Hooked):
    def test_says_unchanged_when_nothing_moved_and_draws_it_whole_on_request(self) -> None:
        self.said("--window", "--session", "s-alpha")

        _, again = self.said("--window", "--session", "s-alpha")
        _, full = self.said("--window", "--session", "s-alpha", "--full")

        self.assertIn("window unchanged since your last one", again)
        self.assertIn("--full", again)
        self.assertIn("path (root to current):", full)

    def test_a_call_it_does_not_know_prints_the_calls_it_does(self) -> None:
        status, said = self.said("go", "q-0010", "--session", "s-alpha")

        self.assertEqual(2, status)
        self.assertIn("at, open, move, depend, undepend, close", said)


class AFirstWake(RepositoryCase):
    def setUp(self) -> None:
        super().setUp()
        remember_windows_in_the_case(self)

    def test_in_a_tree_without_a_store_registers_the_first_session(self) -> None:
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            status = questions.main(["--wake"], root=self.root, today=TODAY)

        tag = out.getvalue().splitlines()[0].split()[1].rstrip(",")
        self.assertEqual(0, status)
        self.assertEqual(f"{tag} running 2026-09-29 -\n", self.read(SESSIONS))


class NoStoreToDraw(RepositoryCase):
    def test_the_window_says_there_is_no_store_and_exits_zero(self) -> None:
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            status = questions.main(["--window", "--session", "s-alpha"], root=self.root)

        self.assertEqual(0, status)
        self.assertIn("no store", out.getvalue())


class NoStore(RepositoryCase):
    def test_a_tree_without_a_store_says_so_and_exits_zero(self) -> None:
        said = io.StringIO()
        with contextlib.redirect_stdout(said):
            status = questions.main(["--check"], root=self.root)

        self.assertEqual(0, status)
        self.assertEqual("absent", json.loads(said.getvalue())["store"])


if __name__ == "__main__":
    unittest.main()
