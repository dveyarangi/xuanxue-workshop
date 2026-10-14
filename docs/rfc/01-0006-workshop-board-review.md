# Workshop board review — implementation plan

- **record of** what it intends to become

**Authored:** 2026-10-15

Implements [workshop-board-review](../tickets/01-0006-workshop-board-review.md).

## Governing shape

The accepted [specification](../spec/01-0006-workshop-board-review.md), local L23 and
the assignment-review mechanism govern authority and semantic review. The detector
does not decide acceptance. The full existing Codex chat supplies tool access and
applies /review-assignments; the network-isolated Telegram conversation worker is not invoked.
No model or reasoning setting is overridden.

## Implementation

A Python-standard-library command in the existing review mechanism provides
scan, claim, renew, prepare, publish, finish, status and check operations. Its GitHub
boundary uses the authenticated gh REST client, complete pagination and structured
JSON publication. Repository and recipient labels are explicit configuration;
credentials remain with gh. Untrusted issue text never supplies executable commands.

Discovery reads bodies, comments and full timelines. Recognized linked GitHub
issues/PRs, source paths, commits and action runs are observed one hop deep, including
PR reviews and current-head check/status outcomes. Linked-read failures are explicit
evidence gaps; primary-board failure fails discovery without advancing progress.
Snapshots retain actual source material for agent inspection, rather than substituting
a status or summary for proof. External runtime/fixture changes are checked by the
full reviewer when its next evidence follow-up falls due.

SQLite persists per-issue observed/reviewed fingerprints, due times, bounded review
leases and prepared/sending/confirmed/conflicted/uncertain publication state.
Snapshots are local working material. Both state and snapshots are excluded from Git.
There is no separate acceptance ledger: local outcomes are processing positions;
the original issue and existing Workshop records retain acceptance authority.

A claim returns a unique expiring token and the exact current snapshot. Prepare,
publication and completion require that token and current premises. Publication
first persists the exact body with a stable marker and operation identifier, then
re-reads live material before sending. Only exact locally known publications from
the authenticated account are ignored as self-generated changes. Edits to those
publications and deletion of confirmed comments are visible.

The sending transition is durable before HTTP publication. A resumed sending or
uncertain operation reads back the exact marker/body/author and confirms the existing
comment if found. Absence after an ambiguous attempt does not authorize blind resend.
Confirmed delivery is distinct from review completion. A stale case stays pending.

Local leases exclude cooperating automatic reviewers. They do not reserve GitHub
against independent humans or provide a cross-host distributed lock. The reviewer
reads the current question window, leaves an actively owned manual scope alone and
re-reads before mutation. A remote change between the last read and GitHub accepting
the comment cannot be atomically excluded by the issue-comment API; discovery catches
subsequent changes and the reviewer reassesses them.

The same-chat heartbeat invokes a project-local periodic-review instruction in the
existing mechanism. That instruction owns the mechanical command sequence and points
to semantic review, rather than copying it. Only the responsible project agent performs
question-store calls. Operator notifications stay in this chat under the accepted
scope; the new Telegram sending authority adds no requirement to use Telegram here.
Local L25 supplies hourly cadence and a short dated completion report for meaningful
results, decisions and actionable failures. Unchanged runs remain silent; wake does
not repeat reports. The host's chat history retains reports without an additional
local report record.

## Stages and verification

1. A tracer test discovers an open and closed case, marks the studied case reviewed
   and proves an unchanged scan is quiet across restart. Implement its path first.
2. Add changed/failed/linked evidence, pagination and due-follow-up counterexamples.
3. Add lease conflicts, stale preparation and interrupted-publication tests, including
   externally created remote comment recovery and retained ambiguity.
4. Document and bind periodic execution; check the existing mechanism and local rules.
5. Run a read-only live-board pass. Demonstrate a clearly identified temporary proof
   issue, exact response recovery and a concrete operator escalation. Grade semantics
   separately from mechanical tests and retain the results under the owning question.
6. Complete /verify, publish scoped changes, configure the same-chat recurrence and
   retain any outstanding operator grading as an explicit incomplete criterion.

## Impact

Mechanical discovery, local delivery state, review activation and original-issue
publication are affected. Existing semantic review and acceptance remain owned by
the review mechanism. The Telegram working tree and recipient code stay outside scope.

## Hidden edges

Header timestamps alone miss edits and linked-source changes. The worker's own
messages must not cause an endless trigger. Publication timeout does not establish
failure. Manual responses can obsolete prepared work. Authentication/network access
during an unattended run is a live condition, not implied by scheduler availability.

## Leave alone

Shared application contracts, recipient release authority, global switches, existing
queue order relative to other tickets, Telegram implementation and other sessions'
uncommitted changes.

## Recommendation

Proceed with the accepted single vertical slice. Reuse gh, SQLite, the existing
review mechanism and the app's scheduler. Do not introduce a separate agent runtime,
daemon, queue service, generalized workflow engine or second dispatch board.
