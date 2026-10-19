# Workshop board review

- **record of** what happened
- **Status:** Done (2026-10-15)
- **Type:** HITL
- **Minted:** 2026-10-15
- **Plan:** [workshop-board-review RFC](../../rfc/done/01-0006-workshop-board-review.md) — mechanical discovery and recoverable publication with full standalone agent review and a shared report
- **Answers:** [q-0002.0013](../../questions/done/q-0002.0013-how-should-workshop-review-and-answer-board-changes-without-an-operator-present.md)
- **Outcome:** Workshop periodically discovers changed assignments and evidence, studies them under its existing methodology, responds within authority and returns operator decisions without duplicate publication after interruption.

## Parent

The [accepted workshop-board-review specification](../../spec/done/01-0006-workshop-board-review.md)
covers this single vertical slice. The user accepted its scope and one-ticket
breakdown on 2026-10-15. The [impact assessment](../../questions/done/q-0002.0013-how-should-workshop-review-and-answer-board-changes-without-an-operator-present.md#impact--proposed-single-slice-2026-10-14)
established the slice; no recipient implementation is a prerequisite.

## What to build

Discover addressed requests and issued assignments in every issue state, including
edited discussions and changed linked evidence. Full agent review applies existing
agreements, checks source and executed evidence, and answers in the original issue
under local L23. Missing facts return to the responsible participant; new shared
decisions and out-of-scope actions remain visible to the operator in the shared report.

Preserve pending work through restart, revalidate before publication and recover
uncertain delivery by inspecting the remote issue. Intervening manual work and
concurrent automatic reviewers cannot silently consume the same local review.
The accepted cadence is hourly. Mechanical discovery precedes model invocation;
available work starts a separate full reviewer. Meaningful results, required
decisions and failures update `docs/board-review.md`, read by wake and the bot without
automatic distribution. Review-assignments owns its format and writing instructions.
The local computer and signed-in account provide execution independently of Desktop.

## Acceptance criteria

- [x] 2026-10-15 Complete discovery distinguishes changed, unchanged, due and inaccessible material, including closed-issue reports, edited/deleted comments and linked checks/source.
- [x] 2026-10-15 A full reviewer studied the controlled issue and governing sources, published its revalidated response, recovered the receipt and retained the outcome; see [periodic review evidence](../../mechanisms/review-assignments.evidence.md#periodic-review-implementation--2026-10-15).
- [x] 2026-10-15 Interruption after remote publication is recovered without another comment; uncertain delivery remains explicit and cannot silently mark review complete. Proven with an independent comment fixture, local HTTP delivery and real GitHub comment 6180599165.
- [x] 2026-10-15 Competing automatic work and intervening manual changes leave pending work visible instead of publishing a stale response.
- [x] 2026-10-15 The operator accepted all five representative full-review outcomes in control issue 14: missing evidence, complete result, protocol decision, instruction override and a closed-issue report.
- [x] 2026-10-15 The read-only live-board pass and controlled issue 14 publication/recovery/operator-escalation example preceded recurring activation; operator grading remains separate.
- [x] 2026-10-15 Quiet mechanical discovery starts no model and leaves the shared report unchanged; work, busy cases and failed reads remain distinct. Ten controller/report tests and a real cross-process busy refusal passed.
- [x] 2026-10-15 A real standalone Codex read and replaced the controlled report while preserving its open matter; the actual bot role read the shared report and returned its date and open matter. Stale/invalid replacements and operational preservation passed behavioral tests.
- [x] 2026-10-15 The actual hourly user task completed live discovery with retained receipt and cross-process exclusion; the full replacement is enabled and the former heartbeat is paused. First autonomous full-batch review remains unobserved.
- [x] 2026-10-15 A real standalone Codex successfully used scoped host identity and issue-read capabilities, then replaced the controlled report while retaining its open matter. Four capability tests prove bounded mutation and duplicate-safe delivery; two launcher tests prove credential-environment exclusion and refusal of completion without a report. No raw credential delegation is used; discovery-only mode is removed.
- [x] 2026-10-15 /verify passed: 88 tests; harness source check; installed-rule and mechanism checks; question, ticket and edge validators; shared-report validation. Full-review semantic grading and real publication recovery were accepted earlier; host read/report proof does not claim an unattended remote publication.

## Out of scope

Recipient source changes/releases and shared contract changes retain their existing
owners and decision paths. Telegram remains under
[telegram-workshop-access](../01-0020-telegram-workshop-access.md). This work creates
no second board, general workflow platform or global autonomy-switch change.

## Parent scope addressed

All eight user stories in the accepted specification are covered by this slice.
