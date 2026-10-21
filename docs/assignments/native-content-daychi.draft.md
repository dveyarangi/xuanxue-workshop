# daychi: serve protected native content through the Cabinet session

## Recipient and outcome

Recipient: Daychi agent under its operator, `project:daychi`.
Original coordination: [one-cabinet-login #11](https://github.com/dveyarangi/xuanxue-workshop/issues/11).
One Cabinet login in the native app gives access to its protected wiki content,
including recording links, while invalidated sessions refuse new reads and
temporary Cabinet failures permit recovery without losing the credential.

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
acceptance reduction above. The original issue remains the consumer work/report channel.

### Credited — no repeat build, installation or source/test request

- PR18 bb7295f native-content adapter, mounted reader, lifecycle/generation safety,
  recording protection and scoped source/CI results are reviewed in the
  [mounted-reader review](https://github.com/dveyarangi/xuanxue-workshop/issues/16#issuecomment-6238564666)
  and [full-parent review](https://github.com/dveyarangi/xuanxue-workshop/issues/16#issuecomment-6240310972).
  Synthetic full-parent/navigation/restoration/error evidence is credited within
  its declared scope; existing account-8 acceptance remains reusable.
- The [7be8dac client/configuration receipt](https://github.com/sleontenko/daychi/blob/7be8dac39523380702ccaec9d94dab79ae061edb/docs/qa-native-materials-staging-2026-10-20/README.md)
  identifies PR18 source and an ordinary installed iOS27 Simulator Debug 1.0.0(18)
  build with the native-content path enabled, its selected backend and real
  Cabinet staging. This supersedes the old unknown build/backend mapping. The
  installed signed-out screen and reported 296-test run retain Daychi provenance;
  neither claims authenticated material/recording delivery.
- [Workshop's runtime-preparation review](https://github.com/dveyarangi/xuanxue-workshop/issues/16#issuecomment-6300821580)
  inspected complete 93f6d29/f8c28dc bootstrap deltas and the ownership-call fix.
  Product backend/app modules are unchanged. The published/tested correction is
  credited as source preparation; it has not been observed running.
- Cabinet provider implementation, executed checks, staging deployment and
  installed boundary context are credited in [15](https://github.com/dveyarangi/xuanxue-workshop/issues/15).
  No new provider code, deployment or quota-history correction is required.

### Remaining actions and responsible parties

| Owner | Only remaining action | Completion evidence / condition |
|---|---|---|
| Daychi under @stnleo | Make the selected backend usable for the installed client, or select any other suitable Daychi backend. The reported first deployment failed and no corrected replacement was queued during the platform pause. | The 21 October health read of the selected Railway origin still returns edge 404 Application not found. A working chosen backend enables the read; this particular Railway service and hosting platform are not acceptance criteria. No new app build/upload is required merely to repeat credited installation. |
| Daychi under @stnleo | Use the existing authorized Cabinet staging account/native grant to show actual protected material and recording-bearing delivery through installed iOS Simulator Daychi and the chosen backend. | Return the two actual read outcomes and identify the versions/runtime used; reuse the already reported mapping where unchanged. This is the remaining live acceptance evidence. |
| Cabinet under @kotlarewski | Assist with account/read authority only if an actual unresolved access need appears. | Existing account evidence and roles remain. No new account-role mutation, two-grant/browser setup or live revocation/status/outage fixture is assigned. |
| Workshop under @Yarangi | Reconcile those actual reads with the credited source/executed automated cases, then record full acceptance and close when complete. | No repeat of existing CI, synthetic navigation/restoration, account acceptance, build or installation without a concrete changed basis or coverage gap. |

The [scope correction](https://github.com/dveyarangi/xuanxue-workshop/issues/16#issuecomment-6299218976)
withdraws the superseded live two-grant/browser, revocation, block/unblock and
outage requests. Every case except material/recording delivery uses executed
automated evidence. Physical hardware, Android, TestFlight, production activation,
browser DNS, reminder 17 and closure of 15 are non-blocking. Keep existing
Teacher/Developer roles; the actual read requires a valid account, not a new role.

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

- Complete and connect the native Cabinet session check to every in-scope
  protected native wiki read, including content/recording links and aliases.
  Before delivery, forward exactly the presented bearer to fixed matching Cabinet
  GET me over verified HTTPS, with no cookies/service secret, redirects, retry
  within the read, positive cache or persisted profile/reader account.
- Enforce the contract's response validation, five-second total deadline and
  401/403/503 meanings, rate-delay handling, credential retention/replacement
  safety and no sensitive downstream/log data. Read required account/session
  fields only to validate Cabinet's response, not to add local reader eligibility.
- Connect the native app's existing Cabinet session to that content path.
  Native-app-to-Daychi-backend bearer transport is exactly the accepted Authorization header;
  internal app/API route selection is Daychi-owned. Explicitly distinguish the
  selected Cabinet path from legacy paths without token guessing or failure
  fallback. Publish the internal route/alias inventory and tested client mapping
  in the implementation report so coverage is inspectable.
- Preserve legacy native consumers and content identity/formats, owner/import
  and meeting/Zoom authorities and the browser cookie policy. A native bearer
  must not bypass canonical browser-wiki routes. Preserve ordinary schedule,
  selections/cache, legacy access and OS reminders; no unrelated redesign or
  global legacy retirement is assigned.

Native acquisition/lifecycle still returns in
[original #8](https://github.com/dveyarangi/xuanxue-workshop/issues/8); browser
implementation and prospective public-reader transition remain in
[original #13](https://github.com/dveyarangi/xuanxue-workshop/issues/13).
Coordinate integration with those scopes; do not recreate already-valid work.

## Execution dependencies

The deployed Cabinet contribution [15](https://github.com/dveyarangi/xuanxue-workshop/issues/15)
is eligible for the agreed actual reads; waiting for its closure is unnecessary.
The selected Daychi runtime startup/availability and the two actual authenticated
reads are the remaining conditions. Use existing authorized staging account/grant
access and reported client mapping; Cabinet assists only for a real access gap.
No particular Daychi backend host, browser DNS, reminder implementation,
TestFlight distribution, successful account rerun or live status/outage/revocation
arrangement is required. Each recipient retains runtime/release ownership.

## BOUNDARY_SUMMARY

```markdown
Existing boundaries: Daychi native app (apps/practice-app) and web wiki
(apps/wiki-graph) ↔ Daychi backend (practice_api); Knowledge supplies reviewed
editorial/import inputs. Daychi owns content and its client/API transport;
Cabinet owns account/session validity. Existing native/owner/import/meeting access
and content v1 remain fulfilled until their independently coordinated transition.

Accepted schedule/native-account targets remain governed by the
[target contracts](https://github.com/dveyarangi/xuanxue-workshop/blob/a07f08747aa7d97e4d3496e87e1d8319db413698/docs/boundaries.md#target-connections) and
[native account profile](https://github.com/dveyarangi/xuanxue-workshop/blob/a07f08747aa7d97e4d3496e87e1d8319db413698/docs/contracts/native-account-session.md). Native sign-in,
renewal, secure storage and installation-scoped sign-out remain their own scope.

Accepted native content connection: each protected Cabinet-authenticated native
read forwards the presented bearer to the fixed matching Cabinet GET me. Its
current native grant/account decision is sufficient; no additional reader role,
invitation, account replica or positive cache is used. Daychi owns explicit
coexistence with legacy native transport, downstream protected delivery and
failure/recovery. Ordinary shared-egress reads remain usable without a prescribed quota or counter.
The [native content contract](https://github.com/dveyarangi/xuanxue-workshop/blob/3c6ff8a7136483b3d266786fa8267eab4f2d2828/docs/contracts/native-content-session.md) owns exact
wire, compatibility and current common cases; activation and joint proof remain work.

Accepted browser-wiki target remains separate under the
[web-wiki contract](https://github.com/dveyarangi/xuanxue-workshop/blob/a07f08747aa7d97e4d3496e87e1d8319db413698/docs/contracts/web-wiki-session.md): shared Cabinet browser cookie,
per-request authoritative check, fixed matching environment, renewal/return/logout,
protected reader delivery and coordinated origin/path/cache transition. The
limited public homepage graph overview remains its canonical exception. Native
bearers do not replace this browser policy. Knowledge's editorial/import ownership
and structured-article compatibility remain unchanged.
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
