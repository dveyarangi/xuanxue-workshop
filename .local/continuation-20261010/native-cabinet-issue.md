Accepted native account-session implementation assignment.

Prepared within [01-0008-native-cabinet-account-session](https://github.com/dveyarangi/xuanxue-workshop/blob/b8ab296e2713580eb4b91155b0c333ea758a74ce/docs/tickets/01-0008-native-cabinet-account-session.md).
Shared contract revision: `b8ab296e2713580eb4b91155b0c333ea758a74ce`.

Consumer contribution: [daychi-native-account-session #8](https://github.com/dveyarangi/xuanxue-workshop/issues/8).

## Recipient and outcome

Cabinet supplies browser/code-and-PKCE acquisition, native bearer account read,
renewal and grant-scoped revocation for native Daychi. Cabinet owns account data,
executable definitions, implementation and release under its own operator.
Daychi implements the consumer. Workshop reviews the shared outcome and evidence.

## Expected / observed

At Cabinet `868a4edb09926a950b78e8daa3ce495c6e8e256e`, the auth guard is cookie-only,
browser sessions roll after seven days with a 90-day credential lifetime, and
logout clears the browser cookie. No native authorization grant, code exchange
or native grant-revocation behavior was found in the scoped sources.
[Current evidence](https://github.com/dveyarangi/xuanxue-workshop/blob/b8ab296e2713580eb4b91155b0c333ea758a74ce/docs/current-system.md#native-account-session-source--2026-10-08)
links those primary files and the independently owned Daychi client boundary.
Existing account restrictions and browser login methods remain supported.
The [2026-10-10 source comparison](https://github.com/dveyarangi/xuanxue-workshop/blob/b8ab296e2713580eb4b91155b0c333ea758a74ce/docs/current-system.md#assignment-and-native-profile-recheck--2026-10-10)
used Cabinet `fee65f3b8004d4ecac6c2d3da668cf966be0d0f5`: the inspected auth
guard/controller and browser token/renewal files are unchanged from that baseline;
current `MeDto` and its mapper add required normalized `homeHiddenTiles`.

## Shared contract and conformance

The sole accepted shared definition is
[native account-session profile](https://github.com/dveyarangi/xuanxue-workshop/blob/b8ab296e2713580eb4b91155b0c333ea758a74ce/docs/contracts/native-account-session.md), including
operations, field validation, account/token identities, lifecycle, failure recovery,
isolation and common cases N01–N17. Its publication revision must be identical in
both assignments. Do not independently choose redirect URI, durations, DTOs,
errors or refresh behavior. Native credentials do not authorize existing Daychi
content endpoints or Cabinet staff operations.

## Impact and required changes

- Supply the external-browser authorization entry using existing Cabinet login,
  strict registered callback, state/issuer binding and S256 PKCE. Reuse a valid
  active browser session automatically; necessary sign-in also returns automatically,
  without an additional Cabinet account-confirmation, consent or Continue screen.
  Preserve internal-only web login return targets. The contract owns the accepted
  client-impersonation risk; no native app-identity proof is claimed.
- Supply atomic single-use code exchange and distinct revocable native grants.
  Implement the profile's native token, account-read, renewal and revoke operations,
  with the exact declared request/response/error behavior.
- Validate native credential kind, grant and current account on read/renewal.
  Return the complete web `MeDto` as the native account, including optional email
  omission, effective-role/student-mode semantics and normalized `homeHiddenTiles`.
  Cover empty/populated/normalized preference parity under N01;
  exposing role data does not grant staff operations.
  Keep predecessor credentials valid for interrupted-renewal recovery; acknowledged
  revocation invalidates every credential of that grant, including concurrent issuance.
- Preserve browser cookie login/renewal/logout, current account restrictions and
  all other native grants. Native endpoints must not accept cookies as substitutes,
  emit browser session cookies or accidentally inherit a browser-only CSRF requirement.
- Own executable interfaces and meaningful provider checks against the common
  cases. Storage schema, crypto representation, internal browser/API routing and
  libraries remain Cabinet choices consistent with the profile.

## Execution dependencies

Implementation uses the accepted, accessible pinned profile under Cabinet's own
operator. No Workshop readiness confirmation, collaboration-installation acceptance,
Daychi public pilot completion or consumer deployment gates this implementation.

Provider execution evidence needs disposable controlled accounts/time and two
native grants plus a browser session for isolation. Cabinet's operator owns fixture
writes and deployment approval. Actual joint native proof additionally needs a
reachable conforming provider, its exact origin/revision, a controlled active test
account and Daychi's actual native build. Workshop accepts conformance evidence;
it does not release Cabinet. Provider/source availability is reported as facts in
this original issue, without requiring a separate permission ceremony.

## Acceptance evidence

Report here commits/PRs, exact contract revision, executed check counts/outcomes,
redacted failure results, deployment origin/revision and remaining limitations.
Never publish credentials, codes or verifiers. Cover provider aspects of N01–N17,
especially code binding/expiry/replay, strict renewal boundaries, blocked/deleted
accounts, lost-renewal recoverability and cross-grant/browser isolation after revoke.
Use the same case IDs as Daychi so the two reports can be compared.

Supply a reachable authorized test environment/account for the joint read,
restart, logout/isolation and callback/native compatibility checks. Cabinet local
checks can complete before the consumer is deployed; shared integration remains
open until actual native evidence is supplied and Workshop verifies the pair.
No content-admission API, reminder sync, gateway or backend retirement belongs
to this assignment.
