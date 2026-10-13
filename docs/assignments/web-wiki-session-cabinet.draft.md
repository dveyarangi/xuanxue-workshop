# xuanxue-cabinet: Cabinet session for web-wiki reading

**Published, 2026-10-13:** [original assignment](https://github.com/dveyarangi/xuanxue-workshop/issues/12). Recipient label: `project:cabinet`.
The original issue holds current recipient work and reports; this file retains the
reviewed published assignment. Publication is not implementation or deployed proof.

Accepted web-wiki shared-browser-session implementation assignment.

Prepared within [01-0009 web-wiki-cabinet-session](https://github.com/dveyarangi/xuanxue-workshop/blob/25def59e25fc847764cc43de8d963bf62a16512e/docs/tickets/01-0009-web-wiki-cabinet-session.md).
Shared contract revision: `25def59e25fc847764cc43de8d963bf62a16512e`.
Original coordination request: [app/wiki connection #11](https://github.com/dveyarangi/xuanxue-workshop/issues/11).

## Recipient and outcome

Recipient: xuanxue-cabinet under its operator. A user with a valid Cabinet browser
session can read `wiki.xuanxue.su` through the common session, return to the original
wiki page after necessary sign-in and end that browser session through Cabinet.
Cabinet owns accounts, signature/current-account verification, session issuance,
renewal and logout. Daychi owns wiki delivery; Workshop coordinates the shared
contract, access transition and joint acceptance. Internal design and release
authorization remain with the recipient operator.

## Expected / observed

At inspected Cabinet `67d5cbd0041daa13c6973b657479e45a6716486f`,
[session-cookie.ts](https://github.com/gregoryKot/xuanxue-cabinet/blob/67d5cbd0041daa13c6973b657479e45a6716486f/api/src/auth/session-cookie.ts)
issues a host-only `session`; [AuthGuard](https://github.com/gregoryKot/xuanxue-cabinet/blob/67d5cbd0041daa13c6973b657479e45a6716486f/api/src/auth/auth.guard.ts)
already verifies its signature/expiry/current account and renews eligible sessions.
[AuthController](https://github.com/gregoryKot/xuanxue-cabinet/blob/67d5cbd0041daa13c6973b657479e45a6716486f/api/src/auth/auth.controller.ts)
has profile and bound logout operations, while
[returnTo.ts](https://github.com/gregoryKot/xuanxue-cabinet/blob/67d5cbd0041daa13c6973b657479e45a6716486f/web/src/auth/returnTo.ts)
retains internal paths per tab with native continuation first.
These are reusable source facts, not proof of the new shared cookie, session-check
endpoint, wiki entry or logout page. Compare the actual implementation revision
with this baseline; retain any intervening compatible work.

[Original coordination request 11](https://github.com/dveyarangi/xuanxue-workshop/issues/11)
requests one Cabinet login for app/wiki, with no additional role/invitation/content
approval. This contribution covers its accepted browser portion. The separately
proposed native content-server adapter and native caller-trust/capacity questions
are not accepted or implemented by this web assignment.

## Shared contract and conformance

The sole shared definition is the
[accepted web-wiki shared-browser-session contract](https://github.com/dveyarangi/xuanxue-workshop/blob/25def59e25fc847764cc43de8d963bf62a16512e/docs/contracts/web-wiki-session.md).
Its shared-session, environment profiles, compatibility, browser entry/migration, Cabinet-site logout
and current-session-check sections define exact wire, input validation, statuses,
cookie lifecycle, common examples and proof cases. Use the same published revision
as the [Daychi contribution](https://github.com/dveyarangi/xuanxue-workshop/issues/13).
The [implementation plan](https://github.com/dveyarangi/xuanxue-workshop/blob/25def59e25fc847764cc43de8d963bf62a16512e/docs/rfc/01-0009-web-wiki-cabinet-session.md)
maps these obligations and adversarial cases to the whole outcome; it adds no
alternate protocol. Content DTOs remain Daychi-owned.

This profile uses the existing browser cookie, not the historical separate wiki
code/token/secret scheme or the
[native account-session profile](https://github.com/dveyarangi/xuanxue-workshop/blob/3c98d4a5201710f8f777183dd7b61caefe47e2d5/docs/contracts/native-account-session.md).
There is no additional wiki eligibility/role, reader-account replica or client secret.
Native implementation in [original issue 7](https://github.com/dveyarangi/xuanxue-workshop/issues/7)
retains its accepted scope; it is not a predecessor of this web contribution.

## Impact and required changes

- Apply the contract's production/staging profiles. Configure distinct cookie
  names/domains, signing keys and account stores; read only the active name and
  ignore the other profile's cookie. Staging browser cleanup expires only its old
  host-only `session`, never production's parent-domain cookie. Preserve the check's
  renewal-only headers. Staging entry/return/logout use only the staging origins.
  Configure by deployment profile, not `NODE_ENV` alone. Report provider hosting,
  DNS/HTTPS and fixture readiness for both environments.
- Issue and expire the accepted shared production session cookie throughout
  browser login, rolling renewal and logout. Migrate old Cabinet host-only values
  without leaving two competing sessions. Valid-session sharing preserves original
  token/expiry until existing renewal is eligible; it does not require fresh login
  or reset the session clock. Preserve other browser installations/native grants.
- Add the accepted empty current-session check using existing verification and
  current-account restrictions. No self-profile mapping, wiki role or user-data
  response is needed. Preserve the accepted renewal cookie and browser-session
  rate-limit behavior. Refuse duplicate values and cover no-store on guard,
  throttler and exception paths as well as success. The check emits only accepted
  shared-session renewal, not Cabinet-host legacy-expiration session headers;
  legacy cleanup stays in the Cabinet browser flows.
- Provide the accepted root `/wiki` browser entry, destination validation,
  legacy-cookie migration and 303/400/403/503 outcomes. Its cookie fields must
  reach the browser separately before redirect; global `/api` routing or SPA
  fallback cannot replace the actual entry.
- Reuse ordinary Telegram/Google/email sign-in and per-tab nonsecret return
  navigation. Resume the explicit wiki journey through a real Cabinet request,
  preserving original path/query/fragment, another-tab email behavior and the
  bounded storage fallback. An unrelated native attempt cannot take over this
  explicit journey; ordinary Cabinet/native journeys retain their own behavior.
- Expose the accepted Cabinet `/logout` page and existing user-triggered bound
  POST action. GET does not mutate. Confirmed success clears shared and legacy
  cookies; absent/expired-session use, failure/lost-response retry and the normal
  Cabinet login destination retain the agreed behavior. No wiki logout API exists.
- Supply the complete standing boundary summary below for the recipient's
  collaboration context, preserving surrounding collaboration rules. Own internal
  modules, libraries, tests and release mechanics within the fixed shared contract.

## Execution dependencies

Implementation can start under Cabinet's operator against the published settled
contract, independently of Daychi deployment and native issues 7/8. Workshop
readiness or installation acknowledgement is not a further prerequisite.

Provider proof needs authorized disposable account/status/time fixtures and an
actual browser session. Cabinet's operator owns fixture changes and deployment
approval. Joint proof additionally needs compatible deployed Cabinet and Daychi
origins/source/configuration, actual browser execution and the prospective
anonymous-access amendment in
[original article issue 9](https://github.com/dveyarangi/xuanxue-workshop/issues/9).
Cabinet exposes and reports its conforming provider before Daychi's web cutover;
Daychi/Workshop own reader exposure/cache closure and shared acceptance. A local
provider success does not finish the combined connection.

## BOUNDARY_SUMMARY

```markdown
Existing boundary: Cabinet backend ↔ Cabinet frontend, with local entry points
`api/`, `web/` and `shared/`. Cabinet owns accounts and current account restrictions.
Daychi retains its content backend; Knowledge supplies Daychi's editorial/import
inputs. Current scope/evidence: [Workshop current system](https://github.com/dveyarangi/xuanxue-workshop/blob/25def59e25fc847764cc43de8d963bf62a16512e/docs/current-system.md).

Accepted target boundaries, joint integration not established: Cabinet backend ↔
Daychi clients for schedule/account capabilities; Daychi backend ↔ Cabinet backend
for authoritative access checks. [Target contracts](https://github.com/dveyarangi/xuanxue-workshop/blob/25def59e25fc847764cc43de8d963bf62a16512e/docs/boundaries.md#target-connections)
and [native account-session profile](https://github.com/dveyarangi/xuanxue-workshop/blob/3c98d4a5201710f8f777183dd7b61caefe47e2d5/docs/contracts/native-account-session.md) own
their respective scopes; web-wiki work does not change native bearer/private access.

Accepted web-wiki target: Cabinet and wiki share Cabinet's browser session.
Cabinet owns issuance/current-account validation, browser entry/return and logout;
Daychi owns protected web delivery and per-request validation through Cabinet.
All and only valid Cabinet-authenticated web readers receive the same content,
without additional wiki eligibility or persisted wiki reader credentials/accounts.
[Web-wiki session contract](https://github.com/dveyarangi/xuanxue-workshop/blob/25def59e25fc847764cc43de8d963bf62a16512e/docs/contracts/web-wiki-session.md) owns this boundary.
The contract's environment profiles fix matching production/staging origins and
independent cookie/authority/lifecycle behavior.
Implementation, coordinated anonymous-access cutover and deployed joint proof
remain separate evidence from accepting the target.
```

## Acceptance evidence

Include the contract's same-browser environment cases: both sign-in orders,
independent renewal/logout, own-name duplicate refusal, ignored other-profile
cookies, relabeled cross-environment token refusal, legacy staging cleanup and
staging return routing. Identify matching profile configuration, distinct
key/account authorities and origin/TLS evidence without disclosing secrets.

Report in the original published assignment: commit/PR, exact shared authority,
executed checks/counts and expected outcomes, changed instruction context,
deployment origin/revision/configuration, controlled fixture procedure and limits.
Credentials and private account details remain outside issue/log evidence.

Evidence covers the contract's provider cases: current/missing/forged/expired/
deleted/blocked/unblocked/duplicate sessions, empty success versus refusal/failure,
renewal threshold/expiry and multi-reader checks; original/legacy session migration
and all enabled sign-in/return cases; side-effect-free logout page, bound mutation,
both expirations, missing/expired-session logout and lost-response retry.
Assembled HTTP/browser checks establish actual headers, routes and navigation;
a formatter/controller unit test alone is insufficient.

Supply the authorized provider/account environment for joint browser reading,
renewal, return, refusal/failure and logout proof. Workshop compares both recipients'
evidence against the same cases and acknowledges acceptance in their original
assignments. Keep this assignment open until that review; closing an issue or
reporting green CI alone does not establish joint acceptance.
