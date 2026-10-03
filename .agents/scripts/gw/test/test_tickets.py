"""Reading a live ticket's header and sections, and saying whether the record keeps its shape."""

from __future__ import annotations

import contextlib
import io
import json
import unittest

from repository import RepositoryCase

import tickets

LIVE = "docs/tickets/01-0002-live.md"
PLANNED = "docs/tickets/01-0003-planned.md"
RFC = "docs/rfc/01-0003-planned.md"


def ticket(
    header: str,
    sections: str = (
        "## What to build\n\nThe thing.\n\n"
        "## Acceptance criteria\n\n- [ ] It works.\n- [ ] `/verify` has been run.\n"
    ),
    title: str = "# A ticket",
) -> str:
    return f"{title}\n\n{header}\n{sections}"


INCEPTED = (
    "- **Status:** Ready\n"
    "- **Type:** HITL\n"
    "- **Depends on:** [an earlier one](./01-0001-earlier.md) (what it supplies)\n"
    "- **Outcome:** One sentence saying what lands.\n"
)
SHAPED = (
    "- **Status:** In progress\n"
    "- **Type:** AFK\n"
    "- **Plan:** [plan](../rfc/01-0003-planned.md) — what it selected\n"
    "- **Outcome:** One sentence saying what lands.\n"
)


class Records(RepositoryCase):
    """A tree with one incepted ticket, one shaped ticket and its RFC, all conforming."""

    def setUp(self) -> None:
        super().setUp()
        self.write("docs/tickets/README.md", "# Delivery status\n\n**Last updated:** never\n")
        self.write("docs/tickets/01-0001-earlier.md", ticket(INCEPTED))
        self.write(LIVE, ticket(INCEPTED))
        self.write(PLANNED, ticket(SHAPED))
        self.write(RFC, "# A ticket — implementation plan\n")

    def checked(self):
        return tickets.check(self.root)

    def problems(self) -> list[str]:
        return [note.problem for note in self.checked().diagnostics]

    def problem_lines(self) -> list[tuple[str, int]]:
        return [(note.record, note.line) for note in self.checked().diagnostics]


