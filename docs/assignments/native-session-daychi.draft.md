# Daychi: native Cabinet account session

**2026-10-10 wire/security amendment published in [daychi-native-account-session #8](https://github.com/dveyarangi/xuanxue-workshop/issues/8), 2026-10-10.** Recipient label: `project:daychi`.
Prepared within [01-0008-native-cabinet-account-session](../tickets/01-0008-native-cabinet-account-session.md).
The accepted native profile includes full web self-profile parity with
`homeHiddenTiles`, automatic continuation and the accepted client-impersonation
risk. Its accepted security amendment fixes random/hash-only native credentials,
database-backed browser-bound pending authorization and `/login/native` continuation.
Implementation and joint native proof remain pending. The wire/security amendment pins
`3c98d4a5201710f8f777183dd7b61caefe47e2d5`, shared with
[cabinet-native-account-session #7](https://github.com/dveyarangi/xuanxue-workshop/issues/7).
The original issue holds the current recipient assignment and reports. Its body,
recipient label and shared authority were read back against the reviewed text.
Daychi keeps the same public
authorization entry, callback and opaque-token parsing; `/login/native` is Cabinet's
continuation, not a route Daychi constructs or calls.

The [2026-10-15 N11 live-evidence amendment](../contracts/native-account-session.md#accepted-n11-live-evidence-amendment--2026-10-15)
is accepted; the original issue identifies the current shared full-profile revision.

## Recipient and outcome

Native Daychi signs in through Cabinet, securely restores its Cabinet account
session, reads the current account and signs out locally without ending other
clients' sessions. Cabinet owns accounts, native issuance/validation and the provider.
Daychi owns native implementation, UX and release under its operator; Workshop
reviews the shared outcome/evidence.

## Expected / observed

The [scoped source review](https://github.com/dveyarangi/xuanxue-workshop/issues/8#issuecomment-6189041756) covers historical build 18 at immutable [Daychi da5570347d7b23de7cf3e56a472859cba33b3d1b](https://github.com/sleontenko/daychi/tree/da5570347d7b23de7cf3e56a472859cba33b3d1b). Workshop matched all 176 exported file hashes and passed 125 app / 19 shared-wiki tests. This resolves source access for that subset. The mapping is to historical build 18; excluded private inputs, the full original build, fresh Apple/device observations and actual successful Cabinet sign-in are not established. Reuse that scoped source/test evidence without duplicate publication or a new release requirement.

The provider arrangement and accessible registration invitation permit independently available authorized native cases; no live credential-aging arrangement is required under the accepted N11 amendment. Actual version-bound native results and existing retained-behavior proof remain outstanding.

## Shared contract and conformance

The sole accepted shared definition is
[native account-session profile](../contracts/native-account-session.md), including
operations, field validation, account/token identities, lifecycle, failure recovery,
isolation and common cases N01–N17. Its publication revision must be identical in
both assignments. Do not independently choose redirect URI, durations, DTOs,
errors or refresh behavior. The configured Cabinet origin is distinct from
`EXPO_PUBLIC_DAYCHEE_API_URL`; Cabinet credentials never go to that existing backend.

## Impact and required changes

- Implement external-browser S256 PKCE acquisition, secure pending-attempt storage,
  exact callback/state/issuer validation and native code exchange. Handle warm/cold
  starts and superseded/cancelled attempts without resurrecting a session.
  Cover automatic return from an existing Cabinet browser session and after
  necessary sign-in under N01, with no additional Cabinet confirmation step.
  Retain OS/provider interaction and all callback/PKCE protections; the documented
  impersonation risk does not authorize removing those bindings.
  Daychi continues to use `/auth/native/authorize`; it never constructs or calls
  Cabinet's `/login/native` continuation. Treat native credentials as opaque even
  though Cabinet issues random 32-byte values. The server's pending-transaction
  deadline and Daychi's local attempt deadline are independently enforced;
  browser resumption cannot extend the local attempt. Cover same-browser email
  completion in another tab and expired-attempt recovery alongside N01/N04/N05/N17.
- Consume the complete Cabinet web `MeDto` account shape and its optional-email
  omission/effective-role semantics and required `homeHiddenTiles` field/type/keys.
  Cabinet owns its normalized value; consuming it adds no home-tile UI or
  preference editing/synchronization. Profile data does not authorize an operation;
  Cabinet remains authoritative. Cover full profile parity, including empty,
  populated and normalized hidden-home-tile values, under N01.
- Register the additional callback scheme while preserving the existing scheme,
  bundle/package IDs and invitation behavior. Keep code-bearing URLs out of
  logs, analytics, crash reports and persistent navigation.
- Securely persist a separate Cabinet credential by issuer, restore/check the
  account and renew under the shared lifecycle. A failed write or temporary
  failure preserves the usable predecessor; handle lost code-exchange responses
  with a fresh attempt. Reject malformed responses without clearing a valid session.
- Distinguish invalid credentials, blocked account and temporary unavailability.
  Ignore stale responses; clearing a Cabinet session never clears legacy content
  access. Do not infer authorization by decoding token contents.
- Implement immediate local logout, durable secure cleanup and bounded best-effort
  revocation. Offline logout cannot promise remote revocation; storage deletion
  failure cannot be presented as durable logout. Retain ordinary schedule cache,
  local selections, OS reminders, invitations and content access.
- Own executable client definitions, integration libraries, internal state handling
  and product presentation. Add no account/reminder synchronization or background
  polling. Internal choices remain within accepted shared and security decisions;
  Workshop owns security principles and protocol selection even without wire changes.

## Execution dependencies

The [published staging registration invitation](https://github.com/dveyarangi/xuanxue-workshop/blob/88fdfb7c01fea9a2672f65c9506286c2038cad49/docs/current-system.md#cabinet-staging-access--confirmed-2026-10-15) is available and may be shared openly. Registration may be performed personally or with the recipient's authorized agent; private invitation delivery is not a prerequisite. Registration is distinct from completed sign-in and separately authorized staff/status/fixture actions.

Implementation and client interruption/conformance checks can use the accepted,
accessible pinned profile and a conforming fake provider under Daychi's operator.
No Workshop readiness confirmation, collaboration-installation acceptance, public
pilot completion or live-provider deployment gates that implementation.

Actual joint proof needs the conforming Cabinet provider at a reachable configured
origin, its deployed revision, a controlled account and Daychi's actual native
development/release build with the registered callback; Expo Go is insufficient.
[Cabinet's provider assignment](https://github.com/dveyarangi/xuanxue-workshop/issues/7)
supplies provider/fixture evidence.
Cabinet's operator owns its fixtures/release; Daychi's owns its build/device/release.
Workshop accepts integration evidence. Source/fixture/runtime conditions are checked
from current facts, not issue state or an administrative readiness comment.

## Acceptance evidence

The user accepted the [N01/N17 live-evidence clarification](../contracts/native-account-session.md#accepted-n01n17-live-evidence-clarification--2026-10-16) on 2026-10-16. Actual automatic sign-in/return and reuse in the selected persistent system-authentication context suffice for the N01 existing-session subcase; ordinary-Safari sharing is not required. Only N17's age-dependent live browser-cookie renewal demonstration is deferred to existing browser assignments 12/13 and does not block native acceptance. Automated renewal regressions, browser login/logout, isolation and working legacy content/invitation/schedule/reminder preservation remain required. No runtime lifetime/wire changes or full native acceptance are implied.

The user accepted Cabinet's [N11 request](https://github.com/dveyarangi/xuanxue-workshop/issues/7#issuecomment-6197257048) on 2026-10-15. Under the [accepted N11 live-evidence amendment](../contracts/native-account-session.md#accepted-n11-live-evidence-amendment--2026-10-15), live N11 uses two native grants and a browser session on the same account: revoke the first grant with its current credential and verify that the second grant and browser remain usable. N11 requires no live credential-aging arrangement, renewal or predecessor-token revocation. Provider N08/N09/N11 automated checks and client synthetic renewal/predecessor-recovery checks remain required. Credential lifetimes, renewal and grant-wide revocation behavior, N01/N15/N16/N17 and both-platform configuration/client coverage are retained, under the cited N01/N17 live-evidence clarification.

Report here commits/PRs, exact shared revision, executed checks, redacted outcomes,
native build/platform, issuer and deployed provider revision. Cover client aspects
of N01–N17 using the same case IDs as Cabinet. Show sign-in/account read, restart
restoration, renewal/recovery, callback cancellation/mismatch/replay, blocked versus
unavailable states, failed storage operations and stale-response rejection.

Show actual native N01/N11/N15/N16/N17 behavior with the authorized provider;
show both-platform callback configuration/client checks, and record the platform
used for joint proof. Demonstrate that revoking one Cabinet grant leaves another
native grant/browser session usable, and Cabinet logout leaves legacy invitation,
content and ordinary schedule/reminders usable. A fake provider alone does not
establish integration. No content-admission replacement, account-edit sync,
gateway or backend retirement belongs to this assignment.
