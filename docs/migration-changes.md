# Initial migration changes and contribution proposals

Derived from the [accepted target](boundaries.md) and [current source evidence](current-system.md).
The [first-stage goal](stage-1.md) limits this work. This document describes the
required delta and contribution assignments; it does not authorize sibling implementation.

## Changes derived from accepted contracts

This list records required changes separately from the target architecture, which
owns the accepted agreements and rationale. It feeds future project tickets;
implementation details and the contribution breakdown still require their own
alignment. It is not a claim that these changes are implemented or deployed.

| Accepted contract | Cabinet contribution | Daychi contribution | Decisions still needed |
|---|---|---|---|
| [Schedule access](boundaries.md#accepted-schedule-access), [retrieval modes](boundaries.md#accepted-schedule-retrieval-modes) and [source cutover](boundaries.md#accepted-schedule-source-cutover) | Provide public/authenticated schedule access and query-selected count/date-window modes; preserve Cabinet web count behavior and guarantee complete supported windows. | Consume Cabinet schedule with the agreed access behavior and fourteen-day coverage; remove the school-HTML source when Cabinet integration is verified. | Exact query/response schema, shared identifier fields and cutover verification evidence. |
| [Cabinet credentials](boundaries.md#accepted-content-admission) and [provisional acquisition](boundaries.md#provisional-native-credential-acquisition) | Support native bearer issuance and the provisional Cabinet-owned browser/code-and-PKCE handoff while retaining web cookies and authoritative validation. | Consume the provisional handoff and present Cabinet credentials to the target APIs. | Final acquisition contract, token format and remaining lifecycle; gateway work is deferred and Cabinet web access is preserved. |
| [Sign-out scope](boundaries.md#accepted-sign-out-scope) | Preserve other clients' signed-in state when one client signs out. | End authenticated use in the current installation and apply the accepted unsynced-edit discard. | Executable logout contract and verification; account-wide sign-out is not required by ordinary sign-out. |
| [Content admission](boundaries.md#accepted-content-admission) | Provide a narrow authoritative admission check. | Replace independent content admission with the accepted call to Cabinet and distinguish refusal from temporary failure. | Executable check schema, caller trust, verification and any cache bound; removal follows the target contract's consolidation binding. |
| [Reminder selections](boundaries.md#accepted-reminder-selections) | Extend the existing class-ID selection with one-off lesson selections that follow the same occurrence through rescheduling; expose shared account selections to both clients. | Pull account data on sign-in; read and change the shared selection, preserving one-off selection identity when a lesson moves. | Identifier encoding, executable synchronization contract and verification. |
| [Offline reminder editing](boundaries.md#accepted-offline-reminder-editing) | Reconcile choices independently; latest edit wins for the same choice, including removals; retain Cabinet's stored value on equal update times. | Allow offline selection changes and preserve pending edits through refreshes, failures and retries; discard unsynced selection and lead-time edits on explicit sign-out and prevent cross-account replay. | Clock handling, pending-edit tracking, removal retention and verification. |
| [Reminder lead times](boundaries.md#accepted-reminder-lead-times) | Support the agreed options and reconcile the setting independently of selections, latest edited value winning; retain Cabinet's stored value on equal update times. | Honor the shared setting, including 120 minutes and school default; allow offline changes and preserve pending edits. | Clock handling and executable synchronization checks. |
| [Daychi reminder delivery](boundaries.md#accepted-daychi-reminder-delivery) | Expose authoritative schedule and account selections for client refresh; retain existing delivery without cross-client deduplication. | Adapt existing refresh and local OS reminders; retain cached schedule and active reminders after refresh failure and preserve pending edits. Presentation belongs to Daychi; cross-client duplicates are allowed. | Verification; no new background refresh capability. |
| [Removal of per-date skips](boundaries.md#accepted-removal-of-per-date-skips) | Keep per-date skip exceptions out of the target shared reminder contract. | Remove the option and its related behavior; include the accepted user rationale in the ticket text. | Assignment scope is held by the migration question. |

Native server push was rejected by the user as excessive for this scope on
2026-10-04. It is not a required project change.

## Unresolved compatibility details

Compare the [current source inventory](current-system.md) with the target before
selecting changes. The remaining decisions are:

- Executable count/date-window contract: interval boundaries, supported bounds,
  validation and complete-result semantics; response fields and identifier mapping
  between Daychi clients and Cabinet classes/lessons; verification evidence for
  the accepted school-HTML source removal at Cabinet cutover.
- Finalization of the [provisional credential-acquisition
  contract](boundaries.md#provisional-native-credential-acquisition), token format
  and lifecycle, preservation of Cabinet web access, and the admission-check
  request, response and failure contract. Gateway work is deferred; ordinary
  sign-out affects only the current installation.
- Ongoing reconciliation of new local edits and account changes. Initial migration
  scope is held by the [migration question](questions/q-0002.0007-how-will-daychi-migrate-schedule-users-and-reminders-to-cabinet-while-retaining-its-content-backend.md#initial-usage-and-ongoing-synchronization--2026-10-04).
- Verification of accepted failed-refresh and independent-delivery behavior,
  preserving existing refresh and delivery facilities. Cross-client duplicates
  are allowed. Do not add a background-refresh project.

## Boundary evidence

Workshop's [completed comparison](reconciliation-20261004.md#boundary-comparison)
and [current source inventory](current-system.md) already identify the relevant
provider/consumer modules, source revisions, executable definitions, compatibility
gaps and existing checks. Subsequent accepted decisions are held by the boundary
record and migration question. Broad source-inventory requests duplicate that work.

Source inspection, executed checks and deployed evidence remain distinct. Remote
freshness and some runtime/deployment proof remain unverified. Those are specific
limits, not evidence that the full boundary investigation is outstanding.

## Review scenarios

These scenarios describe the agreed boundary outcomes and remaining verification
questions; they are information for scoping work, not agent workflow instructions:

- An unauthenticated caller can receive the schedule without Zoom connection
  details; the schedule with those details requires authentication.
- A user signs in from Cabinet web and from a Daychi native client, then accesses
  Daychi content under the agreed permission policy.
- Access is revoked or credentials expire; each consumer applies the agreed
  outcome and recovery behavior.
- Daychi loads Cabinet selections on sign-in; subsequent changes from either
  client reconcile according to the agreed synchronization policy.
- Explicit sign-out discards unsynced reminder and lead-time edits. Signing in
  again does not replay them into either the original or a different account;
  Cabinet's already-accepted state remains. Connection failures preserve pending
  edits under the accepted rule.
- Sign out of one Daychi installation while the same account is signed in to
  Cabinet and another Daychi installation: authenticated use ends in the calling
  installation, and the other clients remain signed in.
- A failed refresh retains cached schedule and active reminders and preserves
  pending edits. A successful refresh
  reconciles received cancellations and transfers.
- Verified Cabinet schedule integration permits removal of the native school-HTML
  source. The accepted access, window completeness, identity and failed-refresh
  behavior hold through cutover; HTML cannot replace Cabinet data afterward.
- A user has both clients enabled; both may notify for the same lesson. Verify
  that delivery consumes the shared selections and lead time; cross-client
  deduplication is not an acceptance requirement.
- Cabinet's existing frontend keeps working throughout the agreed API transition;
  a failed rollout has a defined recovery path.

These are contract-review scenarios, not assertions that the implementation
already passes them.

## Proposed contribution breakdown

This heading is retained for existing links. The older broad contribution proposal
was promoted into two Planned issues on 2026-10-05. The user then challenged their
scope as repeating Workshop's completed investigation. The earlier statement of
breakdown approval was the assistant's mistaken interpretation. At the user's
request on 2026-10-05, both were withdrawn and closed as `not_planned`. Readback
confirmed closure and the withdrawal notices; no recipient action is required.

### cabinet-contract-contribution — Withdrawn, created in error

[cabinet-contract-contribution #3](https://github.com/dveyarangi/xuanxue-workshop/issues/3)
is addressed to the Cabinet project agent under its operator, with label
`project:cabinet`. Its posted scope requests an API inventory and proposals. That
inventory overlaps Workshop's completed work; the issue's existence does not
establish a remaining need for it.

### daychi-contract-contribution — Withdrawn, created in error

[daychi-contract-contribution #4](https://github.com/dveyarangi/xuanxue-workshop/issues/4)
is addressed to the Daychi project agent under its operator, with label
`project:daychi`. Its posted scope requests a client/content inventory and proposals.
That inventory overlaps Workshop's completed work. Its body contains the user's
skip-removal rationale. No implementation or execution release occurred.

### agreed-target-seam-contracts — Unissued proposal

The older third proposal described dependent Workshop alignment after those
contributions. No local ticket or issue was minted for it. Workshop's comparison
and subsequent alignment already advanced that outcome; it is not an instruction
to wait for repeated project investigations.

The [failure trace](rule-failures.md#2026-10-05--completed-reconciliation-reissued-as-project-investigation)
records the work-selection mistake. Actual remaining project changes are described
by the accepted-contract delta above; unresolved decisions and verification limits
retain their own records. The whole first stage is not an approved delivery breakdown.

## Impact assessment of the contribution split — refreshed 2026-10-05

The first refresh defended the split by project, without checking completed work.
The user rejected the resulting broad investigation scope. This corrected account
supersedes that recommendation; the posted issues are withdrawn and closed,
with their cancelled briefs retained as historical records.

### Impact

The posted issues changed coordination records and requested project investigation
already substantially completed by Workshop. No sibling implementation changed.
The accepted-contract delta still identifies real migration changes, independently
of these mistaken assignments.

### Hidden edges

Old proposal prose was treated as workflow authority, while implementation
ownership was mistaken for investigation ownership. Tracker duplicate searches
could not find completed work held in local source-analysis records. Some narrow
runtime/deployment proof and executable design choices remain open; that does not
make the broad inventory outstanding. Latest accepted contracts remain local.

### Leave alone

Accepted provider assignments and boundary behavior; sibling application code,
releases, deployments, Cabinet-only workflows and project UX; deferred gateway
and backend consolidation; existing refresh facilities and installation/readiness
assignments. No duplicate local tickets or new legacy migration program exists.

### Recommendation

Rethink the assignment scope. The existing comparison and accepted decisions are
the basis for identifying specific remaining changes and unavailable proof. A new
post-impact breakdown has not been accepted or issued. Publication and execution
dependencies remain distinct, and the local delivery queue is unchanged.