class TheHeader(Records):
    def test_written_bare_rather_than_as_a_bullet_list_is_reported_as_the_form(self) -> None:
        self.write(LIVE, ticket(INCEPTED.replace("- **", "**")))

        problems = self.problems()

        self.assertEqual(1, len(problems))
        self.assertIn("bullet list", problems[0])
        self.assertEqual([(LIVE, 3)], self.problem_lines())

    def test_missing_a_required_field_names_it(self) -> None:
        self.write(LIVE, ticket(INCEPTED.replace("- **Type:** HITL\n", "")))

        problems = self.problems()

        self.assertEqual(1, len(problems))
        self.assertIn("Type", problems[0])

    def test_allows_one_parenthetical_qualifier(self) -> None:
        self.write(LIVE, ticket(INCEPTED.replace("Ready", "Ready (aligned 2026-09-08)")))

        self.assertEqual([], self.problems())

    def test_done_must_open_its_parenthetical_with_the_date(self) -> None:
        self.write(LIVE, ticket(INCEPTED.replace("Ready", "Done (split)")))

        problems = self.problems()

        self.assertEqual(1, len(problems))
        self.assertIn("Done", problems[0])
        self.assertIn("date", problems[0])

    def test_done_dated_with_words_after_a_comma_is_fine(self) -> None:
        self.write(LIVE, ticket(INCEPTED.replace("Ready", "Done (2026-09-08, split)")))

        self.assertEqual([], self.problems())

    def test_with_a_type_outside_hitl_and_afk_is_reported(self) -> None:
        self.write(LIVE, ticket(INCEPTED.replace("HITL", "Pairing")))

        problems = self.problems()

        self.assertEqual(1, len(problems))
        self.assertIn("Pairing", problems[0])

    def test_carrying_kind_is_reported_since_it_is_no_longer_a_field(self) -> None:
        self.write(LIVE, ticket(INCEPTED.replace("- **Type:** HITL\n", "- **Type:** HITL\n- **Kind:** Maintenance\n")))

        problems = self.problems()

        self.assertEqual(1, len(problems))
        self.assertIn("Kind", problems[0])

    def test_with_outcome_before_another_field_is_reported(self) -> None:
        swapped = (
            "- **Status:** Ready\n"
            "- **Outcome:** One sentence saying what lands.\n"
            "- **Type:** HITL\n"
        )
        self.write(LIVE, ticket(swapped))

        problems = self.problems()

        self.assertEqual(1, len(problems))
        self.assertIn("Outcome", problems[0])
        self.assertIn("last", problems[0])

    def test_with_known_fields_out_of_the_shelfs_order_is_reported(self) -> None:
        swapped = (
            "- **Type:** HITL\n"
            "- **Status:** Ready\n"
            "- **Outcome:** One sentence saying what lands.\n"
        )
        self.write(LIVE, ticket(swapped))

        problems = self.problems()

        self.assertEqual(1, len(problems))
        self.assertIn("Status", problems[0])
        self.assertIn("order", problems[0])

    def test_a_one_off_field_may_sit_anywhere_before_outcome(self) -> None:
        self.write(
            LIVE,
            ticket(INCEPTED.replace("- **Type:** HITL\n", "- **Related:** [x](./01-0001-earlier.md)\n- **Type:** HITL\n")),
        )

        self.assertEqual([], self.problems())

    def test_with_an_outcome_of_two_sentences_is_reported(self) -> None:
        self.write(
            LIVE,
            ticket(INCEPTED.replace("One sentence saying what lands.", "Two sentences. The second one.")),
        )

        problems = self.problems()

        self.assertEqual(1, len(problems))
        self.assertIn("one sentence", problems[0])

    def test_reads_a_wrapped_bullet_as_one_value(self) -> None:
        self.write(
            LIVE,
            ticket(INCEPTED.replace("One sentence saying what lands.", "One sentence\n  saying what lands.")),
        )

        checked = self.checked()

        self.assertEqual([], checked.diagnostics)
        live = next(record for record in checked.records if record.record == LIVE)
        self.assertEqual("One sentence saying what lands.", live.fields["Outcome"])

    def test_with_a_link_that_does_not_resolve_is_reported(self) -> None:
        self.write(LIVE, ticket(INCEPTED.replace("01-0001-earlier.md", "01-0001-elsewhere.md")))

        problems = self.problems()

        self.assertEqual(1, len(problems))
        self.assertIn("01-0001-elsewhere.md", problems[0])

    def test_a_status_line_in_a_later_section_is_prose_not_header(self) -> None:
        self.write(
            LIVE,
            ticket(INCEPTED, sections="## What to build\n\n**Status:** Accepted, as prose.\n\n"
                   "## Acceptance criteria\n\n- [ ] `/verify` has been run.\n"),
        )

        self.assertEqual([], self.problems())


class ThePlanBullet(Records):
    def test_absent_while_an_rfc_exists_is_reported(self) -> None:
        self.write(PLANNED, ticket(SHAPED.replace("- **Plan:** [plan](../rfc/01-0003-planned.md) — what it selected\n", "")))

        problems = self.problems()

        self.assertEqual(1, len(problems))
        self.assertIn("Plan", problems[0])
        self.assertIn(RFC, problems[0])

    def test_present_while_no_rfc_exists_is_reported(self) -> None:
        self.write(LIVE, ticket(INCEPTED.replace("- **Type:** HITL\n", "- **Type:** HITL\n- **Plan:** [plan](../rfc/01-0002-live.md)\n")))

        problems = self.problems()

        self.assertEqual(1, len(problems))
        self.assertIn("Plan", problems[0])

    def test_pointing_at_another_file_than_the_rfc_is_reported(self) -> None:
        self.write(PLANNED, ticket(SHAPED.replace("../rfc/01-0003-planned.md", "./01-0002-live.md")))

        problems = self.problems()

        self.assertEqual(1, len(problems))
        self.assertIn("Plan", problems[0])
        self.assertIn(RFC, problems[0])


