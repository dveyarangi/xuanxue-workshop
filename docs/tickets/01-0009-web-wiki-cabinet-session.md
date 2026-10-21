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
[existing Daychi browser assignment](https://github.com/dveyarangi/xuanxue-workshop/issues/13),
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

The user-approved staging amendment was published and read back in these same
assignments at `25def59e25fc847764cc43de8d963bf62a16512e`. Both now cite the
same amended authority and carry fixed profile mapping, cookie/authority separation,
staging legacy cleanup and common same-browser proof. Daychi's prior summary
adoption report is recorded in the RFC; it claims no implementation or deployment.

The [2026-10-14 review](../rfc/01-0009-web-wiki-cabinet-session.md#assignment-review--2026-10-14)
verifies Cabinet's profile and session-check source subsets and retains the
missing deployment/browser proof. The
[published-consumer review](../rfc/01-0009-web-wiki-cabinet-session.md#published-consumer-review--2026-10-14-evening)
now establishes inspectable Daychi source and scoped protocol/projection test
evidence at `bdc3cf7`, with a local Windows HTML-decoding finding. Staging hosting,
controlled accounts, exposure/cache transition and joint deployed proof remain
in original issues 12/13; the complete outcome remains in progress.

The [2026-10-15 board review](../rfc/01-0009-web-wiki-cabinet-session.md#board-review--2026-10-15)
verifies the Windows correction, Cabinet summary adoption and bounded direct-host
behavior of an independent synthetic staging service. Canonical DNS/ownership
setup is routed to zone administrator `gregoryKot`, identified by the operator;
Daychi retains canonical TLS/runtime proof and its service/release ownership.
Private Railway ownership-value handoff, authorized Cabinet fixtures and the
remaining joint browser/exposure/cache proof retain their original assignments.

The operator-approved [essential acceptance](../contracts/web-wiki-session.md#essential-acceptance--2026-10-21) governs these criteria and evidence reuse; numeric quota/counter proof and extra runtime/report gates are excluded.

## Acceptance criteria

- [ ] The separately accepted public homepage overview satisfies its restricted allowlist; credentials/query variations cannot expose protected reader data, and click/navigation retains existing-session reuse or Cabinet sign-in/return. The exposure/cache inventory distinguishes this projection from protected reader paths. ([Accepted exception](../contracts/web-wiki-session.md#accepted-public-homepage-graph-overview), 2026-10-14)
- [ ] Production and staging retain the accepted fixed environment profiles. Executed automated tests and inspectable configuration cover separate cookies/authorities, both sign-in orders, independent renewal/logout, cross-environment refusal and legacy staging cleanup. Real Cabinet staging and canonical wiki.staging.xuanxue.su suffice for current acceptance and closure; production rollout and a live production run are non-blocking. ([Accepted environments](../contracts/web-wiki-session.md#accepted-acceptance-environments--2026-10-20), operator, 2026-10-20)
- [x] Cabinet and Daychi have published, read-back recipient briefs citing the same accessible immutable accepted contract, complete ownership/context and common conformance cases. ([Cabinet #12](https://github.com/dveyarangi/xuanxue-workshop/issues/12), [Daychi #13](https://github.com/dveyarangi/xuanxue-workshop/issues/13), amended revision `d689c24af9e848cae8db81e4cc5701f9cb7a610c`, 2026-10-14)
- [ ] A valid existing Cabinet browser session reads wiki without fresh sign-in; migration removes competing legacy cookies and preserves the agreed expiry/renewal behavior.
- [ ] Ordinary Cabinet sign-in automatically resumes the original wiki destination; destination validation, per-tab/another-tab behavior and ordinary/native navigation compatibility satisfy the accepted entry contract.
- [ ] Every valid Cabinet-authenticated web reader receives the same content; missing, forged, expired, duplicate or deleted-account sessions are refused, and blocked-account changes take effect on subsequent reads without an extra wiki eligibility check.
- [ ] Provider timeout, rate limiting, transport failure and unexpected responses deliver no protected content, remain distinguishable from authentication refusal and retain the browser credential for subsequent checks.
- [ ] Successful rolling renewal reaches the browser with the accepted shared cookie; validation is current per read, usable for multiple readers behind one backend and persists no reader credentials/account replicas or credential logs.
- [ ] Cabinet-site logout, reached directly or from wiki, ends the common browser session on subsequent protected reads; normal mutation binding, absent/expired-session handling and failure/lost-response retry satisfy the accepted contract.
- [ ] The anonymous-reader transition is coordinated in existing Daychi issue 13; deployed exposed origins, direct/static content paths and controlled old delivery caches cannot bypass the accepted web-reader boundary.
- [ ] Joint staging browser evidence identifies matching recipient source/runtime/configuration and demonstrates valid-session protected material/recording reads, sign-in with original-page return, and logout followed by refusal of the next protected read. Remaining renewal, expiry, account-status, malformed-response, timeout and boundary cases use inspectable source and executed automated tests; exhaustive live fault injection is not required. Native/private-content and editorial/owner/import authority remain preserved. ([Accepted evidence split](../contracts/web-wiki-session.md#accepted-acceptance-evidence-split--2026-10-20), operator, 2026-10-20)
- [ ] /verify passes against this complete outcome, its accepted contract, recipient evidence and the Workshop verification set; Workshop reconciles the result and acknowledges recipient acceptance in the original assignments.

## Out of scope

Native account-session implementation and proof belong to
[01-0008 native-cabinet-account-session](./done/01-0008-native-cabinet-account-session.md).
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
