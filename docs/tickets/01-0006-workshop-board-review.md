# Workshop board review

- **record of** what it intends to become
- **Status:** Partial (live publication verified; recurrence active; operator grading and unattended-run evidence pending)
- **Type:** HITL
- **Minted:** 2026-10-15
- **Plan:** [workshop-board-review RFC](../rfc/01-0006-workshop-board-review.md) — mechanical discovery and recoverable publication with full agent review in the existing chat
- **Answers:** [q-0002.0013](../questions/q-0002.0013-how-should-workshop-review-and-answer-board-changes-without-an-operator-present.md)
- **Outcome:** Workshop periodically discovers changed assignments and evidence, studies them under its existing methodology, responds within authority and returns operator decisions without duplicate publication after interruption.

## Parent

The [accepted workshop-board-review specification](../spec/01-0006-workshop-board-review.md)
covers this single vertical slice. The user accepted its scope and one-ticket
breakdown on 2026-10-15. The [impact assessment](../questions/q-0002.0013-how-should-workshop-review-and-answer-board-changes-without-an-operator-present.md#impact--proposed-single-slice-2026-10-14)
established the slice; no recipient implementation is a prerequisite.

## What to build

Discover addressed requests and issued assignments in every issue state, including
edited discussions and changed linked evidence. Full agent review applies existing
agreements, checks source and executed evidence, and answers in the original issue
under local L23. Missing facts return to the responsible participant; new shared
decisions and out-of-scope actions return to the operator in this chat.

Preserve pending work through restart, revalidate before publication and recover
uncertain delivery by inspecting the remote issue. Intervening manual work and
concurrent automatic reviewers cannot silently consume the same local review.
The accepted initial cadence is fifteen minutes with six-hour unchanged-evidence
follow-up; the local computer and app provide the execution environment.

## Acceptance criteria

- [x] 2026-10-15 Complete discovery distinguishes changed, unchanged, due and inaccessible material, including closed-issue reports, edited/deleted comments and linked checks/source.
- [x] 2026-10-15 A full reviewer studied the controlled issue and governing sources, published its revalidated response, recovered the receipt and retained the outcome; see [periodic review evidence](../mechanisms/review-assignments.evidence.md#periodic-review-implementation--2026-10-15).
- [x] 2026-10-15 Interruption after remote publication is recovered without another comment; uncertain delivery remains explicit and cannot silently mark review complete. Proven with an independent comment fixture, local HTTP delivery and real GitHub comment 6180599165.
- [x] 2026-10-15 Competing automatic work and intervening manual changes leave pending work visible instead of publishing a stale response.
- [ ] Representative full-review cases distinguish existing decisions, missing evidence, incomplete/complete results and operator decisions; the operator grades the observed outcomes.
- [x] 2026-10-15 The read-only live-board pass and controlled issue 14 publication/recovery/operator-escalation example preceded recurring activation; operator grading remains separate.
- [ ] The fifteen-minute same-chat recurrence is ACTIVE; observe an unattended invocation, quiet unchanged runs and meaningful operator notifications.
- [ ] /verify passes against the ticket, RFC, governing instructions and scoped verification set.

## Out of scope

Recipient source changes/releases and shared contract changes retain their existing
owners and decision paths. Telegram remains under
[telegram-workshop-access](./01-0020-telegram-workshop-access.md). This work creates
no second board, general workflow platform or global autonomy-switch change.

## Parent scope addressed

All eight user stories in the accepted specification are covered by this slice.
