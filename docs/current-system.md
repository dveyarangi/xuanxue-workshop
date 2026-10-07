# Current application structure and boundary evidence

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
Provider conformance, native integration and Workshop source publication remain
incomplete; they are separate from the accepted installation.

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
is verified above; malformed required-data handling remains a conformance defect
under [issue 5](https://github.com/dveyarangi/xuanxue-workshop/issues/5#issuecomment-6011347777).

The user replaced the not-yet-used public pilot's all-or-error guarantee on
2026-10-07. The [amended contract](contracts/public-lessons.md) requires valid-only
best-effort rows and error-level logs for omitted corrupt occurrences, without a
version selector or public completeness metadata. The pinned projection findings
remain invalid emitted data; allowing omission does not authorize malformed rows.
Amended implementation/deployment and native recovery evidence remain unverified.
Cabinet's existing error reporting uses a developer journal and Telegram:
[ADR-0053](https://github.com/gregoryKot/xuanxue-cabinet/blob/af2dcc7542cef7f5f18edc9ab075965310cc453e/docs/adr/0053-server-errors-alert-admin-in-telegram.md)
and [ADR-0132](https://github.com/gregoryKot/xuanxue-cabinet/blob/af2dcc7542cef7f5f18edc9ab075965310cc453e/docs/adr/0132-app-errors-journal-for-developer.md).
Sentry was rejected there. The inspected reporting path is called
by the HTTP-500 filter, so it does not establish reporting for handled omissions
in HTTP 200. Such omissions need their own explicit error-log path.

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
