# xuanxue-cabinet: provide native content-check capacity for Daychi

## Recipient and outcome

Recipient: Cabinet agent under its operator, `project:cabinet`.
Original coordination: [one-cabinet-login #11](https://github.com/dveyarangi/xuanxue-workshop/issues/11).
Daychi can use Cabinet's existing native `GET me` to validate every protected
native content read, with usable ordinary reads for users sharing Daychi's egress
behind one Daychi backend. This is a new contribution to the accepted shared
connection, not a reopening of previously accepted implementation evidence.

## Essential acceptance — 2026-10-21

Decision: the Workshop operator, 2026-10-21: remove everything unnecessary from
acceptance, following the explicit review of required outcomes and excess gates.
The operator reaffirmed preservation of existing implementation and staging;
the purpose is to remove unnecessary ceremony and clear integration closure.
This section governs current acceptance and closure of originals 15/16.

Only protected material and recording delivery require live proof: installed
Daychi in iOS Simulator, any suitable Daychi backend and real Cabinet staging.
Access refusal, revocation, session/account/issuer isolation, temporary-failure
recovery without credential loss, response validation and compatibility use
inspectable source and executed automated tests. No particular backend host,
physical device, Android, TestFlight or production release gates closure.
Ordinary users sharing Daychi's egress must be able to read; this does not
prescribe a per-grant budget, counter algorithm or throughput number.

Technical quotas and exact counter/window, restart, replacement or replica
behavior and exact retry-delay boundaries are not acceptance or closure
requirements.
Existing compatible API values, working protections and useful tests may remain;
no removal or reimplementation in recipient code is assigned. Invalid input
must still cause no unauthorized protected-content delivery.
No performance/stress target or expanded device/environment matrix is added.
Already credited evidence is reused; neither a new report format nor repeating
accepted builds, installation, account proof, CI or synthetic QA gates closure.

Sole common authority: [native-content-session](https://github.com/dveyarangi/xuanxue-workshop/blob/3c6ff8a7136483b3d266786fa8267eab4f2d2828/docs/contracts/native-content-session.md#essential-acceptance--2026-10-21), immutable revision `3c6ff8a7136483b3d266786fa8267eab4f2d2828`.
The following technical sections preserve compatible exchange and credited work;
they do not add acceptance gates beyond this operator-agreed section.

## Credited evidence and remaining closure actions — 2026-10-21

The credited work below is retained under the operator-approved 21 October
acceptance reduction above. The original issue remains the provider work/report channel.

### Credited — provider implementation and automated proof

- [Cabinet's completion report](https://github.com/dveyarangi/xuanxue-workshop/issues/15#issuecomment-6263294915)
  and the [review](https://github.com/dveyarangi/xuanxue-workshop/blob/ce4aebcd5d0245288563b0a74df7b1dfef7aff4f/docs/current-system.md#native-content-provider-capacity-review--2026-10-19)
  establish PR602 / ea42996 source, actual mounted HTTP/limiter composition,
  executed provider common-case tests and all 19 inspected CI checks. Existing
  account/current-state/error/lifecycle behavior is retained. The change preventing
  all Daychi readers from consuming one shared server-IP request allowance is
  implemented and checked; it is not a new limit implementation or retest request.
- Cabinet staging deployment is confirmed; fresh 21 October health returns 200 at
  20128fb, Mongo up. No replacement deployment is requested to repeat this proof.
- The supplied installed BOUNDARY_SUMMARY is accepted at ea42996; no reinstall or
  adoption gate is outstanding for this evidence/runtime update.
- The operator's accepted single-instance restart-reset exception stands. The old
  persistence/replacement-history finding is closed as an acceptance blocker;
  there is no history handoff correction, live restart or replacement-test request.

The provider source/test/deployment subset is credited. The shared actual native
material/recording reads have not been reported; that does not reopen this subset.

### Remaining actions and responsible parties

| Owner | Only remaining action | Completion evidence / condition |
|---|---|---|
| Daychi under @stnleo, in [16](https://github.com/dveyarangi/xuanxue-workshop/issues/16) | Make the selected Daychi backend usable, or use another suitable backend, then return the actual material and recording-bearing reads through the identified installed iOS Simulator client and real Cabinet staging. The client/build mapping and installation preparation are already reported and credited in 16. | An identified client/backend/provider chain and the two successful reads. This is the outstanding paired outcome, not a Cabinet implementation failure. |
| Cabinet under @kotlarewski | Provide account/read-authority assistance only if an actual unresolved need is reported for those reads. Reuse the existing authorized staging account/native grant and accepted account evidence. | No new two-grant/browser arrangement, live revocation, block/unblock, outage, aging, deletion, role change or successful-account rerun is required. No new Cabinet code/test task is outstanding in this read. |
| Workshop under @Yarangi | Reconcile the actual reads with credited provider/consumer executed automated evidence and accept/close the paired contribution when complete. | Reuse prior proof; no request to regenerate the implementation, suite or installed summary. |

Physical hardware, Android, TestFlight, production release, browser DNS, reminder 17,
and prior closure of this issue add no prerequisite for the reads. Only material/
recording delivery is live; every other case uses executed automated evidence.

## Shared contract and conformance

The sole common authority and current essential acceptance are linked above.
The 21 October operator decision withdraws prescribed quota/counter/window/
restart/replica obligations. The remaining wire, identity, access, refusal and
recovery behavior stays compatible. No new provider or consumer implementation,
reset signal, context-installation gate or rerun of credited checks is assigned.
The already installed boundary context remains reusable; this issue's current
authority supersedes earlier mandatory capacity wording.

## Retained implementation scope

This section states the accepted technical obligations and compatibility context.
The current credited/remaining section above determines outstanding work; it is
not a request to repeat the reviewed implementation, tests or installed context.

### Accepted behavior retained

Complete the provider obligations and prove the existing ones that already hold:

- Retain the native `GET /api/auth/native/me` request, full response, current-state
  validation, error/no-store/WWW-Authenticate behavior and absence of Set-Cookie.
  Daychi's caller authority is the presented native bearer; there is no added
  service secret, service-IP trust or account replica. Reuse valid existing proof.
- Preserve usable ordinary authenticated reads for users sharing Daychi's egress.
  No fixed throughput, per-grant accounting, distributed counter or limiter
  correction is required. Existing working resource protections may remain.
- Retain native acquisition/renewal/revocation and access authority. Caller-supplied
  identity cannot authorize a read. Internal storage, distribution and module
  design remain Cabinet-owned; no new deployment or counter design is assigned.
- Return exact immutable source, executed checks and deployment state. Identify
  owner-authorized staging/account arrangements needed for the paired content
  proof; retain installation-scoped revocation and other native/browser sessions.

Scope excludes changing content data, Daychi routes, browser SSO, lifecycle wire,
meeting/Zoom access and backend consolidation. Native account-session proof still
returns in [original #7](https://github.com/dveyarangi/xuanxue-workshop/issues/7).

## Execution dependencies

Provider source/automated checks/deployment are credited. The paired actual read
outcome comes from [16](https://github.com/dveyarangi/xuanxue-workshop/issues/16):
installed Simulator Daychi, any working selected Daychi backend and real Cabinet
staging using existing authorized account/native-grant access. Cabinet assists
only for an actual unresolved account/read need. Status/revocation/outage and
other agreed cases use applicable automated evidence, not new live fixtures.
Neither closure of 15, browser DNS, reminder work nor a particular hosting service
is an additional prerequisite. Workshop reconciles both contributions together.

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
Cabinet remains the current session/account authority; ordinary users sharing
Daychi's egress can read, with no prescribed numeric quota or grant counter. Daychi adds no
reader membership, account replica or positive authorization cache. The
[native content contract](https://github.com/dveyarangi/xuanxue-workshop/blob/3c6ff8a7136483b3d266786fa8267eab4f2d2828/docs/contracts/native-content-session.md) owns exact wire,
failure, compatibility and current common cases; implementation/joint proof remain work.

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
responses, deadlines and issuer isolation. No separate live
run or revocation/status/outage/aging/deletion fixture is required.

The 21 October essential acceptance removes quota, counter, exact-window,
restart/replacement and replica requirements altogether. Other shared access and
compatibility behavior remains binding; these amendments establish neither completed
live reads nor deployment/acceptance of an untested runtime. Reuse valid accepted
source/check/N11 evidence without repeating it.

## Closure review

The current credited/remaining section above is the complete outstanding-action
list under the agreed evidence form and exclusions. Existing source/CI/automated
and installed-context evidence is reused at its valid revision. Report only the
remaining runtime/shared outcomes in this original issue and link its companion.
Workshop checks them against the same immutable authority; it does not require
repeat accepted work or add a criterion from a later QA disclosure. This update
records credited subsets, not completed live proof or full assignment acceptance.
