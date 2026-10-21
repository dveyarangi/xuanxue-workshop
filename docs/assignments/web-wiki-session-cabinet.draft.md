# xuanxue-cabinet: Cabinet session for web-wiki reading

**Published, amended 2026-10-21:** [original assignment](https://github.com/dveyarangi/xuanxue-workshop/issues/12). Recipient label: `project:cabinet`.
The original issue holds current recipient work and reports; this file retains the
reviewed published assignment. Publication is not implementation or deployed proof.

Accepted web-wiki shared-browser-session implementation assignment.

Prepared within [01-0009 web-wiki-cabinet-session](https://github.com/dveyarangi/xuanxue-workshop/blob/3c6ff8a7136483b3d266786fa8267eab4f2d2828/docs/tickets/01-0009-web-wiki-cabinet-session.md).
Shared contract revision: `3c6ff8a7136483b3d266786fa8267eab4f2d2828`.
Original coordination request: [app/wiki connection #11](https://github.com/dveyarangi/xuanxue-workshop/issues/11).

## Recipient and outcome

Recipient: xuanxue-cabinet under its operator. A user with a valid Cabinet browser
session can read `wiki.xuanxue.su` through the common session, return to the original
wiki page after necessary sign-in and end that browser session through Cabinet.
Cabinet owns accounts, signature/current-account verification, session issuance,
renewal and logout. Daychi owns wiki delivery; Workshop coordinates the shared
contract, access transition and joint acceptance. Internal design and release
authorization remain with the recipient operator.

## Essential acceptance — 2026-10-21

Decision: the Workshop operator, 2026-10-21: remove everything unnecessary from
acceptance, following the explicit review of required outcomes and excess gates.
The operator reaffirmed preservation of existing implementation and staging;
the purpose is to remove unnecessary ceremony and clear integration closure.
This section governs current acceptance and closure of originals 12/13.

Live proof on real Cabinet staging and canonical wiki.staging.xuanxue.su covers:
protected material and recording reads with a valid session; Cabinet sign-in
returns to the original wiki page; logout refuses the next protected read.
The already agreed remaining access, renewal, account-status, failure/recovery,
environment-isolation and compatibility behavior uses inspectable source and
executed automated tests. Existing protected/public exposure boundaries remain.
Production rollout and live production proof are non-blocking.

Technical quotas and exact counter/window, restart, replacement or replica
behavior and exact retry-delay boundaries are not acceptance or closure
requirements.
Existing compatible API values, working protections and useful tests may remain;
no removal or reimplementation in recipient code is assigned. Invalid input
must still cause no unauthorized protected-content delivery.
No performance/stress target or expanded device/environment matrix is added.
Already credited evidence is reused; neither a new report format nor repeating
accepted builds, installation, account proof, CI or synthetic QA gates closure.

Sole common authority: [web-wiki-session](https://github.com/dveyarangi/xuanxue-workshop/blob/3c6ff8a7136483b3d266786fa8267eab4f2d2828/docs/contracts/web-wiki-session.md#essential-acceptance--2026-10-21), immutable revision `3c6ff8a7136483b3d266786fa8267eab4f2d2828`.
The following technical sections preserve compatible exchange and credited work;
they do not add acceptance gates beyond this operator-agreed section.

## Credited evidence and remaining closure actions — 2026-10-21

The credited work below is retained under the operator-approved 21 October
acceptance reduction above. The original issue remains the work/report channel.

### Credited — no repeat implementation or test request

- Cabinet's shared cookie and fixed environment profiles, current-session check,
  browser entry/original-page return and logout source/HTTP checks are reviewed:
  [provider review](https://github.com/dveyarangi/xuanxue-workshop/issues/12#issuecomment-6157522375)
  and [entry/return review](https://github.com/dveyarangi/xuanxue-workshop/issues/12#issuecomment-6171246714).
  The installed boundary summary is accepted at 5ea9a8b in the
  [adoption review](https://github.com/dveyarangi/xuanxue-workshop/issues/12#issuecomment-6179411400).
- [The login-return test race](https://github.com/dveyarangi/xuanxue-workshop/issues/12#issuecomment-6261594072)
  is resolved at 88794f6; its existing source/CI proof is credited.
- Cabinet staging deployment is confirmed: fresh 21 October health returns 200,
  commit 20128fb, Mongo up. A new provider deployment is not requested.
- Companion Daychi browser source, restricted public overview and scoped executed
  tests are reviewed in [original 13](https://github.com/dveyarangi/xuanxue-workshop/issues/13#issuecomment-6179412624).
  Prior valid negative/expiry/renewal/failure/profile checks remain reusable.

Credited source/automated evidence retains its inspected-revision scope; the
actual three common staging browser scenarios have not been reported complete.

### Remaining actions and responsible parties

| Owner | Only remaining action | Completion evidence / condition |
|---|---|---|
| Cabinet/DNS operator @kotlarewski, with Daychi @stnleo | Finish the existing staging DNS/ownership handoff in [the original request](https://github.com/dveyarangi/xuanxue-workshop/issues/12#issuecomment-6179411400). Daychi supplies the private Railway ownership value; the zone owner applies the matching canonical staging records. | Canonical wiki.staging.xuanxue.su routes to the selected staging reader; Daychi confirms TLS/routing. The 21 October lookup still fails. Keep the ownership value private. |
| Cabinet and Daychi agents under @kotlarewski / @stnleo | Use the already authorized Cabinet staging account/session with the companion reader for the agreed live cases: valid-session material/recording reads; sign-in with original-page return; logout followed by refusal of the next protected read. | The matching staging source/runtime/configuration and actual observations are reported once in 12/13. Cabinet provides provider/account assistance only for an actual unresolved access need; no new status/aging/deletion fixture is assigned. |
| Workshop under @Yarangi | Reconcile those actual results with the credited source/executed automated cases and companion staging exposure evidence, then record acceptance and close when the remaining contribution is complete. | Reuse existing proof. Only an identified changed basis or concrete coverage gap can require another check. |

Production rollout, a live production run, full live fault/status/renewal matrices,
closed article 9, native content 15/16 and reminder 17 do not add closure holds.

## Shared contract and conformance

The operator accepted the limited public homepage graph overview on 2026-10-14.
The contract's **Accepted public homepage graph overview** section is the sole
definition of that exception: section names/counts and anonymous structure only;
material/subtopic names, original identifiers, dates, content and source/recording
links stay excluded. Daychi owns this separate public projection. The Cabinet
session wire and all protected reader obligations are unchanged. Acceptance of
the exception does not verify the reported local candidate or authorize release.

The sole shared definition is the
[accepted web-wiki shared-browser-session contract](https://github.com/dveyarangi/xuanxue-workshop/blob/3c6ff8a7136483b3d266786fa8267eab4f2d2828/docs/contracts/web-wiki-session.md).
Its shared-session, environment profiles, compatibility, browser entry/migration, Cabinet-site logout
and current-session-check sections define exact wire, input validation, statuses,
cookie lifecycle, common examples and proof cases. Use the same published revision
as the [Daychi contribution](https://github.com/dveyarangi/xuanxue-workshop/issues/13).
The [implementation plan](https://github.com/dveyarangi/xuanxue-workshop/blob/3c6ff8a7136483b3d266786fa8267eab4f2d2828/docs/rfc/01-0009-web-wiki-cabinet-session.md)
maps these obligations and adversarial cases to the whole outcome; it adds no
alternate protocol. Content DTOs remain Daychi-owned.

This profile uses the existing browser cookie, not the historical separate wiki
code/token/secret scheme or the
[native account-session profile](https://github.com/dveyarangi/xuanxue-workshop/blob/3c98d4a5201710f8f777183dd7b61caefe47e2d5/docs/contracts/native-account-session.md).
There is no additional wiki eligibility/role, reader-account replica or client secret.
Native implementation in [original issue 7](https://github.com/dveyarangi/xuanxue-workshop/issues/7)
retains its accepted scope; it is not a predecessor of this web contribution.

## Retained implementation scope

This section states the accepted technical obligations and compatibility context.
The current credited/remaining section above determines outstanding work; it is
not a request to repeat the reviewed implementation, tests or installed context.

### Accepted behavior retained

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

Source/automated provider work above is credited. The remaining common live run
needs canonical staging wiki DNS/TLS, compatible actual reader/provider versions
and the existing authorized Cabinet account/session. DNS/ownership is the named
Cabinet/Daychi handoff above. Daychi owns its running reader/exposure coverage;
Cabinet provides assistance for an actual access gap. No additional Ready,
installation, production, native-content, reminder or closed-article dependency
is introduced. Workshop reviews the shared result in originals 12/13.

## BOUNDARY_SUMMARY

```markdown
Existing boundary: Cabinet backend ↔ Cabinet frontend, with local entry points
`api/`, `web/` and `shared/`. Cabinet owns accounts and current account restrictions.
Daychi retains its content backend; Knowledge supplies Daychi's editorial/import
inputs. Current scope/evidence: [Workshop current system](https://github.com/dveyarangi/xuanxue-workshop/blob/3c6ff8a7136483b3d266786fa8267eab4f2d2828/docs/current-system.md).

Accepted target boundaries, joint integration not established: Cabinet backend ↔
Daychi clients for schedule/account capabilities; Daychi backend ↔ Cabinet backend
for authoritative access checks. [Target contracts](https://github.com/dveyarangi/xuanxue-workshop/blob/3c6ff8a7136483b3d266786fa8267eab4f2d2828/docs/boundaries.md#target-connections)
and [native account-session profile](https://github.com/dveyarangi/xuanxue-workshop/blob/3c98d4a5201710f8f777183dd7b61caefe47e2d5/docs/contracts/native-account-session.md) own
their respective scopes; web-wiki work does not change native bearer/private access.

Accepted web-wiki target: Cabinet and wiki share Cabinet's browser session.
Cabinet owns issuance/current-account validation, browser entry/return and logout;
Daychi owns protected web delivery and per-request validation through Cabinet.
All and only valid Cabinet-authenticated web readers receive the same content,
without additional wiki eligibility or persisted wiki reader credentials/accounts.
[Web-wiki session contract](https://github.com/dveyarangi/xuanxue-workshop/blob/3c6ff8a7136483b3d266786fa8267eab4f2d2828/docs/contracts/web-wiki-session.md) owns this boundary.
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

## Closure review

The current credited/remaining section above is the complete outstanding-action
list under the agreed evidence form and exclusions. Existing source/CI/automated
and installed-context evidence is reused at its valid revision. Report only the
remaining runtime/shared outcomes in this original issue and link its companion.
Workshop checks them against the same immutable authority; it does not require
repeat accepted work or add a criterion from a later QA disclosure. This update
records credited subsets, not completed live proof or full assignment acceptance.
