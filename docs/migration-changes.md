# Initial migration changes and contribution proposals

Derived from the [accepted target](boundaries.md) and [current source evidence](current-system.md).
The [first-stage goal](stage-1.md) limits this work. This document describes the
required delta and contribution assignments; it does not authorize sibling implementation.

## Changes derived from accepted contracts

This list records required changes separately from the target architecture, which
owns the accepted agreements and rationale. It feeds future project tickets;
implementation details and the contribution breakdown still require their own
alignment. It is not a claim that these changes are implemented or deployed.

The public schedule pilot has verified staging and production providers. The
[2026-10-06 environment evidence](current-system.md#cabinet-public-schedule-environments--checked-2026-10-06)
owns its concrete origin, runtime and existing fixture controls. Native Daychi
integration, the provider required-data correction and broader source cutover
remain separate outcomes. Deployment does not establish full provider conformance.

| Accepted contract | Cabinet contribution | Daychi contribution | Decisions still needed |
|---|---|---|---|
| [Schedule access](boundaries.md#accepted-schedule-access), [retrieval modes](boundaries.md#accepted-schedule-retrieval-modes) and [source cutover](boundaries.md#accepted-schedule-source-cutover) | Public pilot route is deployed; correct required-data enforcement and preserve protected Cabinet web behavior. Broader authenticated retrieval remains migration work. | Implement and verify the native public pilot against its fixed contract; remove the school-HTML source at the later verified Cabinet cutover. | Public pilot schema/identities are fixed. Provider correction and native proof remain; broader authenticated retrieval and cutover compatibility remain separate. |
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

- The [public pilot contract](contracts/public-lessons.md) settles its query,
  projection, identities and refresh/error semantics. The broader authenticated
  schedule and account/reminder migration still needs executable compatibility
  definitions and verification for the accepted school-HTML source removal at cutover.
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

The earlier broad investigation pair was withdrawn as duplicate work. Its
[disposition and corrected impact](reconciliation-20261004.md#withdrawn-contribution-proposal--2026-10-05)
are historical evidence. It creates no recipient obligation.

The accepted public pilot is tracked by
[cabinet-daychi-public-schedule-connection](tickets/01-0007-cabinet-daychi-public-schedule-connection.md).
Its provider and consumer use the same published contract. Broader migration
changes above retain their unresolved decisions and require separately authorized scope.

## Impact assessment of the contribution split — refreshed 2026-10-05

See the [historical assessment](reconciliation-20261004.md#withdrawn-contribution-proposal--2026-10-05).
The current accepted-contract delta is the table above.
