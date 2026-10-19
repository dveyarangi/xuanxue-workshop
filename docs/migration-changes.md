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
production retained `fc2dee2` at that review. Provider acknowledgement was published
on 2026-10-08; [provider 5 is closed](https://github.com/dveyarangi/xuanxue-workshop/issues/5#issuecomment-6260697241)
as of 2026-10-19. The regional staging-network incident is closed and non-blocking
until an actual customer complaint; no network repair, repeated provider
acknowledgement or temporary-role disposition is an additional gate to Daychi.

| Accepted contract | Cabinet contribution | Daychi contribution | Decisions still needed |
|---|---|---|---|
| [Schedule access](boundaries.md#accepted-schedule-access), [retrieval modes](boundaries.md#accepted-schedule-retrieval-modes) and [source cutover](boundaries.md#accepted-schedule-source-cutover) | Valid public rows, omission logs and protected-route regressions are verified at `868a4ed` on staging; amended production deployment is not established. Broader authenticated retrieval remains migration work. | Implement and verify the native public pilot against its fixed contract; remove the school-HTML source at the later verified Cabinet cutover. | Public pilot schema/identities are fixed; valid best-effort rows carry no completeness metadata. Provider acknowledgement is complete; regional staging-network repair is closed and non-blocking until an actual customer complaint. Ordinary native proof, broader authenticated retrieval and cutover compatibility remain separate. |
| [Native account-session profile](contracts/native-account-session.md) | Provider contribution is accepted at 5ea9a8b. | Client and joint-native contribution is accepted for tested d1a85fe / native iOS Simulator Debug 1.0.0 (18), with both-platform configuration/client evidence. | [Native outcome acceptance](current-system.md#native-client-and-joint-acceptance--2026-10-17) completes this slice under profile 18cfe41 and its accepted evidence amendments. Native-content capacity 15/16, browser 12/13 and production release remain separate; gateway work stays deferred. |
| [Sign-out scope](boundaries.md#accepted-sign-out-scope) | Grant-wide native revocation with other native grants/browser sessions preserved is accepted within the native provider contribution. | Native local-exit, durable cleanup/recovery and legacy preservation are accepted in the [client/joint account-session outcome](current-system.md#native-client-and-joint-acceptance--2026-10-17). | Native account-session sign-out is complete under its agreed evidence scope. Account-wide logout is not required; future reminder/account synchronization retains its separate agreement. |
| [Native content validation](contracts/native-content-session.md) | Retain native GET me current-state validation; isolate its valid-request capacity by native grant while retaining invalid-input protection. | Connect protected native content reads to the fixed matching Cabinet bearer check, preserving failure/recovery, legacy consumers and the separate browser policy. | Contract accepted and published 2026-10-16 at a07f087. [Cabinet #15](https://github.com/dveyarangi/xuanxue-workshop/issues/15) and [Daychi #16](https://github.com/dveyarangi/xuanxue-workshop/issues/16) own implementation, conformance and authorized joint content proof under original issue 11; backend retirement remains deferred. |
| [Web-wiki reader access](boundaries.md#accepted-web-wiki-reader-access) and [shared browser session](contracts/web-wiki-session.md#accepted-shared-browser-session) | Extend existing browser-cookie issuance/renewal/logout to the shared domain; expire the legacy host-only cookie during migration; retain account/session authority and expose current-session/account validation. | Receive the shared cookie at the wiki-origin reader API and validate it through Cabinet before content; persist no reader credential, local session or account replica; close anonymous delivery and controlled cache bypasses while preserving other authority scopes. | Shared-session direction and [GET /api/auth/session check](contracts/web-wiki-session.md#accepted-current-session-check) accepted by the user on 2026-10-12. [Cabinet-site logout](contracts/web-wiki-session.md#accepted-cabinet-site-logout) accepted on 2026-10-13, with a wiki navigation link and no wiki logout API/proxy. [Entry/migration/automatic return](contracts/web-wiki-session.md#accepted-browser-entry-and-migration) accepted by explicit clarification on 2026-10-13. Coordinated anonymous-access cutover, recipient implementation and joint deployed proof remain work. The separate wiki code/token/secret/encrypted-storage direction is superseded; [01-0009 web-wiki-cabinet-session](tickets/01-0009-web-wiki-cabinet-session.md) tracks published assignments and remaining implementation/proof. |
| [Reminder selections](boundaries.md#accepted-reminder-selections) | Expose explicit class and stable one-off lesson choices shared by both clients; new accounts have no reminder selections. Keep other notification-kind filters separate. | Read Cabinet settings on sign-in and preserve chosen occurrence identity across moves; shared edits require a Cabinet save. | Executable online synchronization contract and verification. |
| [Online-only reminder editing](boundaries.md#accepted-online-only-reminder-editing) | Apply independent per-choice saves in Cabinet commit order; expose current confirmed settings for recovery. | Disable offline shared edits, retain confirmed cache and scheduled reminders, and read back uncertain saves without automatic mutation replay or an offline queue. | Executable wire/recovery checks and verification; the 19 October decision supersedes offline/client-clock reconciliation. |
| [Reminder lead times](boundaries.md#accepted-reminder-lead-times) | Support the agreed options and save lead time independently in Cabinet commit order. | Honor 0/15/30/60/120 and school default; save only through Cabinet and preserve confirmed values on failures. | Executable synchronization and delivery checks; no client-clock decision remains. |
| [Daychi reminder delivery](boundaries.md#accepted-daychi-reminder-delivery) | Expose authoritative calendar and confirmed account settings; retain delivery without cross-client deduplication. | Adapt existing refresh/local OS reminders; retain confirmed cache and active reminders after read failures. Presentation belongs to Daychi; cross-client duplicates are allowed. | Zero-minute timing tolerance is accepted; proposed native-capacity behavior and verification remain. No new background refresh capability. |
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
- Shared reminder changes require Cabinet confirmation; offline editing is
  unavailable. Explicit sign-out clears transient local drafts/request state,
  without later replay into the original or another account. Cabinet's accepted
  state remains. An uncertain save is recovered by reading current server settings.
- Sign out of one Daychi installation while the same account is signed in to
  Cabinet and another Daychi installation: authenticated use ends in the calling
  installation, and the other clients remain signed in.
- A failed refresh retains cached schedule, confirmed settings and active
  reminders without an offline-edit queue. A successful refresh
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
