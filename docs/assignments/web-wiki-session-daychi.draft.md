# daychi: Cabinet-authenticated web-wiki reading

**Published, amended 2026-10-21:** [original assignment](https://github.com/dveyarangi/xuanxue-workshop/issues/13). Recipient label: `project:daychi`.
The original issue holds current recipient work and reports; this file retains the
reviewed published assignment. Publication is not implementation or deployed proof.

Accepted web-wiki shared-browser-session implementation assignment.

Prepared within [01-0009 web-wiki-cabinet-session](https://github.com/dveyarangi/xuanxue-workshop/blob/3c6ff8a7136483b3d266786fa8267eab4f2d2828/docs/tickets/01-0009-web-wiki-cabinet-session.md).
Shared contract revision: `3c6ff8a7136483b3d266786fa8267eab4f2d2828`.
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

## Essential acceptance — 2026-10-21

Decision: the Workshop operator, 2026-10-21: remove everything unnecessary from
acceptance, following the explicit review of required outcomes and excess gates.
The operator reaffirmed preservation of existing implementation and staging;
the purpose is to remove unnecessary ceremony and clear integration closure.
This section governs current acceptance and closure of originals 12/13.

Live proof on real Cabinet staging and canonical wiki.staging.xuanxue.su covers:
protected material and recording reads with a valid session; Cabinet sign-in
returns to the original wiki page; logout refuses the next protected read.
The already agreed remaining access, renewal, account-status, failure/recovery,
environment-isolation and compatibility behavior uses inspectable source and
executed automated tests. Existing protected/public exposure boundaries remain.
Production rollout and live production proof are non-blocking.

Technical quotas and exact counter/window, restart, replacement or replica
behavior and exact retry-delay boundaries are not acceptance or closure
requirements.
Existing compatible API values, working protections and useful tests may remain;
no removal or reimplementation in recipient code is assigned. Invalid input
must still cause no unauthorized protected-content delivery.
No performance/stress target or expanded device/environment matrix is added.
Already credited evidence is reused; neither a new report format nor repeating
accepted builds, installation, account proof, CI or synthetic QA gates closure.

Sole common authority: [web-wiki-session](https://github.com/dveyarangi/xuanxue-workshop/blob/3c6ff8a7136483b3d266786fa8267eab4f2d2828/docs/contracts/web-wiki-session.md#essential-acceptance--2026-10-21), immutable revision `3c6ff8a7136483b3d266786fa8267eab4f2d2828`.
The following technical sections preserve compatible exchange and credited work;
they do not add acceptance gates beyond this operator-agreed section.

## Credited evidence and remaining closure actions — 2026-10-21

The credited work below is retained under the operator-approved 21 October
acceptance reduction above. The original issue remains the work/report channel.

### Credited — no repeat implementation or test request

- Daychi's protected reader, per-read Cabinet check, restricted public homepage
  projection, route/profile refusal and scoped browser/source checks are reviewed
  in the [published-source review](https://github.com/dveyarangi/xuanxue-workshop/issues/13#issuecomment-6175265222).
- The UTF-8/Windows defect and inspectable-source hold are resolved. The
  [correction review](https://github.com/dveyarangi/xuanxue-workshop/issues/13#issuecomment-6179412624)
  records all 43 boundary tests passing and executed CI (241 backend / 42 app /
  23 wiki). The source and corrections are available at c146326; no repeat source
  publication or Windows run is requested.
- Separate reader service/configuration and bounded direct-host synthetic preview,
  anonymous/invalid refusal and fixed canonical redirects were inspected in that
  same review. This preparation is credited, within its reported source/runtime
  limits; direct-host responses are not the unreported canonical browser result.
- Cabinet's provider source/HTTP proof and current staging deployment are reusable.
  Fresh 21 October Cabinet health is 200 at 20128fb; no new provider implementation
  or deployment is a prerequisite.

### Remaining actions and responsible parties

| Owner | Only remaining action | Completion evidence / condition |
|---|---|---|
| Daychi @stnleo and DNS operator @kotlarewski | Complete the existing private ownership-value handoff and canonical staging DNS/TLS mapping, coordinated through [12](https://github.com/dveyarangi/xuanxue-workshop/issues/12#issuecomment-6179411400). | wiki.staging.xuanxue.su reaches the chosen independent staging reader with working TLS; the 21 October lookup still fails. This blocks the canonical live browser run, not completed source/test work. |
| Daychi @stnleo | Identify the actual staging reader source/configuration and complete the existing exposure/controlled-cache inventory for the accepted staging surface. Reuse inspected route/alias/public-projection tests; return the remaining deployment/configuration evidence rather than repeat the implementation. | The accepted protected reader boundary and limited public overview correspond to the running staging revision; controlled old staging paths/caches provide no bypass. |
| Daychi and Cabinet under @stnleo / @kotlarewski | Show the three agreed live staging scenarios with the existing authorized account/session: valid-session material/recording reads; sign-in/original-page return; logout then next-read refusal. | Matching provider/reader/runtime observations are linked once in 12/13; no live expiry/deletion/status/outage matrix is required. |
| Workshop under @Yarangi | Reconcile those observations and staging coverage with credited source/executed automated proof, then record acceptance and close when the remaining contribution is complete. | No new case or repeated accepted check without an identified changed basis or concrete gap. |

Production rollout and live production proof are non-blocking. Browser transition
belongs here with 12; closed article 9 has no remaining action. Native content,
reminder work, new platform screenshots and repeated account acceptance add no hold.

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
[accepted web-wiki shared-browser-session contract](https://github.com/dveyarangi/xuanxue-workshop/blob/3c6ff8a7136483b3d266786fa8267eab4f2d2828/docs/contracts/web-wiki-session.md).
Use the same published revision as the
[Cabinet contribution](https://github.com/dveyarangi/xuanxue-workshop/issues/12).
The contract fixes production/staging profiles, exact session-check request/statuses,
deadline/redirect/retry rules, renewal-cookie relay, browser entry/destination
validation, Cabinet-site logout, compatibility and common proof cases.
The [implementation plan](https://github.com/dveyarangi/xuanxue-workshop/blob/3c6ff8a7136483b3d266786fa8267eab4f2d2828/docs/rfc/01-0009-web-wiki-cabinet-session.md)
maps the complete outcome and adversarial coverage; it defines no alternate wire.

This is the shared browser cookie, not the superseded wiki handoff/token/secret
scheme or the accepted native account-session work in
[original issue 8](https://github.com/dveyarangi/xuanxue-workshop/issues/8).
There is no wiki-specific role, reader registration, account replica, credential
database, client secret, signing key or independent wiki session/logout lifecycle.
Business/editorial/native records and nonsecret bookmarks are not removed by this scope.

## Retained implementation scope

This section states the accepted technical obligations and compatibility context.
The current credited/remaining section above determines outstanding work; it is
not a request to repeat the reviewed implementation, tests or installed context.

### Accepted behavior retained

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

Source/automated reader work above is credited. Canonical staging DNS/TLS blocks
the agreed live browser run. That run uses the existing authorized Cabinet
staging session and matching actual reader/provider configuration; it does not
need new live status/expiry/deletion/outage fixtures. Daychi owns running-reader
and controlled staging exposure/cache coverage; Cabinet/DNS owns its named
handoff, with Daychi's private ownership-value assistance. Browser transition
remains in 13 paired with 12, not closed article 9. Production rollout, native
content and reminder work do not gate current acceptance.

## BOUNDARY_SUMMARY

```markdown
Existing boundaries: native Daychi (`apps/practice-app`) and shared wiki reader
(`apps/wiki-graph`) ↔ Daychi content backend (`practice_api`). Native schedule
also retains its school-HTML and Telegram-correction path. Native/private reader,
Zoom and owner/import access remain Daychi-owned; Cabinet web authentication does
not replace them. [Current scope/evidence](https://github.com/dveyarangi/xuanxue-workshop/blob/3c6ff8a7136483b3d266786fa8267eab4f2d2828/docs/current-system.md#daychi).

Knowledge→Daychi editorial/owner import and shared reader→Daychi article/concept/
graph projections remain existing content boundaries. [Original article issue 9](https://github.com/dveyarangi/xuanxue-workshop/issues/9)
and Daychi's provider-owned content definitions govern active v1, projection,
identity/redaction and source consistency. Authentication work does not retire v1
or change editorial authority.

Accepted target boundaries, joint integration not established: Daychi clients ↔
Cabinet backend for schedule/account capabilities; Daychi backend ↔ Cabinet backend
for authoritative access checks. [Target contracts](https://github.com/dveyarangi/xuanxue-workshop/blob/3c6ff8a7136483b3d266786fa8267eab4f2d2828/docs/boundaries.md#target-connections)
and [native account-session profile](https://github.com/dveyarangi/xuanxue-workshop/blob/3c98d4a5201710f8f777183dd7b61caefe47e2d5/docs/contracts/native-account-session.md) own
their distinct scopes.

Accepted web-wiki target: Cabinet owns the shared browser session and current-account
validation; Daychi owns protected web delivery and calls Cabinet for each protected
read. All and only valid Cabinet-authenticated web readers receive the same content,
without extra wiki eligibility or persisted reader credentials/accounts.
[Web-wiki session contract](https://github.com/dveyarangi/xuanxue-workshop/blob/3c6ff8a7136483b3d266786fa8267eab4f2d2828/docs/contracts/web-wiki-session.md) owns common cookie,
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

## Closure review

The current credited/remaining section above is the complete outstanding-action
list under the agreed evidence form and exclusions. Existing source/CI/automated
and installed-context evidence is reused at its valid revision. Report only the
remaining runtime/shared outcomes in this original issue and link its companion.
Workshop checks them against the same immutable authority; it does not require
repeat accepted work or add a criterion from a later QA disclosure. This update
records credited subsets, not completed live proof or full assignment acceptance.
