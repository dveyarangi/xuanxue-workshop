# Current application structure and boundary evidence

## Public-schedule pilot closure — 2026-10-19

The [accepted pilot closure](contracts/public-lessons.md#accepted-pilot-closure--2026-10-19) owns the operator acceptance, evidence waiver and reopen-on-problem disposition. No public-pilot recipient action remains.

The [original Daychi run](https://github.com/dveyarangi/xuanxue-workshop/issues/6#issuecomment-6212524880) reports native move/cancel/restore observations and separate endpoint creation/outside-window observations. Existing source/synthetic checks remain reusable. This operator acceptance adds no claim of exhaustive device verification or production rollout. Earlier dated reviews below retain their historical evidence scope.

## Reminder implementation updates — checked 2026-10-19

An explicit fresh update check covered all 17 Workshop issues in every state.
Only original 17 has new recipient reports since the previous scoped reviews;
15/16's latest body changes are Workshop's accepted restart-reset amendment.
No new recipient report was found for 6, 9, 11, 12 or 13; closed issue states
remain unchanged. Issue 17's complete current body, eight comments and 13-event
timeline were read, and both project main heads were independently checked.

[Daychi reports](https://github.com/dveyarangi/xuanxue-workshop/issues/17#issuecomment-6264351647)
local, unmounted protocol groundwork: complete account-bound snapshot validation,
canonical IDs/catalogue fields, arbitrary-precision revisions/equal-revision
metadata and strict 1..64-key encoding. Eight new synthetic protocol tests and
all 133 app tests reportedly pass alongside types/lint/artifact checks. These
artifacts are unpublished; this is reported preparation, not independently
inspected implementation or complete consumer conformance. Authenticated
transport, confirmed saves/readback, fencing, account/guest state and OS/device
work remain with Daychi.

[Cabinet's operator correction](https://github.com/dveyarangi/xuanxue-workshop/issues/17#issuecomment-6265787981)
supersedes the earlier no-current-Cabinet-users assumption: production has real
registered people and exams are in use. The operator explicitly accepts the
existing initial reminder rollout for real accounts, including no reminder
subscriptions inherited from a default all-classes filter. Explicit selected
IDs, lead values and other notice filters are preserved by that same contract;
exam data is outside the work. Cabinet reports implementation is starting and
requests no contract change. The correction introduces no new migration choice,
data deletion or staged-client protocol.

Published heads remain Cabinet `ea4299606ef8a8e2091931645bf4d21c20c5a450` and
Daychi `c146326c7ea552772d8c804b3a08ad5637ca5eb0`. No published reminder
implementation or new installed native build is established by this check.
The [reminder contract](contracts/reminder-sync.md) and original issue retain
their accepted wire/behavior; their usage preface is corrected editorially.

## Native content provider capacity review — 2026-10-19

Workshop reviewed [Cabinet's completion report in original 15](https://github.com/dveyarangi/xuanxue-workshop/issues/15#issuecomment-6263294915)
against the accepted [native-content contract](contracts/native-content-session.md#capacity-and-identity).
Merged [PR602](https://github.com/gregoryKot/xuanxue-cabinet/pull/602) is
`ea4299606ef8a8e2091931645bf4d21c20c5a450`. Inspection covered its complete delta,
real-AppModule e2e fixture, controller/limiter/filter composition, retained
renew/revoke limits and exact installed BOUNDARY_SUMMARY, which matches issue 15.

All 19 checks in [main CI 39223428645](https://github.com/gregoryKot/xuanxue-cabinet/actions/runs/39223428645)
succeeded. Executed e2e logs show `native-me-budget.e2e-spec.ts` and existing
account/revoke/parity suites; the two e2e shards passed 504 and 552 tests.
API unit/coverage logs show the limiter suite in the passing 2791-test shard;
the corresponding Australia/Sydney unit shard also passed. These are inspected
CI executions, not a local rerun of all suites. Provider conformance for same-IP
grant isolation, renewed/predecessor sharing, exact 60-second boundary, retry
rounding and invalid-input isolation is supported within one process lifetime.

Three independent credential-free GETs at 08:57 UTC observed staging health
`200`, commit `ea42996`, Mongo up; staging native me `401 invalid_token`,
`Cache-Control: no-store`, the expected Bearer WWW-Authenticate and no Set-Cookie;
production health remained `fc2dee2`. No account, token, fixture, deployment or
live process was changed. Health does not establish replica configuration or
successful authenticated content delivery.

The following review finding was superseded by the operator's restart-reset
exception on 2026-10-19; the observed source behavior remains unchanged. The
[limiter](https://github.com/gregoryKot/xuanxue-cabinet/blob/ea4299606ef8a8e2091931645bf4d21c20c5a450/api/src/native-auth/native-me-limiter.ts#L81)
owns a new in-memory window per process; [ADR0184](https://github.com/gregoryKot/xuanxue-cabinet/blob/ea4299606ef8a8e2091931645bf4d21c20c5a450/docs/adr/0184-native-me-budget-per-grant.md)
explicitly says deployment resets that history. The accepted deployment-wide
rolling allowance at the time had no reset exception. Workshop executed the exact pinned
limiter/error source after TypeScript transpilation, with synthetic grant/time
inputs: 60 successful checks at T0, 429 on the next check and again at T0+1s;
a fresh limiter at T0+1s admitted 60 further checks for the same grant. That is
120 successful admissions in two seconds across process-state replacement.
This is a deterministic local state-loss reproduction, not a live restart or
an observed customer incident. Single-replica operation alone does not preserve
the history across replacement; overlapping processes would have separate windows.

Current disposition in existing 15: the operator explicitly allowed quota resets
on restart and removed this finding as a blocker. The
[amended capacity contract](contracts/native-content-session.md#capacity-and-identity)
accepts the current single-instance state-loss behavior as a non-blocking limitation.
No persistence correction, replacement-proof requirement or consumer change remains.
The already reviewed source/CI/staging progress stands. Actual joint content proof
and owner-authorized runtime arrangements remain outstanding; source/health success
alone does not establish that outcome. Concurrent multi-instance quotas retain
the shared bound; this amendment adds no scaling requirement to the current setup.

For [Daychi 16](https://github.com/dveyarangi/xuanxue-workshop/issues/16), the reviewed
mounted/default-off adapter and synthetic full-parent navigation evidence stand.
The old claim that the provider implementation is simply absent is superseded.
Authorized functional joint staging checks can be arranged against identified
ea42996 without waiting for issue closure. Restart quota persistence is no longer
a readiness or acceptance gate; the supported current provider can be used for
the existing joint checks under the owners' authority.
Daychi supplies the actual installed client/backend revision mapping; Cabinet
and Daychi operators supply the matching authorized account/grant/status/outage
arrangements. Those arrangements and actual protected material/recording,
revocation/isolation and recovery proof are not established by the reports.
Coordination 11, browser 12/13 and reminder 17 retain their separate scope.

## Native reminder guard provenance - 2026-10-19

Daychi's pinned [reminder-plan.ts:22](https://github.com/sleontenko/daychi/blob/c146326c7ea552772d8c804b3a08ad5637ca5eb0/apps/practice-app/src/features/schedule/reminder-plan.ts#L22)
throws when `plan.length > 60`. Blame/history traces the guard to the available
imported baseline [a8b53df](https://github.com/sleontenko/daychi/commit/a8b53df34b638247c183329881714f621548da42),
dated 2026-09-17; this establishes its presence there, not its original rationale.
The inspected source and repository documentation do not explain exactly 60 or
establish that it is a current platform requirement. No supported-device capacity
test was run by Workshop. The proposed fixed shared 60-reminder limit and its
operator approval question are withdrawn. Daychi owns local queue/platform
handling under the [scope agreement](agent-contract.md#boundary-scope-and-product-language);
the complete shared account selection and accepted delivery behavior remain fixed.

## Online-only reminder decision - 2026-10-19

The user accepted [online-only shared reminder editing](boundaries.md#accepted-online-only-reminder-editing)
on 19 October after reconsidering offline changes and device-clock ordering.
Selections and lead time require Cabinet confirmation; Cabinet orders successful
saves. Cached viewing and already scheduled reminders remain available offline.
Uncertain saves recover by reading current server settings, without automatic
mutation replay. The prior offline-edit preservation, timestamp tie, clock guard
and timestamp-tombstone requirements are superseded; per-choice independence and
chosen-only empty defaults remain accepted. The [accepted synchronization contract](contracts/reminder-sync.md)
owns the resulting wire, behavior and common cases. These are changed requirements, not recipient
implementation or deployment evidence. The earlier source comparison's offline
ordering gaps no longer establish required work; its pinned observations remain
historical evidence.

## Login-return test correction review - 2026-10-19

The [Cabinet diagnosis in original 12](https://github.com/dveyarangi/xuanxue-workshop/issues/12#issuecomment-6261541656)
is supported by the inspected [two-file test-only delta](https://github.com/gregoryKot/xuanxue-cabinet/compare/5838fa5fef3bbd7a0e22aa43b68cf7fd72397a05...88794f67d45b2fd31c2bbbc796e0effa1591699d)
in merged [PR601](https://github.com/gregoryKot/xuanxue-cabinet/pull/601).
Both return suites now wait for the authenticated-state check to finish with
`guest` before emitting focus/visibility events; rendering a login button did
not establish that the return listener was subscribed. Application source is
unchanged. The reported local race reproduction and three repeated local runs
retain Cabinet provenance; Workshop did not rerun them.

At Cabinet main `88794f67d45b2fd31c2bbbc796e0effa1591699d`, all 19 returned checks
are completed/success and [main CI39211993560](https://github.com/gregoryKot/xuanxue-cabinet/actions/runs/39211993560)
is successful. PR CI39211382196 is also successful. The prior failed-CI diagnosis
request is satisfied within this source/check scope. Existing native-account
acceptance stands; no new recipient action in closed original 7 is established.
The [reminder comparison](contracts/reminder-sync.md) retains its historical
5838fa5 baseline: this later test-only delta changes none of its application facts.

The browser outcome in original 12 remains open for canonical host readiness and
actual browser lifecycle proof. A fresh local CNAME lookup for
`wiki.staging.xuanxue.su` returns DNS name does not exist; this is local resolver
evidence, not an authoritative DNS audit. Staging auto-deployment is reported by
Cabinet, not independently verified here; no production release or authenticated
browser/native run was performed. Daychi main remains `c146326`, its draft PR18
remains unmerged at `bb7295f`, and Knowledge remains `b9eb1684`.

## Reminder synchronization source comparison - 2026-10-19

This comparison inspects immutable Cabinet main
[`5838fa5`](https://github.com/gregoryKot/xuanxue-cabinet/tree/5838fa5fef3bbd7a0e22aa43b68cf7fd72397a05)
and Daychi main
[`c146326`](https://github.com/sleontenko/daychi/tree/c146326c7ea552772d8c804b3a08ad5637ca5eb0).
Daychi's separate draft PR18 at `bb7295f` is not merged reminder synchronization.
These are source observations, not new deployment/native acceptance. No sibling
working files were changed and no recipient suites were rerun for this comparison.
The comparison predates the accepted online-only contract; its former clock-ordering
requirements and rollout assumptions below are historical, superseded by the
[accepted synchronization contract](contracts/reminder-sync.md) and
[later usage correction](#reminder-implementation-updates--checked-2026-10-19).

| Concern | Cabinet | Daychi | Shared gap |
|---|---|---|---|
| Identity | Public lessons expose stable occurrence `id` and `classId`. | Ordinary schedule hashes weekday/title, then adds a date; the isolated public pilot already understands Cabinet IDs. | Account reminders need the authoritative Cabinet source and IDs, without heuristic legacy matching. |
| Selection meaning | `all`/`selected` class scope, remembered class list, maximum 50 classes; no individual lesson choice. | Individual choices, recurring series with a start date and per-date skips. | Add one-off Cabinet lesson choices, agree scope compatibility and implement accepted skip removal. |
| Writes | Scope PUT replaces mode and the complete list; lead PUT changes a separate field. | Whole device preference state saved locally; no account choice transport. | Whole-list writes can erase independent changes; both account writers need per-choice merge. |
| Ordering | Preference document has an overall timestamp, without per-choice edit times or removal evidence. | No per-choice timestamps or tombstones. | Neither side yet implements accepted latest-edit/tie/removal rules. |
| Lead time | Personal 15/30/60/120 or school default; school setting accepts integer 5..1440. | Local 0/15/30/60, initial 30; saved values outside that set restore to 30. | Zero and 120/default support must converge; defaults need not be preset values. |
| Delivery | Scheduled-lesson filter, per-account/lesson deduplication; current planner excludes lessons at/past start. | Local OS planning, chosen future reminders; a plan over 60 throws before reconciliation. | Backend zero cannot work unchanged; native capacity needs defined partial coverage instead of whole-plan failure. |
| Lifecycle | Current notification routes use browser authentication; native account credential lifecycle is separately implemented. | Native owner has issuer binding and late-response guards; ordinary reminder preferences use device-wide keys. | Add authenticated native reminder access and issuer/account isolation, distinguishing explicit logout from failures. |
| Other notifications | Class scope also filters lesson cancellation, recording and class-linked material notices. | Device enablement and OS permission control local delivery. | Shared selections must not overwrite channel preferences or accidentally broaden other notification types. |

Source anchors: Cabinet [shared types/routes](https://github.com/gregoryKot/xuanxue-cabinet/blob/5838fa5fef3bbd7a0e22aa43b68cf7fd72397a05/shared/src/lesson-notifications.ts),
[scope persistence](https://github.com/gregoryKot/xuanxue-cabinet/blob/5838fa5fef3bbd7a0e22aa43b68cf7fd72397a05/api/src/notifications/lesson-scope.service.ts),
[controller](https://github.com/gregoryKot/xuanxue-cabinet/blob/5838fa5fef3bbd7a0e22aa43b68cf7fd72397a05/api/src/notifications/lesson-notifications.controller.ts),
[reminder planner](https://github.com/gregoryKot/xuanxue-cabinet/blob/5838fa5fef3bbd7a0e22aa43b68cf7fd72397a05/api/src/lessons/lesson-reminder-plan.ts)
and [public lesson identity](https://github.com/gregoryKot/xuanxue-cabinet/blob/5838fa5fef3bbd7a0e22aa43b68cf7fd72397a05/shared/src/public-lessons.ts);
Daychi [attendance](https://github.com/sleontenko/daychi/blob/c146326c7ea552772d8c804b3a08ad5637ca5eb0/apps/practice-app/src/features/schedule/attendance.ts),
[ordinary schedule/persistence](https://github.com/sleontenko/daychi/blob/c146326c7ea552772d8c804b3a08ad5637ca5eb0/apps/practice-app/src/features/schedule/use-schedule.ts),
[source identities](https://github.com/sleontenko/daychi/blob/c146326c7ea552772d8c804b3a08ad5637ca5eb0/apps/practice-app/src/features/schedule/source.ts),
[planner](https://github.com/sleontenko/daychi/blob/c146326c7ea552772d8c804b3a08ad5637ca5eb0/apps/practice-app/src/features/schedule/reminder-plan.ts)
and [account lifecycle](https://github.com/sleontenko/daychi/blob/c146326c7ea552772d8c804b3a08ad5637ca5eb0/apps/practice-app/src/features/cabinet-account/session-core.ts).

The user approved this preparation and confirmed only test users/data in Daychi
on 2026-10-19. A real-user legacy migration is therefore not established as
necessary; deletion or automatic guest import is not authorized. The comparison informed the subsequently
[accepted synchronization contract](contracts/reminder-sync.md); implementation
and joint proof are held by [existing issue 17](https://github.com/dveyarangi/xuanxue-workshop/issues/17).

The earlier no-current-Cabinet-users assumption was superseded by
[Cabinet's operator correction](#reminder-implementation-updates--checked-2026-10-19).
The accepted contract owns the rollout for those real accounts; the comparison
does not authorize data deletion or establish implementation or deployment.

## Provider closure and regional-network disposition - 2026-10-19

At the user's direction, [Cabinet provider 5](https://github.com/dveyarangi/xuanxue-workshop/issues/5#issuecomment-6260697241)
is closed as completed, preserving its accepted `868a4ed` contribution. The regional
staging-network incident is closed as non-blocking; further investigation or repair
is deferred until an actual customer complaint about the related access problem.
Probe-only failures and existing operator testing reports are not that trigger.
The [Daychi 6 body and follow-up](https://github.com/dveyarangi/xuanxue-workshop/issues/6#issuecomment-6260697771)
explicitly exclude this network incident, provider issue status and temporary-role
disposition from implementation or acceptance gates. Temporary teacher-role state
remains unverified; closure establishes no cleanup or account mutation.

Daychi's outstanding ordinary native evidence still needs a reachable conforming
provider and authorized fixtures under the existing contract. The network
disposition does not accept missing consumer evidence or alter API/session behavior.
The [board review](board-review.md) retains the dated network measurements.

## Public-pilot evidence and test-lesson disposition — 2026-10-18

The user reaffirmed the 15 October Telegram decision: only the live mixed-row/
repair subcase of common case 10 is removed. The [accepted amendment](contracts/public-lessons.md#accepted-live-evidence-amendment--2026-10-18)
retains provider CI, client source/synthetic checks, ordinary actual native
creation/moves/cancellation/restoration, failed-refresh retention/recovery and
ordinary-state preservation. No wire or implementation behavior changes.

The [Cabinet operator confirmation](https://github.com/dveyarangi/xuanxue-workshop/issues/5#issuecomment-6248164725)
establishes authorization for the existing class and performed staff actions.
The user then confirmed the existing test lesson in Codex on 2026-10-18;
its use/disposition is accepted for this follow-up, not a fresh approval hold.
No deletion or teacher-role removal is claimed. The existing class is not a
deletion target. Teacher-role disposition and the separate reported TLS-path
incident are not resolved by this decision. Historical provider acceptance
at 868a4ed stands; no full Daychi or joint-pilot acceptance is added.

## Native client and joint acceptance — 2026-10-17

The native account-session outcome is accepted under full profile `18cfe41`: Cabinet at `5ea9a8b` and Daychi tested source `d1a85fe`, native iOS Simulator Debug 1.0.0 (18), satisfy the provider, client and joint-native criteria within the accepted verification scope. Production release, browser-wiki acceptance and native-content validation remain separate outcomes.

The [completed evidence review](https://github.com/dveyarangi/xuanxue-workshop/issues/8#issuecomment-6233267073)
inspected the immutable [40-file QA package](https://github.com/sleontenko/daychi/blob/bc8f1d5a23f732bdcf6b404f6242f5c5c68437f2/docs/qa-native-account-live-review-2026-10-16/README.md):
all byte sizes/SHA-256 hashes matched and all 26 original PNGs were visually
inspected. This completion pass reuses that scoped review, verifies the retained
40-file package again and freshly confirms PR15 remains at d1a85fe with three
successful exact-source checks. The existing 63/63 targeted client-test log,
historical independent source/wrapper/configuration review and provider automation
retain their original execution provenance. No recipient application suite,
authenticated runtime, build, merge or release was repeated here.

| Accepted obligation | Evidence and retained scope |
|---|---|
| N01 sign-in, profile and restoration | Actual system sign-in/automatic return, persistent-context reuse and restart frames; same-state web/native profile comparison. Populated/normalized profile variants retain automated proof. Ordinary-Safari sharing is not required. |
| N11 grant isolation | Current-grant revoke 200 and subsequent refusal, with the second native grant and browser still usable. Provider/client renewal and predecessor recovery retain automated proof under the accepted live amendment. |
| N15 durable local exit and recovery | Actual request failure, local sign-out, signed-out restart and non-resurrection by a late callback. Exact in-app cancellation and secure-delete failure retain source/synthetic coverage. |
| N16 callback, issuer and invitation compatibility | Warm/cold native callback and ordinary legacy invitation evidence, both-platform configuration/wrapper checks and issuer-bound source/tests. Cold callback used the original request with manual Safari continuation; it is not automatic browser-reuse proof. |
| N17 retained behavior | Separate browser/native logout, schedule sources, selections, two reminders and an actual Simulator local notification. Legacy HTTP records preserve the same protected-response hash and separate grant through Cabinet sign-in/logout/restart, with anonymous refusal and test-access cleanup. |
| Remaining N02–N14 provider/client obligations | Previously inspected immutable implementation/assertions and executed checks cover PKCE/code binding, cancellation/replay, lifetime and renewal boundaries, invalid/blocked/unavailable categories, interrupted persistence and recovery; no new wire or exception is introduced. |

Request-failure instrumentation is not OS airplane mode. Sampled encrypted host
events are not a full decrypted lifetime trace. Private material pixels remain
excluded; inspected nonsecret status/hash/link-presence and cleanup evidence
support the agreed preservation scope. These disclosed limits create no additional
unmet criterion under the accepted joint verification and N11/N01/N17 amendments.
No recipient action remains in native account-session contributions 7/8.

The [provider acceptance](#native-account-session-provider-acceptance--2026-10-17)
and this client/joint acceptance complete
[native-cabinet-account-session](tickets/done/01-0008-native-cabinet-account-session.md).
The original issues hold acknowledgement/closure. Browser 12/13 retains deferred
live browser-cookie renewal and its original browser acceptance; native-content
15/16 and public-schedule 6 retain their separate contracts and remaining work.
No shared boundary, credential lifetime or runtime behavior changed.

## Native account-session provider acceptance — 2026-10-17

Cabinet's native account-session provider contribution is accepted at `5ea9a8ba16ecfdeecede086f6e35837f768f6994` under profile `18cfe41db0203fa6fc72d429caa584960d0c2522`. No outstanding Cabinet action remains in this contribution. Daychi's remaining evidence review and complete joint native acceptance stay open in original issue 8.

Scope: [Cabinet provider contribution 7](https://github.com/dveyarangi/xuanxue-workshop/issues/7)
in [native-cabinet-account-session](tickets/done/01-0008-native-cabinet-account-session.md).
The accepted [native profile](contracts/native-account-session.md) and its N11 and
N01/N17 evidence amendments are unchanged. Acceptance concerns the provider
criterion; it does not accept Daychi's implementation, the complete joint outcome,
production deployment, browser-wiki work or native-content capacity in issue 15.

Evidence retained and reconciled:

- [Provider source and executed-check review](#native-provider-evidence--reviewed-2026-10-11)
  covers the native provider's N01–N17 obligations, including full profile parity,
  code/attempt/PKCE binding, lifetime boundaries, predecessor recovery, grant-wide
  revocation, account refusal and existing browser regressions. Its recorded test
  counts remain the results of that exact historical run, not a new execution.
- [Log-protection correction](#native-log-protection-correction--reviewed-2026-10-11)
  at 67d5cbd resolves the only demonstrated provider deviation. Fresh comparison
  through 5ea9a8b finds no later logging changes and only the already-reviewed test
  support change under api/src/native-auth/. Shared browser/session changes retain
  their own reviewed evidence and regression obligations.
- A fresh read resolves Cabinet main to 5ea9a8b; all 30 returned check records on
  that exact head completed successfully, including the [application verification
  run](https://github.com/gregoryKot/xuanxue-cabinet/actions/runs/38642412159).
  Source and successful checks supplement the inspected assertions; neither alone
  establishes actual native UI behavior. No application suite reran in this pass.
- [Cabinet's environment/account arrangement](https://github.com/dveyarangi/xuanxue-workshop/issues/7#issuecomment-6194395822)
  was fulfilled by the subsequently reported actual Daychi runs against staging
  5ea9a8b. The [scoped native evidence review](https://github.com/dveyarangi/xuanxue-workshop/issues/8#issuecomment-6224902214)
  supports automatic system-context sign-in/reuse and current-credential native/
  browser isolation, without assigning a remaining provider defect or fixture
  action. Live aging was removed or deferred by the accepted evidence amendments.

The outstanding accessible native UI/build-artifact subset belongs to
[Daychi contribution 8](https://github.com/dveyarangi/xuanxue-workshop/issues/8).
It does not require Cabinet implementation or an additional Cabinet arrangement.
The ticket's separate client, joint-native and whole-verification criteria remain
unchecked. Workshop reopens original 7 if that review demonstrates a concrete
remaining Cabinet obligation, preserving this accepted contribution. The original
issue holds the acknowledgement and closure state. No shared boundary changed;
no fresh authenticated runtime, private image inspection, fixture write or release
is claimed.

## Native content-check source baseline — 2026-10-16

Fresh repository reads resolve Cabinet main to `5ea9a8ba16ecfdeecede086f6e35837f768f6994`
and Daychi main to `c7af6f6682d86618f258129b457db9c6c35698e6`. Cabinet's
[native controller](https://github.com/gregoryKot/xuanxue-cabinet/blob/5ea9a8ba16ecfdeecede086f6e35837f768f6994/api/src/native-auth/native-account.controller.ts)
calls current credential/grant/account authentication and the shared full-profile
mapper. Its GET me shares the 60/minute native IP budget; the global tracker
recognizes browser cookies, not validated native grants. Thus the newly accepted
[grant-isolated native content-check capacity](contracts/native-content-session.md)
is an implementation delta, not an observed provider capability.

The [Daychi local adapter report](https://github.com/dveyarangi/xuanxue-workshop/issues/11#issuecomment-6124308245)
retains its recipient-reported synthetic/invalid-session scope. The reported
`practice_api/cabinet_session_http.py` is absent at published web-candidate
`dfed3203c3c8b55ed077a07ed456d02704ae7e2a`; a read of that exact path/revision
returned 404. This does not refute the local preparation or establish mounted
content integration. No successful account/content read, new test run, deployment
or accepted application result was established by this source pass.

Independent recipient reading also inspected
[the native wiki client at PR15 head d1a85fe](https://github.com/sleontenko/daychi/blob/d1a85fe28e86b60ca6271a2e75871d6360b9f25a/apps/practice-app/src/features/wiki/api.ts):
it delegates to legacy privateRequest. PR15 explicitly excludes wiki/native-content
work. The new connection therefore includes app/backend integration rather than
treating the published account-session client as completed protected-content proof.

Source inventory with separately scoped live checks below; not a claim of completed integration.
Cabinet's general boundary inspection used revision
`27f3e7bf50ac0a1e1f981519b7009fc2a19e7042`; reminder behavior was rechecked on
2026-10-04 at `628314472aa2752ebb2bbe9ab75ac3dea9791719`. Daychi was inspected at
`5f9ba442e04cd5dfa70527b9e670b491c491888c`. The dated inspection and access history
is retained in the [reconciliation report](reconciliation-20261004.md).
General Cabinet seam evidence below was also rechecked at `62831447` on 2026-10-04;
newer source, installation and scoped deployment evidence follows.

On 2026-10-06, assignment timelines supplied newer Cabinet evidence:
[PR 561](https://github.com/gregoryKot/xuanxue-cabinet/pull/561) retained the
collaboration installation from Workshop `e209d27` in Cabinet commit `130fb09`;
[PR 562](https://github.com/gregoryKot/xuanxue-cabinet/pull/562) added the public
lessons route and merged as `fc2dee20d64d91122a58e57709c378c5fc91bae7`, the directly
read remote `main`. All 19 checks succeeded on each PR's final head. This does
not refresh every older seam inspection or establish running deployment.
The [assignment review](reconciliation-20261004.md#cabinet-assignment-review--2026-10-06)
records the retained installation, public-route behavior and remaining contract
gaps. Direct Cabinet reports now exist in both original assignments. Cabinet's
collaboration installation is [accepted and issue 1 closed](https://github.com/dveyarangi/xuanxue-workshop/issues/1#issuecomment-6011474155).
The newer provider review below supersedes the public-row conformance gap.
Native integration and broader Workshop source publication remain incomplete.

## Cabinet staging access — confirmed 2026-10-15

The Workshop operator supplied the [Cabinet staging invitation](https://staging.xuanxue.su/join/307eff9265324126fc0fbf0fc1d08bbd)
on 2026-10-15 for @stnleo (Daychi) to register, personally or with their agent.
This is the available registration link, superseding the earlier missing-link/private-
handoff description in [issue 7](https://github.com/dveyarangi/xuanxue-workshop/issues/7#issuecomment-6194395822).
The operator explicitly permits sharing invitations in the group. Availability of
this link does not establish completed registration, a granted teacher role or an
already prepared test class. The latter arrangements remain separately recorded in
[issue 5](https://github.com/dveyarangi/xuanxue-workshop/issues/5#issuecomment-6194557568).
The link was supplied by the operator; no registration was performed by Workshop.
This dated invitation observation does not describe the later fixture state.
[Subsequent lesson and role dispositions](#public-pilot-evidence-and-test-lesson-disposition--2026-10-18)
and [provider closure](#provider-closure-and-regional-network-disposition---2026-10-19)
own the later evidence and acceptance limits.

## Web-wiki assignment evidence — reviewed 2026-10-14

Against [shared authority 25def59e](contracts/web-wiki-session.md),
[Cabinet PR 591](https://github.com/gregoryKot/xuanxue-cabinet/pull/591)
merged as `8c5a4b8b5b7712b1d01a512e3f31e7fe2f52680a`. Inspected
[cookie profiles](https://github.com/gregoryKot/xuanxue-cabinet/blob/8c5a4b8b5b7712b1d01a512e3f31e7fe2f52680a/api/src/auth/session-cookie.ts)
and AuthService implement active-name parsing, duplicate refusal, fixed shared
attributes and separate legacy expiration. Staging logout does not expire the
production shared cookie. The installed Cabinet boundary summary matches the
amended assignment. [Merge CI](https://github.com/gregoryKot/xuanxue-cabinet/actions/runs/38435420201)
executed both profile HTTP suites; 32 independent profile/signature/expiry probes
passed. This establishes the profile subset, not the complete provider assignment.

Before publication, [PR 593](https://github.com/gregoryKot/xuanxue-cabinet/pull/593)
merged as `4e5cc1ddfee2dacec39227a1d44cdc53fbda3025`. Its
[session-check controller](https://github.com/gregoryKot/xuanxue-cabinet/blob/4e5cc1ddfee2dacec39227a1d44cdc53fbda3025/api/src/auth/session-check.controller.ts)
uses AuthGuard for current-account validation and empty 204, places no-store
before guards and renews only the active cookie. Inspected
[PR-head CI](https://github.com/gregoryKot/xuanxue-cabinet/actions/runs/38482963921)
at `8feb44b` executed the session-check and both profile HTTP suites; 34
independent profile/signature/expiry/active-renewal probes passed on the reviewed
source. Merge CI and deployment are separate evidence; source success does not
establish the running operation or the remaining entry/return/logout pages.

The PR and merge source trees are identical (`a9f55d3`).
[Session-check merge CI](https://github.com/gregoryKot/xuanxue-cabinet/actions/runs/38484480181)
also completed successfully before publication.

Read-only HTTPS observations at 2026-10-13 23:36 UTC (2026-10-14 Jerusalem)
found production health at `fc2dee2` and staging at `4e5cc1d`, with Mongo up.
Staging `/api/auth/session` returned 401 with no-store and no cookie fields for
anonymous and invalid-fixture requests; production still returned 404 without
no-store. This supersedes the earlier unavailable staging check, without proving
valid-account or renewal behavior on the running deployment.
`/wiki?returnTo=%2F` and `/logout`
returned each origin's ordinary SPA HTML, with no redirect or cookie fields;
this does not establish the accepted entry or logout page. Production wiki
HTML was reachable; `wiki.staging.xuanxue.su` failed DNS resolution from this
environment. Valid-account issuance, browser migration, distinct deployed
keys/account stores and joint lifecycle proof were not exercised.

[Daychi's reports](https://github.com/dveyarangi/xuanxue-workshop/issues/13#issuecomment-6143866898)
describe local implementation and controlled tests, followed by a
[site/package update](https://github.com/dveyarangi/xuanxue-workshop/issues/13#issuecomment-6144683862).
The latest reported commit `4e9f68e2ce18c3c79c5add477f47258f6a1f765f` was
unavailable through the repository API (422) and absent from the local clone;
its candidate branch was absent remotely. Published Daychi main was `c7af6f6`.
Consumer code/test conformance, release packaging and exposure/cache closure
therefore remain recipient claims. The
[owning web review](rfc/01-0009-web-wiki-cabinet-session.md#assignment-review--2026-10-14)
holds the scoped comparison, remaining owner actions and resumption conditions.

## Web-wiki board follow-up — reviewed 2026-10-14

[Cabinet PR 594](https://github.com/gregoryKot/xuanxue-cabinet/pull/594)
merged as `92921a0`; [PR 595](https://github.com/gregoryKot/xuanxue-cabinet/pull/595)
merged as `e0e823c`. Inspected published source implements fixed-origin server
entry, validated relative destinations, shared-cookie migration with remaining
lifetime, per-tab login return/full-page resumption and a user-triggered logout
page. PR checks are green; executed entry HTTP suites were inspected. At
14:38 UTC, production health remained `fc2dee2` and staging reported `92921a0`.
Staging guest entry returned 303/no-store to Cabinet login with the retained wiki
destination; its session check retained 401/no-store. Production still returned
404 for the check. Staging wiki DNS resolution failed from this environment.
The latest browser deployment, real-account lifecycle and joint reader proof
remain unverified; source progress does not establish whole-assignment acceptance.

[Daychi's new report](https://github.com/dveyarangi/xuanxue-workshop/issues/13#issuecomment-6167681279)
claims operator-requested restoration of an anonymous homepage graph overview,
using a separate restricted site projection. The latest local candidate
`ec5a67c16081dc972da58cad37629ffb00d2e87a` remains unavailable through the
repository API (422); its 201 backend/21 web test and packaging claims are
unverified. The user accepted the limited public overview on 2026-10-14;
the [canonical exception](contracts/web-wiki-session.md#accepted-public-homepage-graph-overview)
defines its allowlist and proof. This accepts the exposure boundary, not the
local candidate or its deployment. Existing protected readers and the Cabinet
wire retain their accepted obligations.

[Cabinet's later staging report](https://github.com/dveyarangi/xuanxue-workshop/issues/12#issuecomment-6171171619)
claims staging `e0e823c` at 14:40–14:50 UTC, guest entry/session refusal,
invalid-return rejection and the browser login/logout pages. It leaves production
at `fc2dee2`, staging wiki DNS absent and real-account lifecycle/joint browser
proof outstanding. This is recipient-reported deployment evidence; Workshop's
earlier anonymous observation above is independently established.

## Published Daychi web-wiki candidate — inspected 2026-10-14

The [publication report](https://github.com/dveyarangi/xuanxue-workshop/issues/13#issuecomment-6173519859)
and [draft PR 13](https://github.com/sleontenko/daychi/pull/13) make the former
local-only source accessible at `bdc3cf76af45729f3e6f5186af10eff2e901398e`, based
on `c7af6f6682d86618f258129b457db9c6c35698e6`. Workshop downloaded that exact
revision and inspected its boundary, projection, actual routes, browser handling,
deployment package, QA and installed summary against authority `d689c24`.

The [reader boundary](https://github.com/sleontenko/daychi/blob/bdc3cf76af45729f3e6f5186af10eff2e901398e/practice_api/web_wiki_session.py)
uses the fixed environment profile, raw active-cookie duplicate refusal,
per-read empty Cabinet validation, total five-second deadline, no retries or
redirects, refusal/failure distinction and scoped renewal relay. All public-reader
aliases are gated regardless of host; canonical wiki private reads are gated
while unrelated native/private/owner APIs retain their own authority elsewhere.
The [separate homepage projection](https://github.com/sleontenko/daychi/blob/bdc3cf76af45729f3e6f5186af10eff2e901398e/practice_api/public_wiki.py)
replaces section/node identities, exposes only section names/counts and structural/
series relationships, empties material/subtopic labels and excludes reader layers.
Cookie/query variations add no content or provider calls; canonical wiki refuses
the site API. Browser source uses credential-free preview fetch and fixed-profile
reader entry, cookie-only reads, request invalidation and protected-state teardown.
Authenticated archive recording delivery and default projection redaction are
covered by the merged candidate's actual-route tests; source publication adds no
deployment or content-import proof.

[PR CI 38600899781](https://github.com/sleontenko/daychi/actions/runs/38600899781)
was inspected: 237 backend, 42 app and 23 wiki tests executed successfully;
the wiki job rebuilt the committed bundle and checked for differences. Workshop
reproduced all 23 wiki tests and the bundle byte-for-byte (SHA-256
`d670ffb2d732e7335f42bf57c04425ecf700dd48c70dc658b123fa02f9c88179`).
All 39 scoped backend boundary tests pass with Python 3.12 UTF-8 mode, and 119
independent observations pass for GET/HEAD/trailing-slash/query refusal on
canonical/direct/site hosts, forwarded-host non-authority, private identifiers,
cookie isolation and streaming/nonempty/cache/redirect provider failures.

The `bdc3cf7` review found a local portability defect: on Windows with default cp1252, six of
those backend tests fail at `web_wiki_session.py:196`, where `Path.read_text()`
reads the UTF-8 wiki HTML without an explicit encoding. Thirty-three pass;
`python -X utf8` makes all 39 pass. This is an inspected local decoding failure,
not evidence that the Linux deployment or session protocol fails. The remaining
recipient action was reported in original issue 13; Workshop changed no recipient
source. No shared-contract defect was found in the inspected source/test scope.

Workshop's read-only HTTPS observations at 18:04 and 18:14 UTC establish:

| Surface | Observed result | Scope and limit |
|---|---|---|
| Cabinet staging | Health `75a6262`, Mongo up; anonymous/invalid session 401/no-store; guest entry 303/no-store; logout page 200 | [Full source comparison from inspected `e0e823c`](https://github.com/gregoryKot/xuanxue-cabinet/compare/e0e823cb5588529739fe766df989cd93c64bd5c0...75a62625b7d62aec46c7e7e1576e96811e7c2d36) changes tooling only; valid-account lifecycle remains unexecuted |
| Cabinet production | Health `fc2dee2`; session-check 404; entry is still the SPA | New provider profile/entry/check operations are not deployed there |
| `wiki.staging.xuanxue.su` | DNS lookup fails | Independent reader hosting/TLS and two-site proof remain unavailable |
| `wiki.xuanxue.su`, direct Railway and `app.xuanxue.su` | Anonymous `/api/public/wiki/categories` 200/no-store with the same body fingerprint; private `/api/wiki/graph` 401; new `/api/site/wiki-graph` 404 | Existing public-reader release remains live; candidate activation/cutover is not established. Sampling identifies these three exposed paths but does not enumerate every alias or controlled old cache |

The source-access gap is resolved. The [recipient cutover inventory](https://github.com/sleontenko/daychi/blob/bdc3cf76af45729f3e6f5186af10eff2e901398e/docs/qa-web-wiki-cabinet-2026-10-13/CUTOVER.md)
still leaves independent staging hosting, authorized provider/account/browser
fixtures, native public-reader transition and complete alias/cache ownership
outstanding. Source conformance in this scope is not merged/deployed reader
acceptance, production rollout or completed joint lifecycle proof.

### Follow-up — verified 2026-10-15

The [Daychi correction report](https://github.com/dveyarangi/xuanxue-workshop/issues/13#issuecomment-6176093616)
publishes `9677210c2d0e19222ba8d6a6eb1061f713233a1b`; draft PR 13 now has
docs-only follow-up head `dfed3203c3c8b55ed077a07ed456d02704ae7e2a`.
The source change makes the wiki-shell read explicitly UTF-8 and adds four
production/staging and `/wiki`/`/wiki/graph` regressions. Workshop reran all 43
boundary tests on native Windows/Python 3.12 with its default encoding, without
`-X utf8`: all pass. The earlier cp1252 finding is resolved at this source.
[Executed correction CI](https://github.com/sleontenko/daychi/actions/runs/38620185804)
also shows 241 backend, 42 app and 23 wiki tests passing. Previously inspected
preview/routes/browser source, HTML and compiled bundle are byte-unchanged, so
their scoped evidence remains applicable; no new UX acceptance is inferred.

The [independent staging deployment report](https://github.com/dveyarangi/xuanxue-workshop/issues/13#issuecomment-6176592679)
and [published configuration/bootstrap evidence](https://github.com/sleontenko/daychi/blob/dfed3203c3c8b55ed077a07ed456d02704ae7e2a/docs/qa-cabinet-staging-2026-10-14/README.md)
identify a separate service, pinned source `9677210`, staging profile and one
ephemeral synthetic material, without a production volume/corpus or copied
Cabinet credentials. The bootstrap/runtime override is separate from source.
These control-plane/source-pin/permission facts are recipient-reported; Workshop
inspected the sanitized artifacts and independently sampled direct HTTPS behavior.

At 2026-10-14 21:55 UTC (2026-10-15 00:55 Asia/Jerusalem), direct
`daychi-wiki-staging.up.railway.app` health and restricted site preview return
200/no-store. The preview contains one section, two nodes and one structural
edge, with an empty material label and no original fixture identity/title.
Sampled public categories/graph and private graph return 401/no-store; invalid
staging/production cookie variants refuse without Set-Cookie. `/wiki` and
`/wiki/graph` redirect 307/no-store to the fixed staging canonical hostname,
preserving query. Canonical `wiki.staging.xuanxue.su` still fails DNS resolution;
direct-host refusal and redirects do not establish canonical cookie delivery,
TLS, valid-account checking, renewal or browser SSO.

The [Cabinet instruction report](https://github.com/dveyarangi/xuanxue-workshop/issues/12#issuecomment-6179162461)
is verified at merged PR 598 / `5ea9a8ba16ecfdeecede086f6e35837f768f6994`:
the current issue 12 BOUNDARY_SUMMARY appears exactly in `CLAUDE.md`; its diff
changes only the supplied contract/context pins and homepage-exception paragraph.
Surrounding rules and native authority pin remain unchanged. Applicable docs-only
CI checks passed; skipped application jobs are not new application-test evidence.
Staging health now reports `5ea9a8b`, with anonymous session 401/no-store;
production remains `fc2dee2` and its check 404.

The Workshop operator named `gregoryKot` as administrator of the `xuanxue.su`
DNS zone on 2026-10-15. The [Daychi owner-handoff request](https://github.com/dveyarangi/xuanxue-workshop/issues/13#issuecomment-6177062061)
therefore routes to that administrator through original Cabinet issue 12.
Daychi retains its service/domain configuration, canonical TLS/runtime proof
and release responsibility. Its generated Railway ownership value is held
privately by its operator; it is not in the public evidence. Exact private
handoff or retrieval by an authorized Railway project member remains necessary
before the zone administrator can finish DNS/ownership validation. Production
DNS is outside this staging-only action. Controlled Cabinet accounts, canonical
browser lifecycle and native-reader/alias/cache transition retain their existing
scope after canonical DNS/TLS is available.

## Knowledge reception evidence — inspected 2026-10-12

At [Knowledge e400680](https://github.com/sleontenko/daychi-knowledge/tree/e4006807c3adaa373ad3a6f63396d0a2eaea66ef),
README and AGENTS identify source preparation, transcription, editorial review and
gated imports as Knowledge's role, with `sleontenko` accountable. Daychi retains
the API, storage, access and readers. Inspected importers target Daychi's existing
owner content, semantic-content and article operations; this is source evidence,
not Workshop acceptance of their deployed behavior.

The retained collaboration skill matches Workshop `e209d27239391be3af2be71b898c79f453851c01`
after the project-label/source-revision substitutions, Installation removal and
blank-line normalization. Its companion matches after the pinned portable-link
adaptation. AGENTS invokes it at startup and boundary work; CLAUDE points to
AGENTS. Both retained `project:daychi` at that inspected revision. GitHub confirms `sleontenko` has
Workshop write permission; the original issue-9 report demonstrates that account's
return path. Knowledge's migration record names a Mac Mini checkout and Claude/Codex
entry points; that source inspection alone did not verify the actual host session.

[Knowledge PR 4](https://github.com/sleontenko/daychi-knowledge/pull/4) is merged;
its inspected CI executed 114 passing tests and the repository guard. The
[issue-9 completion report](https://github.com/dveyarangi/xuanxue-workshop/issues/9#issuecomment-6113936401)
claims the structured-article pilot is deployed. Reception does not accept that
application result. The initial review found no Knowledge-specific installation assignment.
The user subsequently accepted [separate participation and addressing](agent-contract.md#accepted-knowledge-participation--2026-10-12);
the inspected `project:daychi` installation is the baseline for the scoped
recipient update, not evidence that the accepted label is installed.
The scoped [Knowledge assignment, issue 10](https://github.com/dveyarangi/xuanxue-workshop/issues/10)
was published on 2026-10-12; its body and `project:knowledge` label were read back
and matched the approved brief. The reception's accepted result is recorded below.

### Knowledge collaboration acceptance — 2026-10-15

Workshop inspected [Knowledge PR 6](https://github.com/sleontenko/daychi-knowledge/pull/6)
at `cc75bf1b1e48378d28ff3508a49ccd01353b0b34`: the scoped change sets
`project:knowledge` and the supplied boundary summary while preserving source
provenance, retained skill/companion and entry invocation. The PR remains open;
the inspected default branch is not evidence of its merge or actual host adoption.

The user stated that Knowledge had already been checked, then confirmed all three
specified observations with "все так" on 2026-10-15: the working Knowledge checkout
uses `project:knowledge` and the agreed boundary context; a fresh session discovers
issue 10 through that label; reading and sending replies to Workshop work from
that Knowledge environment. Workshop accepts this explicit operator-witnessed
verification as the host evidence for the reception outcome and records it in
original issue 10. No repeat host run or separate bot-authored report is required
for this acceptance. An exact local checkout path/branch was not supplied, and
Workshop does not claim it independently reran that session or that PR 6 merged.

Knowledge's collaboration connection is accepted on that basis. The
[reception question](questions/done/q-0002.0011-how-should-daychi-knowledge-participate-in-workshop.md)
retains its provenance; [structured-article issue 9](https://github.com/dveyarangi/xuanxue-workshop/issues/9)
remains a separate application-result review. No import, deployment, release or
general instruction-source rollout is accepted by collaboration closure.

## Native log-protection correction — reviewed 2026-10-11

Cabinet's [correction report](https://github.com/dveyarangi/xuanxue-workshop/issues/7#issuecomment-6103679689)
and merged [PR 589](https://github.com/gregoryKot/xuanxue-cabinet/pull/589) identify
revision `67d5cbd0041daa13c6973b657479e45a6716486f`. Workshop inspected the complete
four-file change against the previous `97642c7` review and the unchanged native
profile at `3c98d4a5201710f8f777183dd7b61caefe47e2d5`. The serializer now decodes
each query parameter name with `URLSearchParams` before selecting redaction;
it preserves the raw name and replaces its sensitive value. The authorization
parser, duplicate rejection and shared wire are unchanged.

The exact-revision [CI run 38097551022](https://github.com/gregoryKot/xuanxue-cabinet/actions/runs/38097551022)
passed. Downloaded logs show `logging.module.spec.ts`,
`request-serializer.spec.ts` and `native-browser-query.spec.ts` executed and
passed in both coverage and Australia/Sydney jobs. The new HTTP logger test
first asserts that the encoded-name authorization request is valid, then asserts
that neither synthetic state nor challenge occurs anywhere in the production
Pino HTTP log line. API unit shards total 5,570 passing tests in each of the
coverage and Australia/Sydney runs; the HTTP e2e shards total 1,007 passing tests.

Workshop independently loaded the pinned original modules without source edits,
using local TypeScript/Pino dependencies. The original encoded-name counterexample
and canonical request remain accepted and are redacted. Checks passed for 20
accepted state/challenge encoding combinations, 14 canonical/encoded sensitive
parameter aliases, preservation of distinct names and rejection of duplicate
decoded names. Two real local HTTP requests through the original
`buildPinoHttpOptions('production', 'info')` confirmed absence of synthetic query,
cookie, authorization, response-cookie and callback-code values throughout the
emitted log line. The [scoped result](../.local/native-log-correction-01a1284c/result.json)
records these checks. No live log or real account credential was inspected.

A separate anonymous staging health read on 2026-10-11 returned `status: ok`,
`commit: 67d5cbd` and `mongo: up`. This establishes the observed staging revision,
not production deployment or an authenticated native flow. The earlier
log-redaction deviation below is resolved within this reviewed scope. No shared
contract changed. Issue 8 still has no Daychi report; the controlled account,
client implementation and joint native N01/N11/N15/N16/N17 evidence remain
unverified. This correction review does not acknowledge or close either assignment.

## Native provider evidence — reviewed 2026-10-11

Cabinet's [native provider report](https://github.com/dveyarangi/xuanxue-workshop/issues/7#issuecomment-6102552279)
identifies merged PRs [585](https://github.com/gregoryKot/xuanxue-cabinet/pull/585),
[586](https://github.com/gregoryKot/xuanxue-cabinet/pull/586) and
[588](https://github.com/gregoryKot/xuanxue-cabinet/pull/588), with final inspected
revision `97642c734a0cc327d13bc58f193ac10a13b8d476`. Workshop read the original
issue timeline, PR conversations and merge identities, froze the committed source
and compared the provider against the accepted native profile at Workshop
`3c98d4a5201710f8f777183dd7b61caefe47e2d5`. This supersedes the older native-provider
gap within that scope; older dated observations below retain their provenance.

The [native grants service](https://github.com/gregoryKot/xuanxue-cabinet/blob/97642c734a0cc327d13bc58f193ac10a13b8d476/api/src/native-auth/native-grants.service.ts)
implements random 32-byte base64url credentials with SHA-256-only stored
associations, full current-user checks, whole-second expiry/renewal, preserved
predecessors and grant-wide revocation. The
[authorization service](https://github.com/gregoryKot/xuanxue-cabinet/blob/97642c734a0cc327d13bc58f193ac10a13b8d476/api/src/native-auth/native-authorizations.service.ts)
uses a database record for validated bindings, fixed pending/code deadlines,
atomic completion and single-use S256 code exchange. Separate controllers enforce
native request/error shapes and use the same `toMeDto` as web. Browser flow reads
the existing session without renewing it; `/login/native` resumes automatically
through tab-local attempt context and rereads the session on return from email
login in another tab. This source inspection does not demonstrate actual Daychi
callback, restoration or content behavior.

The exact-revision [CI run 38087888957](https://github.com/gregoryKot/xuanxue-cabinet/actions/runs/38087888957)
passed. Its downloaded logs confirm 5,563 API unit tests in each of coverage and
Australia/Sydney runs, 1,007 HTTP e2e tests and 4,947 web tests in each of coverage
and Australia/Sydney runs. All 14 native API unit files and seven native HTTP
suites executed; web native-screen, attempt and return-path suites executed.
Inspected assertions cover full web/native profile parity and normalized hidden
tiles, 59/60-second code expiry, 899/900-second pending expiry, wrong-verifier
nonconsumption, concurrent single-use exchange/completion, 604800/604801-second
renewal, retained predecessor use, revoke/renew races and current blocked/deleted
account refusal. Native revocation HTTP assertions exercise another native grant;
an actual Daychi build and joint browser/native isolation proof remain separate.

Anonymous HTTPS refusal probes on 2026-10-11, recorded at 23:10 UTC on
2026-10-10 (02:10 in Asia/Jerusalem), found
`https://staging.xuanxue.su/api/health` returning 200, `commit: 97642c7`, `mongo: up`.
Native `me` without a bearer returned 401 `invalid_token` with `WWW-Authenticate`;
an unknown synthetic code returned 400 `invalid_grant`; an unregistered callback
returned a local 400; invalid scope returned a registered callback containing
only `error`, `state`, `iss`, with the staging issuer. Each native refusal carried
`no-store`/`no-cache` and no `Set-Cookie`. No account, pending authorization,
issued credential, live fixture or deployment was changed. These probes establish
the inspected staging revision and anonymous paths, not an authenticated native
flow or production deployment. The [local probe result](../.local/native-provider-review-20261011/runtime-result.json)
retains the observations.

One provider deviation is reproduced against the native profile's
[Transport and common representation](contracts/native-account-session.md#transport-and-common-representation)
log protection. The
[query parser](https://github.com/gregoryKot/xuanxue-cabinet/blob/97642c734a0cc327d13bc58f193ac10a13b8d476/api/src/native-auth/native-browser-query.ts)
accepts percent-encoded parameter names through `URLSearchParams`, whereas
[request URL redaction](https://github.com/gregoryKot/xuanxue-cabinet/blob/97642c734a0cc327d13bc58f193ac10a13b8d476/api/src/logging/request-serializer.ts)
matches the raw name. A fully valid synthetic authorization URL with `%73tate`
and `%63ode_challenge` retains both values in the actual local Pino JSON
`req.url`, although parsed `req.query` is redacted. Canonical names are redacted;
duplicate decoded names are rejected. The
[counterexample](../.local/native-provider-review-20261011/counterexample.cjs) loads
frozen original modules without source edits and uses synthetic values only;
its [result](../.local/native-provider-review-20261011/counterexample-result.json)
records the mismatch. This does not establish disclosure of any real credential
or access to live provider logs. Cabinet owns correcting the redaction and
supplying executed regression evidence in original issue 7. No shared contract
amendment is needed. Full provider conformance, Daychi implementation and joint
native proof are not accepted by this review.

## Assignment evidence — reviewed 2026-10-08

Cabinet's [provider report](https://github.com/dveyarangi/xuanxue-workshop/issues/5#issuecomment-6052693441)
identifies [PR 570](https://github.com/gregoryKot/xuanxue-cabinet/pull/570), merged as
`868a4edb09926a950b78e8daa3ce495c6e8e256e`. Workshop inspected the public mapper,
service, controller, shared lookup and field/omission checks. Invalid selected
occurrences are omitted with error logs containing cause and available IDs;
count limits precede validation without refill, windows remain uncapped, and
read/code failures propagate. Protected student missing-class behavior is retained.
The executable definition cites Workshop `4aec5f8`.

The merge [CI run](https://github.com/gregoryKot/xuanxue-cabinet/actions/runs/37729360044)
passed. Logs confirm executed omission, public/query and protected-student HTTP
suites and mapper/service/timezone checks. Disposable HTTP fixtures cover mixed
corruption, shared bad class, missing class, repair recovery, all-invalid and
truly empty selections, count without refill, omission logs and genuine read
failure. Unchanged earlier query/identity/exposure evidence remains applicable.
No remaining provider deviation was found in this assignment's scope. Provider
acknowledgement awaits publication of these records; actual native proof remains
in issue 6.

Read-only HTTPS checks on 2026-10-08 at approximately 05:14 UTC found staging
`https://staging.xuanxue.su/api/health` reporting `868a4ed`, `mongo: up`, and
production `https://xuanxue.su/api/health` reporting `fc2dee2`, `mongo: up`.
The staging window from `2026-10-08T00:00:00+03:00` to
`2026-10-22T00:00:00+03:00` returned 63 rows with the public field set and no Zoom
substring. Corruption/logging proof comes from disposable CI data; no live data
was corrupted. The amended provider is verified on staging; production retains
the earlier implementation. The dated environment checks below remain historical.

Daychi's [installation report](https://github.com/dveyarangi/xuanxue-workshop/issues/2#issuecomment-6043001309)
and [PR 7](https://github.com/sleontenko/daychi/pull/7) expose retained instructions
at `6fd2657b9dd66fe8a85947fc62f492280978856b`. Both installed files match Workshop
`e209d27` exactly after the reported label, source-revision, Installation removal
and immutable companion-link adaptations. AGENTS.md has the existing/target
boundary summary and invocation rule. The accessible verification record reports
matching host hashes and fresh-session invocation/discovery; the original report
demonstrates authenticated return. PR 7 remains open. These findings establish
installation evidence, not a merge, application integration or release; the
[original acceptance](https://github.com/dveyarangi/xuanxue-workshop/issues/2#issuecomment-6052903501)
and completed closure satisfy issue 6's installation dependency.

## Assignment and native-profile recheck — 2026-10-10

The full Workshop issue timelines were read across all returned pages, including
closed assignments and cross-references. At that review no native-auth assignment existed.
Daychi's [native progress report](https://github.com/dveyarangi/xuanxue-workshop/issues/6#issuecomment-6086520134)
and [TestFlight 17 report](https://github.com/dveyarangi/xuanxue-workshop/issues/6#issuecomment-6089038600)
claim actual staging reads, client checks and an operator-authorized internal beta.
Their client commits, frozen snapshot and QA records remain local references;
Workshop has not inspected that implementation or verified the reported native
observations, release status or regressions. Controlled provider create/move/cancel
and mixed-corrupt/repair proof remain outstanding. The
[Cabinet fixture follow-up](https://github.com/dveyarangi/xuanxue-workshop/issues/5#issuecomment-6090400430)
requests its authorized operator, environment, fixture identities and timing;
the [Daychi review](https://github.com/dveyarangi/xuanxue-workshop/issues/6#issuecomment-6090404158)
records the missing accessible artifacts and scoped acceptance remainder.

Fresh remote heads are Cabinet
`fee65f3b8004d4ecac6c2d3da668cf966be0d0f5` and Daychi
`0a3c824c1586eb7b3ca16ca0b3a365539076b025`. Compared with the 2026-10-08 baseline,
Cabinet's inspected auth guard/controller, browser token/renewal and public lesson
paths have no changed files. Its account mapper now includes a new required web
self-profile field. Daychi's comparison contains the published collaboration
installation and wiki changes, but no changes to the inspected native access,
intent or app-configuration paths and no published public-pilot client. These
source comparisons establish neither current deployment nor native runtime behavior.

At that exact Cabinet head, [MeDto](https://github.com/gregoryKot/xuanxue-cabinet/blob/fee65f3b8004d4ecac6c2d3da668cf966be0d0f5/shared/src/me.ts#L95)
requires `homeHiddenTiles: HomeTileKey[]`.
[The shared keys and normalization](https://github.com/gregoryKot/xuanxue-cabinet/blob/fee65f3b8004d4ecac6c2d3da668cf966be0d0f5/shared/src/home-tiles.ts)
define `nextLesson`, `notice`, `exams`, `payment`, `grading`, `events` in that
canonical order, remove duplicates/unknown stored keys and map absent stored
data to `[]`. [toMeDto](https://github.com/gregoryKot/xuanxue-cabinet/blob/fee65f3b8004d4ecac6c2d3da668cf966be0d0f5/api/src/auth/user.mapper.ts)
returns this normalized field. This is a source fact, not a new native UI or
mutation requirement. The accepted native contract's full-current-web parity
obligation remains fixed. Both independent recipient readers found the field
missing from the fixed native definition/example and N01 inputs. The user accepted
its addition on 2026-10-10; the
[native contract](contracts/native-account-session.md#accepted-web-self-profile-parity)
now defines that read-only parity field and its common cases. The
[native ticket](tickets/done/01-0008-native-cabinet-account-session.md#recipient-revalidation--2026-10-10)
owns affected revalidation and publication. This reconciles the accepted definition,
not provider/client implementation. The 2026-10-09 profile baseline below
does not establish the current complete field set.

## Native security amendment source check — 2026-10-10

Preparation of the accepted security amendment re-read original native issues
7 and 8: their bodies still cite Workshop `b8ab296`, retain the original recipient
labels, and contain no comments or intervening implementation evidence.
Cabinet's local source is `f5036604a414f5e509ca3c9a73d5bcaaa72b3961`;
its only changed file since the inspected `fee65f3b` baseline is `CLAUDE.md`.
The scoped native-auth, web self-profile and hidden-home-tile observations above
remain applicable. Neither changed instructions nor this source comparison
establish native implementation or deployment.

The current public Daychi main remains
`0a3c824c1586eb7b3ca16ca0b3a365539076b025`, read directly from GitHub; the compare
from that baseline to main is identical with no changed files. The older local
checkout is `5f9ba442e04cd5dfa70527b9e670b491c491888c`, not that public head.
Its presence does not supersede the newer immutable source comparison above.
The original public-pilot assignment's private client reports remain outside
this native-auth source evidence; no native-auth implementation is inferred.

## Native account-session source — 2026-10-08

This scoped read used Cabinet main
`868a4edb09926a950b78e8daa3ce495c6e8e256e` and Daychi main
`e1ab559c8d5db3dbd7db95aa7400941381ada12a`. Compared with the native ticket's
earlier `fc2dee2` / `5f9ba44` evidence, the inspected authentication/access paths
have no intervening changes. The newer revisions do not establish native support.

Cabinet's
[guard](https://github.com/gregoryKot/xuanxue-cabinet/blob/868a4edb09926a950b78e8daa3ce495c6e8e256e/api/src/auth/auth.guard.ts)
still accepts a browser cookie, checks the current account and rejects blocked
accounts. Its browser credential expires 90 days after issuance and is reissued
when its age is strictly greater than seven days:
[token](https://github.com/gregoryKot/xuanxue-cabinet/blob/868a4edb09926a950b78e8daa3ce495c6e8e256e/api/src/auth/session-token.ts),
[renewal](https://github.com/gregoryKot/xuanxue-cabinet/blob/868a4edb09926a950b78e8daa3ce495c6e8e256e/api/src/auth/session-renewal.ts).
The inspected auth controller exposes browser login/profile/logout, with logout
clearing the cookie; it supplies neither native code exchange nor grant revocation.
The guard's mutation CSRF check also applies to public routes unless explicitly
skipped. Native form/Bearer operations therefore need deliberate channel handling.
[Browser return targets](https://github.com/gregoryKot/xuanxue-cabinet/blob/868a4edb09926a950b78e8daa3ce495c6e8e256e/web/src/auth/returnTo.ts)
are internal paths in tab session storage; native authorization must preserve that
restriction rather than turn login into an arbitrary redirect service.

Daychi's
[access session](https://github.com/sleontenko/daychi/blob/e1ab559c8d5db3dbd7db95aa7400941381ada12a/apps/practice-app/src/features/access/session.ts)
stores its own backend's opaque credential in SecureStore, restores it through
that backend and protects against stale responses. Its current logout waits for
the backend before clearing storage. Neither operation implements Cabinet native
account access. The
[native intent handler](https://github.com/sleontenko/daychi/blob/e1ab559c8d5db3dbd7db95aa7400941381ada12a/apps/practice-app/src/app/+native-intent.tsx)
handles invitation links, and
[app configuration](https://github.com/sleontenko/daychi/blob/e1ab559c8d5db3dbd7db95aa7400941381ada12a/apps/practice-app/app.json)
registers `quietpractice` with existing iOS/Android identity
`ai.mypraxis.quietpractice`. The package already has browser, linking, crypto and
secure-storage libraries; no Cabinet-specific callback/store/profile flow was
found in the inspected paths.

The [native account-session profile](contracts/native-account-session.md) is an
accepted addition to those boundaries; acceptance does not establish deployed
capability. This dated source inspection did not itself approve native lifetime
or renewal policy; the profile owns the user's subsequent accepted decisions.
No authenticated mutation, token issuance, sibling edit or native runtime check
was performed by this source inspection.

## Native consumer needs — 2026-10-09

A fresh GitHub read confirmed Daychi main remains
`e1ab559c8d5db3dbd7db95aa7400941381ada12a`. The local checkout is the older
`5f9ba442e04cd5dfa70527b9e670b491c491888c`; the inspected access/session and
access-screen sources agree with the freshly fetched main files. This is source
evidence, not a new native/runtime verification.

The [session client](https://github.com/sleontenko/daychi/blob/e1ab559c8d5db3dbd7db95aa7400941381ada12a/apps/practice-app/src/features/access/session.ts)
receives its own backend's opaque `token`, stores it in SecureStore and sends
`Authorization: Bearer ...`. Restoration checks `/api/access/session`;
[the server](https://github.com/sleontenko/daychi/blob/e1ab559c8d5db3dbd7db95aa7400941381ada12a/practice_api/daychee_app.py)
returns `{ "active": true }`, not an account profile. Native consumers use that
credential for `/api/wiki/*` catalog/material reads and `/api/access/zoom`.
Public schedule reads and ordinary local selection/reminders do not require it.

The [access screen](https://github.com/sleontenko/daychi/blob/e1ab559c8d5db3dbd7db95aa7400941381ada12a/apps/practice-app/src/features/access/access-screen.tsx)
offers a request/invitation flow and "Выйти на этом телефоне". The inspected
screen, settings and session paths have no Cabinet account picker, account
profile or in-place account-switching story. They do not establish a need for
email, phone, roles or per-material permissions in a Cabinet token/profile.
Names and Telegram entered in an access request are request data, not claims
required by these authenticated content readers.

The accepted target differs from this current implementation:
[content admission](boundaries.md#accepted-content-admission) uses a Cabinet-issued
bearer presented to Cabinet and Daychi, with authoritative admission checked by
Cabinet. Its server-to-server check remains unsettled. The accepted native account-session
profile defines acquisition and lifecycle while preserving the existing content
credential; its `account:read` scope alone does not complete unified content access.

Browser interaction was checked against
[RFC 8252 section 8.6](https://www.rfc-editor.org/rfc/rfc8252#section-8.6):
automatic authorization without interaction is discouraged when native client
identity cannot be assured, even after previous approval of a client ID. The
accepted custom scheme and PKCE bind an exchange to its initiator; they do not
prove that initiator is the genuine Daychi application. Merging authorization
interaction into fresh browser sign-in was a UX proposal. The user subsequently
accepted [automatic continuation](contracts/native-account-session.md#accepted-browser-continuation-without-additional-confirmation)
and the [client-impersonation risk](contracts/native-account-session.md#accepted-risk--native-client-impersonation)
on 2026-10-09, removing the extra Cabinet confirmation. This is a recorded
decision, not changed provider behavior or a claim of compliance with that RFC
recommendation.

## Cabinet web self-profile — 2026-10-09

A fresh GitHub branch read found Cabinet main at
`1ad7fb7e93a1440fa59330481eba4f2f0c0eb025`, newer than the 2026-10-08 native
source baseline. This check inspected self-profile sources at that exact revision;
it does not refresh every earlier auth/runtime observation.

The [web AuthProvider](https://github.com/gregoryKot/xuanxue-cabinet/blob/1ad7fb7e93a1440fa59330481eba4f2f0c0eb025/web/src/auth/AuthProvider.tsx)
reads `GET /auth/me` as
[MeDto](https://github.com/gregoryKot/xuanxue-cabinet/blob/1ad7fb7e93a1440fa59330481eba4f2f0c0eb025/shared/src/me.ts).
Its fields are `id`, `name`, `roles`, `status`, `telegramLinked`, `botChatActive`,
`hasEmail`, optional `email`, `googleLinked`, optional `pendingEmail`, `noTelegram`,
`needsProfile`, `studentMode` and `canUseStudentMode`.
The [mapper](https://github.com/gregoryKot/xuanxue-cabinet/blob/1ad7fb7e93a1440fa59330481eba4f2f0c0eb025/api/src/auth/user.mapper.ts)
omits absent emails and uses effective roles, empty in student mode. The
[guard](https://github.com/gregoryKot/xuanxue-cabinet/blob/1ad7fb7e93a1440fa59330481eba4f2f0c0eb025/api/src/auth/auth.guard.ts)
checks the current account and refuses a blocked account before successful profile
read. Telegram/Google raw identity IDs and a phone field are absent from MeDto.

The user required the full web profile for native Daychi on 2026-10-09. This
requirement lives in
[accepted web self-profile parity](contracts/native-account-session.md#accepted-web-self-profile-parity);
the earlier consumer-needs observation is not a reason to narrow that payload.
The user subsequently excluded phone on 2026-10-09, matching the checked web shape.
No profile mutation, sibling edit or new native proof was performed.

## Cabinet public-schedule environments — checked 2026-10-06

Cabinet's
[runbook](https://github.com/gregoryKot/xuanxue-cabinet/blob/fc2dee20d64d91122a58e57709c378c5fc91bae7/docs/RUNBOOK.md#2-деплой)
identifies staging as `https://staging.xuanxue.su` from `main`, and production as
`https://xuanxue.su` from `release`.

Workshop repeated anonymous read-only HTTPS checks on 2026-10-06 at 07:09 UTC
(10:09 in `Asia/Jerusalem`) after Cabinet's deployment report. These results
supersede the earlier production `27f3e7b`/404 observation:

| Environment | API origin | Observed deployment | Public lessons result |
|---|---|---|---|
| Staging; native pilot test environment | `https://staging.xuanxue.su` | `/api/health`: 200, `mongo: up`, `commit: fc2dee2` | Fourteen-date window: 200 bare array, 63 distinct lessons; `limit=0`: 400 `invalid_input`; protected `/api/me/lessons` without a session: 401 |
| Production | `https://xuanxue.su` | `/api/health`: 200, `mongo: up`, `commit: fc2dee2`; `release` and tag `prod-20261006-0630` identify full commit `fc2dee20d64d91122a58e57709c378c5fc91bae7` | Same window: 200 bare array, 67 distinct lessons; `limit=0`: 400 `invalid_input`; protected `/api/me/lessons` without a session: 401 |

The [accepted production promise](boundaries.md#accepted-first-schedule-connection)
records the same public API at the production origin. Cabinet's
[production report](https://github.com/dveyarangi/xuanxue-workshop/issues/5#issuecomment-6010762378)
and successful [release workflow](https://github.com/gregoryKot/xuanxue-cabinet/actions/runs/37424107719)
agree with the live revision. The workflow's backup and promotion jobs succeeded.

The same-origin `/api` routing is confirmed by these responses. The configured
origin excludes `/api`; the operation already supplies `/api/public/lessons`.
An anonymous staging request for
`from=2026-10-06T00:00:00+03:00` and `to=2026-10-20T00:00:00+03:00`, with the
offsets URL encoded, returned 63 staging rows and 67 production rows, all
scheduled, with distinct IDs, ascending starts and the allowlisted field set.
Neither response contained a `zoom` substring. The earlier staging sample also
checked required types/enums. These samples do not
establish full conformance, the malformed-source guarantee, session-bearing
projection, controlled changes, or reachability from an actual native device.
The [public lessons contract](contracts/public-lessons.md) remains the wire
authority. Its identity scope is one data environment; production and staging
IDs/data are not interchangeable.

### Existing controls for the native test

Cabinet already supplies the fixture operations. At `fc2dee2`,
[PlanningScreen](https://github.com/gregoryKot/xuanxue-cabinet/blob/fc2dee20d64d91122a58e57709c378c5fc91bae7/web/src/planning/PlanningScreen.tsx)
opens `/planning/new` through **Занятия → Разовое занятие**, and opens the
lesson editor at `/planning/{lessonId}`. The create form selects an existing
class, start, duration and topic. The existing editor changes start time and
offers **Отменить занятие** with confirmation; its restore action is
**Вернуть в расписание**. Date/time fields use the operator browser's local
timezone, converted to UTC by
[formatDate](https://github.com/gregoryKot/xuanxue-cabinet/blob/fc2dee20d64d91122a58e57709c378c5fc91bae7/web/src/lib/formatDate.ts).

The corresponding authenticated
[lesson operations](https://github.com/gregoryKot/xuanxue-cabinet/blob/fc2dee20d64d91122a58e57709c378c5fc91bae7/api/src/lessons/lessons.controller.ts)
are `POST /api/lessons` (existing `classId`, `startsAt`, optional duration/topic),
`PATCH /api/lessons/{id}` with `startsAt` for a move, and the same PATCH with
`status: cancelled` for cancellation. The controller permits teacher, assistant
and admin roles. The service changes the same occurrence ID. This is inspected
source behavior, not an authenticated staging UI or mutation test.

The joint test can use a dedicated one-off staging lesson, refresh Daychi,
move that same lesson within and outside the selected window, and cancel it
inside the window. Cabinet's authorized operator owns those writes; Daychi
remains read-only. Available operator access, the actual fixture/class
IDs, timing and the observed native refresh results require coordination or
execution evidence. No live lesson, credential or deployment was changed by
this check. Cabinet's operator performed the reported production promotion;
Workshop verified its public result.

## Cabinet

At `fc2dee2`, Cabinet additionally supplies anonymous `GET /api/public/lessons`
for public schedule readers, with Daychi native as its intended new consumer.
Its Cabinet-owned [executable definitions](https://github.com/gregoryKot/xuanxue-cabinet/blob/fc2dee20d64d91122a58e57709c378c5fc91bae7/shared/src/public-lessons.ts)
implement the original public wire shape at
[Workshop e209d27](https://github.com/dveyarangi/xuanxue-workshop/blob/e209d27239391be3af2be71b898c79f453851c01/docs/contracts/public-lessons.md).
The route uses count or complete bounded-window selection and an explicit public
projection; the protected `/api/me/lessons` route remains separate. Deployment
is verified above. The malformed-data defect at this older revision is superseded
by the `868a4ed` review above; production still uses this older implementation.

The user replaced the not-yet-used public pilot's all-or-error guarantee on
2026-10-07. The [amended contract](contracts/public-lessons.md) requires valid-only
best-effort rows and error-level logs for omitted corrupt occurrences, without a
version selector or public completeness metadata. The pinned projection findings
remain invalid emitted data; allowing omission does not authorize malformed rows.
Amended implementation and staging availability are verified above; amended
production deployment is not established by that review. The later [pilot closure](#public-schedule-pilot-closure--2026-10-19) waives remaining native recovery evidence as a closure requirement.
Cabinet's existing error reporting uses a developer journal and Telegram:
[ADR-0053](https://github.com/gregoryKot/xuanxue-cabinet/blob/af2dcc7542cef7f5f18edc9ab075965310cc453e/docs/adr/0053-server-errors-alert-admin-in-telegram.md)
and [ADR-0132](https://github.com/gregoryKot/xuanxue-cabinet/blob/af2dcc7542cef7f5f18edc9ab075965310cc453e/docs/adr/0132-app-errors-journal-for-developer.md).
Sentry was rejected there. The inspected reporting path is called
by the HTTP-500 filter, so it does not establish reporting for handled omissions
in HTTP 200. The `868a4ed` public service supplies that explicit error-log path;
no new alert-delivery guarantee is inferred.

Cabinet has a React/Vite web client, NestJS API, shared TypeScript contracts, and
MongoDB persistence. The API serves the web application and `/api` on the same
origin in the inspected deployment configuration. Its
[route map](https://github.com/gregoryKot/xuanxue-cabinet/blob/27f3e7bf50ac0a1e1f981519b7009fc2a19e7042/shared/src/api-routes.ts)
connects typed requests to the frontend and backend; TypeScript and registered-route
checks already protect parts of this seam. Cabinet-only workflows include payments,
materials, recordings, and exams.

The [authentication guard](https://github.com/gregoryKot/xuanxue-cabinet/blob/27f3e7bf50ac0a1e1f981519b7009fc2a19e7042/api/src/auth/auth.guard.ts)
reads the session cookie, verifies the credential, checks the current user, and
rejects blocked users. It does not yet implement the agreed native bearer contract.
The current profile endpoint is not a narrow content-admission check.

Cabinet models recurring classes and dated lessons. Its
[student schedule](https://github.com/gregoryKot/xuanxue-cabinet/blob/27f3e7bf50ac0a1e1f981519b7009fc2a19e7042/shared/src/my-lessons-routes.ts)
is authenticated and returns upcoming lessons with optional Zoom information.
The request accepts a count limit (default 10, maximum 50), not a date window.
A date filter on a different API cannot be inferred for this endpoint.
`MyLessonDto` returns the lesson ID but no `classId`, whereas recurring reminder
scope uses `classIds`. The inspected mapper confirms that omission; a shared
lesson-to-class mapping for the broader shared subscription migration remains
unverified. The additive public pilot supplies `classId` under its fixed contract.

The [reminder settings API](https://github.com/gregoryKot/xuanxue-cabinet/blob/628314472aa2752ebb2bbe9ab75ac3dea9791719/shared/src/notifications-routes.ts)
reads lesson notification preferences and updates scope and lead time through
`GET /me/notifications/lessons`, `PUT /me/notifications/lessons/scope`, and
`PUT /me/notifications/lessons/reminder-minutes`. Scope is all classes or selected
`classIds`; lead time is 15/30/60/120 minutes or the school default. It does not
represent one-off lesson-date selections.
This class scope also filters cancellation, recording and class-linked material
notices; adapting reminder selections must preserve those Cabinet web obligations.

Cabinet frontend reference rechecked on 2026-10-04 at `62831447`:
`web/src/notifications/LessonScopeClassList.tsx` and `lessonScopeEdit.ts` edit
selection by class ID; `useLessonScope.ts` reads the shared account settings and
writes the full class scope, applying the server's saved response. Scope and
lead-time responses update their own parts to avoid overwriting an independent
in-flight change. The current types expose class scope and lead time, not one-off
lesson selection or offline per-choice synchronization.

`web/src/student/StudentLessonsScreen.tsx` identifies cards by lesson ID and
renders received lesson data. `api/src/lessons/lessons.service.ts` updates the
same lesson ID when `startsAt` changes; `lesson-reminder-plan.ts` uses the current
`startsAt`, filters by selected class and emits the lesson ID. These support the
identity reference, but do not establish an existing one-off reminder feature.

The scheduler runs every minute. The
[reminder service](https://github.com/gregoryKot/xuanxue-cabinet/blob/628314472aa2752ebb2bbe9ab75ac3dea9791719/api/src/lessons/lesson-reminder.service.ts)
uses current server data to create an inbox notice once per user and lesson, then
invokes browser push. The
[browser sender](https://github.com/gregoryKot/xuanxue-cabinet/blob/628314472aa2752ebb2bbe9ab75ac3dea9791719/api/src/push/push-sender.service.ts)
sends an empty ping; the
[web service worker](https://github.com/gregoryKot/xuanxue-cabinet/blob/628314472aa2752ebb2bbe9ab75ac3dea9791719/web/public/sw.js)
fetches the inbox and displays the notification. This does not provide a native
Daychi push adapter.

## Daychi

Daychi includes an Expo native client (`apps/practice-app`), the active FastAPI
application (`practice_api.daychee_app`), and a separate web wiki (`apps/wiki-graph`).
Its backend also serves access flows, feedback, administrative operations, schedule
and Zoom data, public pages and downloads. These responsibilities matter to any
future service retirement; they are not all content-serving code.

The native [schedule loader](https://github.com/sleontenko/daychi/blob/5f9ba442e04cd5dfa70527b9e670b491c491888c/apps/practice-app/src/features/schedule/load.ts)
races its own API with the school's public HTML source. Web loading cannot use that
HTML fallback because of browser restrictions. The calendar covers fourteen days.

Its decoder requires a snapshot envelope with revision, fetch/expiry timestamps,
school source URL, `Asia/Jerusalem`, `weekly_template`, and exception-verification
status. Occurrences use series/date IDs, `starts_at` and `ends_at`. Cabinet's
upcoming array is not directly compatible with that decoder. Daychi also applies
bundled timing corrections in `schedule/zoom.ts`; the migration must account for
those corrections rather than silently applying school-HTML corrections to
Cabinet's dated lessons.

The [active schedule flow](https://github.com/sleontenko/daychi/blob/5f9ba442e04cd5dfa70527b9e670b491c491888c/apps/practice-app/src/features/schedule/use-schedule.ts)
stores choices and preferences on the device, loads on startup and foreground
return, and refreshes every five minutes while active. Its
[attendance model](https://github.com/sleontenko/daychi/blob/5f9ba442e04cd5dfa70527b9e670b491c491888c/apps/practice-app/src/features/schedule/attendance.ts)
supports individual dates, recurring subscriptions, and skipped-date exceptions.
Skipping also affects the personal upcoming-class selection. Lead times are
0/15/30/60 minutes.

[Local notification delivery](https://github.com/sleontenko/daychi/blob/5f9ba442e04cd5dfa70527b9e670b491c491888c/apps/practice-app/src/features/schedule/local-reminders.ts)
plans OS notifications from the loaded schedule and choices, cancelling and
rescheduling when those inputs change. The active flow retires the older server
reminder registration before enabling local delivery. Legacy push-panel code is
not evidence of an active native server-push flow.

On startup the active flow restores cached schedule and reconciles reminders
before its first refresh. A failed refresh marks the UI offline and retains the
loaded data. This is the observed starting point for the
[accepted stale-data behavior](boundaries.md#accepted-daychi-reminder-delivery),
not a guarantee that cancellations reach an offline device or verification that
the Cabinet integration satisfies the target.

Schedule choices and local reminders are already usable without signing in:
the [app layout](https://github.com/sleontenko/daychi/blob/5f9ba442e04cd5dfa70527b9e670b491c491888c/apps/practice-app/src/app/_layout.tsx)
does not gate the schedule and the
[schedule screen](https://github.com/sleontenko/daychi/blob/5f9ba442e04cd5dfa70527b9e670b491c491888c/apps/practice-app/src/features/schedule/schedule-screen.tsx)
does not require a session for selection controls. This is existing functionality,
not a proposed guest-account feature.

The [access client](https://github.com/sleontenko/daychi/blob/5f9ba442e04cd5dfa70527b9e670b491c491888c/apps/practice-app/src/features/access/session.ts)
stores its own opaque bearer credential. Its format validation does not accept
arbitrary Cabinet token formats; an unauthorized response clears the credential,
whereas a network failure retains it. The
[API composition](https://github.com/sleontenko/daychi/blob/5f9ba442e04cd5dfa70527b9e670b491c491888c/practice_api/daychee_app.py)
uses Daychi's existing access authority.

Content delivery covers categories, search, detail, annotations and graph data.
Stable material identities underpin bookmarks. Authored JSON content and SQLite
identity/annotation storage participate in versioned, replay-safe imports.
External media hosting and content preparation are separate from the request API.
Cabinet's existing materials model does not establish compatibility with this wiki.

## Observed seams and limits

Cabinet web consumes Cabinet's protected API. Cabinet now also exposes the public
dated-schedule route on staging and production; Cabinet owns its data and fixture
writes. Daychi's inspected ordinary clients still consume Daychi's API and, for
the native schedule fallback, school HTML. Actual native consumption of the new
Cabinet public route is not verified. Other cross-project connections in the
[target](boundaries.md) retain their recorded migration state.

Workshop source inspection establishes interface inventories and existing checks;
project contributions supply changes and evidence that inspection cannot establish.
The scoped public-schedule checks above establish both Cabinet runtime revisions
and staging/production public-route availability. Other running configurations, installed client
versions, production datasets and deployment acceptance have not been verified.
Current-state updates require new evidence; accepting a target or closing an
implementation issue alone is insufficient.
