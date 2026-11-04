# Cabinet sign-in for web wiki

- **record of** what happened
- **Status:** Done (2026-11-05, final operator acceptance with disclosed proof exclusions)
- **Type:** HITL
- **Minted:** 2026-10-13
- **Plan:** [web-wiki-cabinet-session RFC](../../rfc/done/01-0009-web-wiki-cabinet-session.md) — shared-browser session and scoped final acceptance
- **Responsible contributor:** Workshop coordinates; Cabinet and Daychi retain their implementation and release ownership
- **Coordination request:** [Original 11](https://github.com/dveyarangi/xuanxue-workshop/issues/11)
- **Answers:** [q-0002.0008.0001.0001.0001](../../questions/done/q-0002.0008.0001.0001.0001-how-should-web-wiki-reuse-an-existing-cabinet-sign-in.md)
- **Outcome:** Web wiki uses Cabinet sign-in and return for protected reading and refuses material after sign-out, accepted by the operator within the recorded evidence scope.

## Parent

The [final operator scope](../../boundaries.md#final-operator-acceptance--2026-11-05)
and [browser contract](../../contracts/web-wiki-session.md#final-operator-acceptance--2026-11-05)
own the accepted behavior, sufficient evidence and exclusions. The original
13 October browser outcome is accepted on 5 November with the disclosed limits,
without claiming later requirements were independently proved earlier.

## What to build

Cabinet remains the sole browser identity/session authority; Daychi's protected
reader reuses that session, preserves original-page return and refuses reads after
sign-out. Existing profile separation, public-preview restrictions, per-read
validation, renewal/refusal/failure and compatibility promises remain binding.
The accepted implementation is supported by credited provider/consumer source,
executed checks and operator-observed login/logout/return/material/refusal.
Separate live recording, runtime matching and exhaustive exposure/cache evidence
are excluded from closure, not represented as independently verified deployment.

## Acceptance criteria

- [x] Provider/consumer source, executed boundary/HTTP/CI and existing projection/environment proof are accepted under the final contract. (2026-11-05)
- [x] The operator's observed Cabinet sign-in/out, original-page return, material read and refusal after sign-out are credited without requiring a repeated report. (2026-11-05)
- [x] Final authority and exact evidence exclusions are published; originals 12/13 and parent 11 are acknowledged and closed/completed with exact body/state/recipient-label readback. (2026-11-05)
- [x] /verify passed against the final governing scope, credited source/evidence, required record validators and checked publication references; the known unrelated harness-entry mismatch remains disclosed. (2026-11-05)

## Out of scope

No unreported recording playback, production cutover, exhaustive live fault matrix,
new account/device/build work or recipient deployment is claimed. Native-content
and reminder acceptance remain in their owning contracts and originals. Closing
this ticket starts no next delivery cycle.

## Parent scope addressed

1. Cabinet-authenticated protected web reading and source/automated public-boundary coverage.
2. Browser entry and original-page return, with operator evidence.
3. Current-validation/renewal/refusal/failure and compatibility promises, with credited automated proof.
4. Final browser contribution acceptance and closure with explicit deployed-proof exclusions.
