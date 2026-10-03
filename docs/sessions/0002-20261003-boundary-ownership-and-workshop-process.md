# Boundary ownership and Workshop process

Session concluded 2026-10-03. Resume the question store from session
`s-1003-5060`; its last position is q-0002.0007. This record supersedes the earlier
session's undecided provider ownership and no-commits workspace snapshot.

## Decisions and work completed

- Installed goodwolf-harness at `ebde4ab`, including the external sequential
  question-ID update. Installation is committed as `867348a`; the previous
  session record is committed as `653b07a`.
- Kept README focused on the product and added the repository map. Installation
  commands belong in the conversation, not the product README.
- Investigated and visualized both projects' frontend/backend calls. The initial
  investigation underrepresented Cabinet's existing capabilities and Daychi's
  active local reminder delivery; the later investigation corrected these points.
- Recorded the user's accepted provider assignments in [architecture](../architecture.md):
  schedule, users, and reminders move to Cabinet backend; Daychi videos and other
  recordings stay in Daychi for now. Ownership is decided; migration is not implemented.
- Captured the user's Workshop process sketch: maintained boundary contracts,
  local agent onboarding and boundary rules, coordination through addressed
  tickets, visibility/error-monitoring obligations, and periodic ticket discovery.
  Workshop holds cross-domain agreements; each project keeps its internal architecture.
- Rejected mandatory bilateral approval as too bureaucratic. A lightweight
  request/change/migration flow is a candidate; its precise mechanics remain open.
- Repaired question tracking after the user identified missing branches. The
  ownership question is closed with an architecture pointer. Other decisions stay
  open, with recommendations distinguished from accepted requirements.

## Resume here

q-0002.0007 — How will Daychi migrate schedule, users, and reminders to Cabinet
while retaining its content backend?

Cabinet already implements recurring classes, dated lessons, user authentication,
per-user reminder preferences, and scheduler-driven inbox/browser push delivery.
Reuse this behavior when preparing the migration contract. Evidence and concrete
differences are in [architecture](../architecture.md) and the
[migration question](../questions/q-0002.0007-how-will-daychi-migrate-schedule-users-and-reminders-to-cabinet-while-retaining-its-content-backend.md).

The unresolved integration choices are public schedule access and date-window
coverage; stable class/occurrence mapping and preservation of saved choices;
Cabinet identity for native clients and retained Daychi content access; and
reminder preferences, native/offline delivery, and duplicate prevention.
Daychi's active client schedules local OS notifications and disables the older
server reminders. Do not treat the old APNs code as the active client flow.

## Other open questions

- q-0002.0002 — How should Workshop maintain and verify boundary contracts?
  Decide authoritative schemas, contract records, and checks without duplicate definitions.
- q-0002.0003 — How should boundary changes and consumer migrations be coordinated?
  Decide triggers, compatibility, deployment availability, and completion evidence.
- q-0002.0004 — Where should shared tickets live, and how are they addressed and claimed?
  The tracker must work across separate clones and survive individual agent sessions.
- q-0002.0005 — How should agents adopt Workshop rules and discover addressed work?
  Decide onboarding verification, rule updates, checking occasions, and unattended execution.
- q-0002.0006 — What visibility and error-monitoring obligations should Workshop enforce?
  Decide required signals, enablement evidence, incident routing, and recovery tracking.
- q-0002 — What is the architecture of Workshop? These process choices remain open.
- q-0001 — What should Workshop deliver first? Still depends on establishing architecture;
  the earlier onboarding-first suggestion was not accepted.

## Workspace and operational handoff

PRODUCT.md, README.md, architecture, question records, rule-failure notes, and this
session record remain uncommitted. No additional commit or push is authorized by
the conclusion request. No sibling application code, running service, or deployment
was changed during the architecture work.

Installed rule blocks validated successfully, and question-store checks passed
after the ownership closure. Automatic host hook execution is still unverified;
manual window/placement calls work. Existing installation follow-ups are recorded
in [delivery status](../tickets/README.md), including Windows loader symlinks and
the source-ref publication limitation. Do not infer hook execution from hook-file presence.

[Rule failures](../rule-failures.md) records the omitted question branching and
insufficient capability investigation, with proposed clarifications that have not
been installed. Preserve the user's preference for ordinary edit tools and no
repeated file-edit approvals. The installed Python 3.14 executable at
`D:/Dev/Tools/Python/uv/python/cpython-3.14-windows-x86_64-none/python.exe` was used
for local harness scripts to avoid unnecessary uv cache permission prompts.
