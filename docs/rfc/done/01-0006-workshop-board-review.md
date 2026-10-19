# Workshop board review — implementation plan

- **record of** what happened

**Authored:** 2026-10-15
**Last amended:** 2026-10-15

Implements [workshop-board-review](../../tickets/done/01-0006-workshop-board-review.md).

## Governing shape

The accepted [specification](../../spec/done/01-0006-workshop-board-review.md), local L23 and
the assignment-review mechanism govern authority and semantic review. The detector
does not decide acceptance. A separate full Codex CLI reviewer supplies tool access and
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

The external controller invokes mechanical discovery before deciding whether to start
Codex. Only unclaimed candidates start the full reviewer; an empty or busy-only scan
makes no model call. A failed read is retained as an operational failure, not an empty
board. A process lock spans discovery and review and releases on crash. Per-issue
leases and publication recovery remain unchanged.

The full reviewer starts a fresh ephemeral CLI session, preserving configured model
and reasoning settings, with workspace-write, network access for authorized review
and no interactive approval dependency. It loads repository entry and review skills;
the source material cannot expand authority. The controller neither attaches to nor
writes a Desktop-held conversation. It retains execution receipts locally and never
marks a case reviewed on behalf of the agent.

The review mechanism owns REPORT.md, a Markdown record validator and atomic writer.
A report has a reviewed timestamp (or none), reviewed scope, results, open matters
and operations sections. A complete replacement requires the digest of its prior
version; conflicts refuse publication. The controller can update only operational
state while preserving review content, deduplicating unchanged failures. Operator
wake and the bot read the same report via local bindings, without auto-distribution.

A Windows current-user interactive task invokes the controller hourly with explicit
working directory and executable paths. The computer and sign-in are prerequisites;
Desktop is not. An initial controlled CLI proof and a scheduled dry discovery precede
pausing the native heartbeat and enabling the replacement. No unrelated task is changed.

The reviewer receives two per-run stdio MCP capabilities. review_board retains the
existing claim, basis, stable publication and finish checks, restricting mutations to
host-selected issues. github_read performs GET only within the configured repository
and the trusted README Repository map; issue links cannot enlarge the scope.
The host authenticates gh through its existing login, without extracting or forwarding
credentials to the model. Read-only host proofs prohibit mutations. The launcher drops
GitHub token environment variables and requires a changed valid report before success.
The deployed hourly task runs full review; the native heartbeat remains paused.


## Replacement verification

1. Reject malformed report replacements before creating the first report; prove a
   valid replacement and a stale-version refusal, and preserve open matters on errors.
2. Prove quiet detection calls no reviewer and leaves the report unchanged; available,
   due, busy, incomplete and faulting scans have distinct results.
3. Prove overlapping controllers exclude one another through review completion;
   recovery leaves pending board state intact.
4. Run a controlled standalone Codex reader and the bot reader against the shared
   report; then verify scheduled discovery and switch off the heartbeat.

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
6. Complete /verify, publish scoped changes, configure the external hourly recurrence and
   retain any outstanding operator grading as an explicit incomplete criterion.

## Impact

Mechanical discovery, local delivery state, review activation and original-issue
publication are affected. Existing semantic review and acceptance remain owned by
the review mechanism. Recipient code and bot execution permissions stay outside scope; the bot gains a read binding only.

## Hidden edges

Loaded Desktop chats reject external resume; the standalone reviewer avoids that boundary.
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
review mechanism and the Windows user task scheduler. Do not introduce a separate agent runtime,
daemon, queue service, generalized workflow engine or second dispatch board.
