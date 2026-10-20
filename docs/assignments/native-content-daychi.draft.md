# daychi: serve protected native content through the Cabinet session

## Recipient and outcome

Recipient: Daychi agent under its operator, `project:daychi`.
Original coordination: [one-cabinet-login #11](https://github.com/dveyarangi/xuanxue-workshop/issues/11).
One Cabinet login in the native app gives access to its protected wiki content,
including recording links, while invalidated sessions refuse new reads and
temporary Cabinet failures permit recovery without losing the credential.

## Expected / observed

The mounted/default-off Cabinet-native reader in [Daychi PR18](https://github.com/sleontenko/daychi/pull/18) and its scoped synthetic checks are already reviewed in [the mounted-reader review](https://github.com/dveyarangi/xuanxue-workshop/issues/16#issuecomment-6238564666) and [full-parent navigation review](https://github.com/dveyarangi/xuanxue-workshop/issues/16#issuecomment-6240310972). The 740a08b continuation supplies synthetic iPhone/iPad/Android navigation/restoration evidence; bb7295f adds the separately reviewed calendar-date correction.

[Daychi's 19 October runtime clarification](https://github.com/dveyarangi/xuanxue-workshop/issues/16#issuecomment-6264347958) confirms external TestFlight 1.0.0(18) does not contain the Cabinet-content path. Its installed full-parent proof used synthetic transport; no installed live-content client/backend mapping is claimed yet. That existing factual gap remains distinct from contract acceptance.

Cabinet's provider source `ea4299606ef8a8e2091931645bf4d21c20c5a450`, all 19 CI checks and staging health ea42996 are inspected in [Workshop's review](https://github.com/dveyarangi/xuanxue-workshop/blob/ce4aebcd5d0245288563b0a74df7b1dfef7aff4f/docs/current-system.md#native-content-provider-capacity-review--2026-10-19). On 19 October the Workshop operator accepted the current single-instance restart quota reset and removed the persistence finding as a blocker. Original 15 no longer requires quota-history preservation or replacement testing. Daychi's request, error and recovery behavior is unchanged.

### Current Daychi action and paired conditions

Arrange an owner-authorized installed Daychi build in iOS Simulator containing the native Cabinet-content path. Any Daychi backend may be used; identify its selected runtime/source and the native build/source mapping. Connect this path to real Cabinet staging with an authorized account/native grant. The reviewed provider evidence is reusable where its basis holds; neither restart quota persistence, closure of 15 nor reminder implementation in 17 is a prerequisite.

Return actual protected material and recording delivery through that installed client/backend/Cabinet staging chain. Every other case, including next-read refusal after revocation, other-session isolation, block/unblock and provider outage/recovery, uses executed automated tests and inspectable source. Physical hardware, Android and TestFlight do not block acceptance or closure. No particular Daychi backend environment, live fault/status/revocation fixture, new platform criterion, reader role or new issue is assigned. Release/production activation remain with Daychi's operator. Existing N11/native-account and automated evidence is reusable; acceptance still requires the agreed actual reads and applicable executed checks.

## Shared contract and conformance

Authority: [native-content-session](https://github.com/dveyarangi/xuanxue-workshop/blob/1fd3890b4a3b56b4a262dfa74e9929b4002d75aa/docs/contracts/native-content-session.md), immutable Workshop revision `1fd3890b4a3b56b4a262dfa74e9929b4002d75aa`. This complete reference includes the operator-approved 19 October restart-reset exception/C11R and the 20 October evidence split and joint-proof runtime. Both recipients use this same amended authority. Wire, identity, security, ordinary rolling-window and C01–C16 behavior remain unchanged; the amendments define sufficient evidence and runtime.

The existing installed BOUNDARY_SUMMARY and its baseline links remain accepted; these evidence/runtime amendments introduce no fresh installation/adoption gate. The current authority above governs the restart exception and acceptance scope. No Daychi reset signal, retry, cache or error-handling change is required.

## Impact and required changes

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

Paired provider: [cabinet-native-content-check #15](https://github.com/dveyarangi/xuanxue-workshop/issues/15). Its deployed conformance enables actual joint activation/proof, not consumer implementation.

Consumer implementation, contract fixtures and local/synthetic tests can proceed
under Daychi's operator against this settled accessible contract, concurrently
with Cabinet. Neither provider acceptance nor full N11/browser completion is an
administrative implementation prerequisite. Real integrated activation needs the
paired provider's conforming Cabinet staging revision/capacity proof, authorized
native account/grant and installed Daychi in iOS Simulator using any Daychi
backend, with identified build/source/runtime mapping. No particular Daychi backend
hosting environment is required. Cabinet owns account authority; Daychi owns its
runtime/release/cutover. Revocation/status/outage cases use executed automated tests
and require no separate live fixture.
Workshop reviews returned evidence. Registration access exists as recorded in
the original native assignment; private invitation delivery is not a new hold.

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
failure/recovery. Cabinet isolates validated GET me capacity per native grant.
The [native content contract](https://github.com/dveyarangi/xuanxue-workshop/blob/1fd3890b4a3b56b4a262dfa74e9929b4002d75aa/docs/contracts/native-content-session.md) owns exact
wire, capacity, compatibility and common cases; activation and joint proof remain work.

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
responses, deadlines, issuer isolation and capacity boundaries. No separate live
run or revocation/status/outage/aging/deletion fixture is required.

The accepted single-instance restart-reset exception/C11R remains: no quota-history
persistence, replacement-safe handoff or restart/replacement test gate is added.
All shared behavior remains binding; these amendments establish neither completed
live reads nor deployment/acceptance of an untested runtime. Reuse valid accepted
source/check/N11 evidence without repeating it.

## Acceptance evidence

- Supply immutable code, the actual protected native route/alias coverage,
  executable check mapping and executed C01–C16 consumer cases. Exercise real
  mounted HTTP paths, including recording-bearing data; failure must not leak it.
  Prove deadline/redirect, malformed full-profile success, late-response credential
  safety, no retries/cache/fallback, issuer isolation and recovery after unblock
  or provider outage. Reuse earlier synthetic work where its basis holds.
- Retain compatibility proof for legacy native/owner/import/meeting and canonical
  browser consumers, ordinary native selections/cache/access/reminders, unchanged
  content identity and existing native sign-out isolation. Prove that a Cabinet
  refusal cannot accidentally use a legacy or public alternative.
- Return actual protected material/recording delivery using installed Daychi in
  iOS Simulator, any Daychi backend and real Cabinet staging, with identified
  client/backend/provider source and runtime mapping under owner authority.
  Revocation/isolation/recovery and every other case use executed automated tests;
  no physical-device, Android, TestFlight or separate live fault/status fixture
  blocks acceptance or closure. Valid N11 evidence remains reusable.
- Retain the accepted installed BOUNDARY_SUMMARY and valid revision evidence,
  preserving surrounding collaboration instructions. No reinstall/adoption gate
  is added solely by these evidence/runtime amendments.
  Workshop reconciles evidence before full acknowledgement.

Report in this original contribution and link coordination issue 11. Publication
is not activation, deployment, account authorization or acceptance.
