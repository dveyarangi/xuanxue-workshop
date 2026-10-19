# Detector-first board duty and actionable review
- **record of** what happened

## Decisions and their reasons

The operator accepted unattended investigation and original-issue responses within
existing agreements, with new shared decisions and out-of-scope actions escalated.
The initial placement in the inter-agent contract was corrected: this is local
operator/agent authorization, owned by [local review authority](../../local.rules.md#l23--unattended-board-review-authority),
not a change to the projects' responsibility contract.

The operator chose hourly discovery, replacing the earlier fifteen-minute cadence.
Unchanged runs remain silent. The intended economy was mechanical discovery before
any model invocation. Desktop-held chats refused external writers, so a separate
standalone reviewer replaced the native same-chat heartbeat, which remains paused.

The operator then chose one shared report readable by session recovery and the
Telegram bot, without automatic distribution or repeated wake summaries. The
[review-assignments mechanism](../../.agents/mechanisms/review-assignments/review-assignments.md)
owns its format and writing; no separate review skill or acceptance ledger was added.
[Architecture](../architecture.md#unattended-board-review) and
[reporting configuration](../../local.rules.md#l25--shared-board-review-report)
hold the accepted result.

## Delivered and verified

[workshop-board-review](../tickets/done/01-0006-workshop-board-review.md) and its paired
RFC are complete and archived. Mechanical discovery, leases, basis revalidation,
stable publication recovery, report validation/atomic replacement and process exclusion
are implemented. The user accepted the five representative semantic outcomes in
control issue 14. Its real interrupted publication recovered the same physical comment.

Windows task WorkshopBoardReview invokes full review hourly as the signed-in user,
independently of this chat and Desktop. Quiet discovery invokes no model. Direct
sandbox GitHub authentication failed; a raw credential-delegation patch was rejected
and not applied. The implemented bounded host MCP interface retains credentials at
the host, restricts writes to selected issues and reads to configured repositories.
The [Windows host record](../edge/board-review-hosts/windows-task.md) holds the proof.

Actual unattended review completed eleven cases at 2026-10-15T09:44:21Z without
controller errors. At conclusion the scheduled 13:02:28+03:00 invocation was running,
with the next invocation at 14:02:27+03:00. Independent GitHub readback at conclusion
confirmed both [issue 8](https://github.com/dveyarangi/xuanxue-workshop/issues/8#issuecomment-6189041756)
and [issue 6](https://github.com/dveyarangi/xuanxue-workshop/issues/6#issuecomment-6189101629)
comments match the locally confirmed sent bodies and author. This establishes actual
authenticated standalone publication, beyond the earlier controlled read/report proof.

The latest instruction pass passed 90 tests, harness-source comparison, mechanism and
installed-rule checks and shared-report validation. Publication is complete through
7105beb before this conclusion; the session/host evidence is published separately.

## Corrections from operator feedback

The operator rejected a status inventory that required humans to reconstruct practical
actions: “если операторы должны из этого сделать практический вывод, то это не сработает”.
The summary had hidden an already exact DNS handoff and called unfinished technical
preparation in issue 11 an operator decision. The repeat is recorded in
[rule failures](../rule-failures.md#2026-10-15--telegram-references-and-next-actions-were-not-usable).

The amended review instruction assesses actual reviewer and recipient-agent tools,
access and authority before escalation, performs available authorized work, and names
its own concrete continuation. The report separates reviewer commitments, recipient
agent work and irreducible operator actions, with exact inputs and observable outcomes.
This strengthens execution and presentation without expanding authority.

## Remaining work and continuation

The activation question is [closed](../questions/done/q-0002.0013-how-should-workshop-review-and-answer-board-changes-without-an-operator-present.md).
The architecture question remains open; native/browser integration and content admission
retain their original agreements, owners and acceptance conditions. The user requested conclusion, then questioned the current run's duration. The
finding was repaired with explicit user approval before conclusion; board duty is active.

The latest [shared report](../board-review.md) is the recovery point for current outcomes,
concrete owner actions and unresolved matters. It is updated by duty independently;
its changing working-tree content and other chats' unfinished changes were preserved.
Issue 11 still needs Workshop's prepared technical recommendation before a human choice.
DNS ownership/private handoff and authorized Cabinet account/data preparation remain
external inputs for the relevant integration checks. Current status and the existing
queue, rather than this dated session account, determine subsequent work.

## Duration finding during conclusion

At 13:36+03:00 the 13:02 scheduled action was still running. The standalone Codex
process began at 13:08:26; recent progress was observed at 13:35:38. Thus about six
minutes were discovery and about twenty-eight minutes were standalone review, not
merely a mechanical poll. No new issue response had been reported in that pass.

Two concrete sources of avoidable review were established. The current reviewer
explicitly schedules waiting/operator follow-ups at 3600 seconds. Separately, a
read-only counterexample built from actual case 1 data changes only the linked
pull request's head.repo.pushed_at; Board.fingerprint changes despite unchanged
PR revision, discussion and checks. This proves an unrelated-repository-push trigger,
not the proportion of the current run attributable to it. Production code/state
were not altered. Relevant-only fingerprints and controlled follow-up scheduling
need scoped correction before the economy claim is considered established.

## Authorized correction and final continuation

The user approved repair with “да, почини пожалуйста”. The new regression first
failed on unrelated PR repository metadata, then the actual live data exposed the
same metadata in cross-reference timelines. The completed projection removes that
noise from fingerprints and model payloads while retaining source refs/commits,
new discussions, reviews and checks. Waiting/operator outcomes now enforce the
accepted six-hour minimum; new relevant evidence still interrupts that wait.

The 13:02 old-code run timed out at 13:48:28+03:00 without a new response or held
lease. New task starts were disabled for repair. A retained SQLite backup preceded
migration of fourteen records under the controller lock. Proven review positions,
actual unreviewed changes and publication identity/delivery state survived; legacy
one-hour deadlines moved five hours later, preserving their original review time.
Migration refuses live reviews and is idempotent; a legacy prepared response still
recovers exactly once.

The completed live discovery at 14:13:17+03:00 had no read errors or model call.
Six metadata-only cases were quiet, while eight genuine discussion/timeline changes
remained pending, including Daychi's new acknowledgement in issue 8. No artificial
review completion was introduced. The final suite passed 102 tests and the scoped
harness/rule/record checks passed. The task is enabled hourly again; its next trigger
is 15:02:27+03:00. The latest shared report and original issues remain the recovery
points. This session ends without stopping duty or starting another delivery cycle.
