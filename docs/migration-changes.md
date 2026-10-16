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
integration and broader source cutover remain separate outcomes. The
[2026-10-08 provider review](current-system.md#assignment-evidence--reviewed-2026-10-08)
verifies omission/logging conformance and staging availability at `868a4ed`;
production retains `fc2dee2`. Provider acknowledgement awaits record publication.

| Accepted contract | Cabinet contribution | Daychi contribution | Decisions still needed |
|---|---|---|---|
| [Schedule access](boundaries.md#accepted-schedule-access), [retrieval modes](boundaries.md#accepted-schedule-retrieval-modes) and [source cutover](boundaries.md#accepted-schedule-source-cutover) | Valid public rows, omission logs and protected-route regressions are verified at `868a4ed` on staging; amended production deployment is not established. Broader authenticated retrieval remains migration work. | Implement and verify the native public pilot against its fixed contract; remove the school-HTML source at the later verified Cabinet cutover. | Public pilot schema/identities are fixed; valid best-effort rows carry no completeness metadata. Provider acknowledgement awaits record publication; native proof, broader authenticated retrieval and cutover compatibility remain separate. |
| [Native account-session profile](contracts/native-account-session.md) | Implement the accepted native bearer issuance, browser/code-and-PKCE handoff, full web self-profile and grant lifecycle while retaining web cookies. | Implement the accepted handoff, restoration, renewal and account read. Existing content access remains in this slice. | The complete native profile was accepted on 2026-10-09 and is published at c9c69c3; implementation and actual native proof remain work. The native content-check connection now has its own accepted contract and contributions; gateway work remains deferred. |
| [Sign-out scope](boundaries.md#accepted-sign-out-scope) | Revoke the calling native grant and all its credentials while preserving other grants and web sessions. | End authenticated use in the current installation through the accepted local-exit and best-effort revocation policy; apply the accepted unsynced-edit discard. | Native logout wire and behavior are accepted in the account-session profile; implementation and verification remain outstanding. Account-wide sign-out is not required by ordinary sign-out. |
| [Native content validation](contracts/native-content-session.md) | Retain native GET me current-state validation; isolate its valid-request capacity by native grant while retaining invalid-input protection. | Connect protected native content reads to the fixed matching Cabinet bearer check, preserving failure/recovery, legacy consumers and the separate browser policy. | Contract accepted and published 2026-10-16 at a07f087. [Cabinet #15](https://github.com/dveyarangi/xuanxue-workshop/issues/15) and [Daychi #16](https://github.com/dveyarangi/xuanxue-workshop/issues/16) own implementation, conformance and authorized joint content proof under original issue 11; backend retirement remains deferred. |
| [Web-wiki reader access](boundaries.md#accepted-web-wiki-reader-access) and [shared browser session](contracts/web-wiki-session.md#accepted-shared-browser-session) | Extend existing browser-cookie issuance/renewal/logout to the shared domain; expire the legacy host-only cookie during migration; retain account/session authority and expose current-session/account validation. | Receive the shared cookie at the wiki-origin reader API and validate it through Cabinet before content; persist no reader credential, local session or account replica; close anonymous delivery and controlled cache bypasses while preserving other authority scopes. | Shared-session direction and [GET /api/auth/session check](contracts/web-wiki-session.md#accepted-current-session-check) accepted by the user on 2026-10-12. [Cabinet-site logout](contracts/web-wiki-session.md#accepted-cabinet-site-logout) accepted on 2026-10-13, with a wiki navigation link and no wiki logout API/proxy. [Entry/migration/automatic return](contracts/web-wiki-session.md#accepted-browser-entry-and-migration) accepted by explicit clarification on 2026-10-13. Coordinated anonymous-access cutover, recipient implementation and joint deployed proof remain work. The separate wiki code/token/secret/encrypted-storage direction is superseded; [01-0009 web-wiki-cabinet-session](tickets/01-0009-web-wiki-cabinet-session.md) tracks published assignments and remaining implementation/proof. |
| [Reminder selections](boundaries.md#accepted-reminder-selections) | Extend the existing class-ID selection with one-off lesson selections that follow the same occurrence through rescheduling; expose shared account selections to both clients. | Pull account data on sign-in; read and change the shared selection, preserving one-off selection identity when a lesson moves. | Identifier encoding, executable synchronization contract and verification. |
| [Offline reminder editing](boundaries.md#accepted-offline-reminder-editing) | Reconcile choices independently; latest edit wins for the same choice, including removals; retain Cabinet's stored value on equal update times. | Allow offline selection changes and preserve pending edits through refreshes, failures and retries; discard unsynced selection and lead-time edits on explicit sign-out and prevent cross-account replay. | Clock handling, pending-edit tracking, removal retention and verification. |
| [Reminder lead times](boundaries.md#accepted-reminder-lead-times) | Support the agreed options and reconcile the setting independently of selections, latest edited value winning; retain Cabinet's stored value on equal update times. | Honor the shared setting, including 120 minutes and school default; allow offline changes and preserve pending edits. | Clock handling and executable synchronization checks. |
| [Daychi reminder delivery](boundaries.md#accepted-daychi-reminder-delivery) | Expose authoritative schedule and account selections for client refresh; retain existing delivery without cross-client deduplication. | Adapt existing refresh and local OS reminders; retain cached schedule and active reminders after refresh failure and preserve pending edits. Presentation belongs to Daychi; cross-client duplicates are allowed. | Verification; no new background refresh capability. |
| [Removal of per-date skips](boundaries.md#accepted-removal-of-per-date-skips) | Keep per-date skip exceptions out of the target shared reminder contract. | Remove the option and its related behavior; include the accepted user rationale in the ticket text. | Assignment scope is held by the migration question. |

The accepted [web-wiki environment profiles](contracts/web-wiki-session.md#accepted-production-and-staging-separation)
also require separate production/staging cookie names and signing/account authority,
fixed matching Cabinet/wiki origins, legacy staging cleanup and independent
lifecycle proof. Cabinet owns provider profiles; Daychi owns reader mapping and
matching validation. Both projects' existing web-wiki assignments carry this
2026-10-13 amendment; provisioning and deployed proof remain work.

The web-reader outcome is held by
[01-0009 web-wiki-cabinet-session](tickets/01-0009-web-wiki-cabinet-session.md),
minted as one HITL scope on 2026-10-13 after the user's approval. Recipient briefs,
implementation, coordinated anonymous-access cutover and joint deployed proof
remain its delivery criteria; minting is not assignment publication or deployment.

Native server push was rejected by the user as excessive for this scope on
2026-10-04. It is not a required project change.

## Unresolved compatibility details

Compare the [current source inventory](current-system.md) with the target before
selecting changes. The remaining decisions are:

- The [public pilot contract](contracts/public-lessons.md) settles its query,
  projection, identities and refresh/error semantics. The broader authenticated
  schedule and account/reminder migration still needs executable compatibility
  definitions and verification for the accepted school-HTML source removal at cutover.
- The [native account-session profile](contracts/native-account-session.md) settles
  acquisition, token transport, lifecycle and native sign-out. Its full profile is
  published at c9c69c3; implementation and actual native proof remain work. The separate
  [native content-check wire, caller trust, capacity and failure contract](contracts/native-content-session.md)
  was accepted on 2026-10-16; its implementation and integrated content proof remain work. Gateway work is deferred; ordinary sign-out affects only
  the current installation.
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
