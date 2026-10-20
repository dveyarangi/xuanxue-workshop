# xuanxue-cabinet: provide native content-check capacity for Daychi

## Recipient and outcome

Recipient: Cabinet agent under its operator, `project:cabinet`.
Original coordination: [one-cabinet-login #11](https://github.com/dveyarangi/xuanxue-workshop/issues/11).
Daychi can use Cabinet's existing native `GET me` to validate every protected
native content read, with independent capacity for legitimate native grants
behind one Daychi backend. This is a new contribution to the accepted shared
connection, not a reopening of previously accepted implementation evidence.

## Expected / observed

Cabinet's [completion report](https://github.com/dveyarangi/xuanxue-workshop/issues/15#issuecomment-6263294915) implements the grant-keyed limiter in merged [PR602](https://github.com/gregoryKot/xuanxue-cabinet/pull/602), source `ea4299606ef8a8e2091931645bf4d21c20c5a450`. [Workshop's review](https://github.com/dveyarangi/xuanxue-workshop/blob/ce4aebcd5d0245288563b0a74df7b1dfef7aff4f/docs/current-system.md#native-content-provider-capacity-review--2026-10-19) inspected the complete delta, real-AppModule e2e composition and installed BOUNDARY_SUMMARY. All 19 [main CI checks](https://github.com/gregoryKot/xuanxue-cabinet/actions/runs/39223428645) passed; executed logs include the budget tests and existing account/revoke/parity suites. Supported progress includes per-grant isolation, predecessor/renewed sharing, independent grants behind one IP, boundary timing, retry rounding and invalid-input separation.

Independent credential-free reads at 08:57 UTC on 19 October confirmed staging health `ea42996`, Mongo up, and native me 401 `invalid_token` with expected WWW-Authenticate/no-store and no Set-Cookie. Production health remained `fc2dee2`. These observations do not establish live authenticated content delivery. Accepted native account-session evidence remains unchanged.

### Restart-reset disposition and remaining work

On 19 October the Workshop operator explicitly allowed quota history to reset when the current single-instance provider restarts or is replaced during deployment, and removed the earlier persistence finding as a blocker. The temporary fresh allowance is a documented, non-blocking operational limitation. The previous request for persistent history, replacement-safe handoff or replacement-proof testing is withdrawn. No implementation correction is required for this reset. Concurrently serving replicas still share the normal deployment-wide allowance; no scaling project is assigned.

Cabinet's reviewed implementation/CI/staging progress stands. The remaining paired live outcome is protected material and recording delivery from installed Daychi in iOS Simulator through any Daychi backend and real Cabinet staging. Cabinet supplies the authorized staging account/provider arrangement and provider-side observations as needed; Daychi supplies the client/backend/source mapping in 16. All other cases, including grant revocation, session isolation, block/unblock and outage/recovery, use executed automated tests. No live status/outage/revocation/aging/deletion fixture, quota-history correction or production release is requested. Full joint acceptance remains pending actual read evidence and the applicable executed automated proof.

## Shared contract and conformance

Authority: [native-content-session](https://github.com/dveyarangi/xuanxue-workshop/blob/1fd3890b4a3b56b4a262dfa74e9929b4002d75aa/docs/contracts/native-content-session.md), immutable Workshop revision `1fd3890b4a3b56b4a262dfa74e9929b4002d75aa`. This complete reference includes the operator-approved 19 October restart-reset exception/C11R and the 20 October evidence split and joint-proof runtime. Both recipients use this same amended authority. Wire, identity, security, ordinary rolling-window and C01–C16 behavior remain unchanged; the amendments define sufficient evidence and runtime.

The existing installed BOUNDARY_SUMMARY and its baseline links remain accepted; these evidence/runtime amendments introduce no fresh installation/adoption gate. The current authority above governs the restart exception and acceptance scope. No Daychi reset signal, retry, cache or error-handling change is required.

## Impact and required changes

Complete the provider obligations and prove the existing ones that already hold:

- Retain the native `GET /api/auth/native/me` request, full response, current-state
  validation, error/no-store/WWW-Authenticate behavior and absence of Set-Cookie.
  Daychi's caller authority is the presented native bearer; there is no added
  service secret, service-IP trust or account replica. Reuse valid existing proof.
- For validated GET me only, implement the contract's grant-keyed rolling budget,
  shared across predecessor/renewed credentials and direct app/server checks.
  Distinct grants behind the same egress IP, including one account's two grants,
  remain independent; existing global/IP caps cannot aggregate validated grants.
- Retain invalid-input/IP abuse protection and native acquisition/renewal/revocation
  and browser budgets. Never assign a trusted bucket from unverified token text
  or caller-supplied identity. Internal storage, distribution and module design
  remain Cabinet-owned within the deployment-wide observable guarantee.
- Return exact immutable source, executed checks and deployment state. Identify
  owner-authorized staging/account arrangements needed for the paired content
  proof; retain installation-scoped revocation and other native/browser sessions.

Scope excludes changing content data, Daychi routes, browser SSO, lifecycle wire,
meeting/Zoom access and backend consolidation. Native account-session proof still
returns in [original #7](https://github.com/dveyarangi/xuanxue-workshop/issues/7).

## Execution dependencies

Paired consumer: [daychi-native-content-access #16](https://github.com/dveyarangi/xuanxue-workshop/issues/16). The consumer can implement concurrently; its identified runtime enables joint proof after provider deployment and owner authorization.

Provider implementation/synthetic checks need the accessible settled authority
and Cabinet operator authorization, not Daychi completion or Workshop readiness.
The Daychi companion can implement and test its consumer concurrently. Real joint
proof needs real Cabinet staging at a reported conforming revision, an authorized
account/native grant and installed Daychi in iOS Simulator using any selected
Daychi backend. No particular Daychi hosting environment is required. Status,
revocation and outage arrangements are automated test cases, not mandatory live
fixtures. Cabinet owns the provider/account arrangement; Daychi owns its runtime;
Workshop assesses the returned proof. Do not create
an additional Ready gate or modify accounts/deployments without owner authority.

## BOUNDARY_SUMMARY

```markdown
Existing boundary: Cabinet backend ↔ Cabinet frontend, with entry points api/, web/
and shared/. Cabinet owns accounts, native grants and current account restrictions.
Daychi retains its content backend; Knowledge owns editorial/import preparation.
Accepted schedule/native-account targets and evidence remain in the
[target contracts](https://github.com/dveyarangi/xuanxue-workshop/blob/a07f08747aa7d97e4d3496e87e1d8319db413698/docs/boundaries.md#target-connections) and
[native account profile](https://github.com/dveyarangi/xuanxue-workshop/blob/a07f08747aa7d97e4d3496e87e1d8319db413698/docs/contracts/native-account-session.md); joint results
remain distinct from source implementation. Native sign-in/lifecycle scope is unchanged.

Accepted native content connection: Daychi backend forwards the presented native
bearer to Cabinet GET /api/auth/native/me before each protected native content read.
Cabinet remains the current session/account authority; validated GET me capacity
is isolated per grant rather than shared by Daychi's server IP. Daychi adds no
reader membership, account replica or positive authorization cache. The
[native content contract](https://github.com/dveyarangi/xuanxue-workshop/blob/1fd3890b4a3b56b4a262dfa74e9929b4002d75aa/docs/contracts/native-content-session.md) owns exact wire,
failure, capacity, compatibility and common cases; implementation/joint proof remain work.

Accepted browser-wiki target remains separate: shared Cabinet cookie, per-reader
current validation, fixed matching production/staging authority, browser entry,
return, renewal and logout. Daychi owns protected browser delivery and the accepted
limited public homepage graph projection. The
[web-wiki contract](https://github.com/dveyarangi/xuanxue-workshop/blob/a07f08747aa7d97e4d3496e87e1d8319db413698/docs/contracts/web-wiki-session.md) owns this scope; native bearer
checks do not bypass its cookie policy. Existing native/owner/import/Zoom consumers
and independently coordinated cutovers retain their existing authority.
```

## Accepted current-delivery evidence and runtime — 2026-10-20

Decision: the Workshop operator, 2026-10-20; authoritative sections are in the
immutable common contract above.

Installed Daychi in iOS Simulator with any Daychi backend and real Cabinet staging
is sufficient for acceptance and closure of originals 15/16. The live read uses
the native-content path through that selected backend and Cabinet staging.
Report the client build/source, selected Daychi backend/runtime/source and
Cabinet staging revision; no particular Daychi backend hosting environment is
required. Physical hardware, Android and TestFlight do not block acceptance or
closure. Production release remains recipient-owned and is not an acceptance gate.

Only protected material and recording delivery require live proof. All remaining
cases use inspectable source and executed automated tests, including revocation/
next-read refusal, other native/browser sessions remaining usable, block/unblock,
provider failure/recovery without credential loss, expiry/deletion, malformed
responses, deadlines, issuer isolation and capacity boundaries. No separate live
run or revocation/status/outage/aging/deletion fixture is required.

The accepted single-instance restart-reset exception/C11R remains: no quota-history
persistence, replacement-safe handoff or restart/replacement test gate is added.
All shared behavior remains binding; these amendments establish neither completed
live reads nor deployment/acceptance of an untested runtime. Reuse valid accepted
source/check/N11 evidence without repeating it.

## Acceptance evidence

- Report immutable implementation, complete common-case mapping and executed
  applicable provider checks. Prove same-IP different-grant isolation, same-account
  different-grant isolation, predecessor/renewed sharing, exact 60-second boundary,
  invalid-input protection and unchanged lifecycle/browser budgets. Exercise the
  real HTTP route and actual tracker/limiter composition in executed tests,
  rather than relying only on tracker-isolated checks.
- Establish C01–C16 provider obligations and reuse existing source/check evidence
  where unchanged. Preserve profile, expiry/revocation/account-status and error
  semantics; no source/CI result alone establishes successful live content reads.
- Return Cabinet staging deployment identity and provider-side observations for
  the actual material/recording reads in installed iOS Simulator Daychi through
  any Daychi backend. All remaining cases use executed automated evidence under
  the common scope above; no separate live fixture is required.
- Retain the accepted installed BOUNDARY_SUMMARY and valid revision evidence,
  preserving surrounding collaboration instructions. No reinstall/adoption gate
  is added solely by these evidence/runtime amendments.
  Workshop reconciles source/deployment/joint evidence before full acknowledgement.

Report in this original contribution and link coordination issue 11. Publication
does not establish implementation, release, account authorization or acceptance.
