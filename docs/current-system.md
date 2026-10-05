# Current application structure and boundary evidence

Source inventory, not a claim about live deployments or completed integration.
Cabinet's general boundary inspection used revision
`27f3e7bf50ac0a1e1f981519b7009fc2a19e7042`; reminder behavior was rechecked on
2026-10-04 at `628314472aa2752ebb2bbe9ab75ac3dea9791719`. Daychi was inspected at
`5f9ba442e04cd5dfa70527b9e670b491c491888c`. Project-agent confirmation is outstanding.

The [first substantive reconciliation](reconciliation-20261004.md) rechecked both
clean local checkouts on 2026-10-04. Cabinet's remote `main` matches `62831447`.
The connected GitHub account receives 404 for Daychi's repository; its remote
revision and running deployment are unverified. General Cabinet seam evidence
below was also rechecked at `62831447`.

## Cabinet

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
lesson-to-class identity must be agreed before Daychi can map subscriptions.

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

Cabinet web consumes Cabinet's API. Daychi clients consume Daychi's API and, for
the native public schedule fallback, school HTML. No deployed Cabinet-to-Daychi
integration was established by this inspection. The cross-project connections in
the [target](boundaries.md) are accepted direction with unresolved details.

The project contributions must confirm complete interface inventories, source
revisions, compatibility constraints, and existing checks. Running configurations,
installed client versions, production datasets and deployment acceptance have not
been verified. Current-state updates require new evidence; accepting a target or
closing an implementation issue alone is insufficient.
