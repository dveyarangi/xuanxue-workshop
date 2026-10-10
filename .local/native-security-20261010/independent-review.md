# Independent recipient review — 2026-10-10

Two fresh readers received only their own prepared issue body, the frozen cited
contract and their own project's sources/instructions. They received no Workshop
conversation, counterpart source or counterpart review. Each reconstructed its
obligations, dependencies, internal freedom and acceptance evidence independently.

Reviewed input SHA-256 values:

- Contract: `2b078281d4a482a77b8ec1457b2839a045915f0287191ae048bb014d19965755`.
- Issue 7 body: `e2243358ca29f6736c4dcbc256a19006732093513485b631742f31f3b7dd0829`.
- Issue 8 body: `0208e5ba5147209b99935ddce0b196b1b3216b8259d02dcd4d73147409e6f8fb`.

After review, only the contract's status sentence changes to record completed
document verification. The final manifest records current bytes; issue-body
semantics and reviewed obligations are unchanged.

## Cabinet reader

Result: semantically ready; no blocking shared-protocol or security choice missing.
The reader reconstructed all five operations, exact issuer/client/scope/callback,
PKCE and code binding, token/grant identity, full web self-profile, expiry/renewal,
revocation races, refusal/recovery, browser isolation, database-backed browser-bound
pending authorization, `/login/native` continuation and provider N01–N17 evidence.

Source: Cabinet `f5036604a414f5e509ca3c9a73d5bcaaa72b3961`, clean tracked tree;
only `CLAUDE.md` changed since `fee65f3b8004d4ecac6c2d3da668cf966be0d0f5`.
Read areas included auth guard/controllers, sessions/renewal, user mapping,
Google OAuth cookie, shared MeDto/home tiles, returnTo, app setup and redaction.

Concrete implementation hazards: the existing `returnTo` rejects `/login*`;
the Google OAuth flow's structured cookie cannot substitute for the accepted
database transaction; cookie-only guards, global errors, CSRF and request logging
need native-specific treatment. The contract determines the required outcomes;
these are implementation obligations, not unresolved shared choices.

## Daychi reader

Result: no semantic blocker. The reader reconstructed all five operations,
raw callback validation, secure attempt/credential persistence, interrupted
exchange and renewal recovery, both 900-second deadlines, strict expiry/renewal,
grant-wide revocation, stale-response handling, immediate durable local logout,
issuer/content isolation, provider continuation and client N01–N17 evidence.

Source: local Daychi `5f9ba442e04cd5dfa70527b9e670b491c491888c`. The supplied
public `0a3c824c1586eb7b3ca16ca0b3a365539076b025` is not a local Git object;
the reader therefore relies on the cited scoped public-source comparison rather
than claiming to have repeated it. Read areas included native entry/linking,
access sessions/invitations, app configuration and schedule/reminder state.

Concrete implementation hazards: existing content `logoutAccess()` waits for
the old backend and deletes its credential, violating Cabinet logout/isolation
if reused; generic invitation routing cannot retain sensitive Cabinet callbacks.
These remedies follow from specified obligations, not missing shared choices.

## Set-wide result and limits

Both reconstructions agree on formats, meanings, timing, lifecycle, failures,
security and joint evidence. Neither imposes tile UI/editing, preference/reminder
sync, content-admission replacement, gateway, retirement or new background polling.
Schema/indexes, atomicity implementation, tab selectors, libraries and client
presentation remain local choices within accepted shared/security guarantees.

The known custom-scheme impersonation and renewable copied-bearer risks remain
explicit accepted tradeoffs. No implementation, deployment or native runtime
proof was established by either review. Publication still requires replacing
`__CONTRACT_REVISION__` with one accessible full commit SHA in both original issues.
