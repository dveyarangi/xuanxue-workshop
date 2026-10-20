# xuanxue-cabinet: Cabinet session for web-wiki reading

**Published, amended 2026-10-20:** [original assignment](https://github.com/dveyarangi/xuanxue-workshop/issues/12). Recipient label: `project:cabinet`.
The original issue holds current recipient work and reports; this file retains the
reviewed published assignment. Publication is not implementation or deployed proof.

Accepted web-wiki shared-browser-session implementation assignment.

Prepared within [01-0009 web-wiki-cabinet-session](https://github.com/dveyarangi/xuanxue-workshop/blob/ec3f17a7808f81a098e432958f89f1018368a32e/docs/tickets/01-0009-web-wiki-cabinet-session.md).
Shared contract revision: `ec3f17a7808f81a098e432958f89f1018368a32e`.
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

The operator accepted the limited public homepage graph overview on 2026-10-14.
The contract's **Accepted public homepage graph overview** section is the sole
definition of that exception: section names/counts and anonymous structure only;
material/subtopic names, original identifiers, dates, content and source/recording
links stay excluded. Daychi owns this separate public projection. The Cabinet
session wire and all protected reader obligations are unchanged. Acceptance of
the exception does not verify the reported local candidate or authorize release.

The sole shared definition is the
[accepted web-wiki shared-browser-session contract](https://github.com/dveyarangi/xuanxue-workshop/blob/ec3f17a7808f81a098e432958f89f1018368a32e/docs/contracts/web-wiki-session.md).
Its shared-session, environment profiles, compatibility, browser entry/migration, Cabinet-site logout
and current-session-check sections define exact wire, input validation, statuses,
cookie lifecycle, common examples and proof cases. Use the same published revision
as the [Daychi contribution](https://github.com/dveyarangi/xuanxue-workshop/issues/13).
The [implementation plan](https://github.com/dveyarangi/xuanxue-workshop/blob/ec3f17a7808f81a098e432958f89f1018368a32e/docs/rfc/01-0009-web-wiki-cabinet-session.md)
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
  DNS/HTTPS and authorized account readiness for staging; inspectable production
  profile configuration remains required, while its release/readiness is non-blocking.
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
- Retain the existing provider and browser-entry guarantees for Daychi's limited
  public homepage overview followed by authenticated reader entry. The preview
  needs no Cabinet auth check or new provider endpoint. Supply the provider side
  of the existing-session/sign-in return proof; Daychi owns the public projection
  and its privacy/exposure checks.
- Supply the complete standing boundary summary below for the recipient's
  collaboration context, preserving surrounding collaboration rules. Own internal
  modules, libraries, tests and release mechanics within the fixed shared contract.

## Execution dependencies

Implementation can start under Cabinet's operator against the published settled
contract, independently of Daychi deployment and native issues 7/8. Workshop
readiness or installation acknowledgement is not a further prerequisite.

Live provider proof needs an owner-authorized staging account and actual browser
session. Cabinet's operator owns fixture changes and deployment approval. Joint
proof needs compatible deployed Cabinet staging and canonical staging wiki,
matching source/configuration, actual main-scenario execution and the reader
exposure/cache transition owned by
[Daychi original 13](https://github.com/dveyarangi/xuanxue-workshop/issues/13), paired
with this contribution. Closed article issue 9 adds no remaining browser action.
Expiry, deletion, status and failure cases use executed automated tests; no new
live aging/deletion/status fixture or production release is required.
Cabinet exposes and reports its conforming provider before Daychi's web cutover;
Daychi/Workshop own reader exposure/cache closure and shared acceptance. A local
provider success does not finish the combined connection.

## BOUNDARY_SUMMARY

```markdown
Existing boundary: Cabinet backend ↔ Cabinet frontend, with local entry points
`api/`, `web/` and `shared/`. Cabinet owns accounts and current account restrictions.
Daychi retains its content backend; Knowledge supplies Daychi's editorial/import
inputs. Current scope/evidence: [Workshop current system](https://github.com/dveyarangi/xuanxue-workshop/blob/ec3f17a7808f81a098e432958f89f1018368a32e/docs/current-system.md).

Accepted target boundaries, joint integration not established: Cabinet backend ↔
Daychi clients for schedule/account capabilities; Daychi backend ↔ Cabinet backend
for authoritative access checks. [Target contracts](https://github.com/dveyarangi/xuanxue-workshop/blob/ec3f17a7808f81a098e432958f89f1018368a32e/docs/boundaries.md#target-connections)
and [native account-session profile](https://github.com/dveyarangi/xuanxue-workshop/blob/3c98d4a5201710f8f777183dd7b61caefe47e2d5/docs/contracts/native-account-session.md) own
their respective scopes; web-wiki work does not change native bearer/private access.

Accepted web-wiki target: Cabinet and wiki share Cabinet's browser session.
Cabinet owns issuance/current-account validation, browser entry/return and logout;
Daychi owns protected web delivery and per-request validation through Cabinet.
All and only valid Cabinet-authenticated web readers receive the same content,
without additional wiki eligibility or persisted wiki reader credentials/accounts.
[Web-wiki session contract](https://github.com/dveyarangi/xuanxue-workshop/blob/ec3f17a7808f81a098e432958f89f1018368a32e/docs/contracts/web-wiki-session.md) owns this boundary.
Daychi's homepage may expose only the contract's separate limited public graph
overview without a Cabinet session. Existing reader APIs remain protected;
entering the reader reuses a valid session or signs in with original-page return.
Daychi owns preview data/projection and exposure controls. This exception changes
no Cabinet wire, account authority, native/private or editorial/import scope.
The contract's environment profiles fix matching production/staging origins and
independent cookie/authority/lifecycle behavior.
Implementation, coordinated anonymous-access cutover and deployed joint proof
remain separate evidence from accepting the target.
```

## Accepted current-delivery acceptance — 2026-10-20

Decision: the Workshop operator, 2026-10-20. The common immutable authority above
includes the accepted evidence split and acceptance-environment amendment.

Current acceptance and closure use real Cabinet staging and canonical
wiki.staging.xuanxue.su. Production rollout remains recipient-owned release work
and does not block either acceptance or closure; it is not a remaining acceptance
action in these contributions. No completed live run or production deployment is
claimed by this scope amendment.

Live browser proof covers protected material and recording reads with a valid
Cabinet session, sign-in with original-page return, and logout followed by refusal
of the next protected read. Renewal, expiry, account deletion/blocking, malformed
responses, timeouts and remaining boundary cases use inspectable source and
executed automated tests; a separate live run of every such case is not required.

Environment isolation remains required in executed automated tests and inspectable
configuration: both profiles/sign-in orders, separate cookies and account/key
authorities, active-name duplicates versus distinct names, cross-environment
refusal, independent renewal/logout, staging legacy cleanup and return routing.
No live production run or simultaneous deployed production/staging run is required.
Actual staging origin/TLS/routing and matching source/runtime/configuration accompany
the live proof; a production DNS alias does not establish a separate staging reader.

## Acceptance evidence

The same authority distinguishes the limited public homepage overview from
protected delivery. Daychi supplies inspectable source and executed checks for
anonymous/empty projection, excluded content/identities, cookie/query input
variations, protected-reader refusal and all inventoried reader/alias/cache
paths. The accepted live sign-in/return/read/logout scenarios use that reader;
the preview introduces no new Cabinet endpoint or credential dependency.

Provider evidence covers current/missing/forged/expired/deleted/blocked/unblocked/
duplicate sessions, exact empty success/refusal/failure, renewal thresholds/relay,
multi-reader traffic, legacy migration, entry/return validation and enabled
sign-in methods, side-effect-free logout GET, bound mutation, cookie expirations,
absent/expired-session handling and lost-response retry. Use executed assembled
HTTP/browser tests for these boundaries; an isolated formatter/controller unit
test does not prove route/header/navigation composition. These cases do not each
need a live deployed account or browser run.

Supply the authorized staging provider/account environment and observations
needed for the common live scenarios. Reuse valid implementation/check evidence.

Report in this original contribution: immutable implementation commits/PRs,
the shared authority, executed case mapping and outcomes, changed instruction
context, actual staging origin/source/runtime/configuration, exposure/cache or
provider evidence as applicable, authorized account procedure and disclosed limits.
Credentials and private account data stay outside issue/log artifacts.

Workshop compares both contributions against the agreed common scope and
acknowledges acceptance in the original assignments. The reader exposure/cache
transition remains in 13 paired with 12; article issue 9 has no remaining browser
action. Keep this assignment open until outstanding recipient acceptance actions
and the common review are complete. Green CI or issue closure alone is not joint
acceptance; production rollout adds no hold after the agreed proof passes.
