# Cabinet sign-in for web wiki

- **record of** what it intends to become
- **Status:** In progress (assignments published; recipient implementation and proof pending)
- **Type:** HITL
- **Minted:** 2026-10-13
- **Plan:** [web-wiki-cabinet-session RFC](../rfc/01-0009-web-wiki-cabinet-session.md) — shared-cookie integration, scoped recipient contributions, coordinated cutover and joint proof
- **Responsible contributor:** Workshop coordinates the shared outcome; Cabinet and Daychi own their contributions under their respective operators
- **Coordination request:** [Original app/wiki request 11](https://github.com/dveyarangi/xuanxue-workshop/issues/11) — this ticket supplies its browser portion
- **Answers:** [q-0002.0008.0001.0001.0001](../questions/done/q-0002.0008.0001.0001.0001-how-should-web-wiki-reuse-an-existing-cabinet-sign-in.md)
- **Outcome:** Все и только пользователи с действующей сессией Cabinet читают web-wiki, возвращаются на исходную страницу после входа и используют общие продление и выход; анонимный доступ закрыт, а весь путь проверен на развёрнутых сайтах.

## Parent

The web-reader contribution in the [accepted migration delta](../migration-changes.md#changes-derived-from-accepted-contracts)
and the [web-wiki shared-browser-session contract](../contracts/web-wiki-session.md)
own this scope. The user approved one complete HITL outcome and minting on
2026-10-13. The [delivery breakdown assessment](../questions/done/q-0002.0008.0001.0001.0001-how-should-web-wiki-reuse-an-existing-cabinet-sign-in.md#delivery-breakdown-assessment--2026-10-13)
recommends proceeding without splitting provider and consumer into horizontal tickets.

There is no predecessor ticket dependency. Contract publication and recipient
preparation are part of this outcome; implementation in either project need not
wait for native-session completion or the other project's deployment. Joint proof
requires compatible running implementations and controlled accounts/origins.
HITL covers operator participation in deployed proof and coordinated access cutover.

## What to build

Cabinet remains the sole account/session authority and provides the accepted
shared browser session, legacy-cookie migration, current-session validation,
ordinary sign-in with original-page return and Cabinet-site logout. An existing
valid Cabinet session enters wiki without mandatory fresh sign-in; sharing alone
does not reset its lifetime. These guarantees preserve the accepted common session
and reuse existing sign-in methods rather than create a wiki account lifecycle.

Daychi accepts that session at the wiki-origin reader boundary and obtains current
Cabinet validation for every protected read. It delivers the same reader content
to every valid Cabinet-authenticated account, distinguishes authentication refusal
from temporary provider failure and relays accepted rolling renewal. No independent
reader credential, session, account replica or extra eligibility check is introduced,
because Cabinet owns the reader's account and the common browser session.

Workshop publishes one accessible immutable shared authority and complete recipient
briefs for Cabinet and Daychi. Each project chooses its internal design within the
accepted contract and provides inspectable implementation/runtime evidence. Workshop
coordinates the breaking anonymous-reader transition through the
[original article coordination issue](https://github.com/dveyarangi/xuanxue-workshop/issues/9),
including exposed reader origins, direct content paths and controlled old caches,
because the existing article work preserves active public access. Earlier article
acceptance is not retroactively failed by this new access requirement.

The actual two-site browser path establishes acceptance. The existing isolated
[browser evidence](../questions/done/q-0002.0008.0001.0001.0001-how-should-web-wiki-reuse-an-existing-cabinet-sign-in.md#browser-delivery-evidence)
supports transport feasibility but cannot substitute for recipient implementation
or deployed proof. Shared wire, routing, failure and compatibility details follow
the accepted contract rather than a second definition in this ticket.

The [Cabinet assignment](https://github.com/dveyarangi/xuanxue-workshop/issues/12) and
[Daychi assignment](https://github.com/dveyarangi/xuanxue-workshop/issues/13) were
published and read back on 2026-10-13 against the same immutable contract at
`66b7b5a9c1096e6ac88550ea986a3026db2b2cd0`. Their local
[Cabinet](../assignments/web-wiki-session-cabinet.draft.md) and
[Daychi](../assignments/web-wiki-session-daychi.draft.md) records retain the reviewed
published bodies. The
[preparation disposition](../rfc/01-0009-web-wiki-cabinet-session.md#assignment-preparation--2026-10-13)
retains incoming request 11's browser scope and the common publication/proof
conditions. Original requests 11 and 9 hold publication/access-transition notices.
Recipient implementation, operator-owned cutover and joint deployed proof remain
pending; publication checks only the brief/authority criterion.

## Acceptance criteria

- [x] Cabinet and Daychi have published, read-back recipient briefs citing the same accessible immutable accepted contract, complete ownership/context and common conformance cases. ([Cabinet #12](https://github.com/dveyarangi/xuanxue-workshop/issues/12), [Daychi #13](https://github.com/dveyarangi/xuanxue-workshop/issues/13), revision `66b7b5a9c1096e6ac88550ea986a3026db2b2cd0`, 2026-10-13)
- [ ] A valid existing Cabinet browser session reads wiki without fresh sign-in; migration removes competing legacy cookies and preserves the agreed expiry/renewal behavior.
- [ ] Ordinary Cabinet sign-in automatically resumes the original wiki destination; destination validation, per-tab/another-tab behavior and ordinary/native navigation compatibility satisfy the accepted entry contract.
- [ ] Every valid Cabinet-authenticated web reader receives the same content; missing, forged, expired, duplicate or deleted-account sessions are refused, and blocked-account changes take effect on subsequent reads without an extra wiki eligibility check.
- [ ] Provider timeout, rate limiting, transport failure and unexpected responses deliver no protected content, remain distinguishable from authentication refusal and retain the browser credential for subsequent checks.
- [ ] Successful rolling renewal reaches the browser with the accepted shared cookie; validation is current per read, usable for multiple readers behind one backend and persists no reader credentials/account replicas or credential logs.
- [ ] Cabinet-site logout, reached directly or from wiki, ends the common browser session on subsequent protected reads; normal mutation binding, absent/expired-session handling and failure/lost-response retry satisfy the accepted contract.
- [ ] The anonymous-reader transition is coordinated in original issue 9; deployed exposed origins, direct/static content paths and controlled old delivery caches cannot bypass the accepted web-reader boundary.
- [ ] Joint deployed browser evidence identifies matching recipient source/runtime/configuration and demonstrates the accepted entry, reading, renewal, refusal/failure and logout cases while preserving native/private-content and editorial/owner/import authority.
- [ ] /verify passes against this complete outcome, its accepted contract, recipient evidence and the Workshop verification set; Workshop reconciles the result and acknowledges recipient acceptance in the original assignments.

## Out of scope

Native account-session implementation and proof belong to
[01-0008 native-cabinet-account-session](./01-0008-native-cabinet-account-session.md).
Native private-content and owner/import/Knowledge authority retain the
[compatibility boundary](../contracts/web-wiki-session.md#compatibility-and-transition);
this outcome neither replaces those authorities nor deletes their business records.
Article representation/publication work retains its
[original coordination issue](https://github.com/dveyarangi/xuanxue-workshop/issues/9).
The broader schedule/account/reminder migration remains in the
[migration delta](../migration-changes.md#changes-derived-from-accepted-contracts).

## Parent scope addressed

1. One Cabinet browser account/session permits all and only authenticated web-wiki reading.
2. Entry/migration/automatic original-page return, shared renewal and Cabinet-site logout.
3. Current validation, refusal/unavailability behavior and absence of wiki reader credential/account persistence.
4. Coordinated anonymous-access cutover and jointly verified deployed Cabinet/Daychi interoperability.
