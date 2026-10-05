# Ticket evidence

## Reconciliation assignment routing — 2026-10-05

The user approved adding the previously shown /ticket-to-/impact instruction to
/reconcile. P12 is authored in `.agents/mechanisms/ticket/ticket.rules.md` and
installed at /reconcile's Issue and report section. The installer generated the
block; the skill was not hand-edited. Tracker routing remains project-owned,
with the existing installation-first and approval contracts preserved.

The ticket declaration accounts for its new reader and handoff; the reconcile
declaration records its dependency and the moment the ticket mechanism owns.
The operator's next new-assignment preview should show a proposed split, its
impact assessment and the applicable breakdown approval before issue creation.
An in-scope update or evidence request in an existing assignment should reuse it
without a new breakdown. These are the semantic grading cases; they have not
yet been exercised by a future issue-creation pass.

Structural checks:

- Baseline injector: six rules files, no diagnostics, orphans or bad blocks.
- After authoring P12 but before installation: exactly one absent ticket block
  at /reconcile was diagnosed. The installer then installed that block and left
  its four other targets present.
- Live injector and mechanism checks: no diagnostics; no orphan/drifted blocks.
- Isolated temporary Git corpus: clean, missing block rejected, restored clean,
  altered impact instruction rejected as drift, restored clean — five assertions.
  No live target was altered by the negative cases.
- Full `harness.py . --check`: `arrived: false`. Injector and shape passed, both
  loader links resolved. Ref differences: the authorized ticket declaration and
  rules-file amendments, plus the previously recorded /align comparison
  limitation. The ref checker was not changed. The new source amendments are
  local divergence from `95535af` and must be preserved when updating core.

No issues, sibling changes, commits or pushes were made.

## Local reconciliation outcomes — 2026-10-05

The user accepted local tickets for the coordinating project's remaining outcomes,
with published project issues as possible outputs. P12 was amended at its authored
home and regenerated into /reconcile. Outcome-based slicing replaces automatic
division by finding or recipient. Existing assignments and routine factual
corrections retain the agreed exception.

The local ticket's criteria distinguish a published handoff from a working
integration. The ordinary ticket format and completion rules are unchanged. No
concrete breakdown was approved or minted in this amendment. Semantic effectiveness
will be assessed against the next actual breakdown and its delivered outputs;
structural installation alone does not establish that effectiveness.

The regenerated block and both declarations pass injector and mechanism checks.
The [reconciliation evidence](reconcile.evidence.md#local-delivery-before-project-publication--2026-10-05)
records the verification scope and the remaining upstream-reference differences.
