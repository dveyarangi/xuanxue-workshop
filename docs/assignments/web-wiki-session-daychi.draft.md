# daychi: Cabinet-authenticated web-wiki reading

**Published, amended 2026-10-20:** [original assignment](https://github.com/dveyarangi/xuanxue-workshop/issues/13). Recipient label: `project:daychi`.
The original issue holds current recipient work and reports; this file retains the
reviewed published assignment. Publication is not implementation or deployed proof.

Accepted web-wiki shared-browser-session implementation assignment.

Prepared within [01-0009 web-wiki-cabinet-session](https://github.com/dveyarangi/xuanxue-workshop/blob/ec3f17a7808f81a098e432958f89f1018368a32e/docs/tickets/01-0009-web-wiki-cabinet-session.md).
Shared contract revision: `ec3f17a7808f81a098e432958f89f1018368a32e`.
Original coordination request: [app/wiki connection #11](https://github.com/dveyarangi/xuanxue-workshop/issues/11).

## Recipient and outcome

Recipient: Daychi under its operator. Visitors may see the separately accepted
limited public homepage graph overview before entering the protected reader.
All and only readers with a valid Cabinet
browser session can read `wiki.xuanxue.su`, reuse Cabinet sign-in with original-page
return and share its renewal/logout. Cabinet owns identity/current-account/session
authority. Daychi owns frontend/backend reader delivery, scoped enforcement and
content representations. Workshop coordinates the shared contract, anonymous-access
transition and joint acceptance; Daychi's operator owns local implementation/release.

## Expected / observed

At inspected Daychi `d2cde6b93ef79734e4de0438ddc2e138698214af`,
[graph.js](https://github.com/sleontenko/daychi/blob/d2cde6b93ef79734e4de0438ddc2e138698214af/apps/wiki-graph/src/graph.js)
uses browser invitation-token storage and a distinct native-host request branch.
[daychee_app.py](https://github.com/sleontenko/daychi/blob/d2cde6b93ef79734e4de0438ddc2e138698214af/practice_api/daychee_app.py)
supplies an invitation authorizer to wiki and other capabilities;
[wiki_app.py](https://github.com/sleontenko/daychi/blob/d2cde6b93ef79734e4de0438ddc2e138698214af/practice_api/wiki_app.py)
also mounts public material/semantic/article readers. These source paths do not
establish the accepted Cabinet web-reader integration.

The [original article completion report](https://github.com/dveyarangi/xuanxue-workshop/issues/9#issuecomment-6113936401)
claims deployed public/private article projections, active v1, recording redaction
and retained owner/import access. Those existing content obligations remain in
scope for regressions; they are not proof of this new authentication transition.
Compare actual implementation/deployment with the inspected baseline and report
the delivered origin/source/configuration rather than assuming a branch equals runtime.

[Original coordination request 11](https://github.com/dveyarangi/xuanxue-workshop/issues/11)
requests the same protected app/wiki content after Cabinet login, including
recording links, without additional role/invitation/per-material approval. This
assignment covers its accepted browser portion. Existing content representations
remain Daychi-owned: retained public projections keep their redaction, while this
scope adds no new recording entitlement within an authenticated wiki projection.
The proposed native content-server adapter, native caller trust and its capacity
question remain separate coordination work, not accepted by this assignment.

## Shared contract and conformance

The operator accepted the limited public homepage graph overview on 2026-10-14.
The contract's **Accepted public homepage graph overview** section is the sole
definition of that exception: section names/counts and anonymous structure only;
material/subtopic names, original identifiers, dates, content and source/recording
links stay excluded. Daychi owns this separate public projection. The Cabinet
session wire and all protected reader obligations are unchanged. Acceptance of
the exception does not verify the reported local candidate or authorize release.

Source and QA accessibility are resolved. [Workshop's published-source review](https://github.com/dveyarangi/xuanxue-workshop/issues/13#issuecomment-6175265222) and [correction review](https://github.com/dveyarangi/xuanxue-workshop/issues/13#issuecomment-6179412624) inspected the candidate; the browser source and follow-up corrections are now in Daychi main `c146326c7ea552772d8c804b3a08ad5637ca5eb0`. No repeat source/QA publication is requested. Canonical staging DNS/ownership/TLS and actual paired browser proof remain outstanding under this assignment's existing criteria; accessible source does not establish deployed acceptance.

The sole shared definition is the
[accepted web-wiki shared-browser-session contract](https://github.com/dveyarangi/xuanxue-workshop/blob/ec3f17a7808f81a098e432958f89f1018368a32e/docs/contracts/web-wiki-session.md).
Use the same published revision as the
[Cabinet contribution](https://github.com/dveyarangi/xuanxue-workshop/issues/12).
The contract fixes production/staging profiles, exact session-check request/statuses,
deadline/redirect/retry rules, renewal-cookie relay, browser entry/destination
validation, Cabinet-site logout, compatibility and common proof cases.
The [implementation plan](https://github.com/dveyarangi/xuanxue-workshop/blob/ec3f17a7808f81a098e432958f89f1018368a32e/docs/rfc/01-0009-web-wiki-cabinet-session.md)
maps the complete outcome and adversarial coverage; it defines no alternate wire.

This is the shared browser cookie, not the superseded wiki handoff/token/secret
scheme or the accepted native account-session work in
[original issue 8](https://github.com/dveyarangi/xuanxue-workshop/issues/8).
There is no wiki-specific role, reader registration, account replica, credential
database, client secret, signing key or independent wiki session/logout lifecycle.
Business/editorial/native records and nonsecret bookmarks are not removed by this scope.

## Impact and required changes

- Route `wiki.staging.xuanxue.su` to the staging reader deployment. Retain the
  production profile for the recipient-owned production release, which is not a
  current acceptance or closure prerequisite. Use the contract's fixed matching Cabinet origin, cookie
  name/domain and entry/return/logout URLs in each profile. Staging forwards only
  `session_staging` to staging Cabinet and ignores production's cookie; neither
  profile falls back to the other. Apply exact profile attributes to renewal
  relay and duplicate handling. Own/report reader DNS/HTTPS and hosting evidence.
- Receive the browser session at the wiki-origin reader boundary, forwarding to
  the internal Daychi backend if hosting differs. Browser code uses cookie delivery
  without reading HttpOnly or attaching a wiki bearer. Replace the web invitation
  login/token use and local logout action; preserve the native host's owned path.
- Validate every protected web read through the fixed Cabinet operation, forwarding
  only the session cookie. Empty success alone authorizes delivery. Implement the
  accepted missing/duplicate refusal, 401/403 distinction and temporary failure,
  total deadline, no redirect following/automatic retry, no-store and valid rolling
  cookie relay. Failure/refusal retains the browser cookie, including after a
  newer sign-in; invalid renewal attributes are integration failure.
- Retain the current wiki path/query/hash for the fixed Cabinet entry and use its
  existing sign-in journey. Provide navigation to Cabinet's logout page only;
  add no wiki mutation/proxy or mandatory return after logout. Current refusal
  removes protected reader state; cached view restore or a stale response cannot
  reinstate it. Temporary-error presentation remains Daychi-owned within the contract.
- Provide the separate public homepage overview within the contract's allowlist.
  Cookie/query/request variations cannot expand it into protected reader data.
  Entering the reader follows the existing fixed-profile session/entry journey;
  its public projection introduces no reader credential or Cabinet dependency.
  Routing, internal DTO, data preparation and visual layout remain Daychi-owned.
- Inventory and close every anonymous web reader-content path, including public
  material/graph/recent/semantic/article/concept APIs, direct origins, aliases,
  embedded/static content and controlled old caches. No-store alone does not purge
  already public delivery caches. Login/application/support assets may stay public
  only when they contain no protected reader data. Distinguish the newly allowed
  homepage projection from these existing reader APIs in the exposure/cache
  inventory; the exception does not reopen them.
- Scope the new authority to web reading. Preserve native/private invitation access,
  Zoom and owner/import/Knowledge authority, content identities/DTOs and existing
  recording/credential redaction. A global replacement of the shared invitation
  authorizer or a frontend native-host flag is not sufficient server enforcement.
  Legacy/native credentials cannot replace Cabinet authority on web delivery.
- Supply the complete standing boundary summary below, preserving surrounding
  collaboration rules. Internal routing/modules/libraries, content API and UI
  representation remain Daychi-owned within the accepted authority and exposure.

## Execution dependencies

Daychi can implement against the published settled contract under its operator
before Cabinet deployment, using controlled provider behavior for local boundary
tests. Native issue 8, public schedule pilot completion, Workshop readiness and
installation acknowledgement do not gate this contribution.

Actual two-site proof and web cutover need the conforming [Cabinet contribution #12](https://github.com/dveyarangi/xuanxue-workshop/issues/12),
reachable origins/source/configuration, controlled accounts/browser and complete
reader exposure/cache inventory. Cabinet's operator owns provider/account fixtures;
Daychi's operator owns reader hosting, cache controls and deployment approval.
Workshop accepts the common proof and coordinates the anonymous-access transition
in this original 13, paired with 12. Closed article issue 9 retains accepted
article work and adds no remaining browser action. The real deployed pair needed
for current proof is Cabinet staging and canonical wiki.staging.xuanxue.su;
production rollout and live boundary-case fixture changes are not prerequisites.
Earlier article work is not retroactively failed by this new access requirement.
After cutover, failure/rollback cannot silently restore anonymous access or an
invitation-based web fallback. Report partial releases as partial.

## BOUNDARY_SUMMARY

```markdown
Existing boundaries: native Daychi (`apps/practice-app`) and shared wiki reader
(`apps/wiki-graph`) ↔ Daychi content backend (`practice_api`). Native schedule
also retains its school-HTML and Telegram-correction path. Native/private reader,
Zoom and owner/import access remain Daychi-owned; Cabinet web authentication does
not replace them. [Current scope/evidence](https://github.com/dveyarangi/xuanxue-workshop/blob/ec3f17a7808f81a098e432958f89f1018368a32e/docs/current-system.md#daychi).

Knowledge→Daychi editorial/owner import and shared reader→Daychi article/concept/
graph projections remain existing content boundaries. [Original article issue 9](https://github.com/dveyarangi/xuanxue-workshop/issues/9)
and Daychi's provider-owned content definitions govern active v1, projection,
identity/redaction and source consistency. Authentication work does not retire v1
or change editorial authority.

Accepted target boundaries, joint integration not established: Daychi clients ↔
Cabinet backend for schedule/account capabilities; Daychi backend ↔ Cabinet backend
for authoritative access checks. [Target contracts](https://github.com/dveyarangi/xuanxue-workshop/blob/ec3f17a7808f81a098e432958f89f1018368a32e/docs/boundaries.md#target-connections)
and [native account-session profile](https://github.com/dveyarangi/xuanxue-workshop/blob/3c98d4a5201710f8f777183dd7b61caefe47e2d5/docs/contracts/native-account-session.md) own
their distinct scopes.

Accepted web-wiki target: Cabinet owns the shared browser session and current-account
validation; Daychi owns protected web delivery and calls Cabinet for each protected
read. All and only valid Cabinet-authenticated web readers receive the same content,
without extra wiki eligibility or persisted reader credentials/accounts.
[Web-wiki session contract](https://github.com/dveyarangi/xuanxue-workshop/blob/ec3f17a7808f81a098e432958f89f1018368a32e/docs/contracts/web-wiki-session.md) owns common cookie,
entry/return, renewal/logout, environment separation and failure guarantees.
Daychi's homepage may expose only the contract's separate limited public graph
overview without a Cabinet session. Existing reader APIs remain protected;
entering the reader reuses a valid session or signs in with original-page return.
Daychi owns preview data/projection and exposure controls. This exception changes
no Cabinet wire, account authority, native/private or editorial/import scope.
Coordinated anonymous-access
cutover, recipient implementation and deployed proof are separate from acceptance.
```

## Accepted current-delivery acceptance — 2026-10-20

Decision: the Workshop operator, 2026-10-20. The common immutable authority above
includes the accepted evidence split and acceptance-environment amendment.

Current acceptance and closure use real Cabinet staging and canonical
wiki.staging.xuanxue.su. Production rollout remains recipient-owned release work
and does not block either acceptance or closure; it is not a remaining acceptance
action in these contributions. No completed live run or production deployment is
claimed by this scope amendment.

Live browser proof covers protected material and recording reads with a valid
Cabinet session, sign-in with original-page return, and logout followed by refusal
of the next protected read. Renewal, expiry, account deletion/blocking, malformed
responses, timeouts and remaining boundary cases use inspectable source and
executed automated tests; a separate live run of every such case is not required.

Environment isolation remains required in executed automated tests and inspectable
configuration: both profiles/sign-in orders, separate cookies and account/key
authorities, active-name duplicates versus distinct names, cross-environment
refusal, independent renewal/logout, staging legacy cleanup and return routing.
No live production run or simultaneous deployed production/staging run is required.
Actual staging origin/TLS/routing and matching source/runtime/configuration accompany
the live proof; a production DNS alias does not establish a separate staging reader.

## Acceptance evidence

The same authority distinguishes the limited public homepage overview from
protected delivery. Daychi supplies inspectable source and executed checks for
anonymous/empty projection, excluded content/identities, cookie/query input
variations, protected-reader refusal and all inventoried reader/alias/cache
paths. The accepted live sign-in/return/read/logout scenarios use that reader;
the preview introduces no new Cabinet endpoint or credential dependency.

Consumer evidence covers current/missing/forged/expired/deleted/blocked/unblocked/
duplicate sessions, exact provider request and empty success, unexpected status/
body/redirect, 429/5xx/deadline/transport/TLS failures without protected delivery,
retained cookies, renewal relay and multiple readers. Source/storage/log review
establishes per-read validation and absence of reader credential/account persistence.

Executed boundary/regression checks cover stale responses, Back/restore/retry,
anonymous requests across all inventoried delivery paths/caches, native/private,
Zoom, owner/import authority, content projection/redaction and active v1. A blocked
graph with anonymously readable protected content is not conforming. The live
main-scenario proof runs against the actual staging reader with Cabinet staging;
mock-only success cannot replace it.

Report in this original contribution: immutable implementation commits/PRs,
the shared authority, executed case mapping and outcomes, changed instruction
context, actual staging origin/source/runtime/configuration, exposure/cache or
provider evidence as applicable, authorized account procedure and disclosed limits.
Credentials and private account data stay outside issue/log artifacts.

Workshop compares both contributions against the agreed common scope and
acknowledges acceptance in the original assignments. The reader exposure/cache
transition remains in 13 paired with 12; article issue 9 has no remaining browser
action. Keep this assignment open until outstanding recipient acceptance actions
and the common review are complete. Green CI or issue closure alone is not joint
acceptance; production rollout adds no hold after the agreed proof passes.
