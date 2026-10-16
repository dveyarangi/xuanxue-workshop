# xuanxue-cabinet: provide native content-check capacity for Daychi

## Recipient and outcome

Recipient: Cabinet agent under its operator, `project:cabinet`.
Original coordination: [one-cabinet-login #11](https://github.com/dveyarangi/xuanxue-workshop/issues/11).
Daychi can use Cabinet's existing native `GET me` to validate every protected
native content read, with independent capacity for legitimate native grants
behind one Daychi backend. This is a new contribution to the accepted shared
connection, not a reopening of previously accepted implementation evidence.

## Expected / observed

Cabinet main at `5ea9a8ba16ecfdeecede086f6e35837f768f6994` already authenticates
native credentials against current grant/account state in
`api/src/native-auth/native-grants.service.ts` and returns the full native profile
from `native-account.controller.ts`. The controller uses NATIVE_AUTH_THROTTLE,
60/minute, while the global tracker recognizes browser cookies rather than native
grants. Thus server-side checks for different native users share an IP budget.
This is source evidence; account/browser/native integration acceptance is separate.

The operator approved completing this connection on 2026-10-16. The governing
content-access rule was already accepted: a currently valid Cabinet login suffices,
without another reader membership/role/invitation. The change completes transport,
trust and capacity definitions rather than choosing that policy again.

## Shared contract and conformance

Authority: [native-content-session](https://github.com/dveyarangi/xuanxue-workshop/blob/a07f08747aa7d97e4d3496e87e1d8319db413698/docs/contracts/native-content-session.md), at immutable Workshop revision `a07f08747aa7d97e4d3496e87e1d8319db413698`. The
entire contract, its pinned full native profile and C01–C16 cases govern both
Cabinet and the paired Daychi contribution. The issue is a projection of that
authority, not a second wire definition.

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
proof needs a deployed conforming provider at a reported revision, authorized
account/status/grant fixtures and the Daychi consumer runtime. Cabinet owns that
provider/account arrangement; Workshop assesses the returned proof. Do not create
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
[native content contract](https://github.com/dveyarangi/xuanxue-workshop/blob/a07f08747aa7d97e4d3496e87e1d8319db413698/docs/contracts/native-content-session.md) owns exact wire,
failure, capacity, compatibility and common cases; implementation/joint proof remain work.

Accepted browser-wiki target remains separate: shared Cabinet cookie, per-reader
current validation, fixed matching production/staging authority, browser entry,
return, renewal and logout. Daychi owns protected browser delivery and the accepted
limited public homepage graph projection. The
[web-wiki contract](https://github.com/dveyarangi/xuanxue-workshop/blob/a07f08747aa7d97e4d3496e87e1d8319db413698/docs/contracts/web-wiki-session.md) owns this scope; native bearer
checks do not bypass its cookie policy. Existing native/owner/import/Zoom consumers
and independently coordinated cutovers retain their existing authority.
```

## Acceptance evidence

- Report immutable implementation, complete common-case mapping and executed
  applicable provider checks. Prove same-IP different-grant isolation, same-account
  different-grant isolation, predecessor/renewed sharing, exact 60-second boundary,
  invalid-input protection and unchanged lifecycle/browser budgets. Exercise the
  real HTTP route and production tracker/limiter composition, not a tracker-only mock.
- Establish C01–C16 provider obligations and reuse existing source/check evidence
  where unchanged. Preserve profile, expiry/revocation/account-status and error
  semantics; no source/CI result alone establishes successful live content reads.
- Return staging deployment identity and paired owner-authorized content outcomes
  as defined by the common contract. No new live aging/deletion fixture is required.
- Install the complete supplied BOUNDARY_SUMMARY with immutable publication links,
  preserving surrounding collaboration instructions; report the resulting revision.
  Workshop reconciles source/deployment/joint evidence before full acknowledgement.

Report in this original contribution and link coordination issue 11. Publication
does not establish implementation, release, account authorization or acceptance.