class TheSections(Records):
    def test_a_required_section_missing_is_reported(self) -> None:
        self.write(LIVE, ticket(INCEPTED, sections="## Acceptance criteria\n\n- [ ] `/verify` run.\n"))

        problems = self.problems()

        self.assertEqual(1, len(problems))
        self.assertIn("What to build", problems[0])

    def test_a_provisional_heading_is_read_as_the_criteria_section(self) -> None:
        self.write(
            LIVE,
            ticket(INCEPTED, sections="## What to build\n\nX.\n\n"
                   "## Acceptance criteria — provisional, firmed at the align\n\n- [ ] `/verify` run.\n"),
        )

        self.assertEqual([], self.problems())

    def test_a_shaped_ticket_with_a_second_unnamed_section_is_reported(self) -> None:
        self.write(
            PLANNED,
            ticket(SHAPED, sections="## Why this exists\n\nBecause.\n\n## Verification — 2026-09-08\n\nNotes.\n\n"
                   "## What to build\n\nThe thing.\n\n## Acceptance criteria\n\n- [ ] `/verify` run.\n"),
        )

        problems = self.problems()

        self.assertEqual(1, len(problems))
        self.assertIn("Verification — 2026-09-08", problems[0])

    def test_a_shaped_ticket_may_carry_one_narrative_section(self) -> None:
        self.write(
            PLANNED,
            ticket(SHAPED, sections="## Parent\n\nThe spec.\n\n## Why this exists\n\nBecause.\n\n"
                   "## What to build\n\nThe thing.\n\n## Open issues\n\n- One.\n\n"
                   "## Acceptance criteria\n\n- [ ] `/verify` run.\n\n## Out of scope\n\nThe rest.\n\n"
                   "## Parent scope addressed\n\nStories 1, 2.\n"),
        )

        self.assertEqual([], self.problems())

    def test_an_incepted_ticket_hosts_any_section(self) -> None:
        self.write(
            LIVE,
            ticket(INCEPTED, sections="## Why this exists\n\nBecause.\n\n## Input from elsewhere\n\nChunks.\n\n"
                   "## Verification — 2026-09-08\n\nNotes.\n\n"
                   "## What to build\n\nThe thing.\n\n## Acceptance criteria\n\n- [ ] `/verify` run.\n"),
        )

        self.assertEqual([], self.problems())

    def test_no_acceptance_box_naming_verify_is_reported_at_either_stage(self) -> None:
        self.write(LIVE, ticket(INCEPTED, sections="## What to build\n\nX.\n\n## Acceptance criteria\n\n- [ ] It works.\n"))

        problems = self.problems()

        self.assertEqual(1, len(problems))
        self.assertIn("/verify", problems[0])

    def test_a_shaped_ticket_with_prose_among_its_criteria_is_reported(self) -> None:
        self.write(
            PLANNED,
            ticket(SHAPED, sections="## What to build\n\nX.\n\n## Acceptance criteria\n\n"
                   "Firmed at the align.\n\n- [ ] It works,\n  wrapped.\n- [x] `/verify` run.\n"),
        )

        problems = self.problems()

        self.assertEqual(1, len(problems))
        self.assertIn("Firmed at the align.", problems[0])
        self.assertEqual([(PLANNED, 14)], self.problem_lines())

    def test_an_incepted_ticket_may_hold_prose_among_its_criteria(self) -> None:
        self.write(
            LIVE,
            ticket(INCEPTED, sections="## What to build\n\nX.\n\n## Acceptance criteria\n\n"
                   "Provisional, firmed at the align.\n\n- [ ] `/verify` run.\n"),
        )

        self.assertEqual([], self.problems())


