# Daychi: native Cabinet account session

**Published as [daychi-native-account-session #8](https://github.com/dveyarangi/xuanxue-workshop/issues/8), 2026-10-10.** Recipient label: `project:daychi`.
Prepared within [01-0008-native-cabinet-account-session](../tickets/01-0008-native-cabinet-account-session.md).
The full native account-session protocol was accepted by the user on 2026-10-09,
including automatic browser continuation, full web self-profile parity without
phone, lifecycle/recovery and the documented native client-impersonation risk.
Implementation and joint native proof remain pending.
The user accepted the `homeHiddenTiles` self-profile addition on 2026-10-10;
its field definition and N01 cases belong to that same shared profile.
The published assignment pins the accepted document and common cases to Workshop
`b8ab296e2713580eb4b91155b0c333ea758a74ce`, shared with
[cabinet-native-account-session #7](https://github.com/dveyarangi/xuanxue-workshop/issues/7).
The original issue holds the current recipient assignment and its reports.

## Recipient and outcome

Native Daychi signs in through Cabinet, securely restores its Cabinet account
session, reads the current account and signs out locally without ending other
clients' sessions. Cabinet owns accounts, native issuance/validation and the provider.
Daychi owns native implementation, UX and release under its operator; Workshop
reviews the shared outcome/evidence.

## Expected / observed

At Daychi `e1ab559c8d5db3dbd7db95aa7400941381ada12a`, the native app has a SecureStore
credential for its own content backend, `quietpractice` invitation handling and
existing startup/foreground restoration. Its content logout waits for that backend.
These paths do not implement Cabinet account access.
[Scoped current evidence](../current-system.md#native-account-session-source--2026-10-08)
links the inspected code and Cabinet provider gap. Browser/linking/crypto/secure
storage dependencies exist; the recipient chooses its integration libraries.

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
  polling; the shared contract fixes observable behavior, not those internals.

## Execution dependencies

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
