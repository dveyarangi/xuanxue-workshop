# Cabinet sign-in for web wiki — implementation plan

- **record of** what it intends to become

**Authored:** 2026-10-13
**Last amended:** 2026-10-13

Implements [01-0009 web-wiki-cabinet-session](../tickets/01-0009-web-wiki-cabinet-session.md).

## Governing scope

The [accepted web-wiki contract](../contracts/web-wiki-session.md) owns shared
cookie scope, session-check wire, entry/migration/return, Cabinet-site logout,
failure behavior and compatibility. [Architecture](../architecture.md#web-wiki-browser-session)
owns the separation of Cabinet authority and Daychi reader delivery. The
[responsibility agreement](../agent-contract.md#boundary-scope-and-product-language)
keeps internal implementation and releases with each project's operator.

Workshop's implementation contribution is the common immutable authority,
complete recipient assignments and joint acceptance. Cabinet and Daychi implement
their own source changes. This plan neither authorizes sibling writes nor claims
implementation/deployment. The accepted design stays fixed across these stages.

## Inspected baseline

Cabinet source is pinned to `67d5cbd0041daa13c6973b657479e45a6716486f`; Daychi
source to `d2cde6b93ef79734e4de0438ddc2e138698214af`. These are inspected baselines,
not a claim that either deployed service already implements the new contract.

| Boundary | Existing source and planned delta |
|---|---|
| Cookie issuance/verification | Cabinet [session-cookie.ts](https://github.com/gregoryKot/xuanxue-cabinet/blob/67d5cbd0041daa13c6973b657479e45a6716486f/api/src/auth/session-cookie.ts), [session-token.ts](https://github.com/gregoryKot/xuanxue-cabinet/blob/67d5cbd0041daa13c6973b657479e45a6716486f/api/src/auth/session-token.ts) and [AuthGuard](https://github.com/gregoryKot/xuanxue-cabinet/blob/67d5cbd0041daa13c6973b657479e45a6716486f/api/src/auth/auth.guard.ts): shared-domain issuance/expiration, unambiguous parsing, same account authority and existing renewal. |
| Browser API | Cabinet [AuthController](https://github.com/gregoryKot/xuanxue-cabinet/blob/67d5cbd0041daa13c6973b657479e45a6716486f/api/src/auth/auth.controller.ts): existing logout remains a bound POST; the accepted empty current-session check is added without the full self-profile mapper. |
| Root entry and serving | Cabinet [root-routes.ts](https://github.com/gregoryKot/xuanxue-cabinet/blob/67d5cbd0041daa13c6973b657479e45a6716486f/api/src/common/root-routes.ts) and [app.setup.ts](https://github.com/gregoryKot/xuanxue-cabinet/blob/67d5cbd0041daa13c6973b657479e45a6716486f/api/src/app.setup.ts): current root exception covers native authorization only; `/wiki` must reach its actual browser controller rather than `/api/wiki` or SPA fallback. |
| Cabinet navigation | [returnTo.ts](https://github.com/gregoryKot/xuanxue-cabinet/blob/67d5cbd0041daa13c6973b657479e45a6716486f/web/src/auth/returnTo.ts), LoginScreen and callback completion currently use per-tab paths and React-router navigation, with native continuation first. Explicit wiki entry needs the accepted compatible selection and full-page dispatch. |
| Daychi composition | [daychee_app.py](https://github.com/sleontenko/daychi/blob/d2cde6b93ef79734e4de0438ddc2e138698214af/practice_api/daychee_app.py) supplies its invitation authorizer to [wiki_app.py](https://github.com/sleontenko/daychi/blob/d2cde6b93ef79734e4de0438ddc2e138698214af/practice_api/wiki_app.py) and other capabilities. The web-reader check is scoped separately; replacing that global authorizer would also change Zoom/native access. |
| Reader exposure | [public_wiki.py](https://github.com/sleontenko/daychi/blob/d2cde6b93ef79734e4de0438ddc2e138698214af/practice_api/public_wiki.py), wiki_app's public semantic/article mounts and [wiki_graph.py](https://github.com/sleontenko/daychi/blob/d2cde6b93ef79734e4de0438ddc2e138698214af/practice_api/wiki_graph.py) expose several routes. Protecting only the graph leaves material, article and concept bypasses. |
| Shared reader | [graph.js](https://github.com/sleontenko/daychi/blob/d2cde6b93ef79734e4de0438ddc2e138698214af/apps/wiki-graph/src/graph.js) distinguishes a native host from browser token storage; [library.js](https://github.com/sleontenko/daychi/blob/d2cde6b93ef79734e4de0438ddc2e138698214af/apps/wiki-graph/src/library.js) shares article/navigation/cache behavior. The browser switches to cookie transport; the native host retains its owned request path. |

The [original article report](https://github.com/dveyarangi/xuanxue-workshop/issues/9#issuecomment-6113936401)
claims deployed anonymous and private projections, recording protection and active
v1 compatibility. Those claims explain affected exposure and required regression
coverage; they do not establish this web-session implementation. Current web
authentication changes do not weaken existing content projection/redaction rules.

## Impact

### Impact

One complete browser path changes Cabinet cookie/navigation behavior and Daychi's
web-reader authority. Workshop publication, both recipient contributions, access
cutover and deployed proof remain one ticket; no extra wiki credential mechanism
or horizontal ticket split is needed.

### Hidden edges

Root-route/SPA dispatch, duplicate cookies, all issuance sites, renewal on otherwise
empty responses, per-tab native continuation, another-tab email completion,
multi-reader throttling, direct anonymous DTOs and old delivery caches cross the
obvious login path. Shared frontend and backend composition can accidentally change
native/private access or content projections if the change is global.

### Leave alone

Account identity, native grants/private reader requests, Zoom, owner/import/editorial
authority, content identities/DTOs/redaction and unrelated schedule/reminder work
retain their documented owners and contracts. Browser bookmarks/navigation state
are not credentials or account replicas; this work does not require deleting them.

### Recommendation

Proceed with the accepted one-outcome scope. Reuse Cabinet verification and Daychi
reader boundaries; remove web invitation-token use rather than add another session
layer. Recipient preparation has no native-ticket dependency. Actual acceptance
depends on compatible deployed versions, controlled accounts and closed bypasses.

## Implementation shapes and flows

### Cabinet

Cookie issuance, rolling renewal, sharing and logout use the same production
domain/name/path definition. Login methods and eligible renewal issue the accepted
shared cookie. Sharing a younger legacy session retains the exact token/expiry;
the entry response clears the Cabinet host-only value separately. Logout clears
both values. Non-school browser installations retain their existing scope.

Migration covers existing Cabinet activity as well as `/wiki`: a login or rolling
response at Cabinet cannot leave a competing host-only session beside its new
shared value. Site-origin responses can expire that legacy value while issuing
the shared cookie. The server-to-server check's accepted renewal is the shared
session cookie; a Cabinet host-only expiration is not a wiki renewal cookie to
relay and is not emitted on the session-check response. Separate cookie-field
composition is tested at every browser issuance
path, including ordinary Cabinet entry and enabled login callbacks.

The current-session API uses the existing signature, expiry, current-account and
blocked rules without role metadata or the self-profile mapper. Its 204 is empty;
renewal remains a response cookie. All status paths are no-store. Duplicate session
values are refused rather than selected by order. Integration tests observe actual
guard/controller/response behavior, not just the cookie formatter.

Guard, throttler and exception responses can precede the controller. The
assembled-application proof includes no-store on 401/403/429 and provider errors,
not only a controller's successful 204. Original token ages of exactly seven
days and just over seven days distinguish sharing from eligible renewal; original
expiry bounds the remaining cookie lifetime. Both migration/expiration headers
remain separate Set-Cookie fields through the actual server/static-serving stack.

The root browser entry validates the destination and applies the accepted
303/400/403/503 behavior. Its missing-session path returns the existing login screen
instead of a generic API 401. Existing verification/account logic is reused across
the guard and entry without a second authority or signing key. Internal module
placement remains Cabinet-owned.

The explicit wiki login journey retains a validated internal entry in existing
per-tab nonsecret navigation state. Successful login or another-tab session refresh
resumes it through an actual Cabinet request; client-only navigation cannot apply
the entry's Set-Cookie/303. Ordinary/native journeys retain their existing behavior,
and an unrelated native attempt cannot take over the explicit wiki journey.
Storage failure retains the accepted Cabinet-home fallback.

Completion/refocus can produce more than one local navigation trigger. Browser
proof checks that the retained destination is not consumed into a home redirect
before the real entry executes. Another-tab refresh is scoped to the originating
wiki login journey; this plan adds no global polling protocol. Failure/refusal
retains the accepted error behavior rather than starting an automatic login loop.

The `/logout` page exposes Cabinet's existing action. GET is side-effect-free;
the user action uses the existing mutation header and POST. Failure/lost response
keeps its error/retry behavior. Wiki offers only navigation to this page.

### Daychi

The wiki-origin browser reader reaches the owned web-reader boundary with its
browser cookie. That boundary calls the fixed Cabinet check once per protected
request, forwards only the session cookie and permits content only on empty 204.
The accepted deadline, no redirects/retry, refusal/unavailability status mapping,
no-store and valid renewal-cookie relay apply to actual response delivery.
There is no positive authorization cache, reader registration or credential store.

The five-second bound covers the complete provider attempt, including connection
and any response processing. A failing response body is neither forwarded nor
needed to classify failure. No credential is forwarded to a redirect target;
missing/duplicate browser sessions have no successful provider path. Only an
accepted success may relay the provider's session cookie; refusal/failure response
cookies cannot delete or replace a newer browser session. A malformed renewal
cookie is integration failure, not an invitation to repair it locally.

Web-reader routes and delivery aliases use this authority; existing native/private
routes retain their invitation/bearer authority. Frontend native-host detection is
not server authorization. A web reader cannot choose a legacy invitation path as
an alternate authentication mode. The recipient's route/origin inventory identifies
which delivery boundary owns each exposed path and proves those separations.

The browser request branch uses cookie delivery without reading the HttpOnly value
or attaching a wiki bearer. Its sign-in action retains current pathname/query/hash
for the accepted fixed Cabinet entry. The old web-token storage/use and web-local
logout action are removed; unrelated user-owned/editorial/native records remain.
401 exposes the Cabinet sign-in path; 403 remains refusal rather than a login loop;
503 remains temporary unavailability without cookie removal. Subsequent refusal
removes protected reader content under the accepted logout behavior.

The current reader has in-memory article/view state and asynchronous detail
requests. Proof includes refusal followed by Back/restore/retry and a delayed
earlier content response: refused protected reader state cannot reappear through
those paths. This is local UI consistency with the accepted subsequent-read
refusal; it adds no server cancellation, global logout broadcast or stronger
cookie-response ordering guarantee. Existing temporary-error/last-good presentation
remains Daychi-owned and cannot produce a new authorized server response.

Existing public projection helpers remain content-projection code, even when their
reader routes require authentication. Changing an access boundary does not justify
replacing a retained public DTO with a private DTO or weakening its redaction.
This is not a new prohibition on existing recording links in an authenticated
wiki's owned content projection, nor an additional wiki entitlement check.
Existing Zoom/owner/private-native authority remains separate.
Daychi owns the concrete content API and UI representation within those retained
guarantees. Graph, recent, material, semantic/article and concept reads, page data,
static content and aliases all belong in the exposure inventory; empty application
shells and public support/privacy assets contain no protected reader data.

## Stages and verification

Stages are delivery descriptions, not authorization for other projects. Recipient
implementation follows one public-interface behavior test, its smallest passing
implementation and refactoring before the next behavior. Existing unrelated
regressions stay green; a failing new behavior is a scoped red step, not an accepted
release. Local implementation choices remain with each project.

1. **Shared authority and recipient preparation.** Workshop's semantic comparison
   covers all applicable contract-shape dimensions and the accepted common cases.
   One verified published commit supplies the accessible immutable authority;
   Cabinet/Daychi briefs cite that same revision, concrete ownership, independent
   starting conditions and joint proof dependencies. Publication review includes
   recipient understanding, set-wide coverage and original issue 9 cutover context.
2. **Cabinet session and browser journey.** Public HTTP tests cover check/refusal/
   unavailability and renewal, then actual entry migration/navigation and logout.
   The smallest counterexample is a real assembled application request to `/wiki`
   returning SPA HTML instead of the accepted redirect, even though a controller
   unit test passes. Source tests use controlled account/clock fixtures; browser
   tests verify cookie fields before redirects and per-tab login completion.
3. **Daychi authenticated web reads.** The first test uses a controlled Cabinet
   boundary and the assembled reader route: the same content succeeds with valid
   authority and is absent on refusal/failure. Further cases cover transport faults,
   renewal, duplicate cookies, the browser branch and every inventoried bypass.
   Test outcomes include response status, absence of content, retained cookies and
   call count; an unrelated route error cannot count as successful protection.
   Native/private, Zoom, owner/import and content-projection regressions stay green.
4. **Coordinated release and anonymous-access cutover.** Cabinet's conforming
   capabilities are available before the web consumer switches. Daychi's release
   inventory includes the actually served entrypoint, reader APIs, alternate origins
   and controlled caches. The original article issue records the prospective access
   amendment without reopening completed content work. Partial release is reported
   as partial; a rollback after cutover retains protected refusal/unavailability
   rather than silently restoring anonymous access or a web invitation fallback.
5. **Joint deployed proof and acceptance.** Controlled actual Cabinet/wiki origins,
   matching source/configuration and authorized account fixtures exercise all common
   cases. Cookie transport witnesses alone and two independent green test suites
   are insufficient. Workshop reconciles recipient evidence and acknowledges the
   original assignments; the ticket closes only when its full criteria and /verify
   hold. Operations/logs carry versions and outcome evidence, not raw cookies,
   signatures or private account data.

## Acceptance coverage

| Ticket criterion | Stage and evidence |
|---|---|
| Common immutable authority and briefs | Stage 1: revision, readable links, recipient labels/body readback and shared conformance coverage. |
| Existing session/migration/lifetime | Stages 2/5: real HTTP/browser cookie state and controlled age/expiry boundaries. |
| Original-page/per-tab return | Stages 2/5: every enabled sign-in method, existing/native continuation, another-tab email and fallback. |
| Valid/current-account/refusal rules | Stages 2/3/5: active, absent, forged, expired, deleted, blocked/unblocked and duplicate cases. |
| Provider failure | Stages 3/5: 429, 5xx, timeout, TLS/transport, redirect and unexpected status/body with no protected response. |
| Renewal/no persistence/multi-reader checks | Stages 2/3/5: renewed browser cookie, exact per-request validation, source/storage/log review and multiple-account traffic. |
| Cabinet-site logout | Stages 2/3/5: side-effect-free page GET, bound POST, both cookie expirations, absent/expired session and lost response/retry. |
| Anonymous-access cutover | Stages 3/4/5: complete origin/path/cache inventory, direct requests and prospective original-issue reconciliation. |
| Joint proof and retained scopes | Stage 5 plus recipient regressions: versions/configuration, actual two-site flow and unaffected authority/projection cases. |
| /verify and acknowledgement | Stage 5: complete criteria, scoped Workshop checks, original-issue reconciliation and acceptance. |

## Shared-shape completeness

This comparison applies the [shared-contract dimensions](../../.agents/skills/coordinate/CONTRACT-SHAPE.md)
to the accepted authority, not to recipient-local file/module choices.

| Dimension | Governing definition and scope |
|---|---|
| Authority and scope | Cabinet account/session authority, Daychi web delivery and scoped exclusions: contract's shared-session and compatibility sections. |
| Operations and transport | The contract fixes HTTPS session check, root browser entry and Cabinet-site page/POST logout; content API transport remains Daychi-owned. |
| Requests | The contract fixes session-only Cookie, absent/duplicate handling and the sole relative returnTo input/default/validation. No user-ID/body/bearer/secret input is added. |
| Responses | Empty 204 and accepted renewal cookie, refusal/unavailability mapping, entry redirects and confirmed logout are fixed there; no cross-project profile or error-body schema is introduced. |
| Identity and relationships | Existing Cabinet account and opaque browser session retain identity; no wiki account identifier, mapping or reader replica exists. Content identities retain their provider-owned definitions. |
| Time and intervals | Existing 90-day issuance and strict age-greater-than-seven-days renewal are source-bound Cabinet policy; migration retains original expiry and the check has a total five-second deadline. Calendar/DST windows do not apply to these operations. |
| Data guarantees | Every valid reader receives the same wiki content, only after current validation. The session check has no content selection, ordering or pagination; existing content DTO/query guarantees stay with Daychi. |
| State and consistency | Per-read current authority, no positive authorization cache/store, per-tab nonsecret return state and existing cookie-response ordering are fixed in the contract. Stronger revocation/response ordering is excluded. |
| Access and exposure | Shared trusted school-domain cookie and all exposed web delivery/cache paths, no extra eligibility, credential logging or account replication; native/private/editorial scopes remain separate. |
| Failures and recovery | Accepted 401/403 versus temporary 503, no retry/redirect following during a reader request, retained credentials, Cabinet logout retry and bounded navigation fallback. |
| Effects and delivery | Entry response cookies precede its 303; logout mutation stays bound to the user-triggered POST; renewed cookie relay is scoped to accepted success. No new grant or delivery queue exists. |
| Evolution and compatibility | Shared-cookie contract supersedes the historical wiki profile; native/session/content authority remains compatible. One published immutable revision governs both recipient briefs and prospective anonymous-access cutover. |
| Acceptance | Contract common cases, the coverage/proof tables here and actual controlled two-site evidence jointly cover the ticket. These are planned checks, not already executed implementation proof. |

Recipient briefs project the same authority: Cabinet supplies current validation,
common cookie and navigation; Daychi consumes only that check and protects web
delivery; Workshop covers immutable publication, the prospective original-issue
access amendment and joint acceptance. No obligation is assigned to neither party,
and no party's brief may redefine a shared field, response or compatibility rule.

## Adversarial proof cases

These cases derive from the accepted contract; they do not define a second wire
profile. Provider and consumer evidence distinguishes the intended failure reason
from an unrelated missing route, unavailable fixture or content error.

| Counterexample | Required observation |
|---|---|
| Valid and invalid session on the same assembled reader route | The same fixture content succeeds only with current authority; refusal has the accepted status and no protected response content. |
| Missing, forged, expired, deleted, blocked, then unblocked account | Actual Cabinet verification/account rules determine the outcome; no cached prior success or role requirement authorizes another read. |
| Two same-name session values, either order | No first/last-value authority selection; no content or credential replacement. |
| 204 without renewal; eligible renewal; malformed renewal attributes | Empty success authorizes, valid session renewal reaches the browser, malformed renewal is integration failure; no local substitute is issued. |
| 200 profile/HTML, redirect, 429, 5xx, transport/TLS error and slow provider | The accepted temporary failure, no protected response, no redirect credential leak, no automatic retry and retained browser cookie; the total deadline is measured. |
| Late refusal after new sign-in | Daychi sends no credential expiration/replacement header, preserving the newer cookie. |
| Age exactly seven days, just over seven days, and expired legacy session | Sharing preserves original token/expiry before renewal eligibility; eligible renewal uses existing policy; expiry cannot be extended by migration alone. |
| Ordinary Cabinet login/renewal with an old host-only session | No competing session remains after site-origin issuance; the server-to-server check still relays only its accepted shared renewal cookie. |
| Eligible renewal through the actual session-check guard/controller | The response contains only the accepted shared session renewal; a global helper cannot append Cabinet-host legacy-expiration session headers. |
| Root `/wiki` under real global prefix and static serving | The browser entry executes; SPA HTML and `/api/wiki` are not mistaken for conformance. |
| Valid original destination; missing destination; boundary-sized UTF-8 value | Default and original path/query/fragment follow the accepted contract, with the byte bound rather than a character count. |
| Duplicate/unknown query fields, malformed escapes, external/scheme-relative path, backslash/control | Accepted 400 without an outward redirect; parsing does not make a forbidden destination valid through another decode. |
| Stale native attempt, ordinary Cabinet deep link, two wiki tabs, another-tab email and storage failure | Explicit wiki journeys retain their own entry; unrelated native/ordinary journeys and the bounded home fallback remain compatible. |
| Repeated login completion/refocus while the same return is pending | The intended real Cabinet entry executes; a second local trigger does not consume it into an unrelated home/native destination. |
| Logout page GET, missing/expired-session POST, lost response and retry | GET does not mutate; the bound action clears shared/legacy cookies on confirmed success, while failure is not reported as confirmed logout. |
| Refusal with cached article/Back state and an earlier response arriving late | Protected reader content stays removed; neither view restore nor a stale callback reinstates refused state. |
| Public material/graph/recent/semantic/article/concept endpoint and direct origin/cache alias | Each protected delivery path refuses anonymous access; success and denial are tested against the same active content fixture. |
| Cookie-only request to native/private or owner/import/Zoom routes; legacy bearer on web delivery | Retained authority scopes are not widened; legacy/native credentials cannot replace Cabinet authority at the web-reader boundary. |
| Multiple valid reader sessions through one backend | Usable accepted browser-session limiting is demonstrated rather than a native IP-only lifecycle budget silently grouping all readers. |

## Limitations and next work

This RFC does not publish recipient assignments, implement application code or
establish runtime conformance. The bounded source baselines above need comparison
with each recipient's implementation revision. Actual deployment topology/cache
inventory and controlled account fixtures are release/proof inputs owned by the
recipients, not evidence supplied by a guessed path or a simulated browser route.
Their absence prevents claiming cutover/proof complete, not preparing compatible
implementations. The common session retains the accepted last-response ordering;
no stronger account-wide revocation or downloaded-content erasure is promised.

## Planning validation

1. **Pass 1 — 2026-10-13.** Ticket, accepted contract, architecture/responsibility,
   original article report and pinned implementation sources were compared. The
   draft distinguishes shared reader code, scoped web authority, root entry
   dispatch, native continuation and public/private content projection. The
   complete outcome fits one RFC. Application code is unchanged.
2. **Pass 2 — 2026-10-13.** The same ticket/RFC/contract and guard, logout,
   continuation and reader-cache paths were re-read adversarially. The plan now
   covers errors before controller execution, exact renewal boundaries, total
   provider deadline, late-refusal cookie retention, stale UI responses, duplicate
   inputs and actual root/static dispatch. Every case has an observable outcome;
   no architecture, session mechanism or application code was changed.
3. **Pass 3 — 2026-10-13.** The revised RFC, ticket, governing scope and issuance/
   composition sources were compared again for completeness and partial release.
   Ordinary Cabinet login/renewal must migrate competing host-only cookies too;
   that expiration is distinguished from check-cookie relay. Repeated completion
   and refocus are included in return proof. All shared-contract dimensions and
   ticket criteria have an owner and evidence path. The accepted wire and scope
   remain unchanged; no load-bearing design decision is left open by this plan.
   Runtime topology/cache/account fixtures remain explicit release/proof inputs,
   and actual implementation/assignments/deployment remain delivery work.

## Assignment preparation — 2026-10-13

[Cabinet draft](../assignments/web-wiki-session-cabinet.draft.md) and
[Daychi draft](../assignments/web-wiki-session-daychi.draft.md) project the same
accepted contract. Scoped tracker search found no existing recipient web-session
assignment; native issues 7/8 and content issue 9 retain their separate scopes.
The incoming [original coordination request 11](https://github.com/dveyarangi/xuanxue-workshop/issues/11)
already covers the combined app/wiki need. The web ticket supplies its browser
portion without resolving native content-server validation/caller trust/capacity.

The preparation comparison distinguishes retained public DTO redaction from
authenticated wiki content; it adds no recording entitlement or public/private
schema change. The issue 11 native adapter is reported local/unmounted and is not
treated as inspected/deployed web support. Its claims remain in the original issue.
The supplied standing summaries were compared with Cabinet CLAUDE.md at 67d5cbd
and Daychi AGENTS.md at d2cde6b, preserving existing native/editorial boundaries.

| Boundary | Affected parties | Promise | Evidence/revision | Delta and consequence | Disposition |
|---|---|---|---|---|---|
| Web reader session | Cabinet provider/account owner; Daychi consumer/delivery owner | Accepted shared browser session and per-read current validation, with no extra wiki eligibility | Accepted web contract; pinned Cabinet 67d5cbd and Daychi d2cde6b; original request 11 | Recipient source/runtime conformance is not established | The paired drafts cover the browser portion of request 11; implementation/cutover/proof remain delivery work. |
| Native content-server validation | Cabinet provider; Daychi backend/native consumer | Native account-session scope is distinct from its content-server integration | Original issues 7/8; request 11's local/unmounted adapter report | Caller trust and aggregated native check capacity are separately requested; no web implementation follows from that reported adapter | Retain in original request 11 and native coordination; no bearer/native-check choice is assigned by these web briefs. |
| Content projections and authority | Daychi provider/web-native readers; Knowledge editorial/import consumer | Daychi owns content DTOs; retained public redaction and native/private/owner scopes persist without extra web eligibility | Pinned public/private reader sources; original article report 9; request 11 | A blanket recording prohibition would exceed the accepted authentication shape | The wording distinguishes redaction of retained public DTOs from existing authenticated wiki content; no new entitlement or content schema is selected. |

Fresh independent Cabinet and Daychi recipient readings reconstructed operations,
dependencies, internal freedom and evidence from the briefs and cited sources.
The issue 11/projection clarifications were re-read with no residual semantic
findings. A candidate duplicate-entry ambiguity was resolved against the existing
invalid-session branch: no credential is selected, and the entry retains its
303 login continuation; no new shared decision or wire was introduced.
Set-wide review covers common session/entry/renewal/logout, all reader exposures,
retained authority/projection scopes, provider/consumer failures and joint proof.

Both drafts remain unpublished. The pending publication action is a verified,
accessible immutable contract commit, identical pinning of both brief/summary
references and creation/readback of the two recipient assignments linked to
original request 11. No native issue or original article issue was changed or
closed by preparation. Draft-format, local-reference, copied-summary link and
ticket checks passed; no application implementation or deployed proof is claimed.

## Assignment recheck — 2026-10-13

The user requested another thorough review after preparation. The ticket, both
briefs, sole contract and RFC were compared again for cookie lifecycle/HTTP fields,
return/login behavior, scoped native/web authority, recording projections, direct
anonymous/cache paths, fault/race behavior and partial release. Fresh independent
set review attempted to construct two locally conforming implementations that
would fail together, without private conversation context.

Targeted current-source reads of Cabinet's cookie writer/existing auth controller
and Daychi's wiki composition/browser reader matched their inspected pinned blob
revisions. Original issue 9/11 comments were re-read without new scoped inputs.
This comparison does not claim the entire default branches or deployed versions
are unchanged, nor that the shared target is implemented.

One composition candidate was clarified at the contract's owning session-check
section: that operation emits accepted shared-session renewal, never Cabinet-host
legacy-expiration session fields. Legacy cleanup remains in browser operations.
The Cabinet projection and actual guard/controller proof case now state this
explicitly. Fresh re-review found the candidate closed, with no remaining allowed
incompatible pair or new architecture/credential/lifecycle guarantee. Publication
wording also distinguishes common new web authority from retained immutable
native/source references. The publication prerequisite and deployed-proof limits
remain unchanged.

## Publication verification — 2026-10-13

The reviewed documentation/assignment package passed the required harness source,
installed-rule and mechanism checks; the Workshop application suite passed 25
tests. Question/ticket validators and scoped local-reference/anchor checks passed.
This verifies publication preparation, not the ticket's recipient implementation
or deployed /verify criterion. Other sessions' changed files are excluded from
the publication commit.

The earlier browser witnesses remain locally retained unpublished evidence, not
required executable authority for recipients. A fresh Chrome 155.0.8059.40 check
passed the delivery fixture; routing assertions completed but asynchronous browser
teardown failed, so that rerun is not recorded as a passing routing check. Neither
fixture establishes Cabinet/Daychi authentication or deployed conformance. The
published provenance describes that bounded local evidence without inaccessible
GitHub links to unpublished scripts.
