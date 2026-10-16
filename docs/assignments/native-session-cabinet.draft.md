# Cabinet: native account-session provider

**2026-10-10 wire/security amendment published in [cabinet-native-account-session #7](https://github.com/dveyarangi/xuanxue-workshop/issues/7), 2026-10-10.** Recipient label: `project:cabinet`.
Prepared within [01-0008-native-cabinet-account-session](../tickets/01-0008-native-cabinet-account-session.md).
The accepted native profile includes full web self-profile parity with
`homeHiddenTiles`, automatic continuation and the accepted client-impersonation
risk. Its accepted security amendment fixes random/hash-only native credentials,
database-backed browser-bound pending authorization and `/login/native` continuation.
Implementation and joint native proof remain pending. The wire/security amendment pins
`3c98d4a5201710f8f777183dd7b61caefe47e2d5`, shared with
[daychi-native-account-session #8](https://github.com/dveyarangi/xuanxue-workshop/issues/8).
The original issue holds the current recipient assignment and reports. Its body,
recipient label and shared authority were read back against the reviewed text.

The [2026-10-15 N11 live-evidence amendment](../contracts/native-account-session.md#accepted-n11-live-evidence-amendment--2026-10-15)
is accepted; the original issue identifies the current shared full-profile revision.

## Recipient and outcome

Cabinet supplies browser/code-and-PKCE acquisition, native bearer account read,
renewal and grant-scoped revocation for native Daychi. Cabinet owns account data,
executable definitions, implementation and release under its own operator.
Daychi implements the consumer. Workshop reviews the shared outcome and evidence.

## Expected / observed

Scoped provider implementation and log-protection evidence is reviewed in [the original provider review](https://github.com/dveyarangi/xuanxue-workshop/issues/7#issuecomment-6103282345) and [the published correction review](https://github.com/dveyarangi/xuanxue-workshop/issues/7#issuecomment-6182910948). The former encoded-parameter log deviation is resolved. Cabinet's [current arrangement](https://github.com/dveyarangi/xuanxue-workshop/issues/7#issuecomment-6194395822) identifies staging issuer `https://staging.xuanxue.su` at `5ea9a8b`, the responsible operator and owner-controlled account/status procedures. The [accepted request](https://github.com/dveyarangi/xuanxue-workshop/issues/7#issuecomment-6197257048) narrows live N11 evidence only; it does not change provider behavior or accept the whole contribution.

Workshop's reviewed tree comparison from `67d5cbd` to `5ea9a8b` finds only test support changed within `api/src/native-auth/`; shared browser/session/native-login changes remain in joint regression scope. These scoped source and anonymous-availability observations do not establish actual authenticated native integration.

## Shared contract and conformance

The sole accepted shared definition is
[native account-session profile](../contracts/native-account-session.md), including
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
  Store validated pending authorization in the database, with an opaque browser
  binding in a Secure, HttpOnly, SameSite=Lax cookie, an unextended 900-second
  server lifetime and atomic single-use completion. Preserve each transaction's
  validated bindings and refuse another tab's transaction, replay or expiry even
  before cleanup. Cover those provider cases alongside N01/N03/N05/N06/N17.
  Use `/login/native` as the explicit internal continuation for the selected
  server transaction, preserving the public entry and general `returnTo` policy.
  Resume automatically after eligible browser login; email completion in another
  tab preserves the original tab's own attempt or offers a fresh one. Continuation
  parameters cannot replace stored authorization bindings or select another tab's
  attempt. Cover those cases alongside N01/N03/N05/N17.
- Supply atomic single-use code exchange and distinct revocable native grants.
  Issue random 32-byte unpadded-base64url native credentials; persist only SHA-256
  hashes associated with their grant and issuance/expiry times, as fixed in the
  accepted native credential protection. Provider evidence covers generation,
  hash-only storage and retained predecessor associations alongside N01/N08/N09/N11/N12.
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
  cases. Storage schema, other internal browser/API routing and libraries remain
  Cabinet choices within the accepted shared and security decisions. Workshop owns security
  principles and protocol selection even when the visible wire remains unchanged;
  the native-token, pending-login and continuation choices above are settled.

## Execution dependencies

The [published staging registration invitation](https://github.com/dveyarangi/xuanxue-workshop/blob/88fdfb7c01fea9a2672f65c9506286c2038cad49/docs/current-system.md#cabinet-staging-access--confirmed-2026-10-15) is available and may be shared openly. Registration may be performed personally or with the recipient's authorized agent; private invitation delivery is not a prerequisite. Registration is distinct from completed sign-in and separately authorized staff/status/fixture actions.

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

The user accepted the [N01/N17 live-evidence clarification](../contracts/native-account-session.md#accepted-n01n17-live-evidence-clarification--2026-10-16) on 2026-10-16. Actual automatic sign-in/return and reuse in the selected persistent system-authentication context suffice for the N01 existing-session subcase; ordinary-Safari sharing is not required. Only N17's age-dependent live browser-cookie renewal demonstration is deferred to existing browser assignments 12/13 and does not block native acceptance. Automated renewal regressions, browser login/logout, isolation and working legacy content/invitation/schedule/reminder preservation remain required. No runtime lifetime/wire changes or full native acceptance are implied.

The user accepted Cabinet's [N11 request](https://github.com/dveyarangi/xuanxue-workshop/issues/7#issuecomment-6197257048) on 2026-10-15. Under the [accepted N11 live-evidence amendment](../contracts/native-account-session.md#accepted-n11-live-evidence-amendment--2026-10-15), live N11 uses two native grants and a browser session on the same account: revoke the first grant with its current credential and verify that the second grant and browser remain usable. N11 requires no live credential-aging arrangement, renewal or predecessor-token revocation. Provider N08/N09/N11 automated checks and client synthetic renewal/predecessor-recovery checks remain required. Credential lifetimes, renewal and grant-wide revocation behavior, N01/N15/N16/N17 and both-platform configuration/client coverage are retained, under the cited N01/N17 live-evidence clarification.

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