class Pairing(Records):
    def test_a_live_rfc_whose_ticket_is_archived_is_reported(self) -> None:
        self.write("docs/tickets/done/01-0003-planned.md", self.read(PLANNED))
        (self.root / PLANNED).unlink()

        problems = self.problems()

        self.assertEqual(1, len(problems))
        self.assertIn(RFC, problems[0])
        self.assertIn("done", problems[0])

    def test_an_archived_rfc_whose_ticket_is_live_is_reported(self) -> None:
        self.write("docs/rfc/done/01-0003-planned.md", self.read(RFC))
        (self.root / RFC).unlink()
        self.write(PLANNED, ticket(SHAPED.replace("../rfc/", "../rfc/done/")))

        problems = self.problems()

        self.assertEqual(1, len(problems))
        self.assertIn("docs/rfc/done/01-0003-planned.md", problems[0])

    def test_an_rfc_naming_no_ticket_is_reported(self) -> None:
        self.write("docs/rfc/01-0009-orphan.md", "# Orphan — implementation plan\n")

        problems = self.problems()

        self.assertEqual(1, len(problems))
        self.assertIn("docs/rfc/01-0009-orphan.md", problems[0])
        self.assertIn("no ticket", problems[0])

    def test_a_closed_pair_is_matched_by_name_and_never_opened(self) -> None:
        self.write("docs/tickets/done/01-0004-closed.md", "**Status:** bare, and never read\n")
        self.write("docs/rfc/done/01-0004-closed.md", b"\xff\xfe not even text".decode("latin-1"))

        self.assertEqual([], self.problems())
        self.assertEqual([], self.checked().skipped)


class AnUnreadableRecord(Records):
    def test_is_skipped_with_its_reason_and_fails_the_run(self) -> None:
        (self.root / LIVE).write_bytes(b"\xff\xfe\x00 not utf-8")

        checked = self.checked()

        self.assertEqual([], checked.diagnostics)
        self.assertEqual(1, len(checked.skipped))
        self.assertEqual(LIVE, checked.skipped[0].record)
        self.assertIn("UTF-8", checked.skipped[0].why)

    def test_without_a_title_line_is_skipped_rather_than_misread(self) -> None:
        self.write(LIVE, "Not a title\n\n- **Status:** Ready\n")

        checked = self.checked()

        self.assertEqual(1, len(checked.skipped))
        self.assertIn("title", checked.skipped[0].why)


class TheCommandLine(Records):
    def invoke(self, *argv: str) -> tuple[int, str]:
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            status = tickets.main(list(argv), self.root)
        return status, out.getvalue()

    def test_refuses_a_bare_invocation_rather_than_choosing_a_mode(self) -> None:
        status, out = self.invoke()

        self.assertEqual(2, status)
        self.assertIn("usage", out)

    def test_reports_a_clean_tree_with_a_zero_status_and_its_records(self) -> None:
        status, out = self.invoke("--check")

        self.assertEqual(0, status)
        report = json.loads(out)
        self.assertEqual([], report["diagnostics"])
        self.assertEqual(3, len(report["records"]))

    def test_reports_a_violation_with_file_line_and_rule_and_a_non_zero_status(self) -> None:
        self.write(LIVE, ticket(INCEPTED.replace("Ready", "Nearly")))

        status, out = self.invoke("--check")

        self.assertEqual(1, status)
        diagnostics = json.loads(out)["diagnostics"]
        self.assertEqual(1, len(diagnostics))
        note = diagnostics[0]
        self.assertEqual(LIVE, note["record"])
        self.assertEqual(3, note["line"])
        self.assertIn("Nearly", note["problem"])

    def test_a_skip_alone_fails_the_run(self) -> None:
        (self.root / LIVE).write_bytes(b"\xff\xfe\x00")

        status, out = self.invoke("--check")

        self.assertEqual(1, status)
        self.assertEqual(1, len(json.loads(out)["skipped"]))


if __name__ == "__main__":
    unittest.main()
