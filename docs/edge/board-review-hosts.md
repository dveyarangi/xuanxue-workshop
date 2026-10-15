# Edge — Board review hosts

- **Status:** Normative

## Contract

The [assignment-review mechanism](../../.agents/mechanisms/review-assignments/review-assignments.md)
provides the mechanical CLI and periodic procedure for an attached full agent reviewer.
The caller supplies a repository, recipient labels, the authenticated GitHub client,
Python 3.12 or later and persistent local state. Local operator authority remains
in [L23](../../local.rules.md#l23--unattended-board-review-authority).

Discovery supplies candidates and source snapshots, not acceptance decisions. A host
claims a case, performs full review, prepares and confirms publication, then records
the processing position. Lost confirmation is recovered through the same publication
identifier. Incomplete delivery remains distinct from finished review.

Detector-first hosts make no model call for quiet or busy-only discovery. A configured
shared snapshot follows the review mechanism's REPORT.md format; complete replacements
reject a changed prior version. Operational updates preserve semantic results and
unresolved matters. Readers do not treat its timestamp as a fresh board read.

## Invariants

- Unchanged studied cases remain quiet across restart. *validated by:* `tests/test_board.py`
- Unconfirmed publication prevents completion and cannot trigger a blind retry. *validated by:* `tests/test_board.py`
- A changed case prevents stale publication and completion. *validated by:* `tests/test_board.py`
- Only one unexpired local claim owns a case. *validated by:* `tests/test_board.py`
- A foreign author's copied marker cannot confirm publication. *validated by:* `tests/test_board.py`
- Linked-evidence updates and due conditions do not require a new issue comment. *validated by:* `tests/test_board.py`
- Primary tracker failure remains explicit and local status remains available offline. *validated by:* `tests/test_board.py`
- Quiet or busy-only controller discovery makes no reviewer call. *validated by:* `tests/test_board_run.py`
- Invalid or stale shared-report replacement cannot destroy the prior report. *validated by:* `tests/test_board_run.py`
- Controller failures preserve unresolved report matters. *validated by:* `tests/test_board_run.py`

## Extending

1. **Discovery** — observe complete board discovery and read explicit source snapshots and evidence gaps.
2. **Review** — demonstrate full applicable methodology and distinguish a settled answer from an operator decision.
3. **Delivery recovery** — confirm a controlled response after losing local confirmation without another remote comment.
4. **Recurrence** — observe the selected host invoking the same procedure with preserved state and operator visibility.

## Extensions

| extension | standing | sidecar |
|---|---|---|
| Current Codex chat | live conformance being observed | [codex-chat](board-review-hosts/codex-chat.md) |
| Windows user task | discovery observed; authenticated review pending | [windows-task](board-review-hosts/windows-task.md) |

## Concerns

The [owning question](../questions/q-0002.0013-how-should-workshop-review-and-answer-board-changes-without-an-operator-present.md)
retains live full-review, operator grading and recurring-run evidence. Local leases
do not reserve a GitHub issue against independent human writes or other hosts.

## Roadmap

[workshop-board-review](../tickets/01-0006-workshop-board-review.md) delivers the current host's end-to-end proof.
