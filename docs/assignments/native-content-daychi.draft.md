# daychi: serve protected native content through the Cabinet session

## Recipient and outcome

Recipient: Daychi agent under its operator, `project:daychi`.
Original coordination: [one-cabinet-login #11](https://github.com/dveyarangi/xuanxue-workshop/issues/11).
One Cabinet login in the native app gives access to its protected wiki content,
including recording links, while invalidated sessions refuse new reads and
temporary Cabinet failures permit recovery without losing the credential.

## Expected / observed

[The original native adapter report](https://github.com/dveyarangi/xuanxue-workshop/issues/11#issuecomment-6124308245)
describes local unmounted policy/HTTP work, synthetic checks and invalid-session
staging refusal. It explicitly does not establish a successful real-account check,
activation or deployment. The reported native adapter is not present in published
web candidate `dfed3203c3c8b55ed077a07ed456d02704ae7e2a`; its local implementation
can be reused after inspection under the settled contract. Published main remains
`c7af6f6682d86618f258129b457db9c6c35698e6`. The native client in
[PR15 at d1a85fe](https://github.com/sleontenko/daychi/pull/15), head
`d1a85fe28e86b60ca6271a2e75871d6360b9f25a`, still delegates wiki requests to
legacy privateRequest. Historical/PR15 evidence does not identify a newly installed
binary or prove protected content access.

The operator approved completing this connection on 2026-10-16. The equal-access
rule was already agreed; no extra school role, invitation, payment, reader
membership or per-material entitlement is introduced.

## Shared contract and conformance

Authority: [native-content-session](https://github.com/dveyarangi/xuanxue-workshop/blob/a07f08747aa7d97e4d3496e87e1d8319db413698/docs/contracts/native-content-session.md), at immutable Workshop revision `a07f08747aa7d97e4d3496e87e1d8319db413698`. The
whole contract, pinned native profile and common C01–C16 cases govern both this
consumer and the paired Cabinet provider. Read the complete authority: its native
response is full-profile 200 JSON, not the browser check's empty 204.

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
paired provider's conforming deployed revision/capacity proof, matching native
account/grant authority and an identified consumer build/source/runtime. Cabinet
owns account/status/fixture authorization; Daychi owns runtime/release/cutover.
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
The [native content contract](https://github.com/dveyarangi/xuanxue-workshop/blob/a07f08747aa7d97e4d3496e87e1d8319db413698/docs/contracts/native-content-session.md) owns exact
wire, capacity, compatibility and common cases; activation and joint proof remain work.

Accepted browser-wiki target remains separate under the
[web-wiki contract](https://github.com/dveyarangi/xuanxue-workshop/blob/a07f08747aa7d97e4d3496e87e1d8319db413698/docs/contracts/web-wiki-session.md): shared Cabinet browser cookie,
per-request authoritative check, fixed matching environment, renewal/return/logout,
protected reader delivery and coordinated origin/path/cache transition. The
limited public homepage graph overview remains its canonical exception. Native
bearers do not replace this browser policy. Knowledge's editorial/import ownership
and structured-article compatibility remain unchanged.
```

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
- Return actual joint staging protected-read/revocation/isolation/recovery results
  with provider/client revisions and installed build/runtime mapping under owner
  authority. Existing N11 evidence can count where it establishes the content
  outcome; no second-platform live run, new live aging or deletion fixture is required.
- Install the complete supplied BOUNDARY_SUMMARY with immutable publication links,
  preserving surrounding collaboration instructions; report the resulting revision.
  Workshop reconciles evidence before full acknowledgement.

Report in this original contribution and link coordination issue 11. Publication
is not activation, deployment, account authorization or acceptance.
