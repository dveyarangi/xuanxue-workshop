# Architecture

Workshop maintains cross-domain boundary contracts and coordinates changes to them.
Project implementation architecture stays in the owning repositories. This document
distinguishes accepted responsibility from currently implemented integration.

## Accepted responsibility boundaries

Decision: the user, 2026-10-03, during the architecture discussion.

| Capability | Target provider | Consumers |
|---|---|---|
| Schedule | Cabinet backend | Cabinet frontend and Daychi clients |
| Users | Cabinet backend | Cabinet frontend, Daychi clients, and Daychi content access integration |
| Reminders | Cabinet backend | Cabinet frontend and Daychi clients |
| Daychi content: videos and other recordings | Daychi backend | Daychi clients |

The user explicitly keeps Daychi content in Daychi for now. No content consolidation
or removal of Cabinet's existing material, recording, or exam features was decided.
The move of schedule, users, and reminders is accepted ownership direction, not a
claim that migration is implemented or deployed.

## Contract surfaces

Daychi will consume Cabinet's schedule, user, and reminder capabilities. Its content
backend remains a distinct provider. Moving users to Cabinet requires defining how
Daychi content access recognizes Cabinet identity and access changes.

Workshop owns the agreement at these boundaries. It does not duplicate the internal
architecture of either project. The schema authority, executable checks, rollout,
and tracker mechanisms are still being worked out in the question store.

## Existing capabilities and migration gaps

Inspection of local source on 2026-10-03 found:

- Cabinet already models recurring classes and dated lessons and provides an
  authenticated student schedule through `GET /api/me/lessons`. Its existing
  contract returns a limited upcoming list, whereas Daychi has public schedule
  loading and a fourteen-day calendar. See [student routes](../../xuanxue-cabinet/shared/src/my-lessons-routes.ts)
  and [schedule loading](../../daychi/apps/practice-app/src/features/schedule/load.ts).
- Cabinet already owns user records and login/session handling. Its current guard
  reads a session cookie; Daychi's protected API reads its own bearer credentials.
  See [Cabinet guard](../../xuanxue-cabinet/api/src/auth/auth.guard.ts) and
  [Daychi access composition](../../daychi/practice_api/daychee_app.py).
- Cabinet already schedules lesson reminders, writes inbox notices, and sends
  browser push. It has class-level selection and per-user reminder timing. See
  [reminder service](../../xuanxue-cabinet/api/src/lessons/lesson-reminder.service.ts)
  and [preferences contract](../../xuanxue-cabinet/shared/src/lesson-notifications.ts).
- Daychi's active client flow uses local OS notifications and disables its older
  server reminder registration before enabling them. Its choices include individual
  dates, recurring selections, and skipped dates. See [local reminders](../../daychi/apps/practice-app/src/features/schedule/local-reminders.ts)
  and [attendance model](../../daychi/apps/practice-app/src/features/schedule/attendance.ts).

These differences require a migration contract; moving ownership does not itself
decide native delivery, offline behavior, public access, identifier mapping, or the
replacement of existing credentials. Source inspection does not verify live deployment.

## Open questions

The [question store](questions/) holds contract maintenance, migration, change
coordination, tracker ownership, onboarding, and operational obligations. No new
implementation or deployment is authorized by this architecture record alone.
