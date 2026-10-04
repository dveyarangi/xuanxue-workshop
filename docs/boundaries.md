# Initial target boundary contracts

Accepted decisions, with unresolved API details identified below. Scope is governed by
[first-stage delivery](stage-1.md); [current behavior](current-system.md) and
[required changes](migration-changes.md) are recorded separately.

## Accepted responsibility boundaries

Decision: the user, 2026-10-03, during the architecture discussion.

| Capability | Target provider | Consumers |
|---|---|---|
| Schedule | Cabinet backend | Cabinet frontend and Daychi clients |
| Users | Cabinet backend | Cabinet frontend, Daychi clients, and Daychi content access integration |
| Reminders | Cabinet backend | Cabinet frontend and Daychi clients |

<straw-dog until="Cabinet serves Daychi content and unified admission is available to every supported client" ticket="docs/tickets/01-0010-daychi-backend-capabilities-in-cabinet.md">
Daychi backend provides its videos and other recordings to Daychi clients.
</straw-dog>

The user deferred backend consolidation to the horizon on 2026-10-04. Cabinet's
existing material, recording, and exam features retain their responsibilities.
The move of schedule, users, and reminders is accepted ownership direction, not a
claim that migration is implemented or deployed.

## Target connections

| Boundary | Provider | Consumer | Responsibility and unresolved contract |
|---|---|---|---|
| Cabinet API for its frontend | Cabinet backend | Cabinet frontend | Preserve existing school workflows. Identify which schedule, identity, access, and reminder promises are also consumed by Daychi, and which routes remain specific to Cabinet. |
| Cabinet API for Daychi | Cabinet backend | Daychi clients | Provide schedule, identity, and reminder capabilities. Apply accepted public/authenticated schedule access. Resolve date windows, stable identifiers, credential lifecycle, preference semantics, and notification delivery. |
| Cabinet admission check for Daychi content | Cabinet backend | Daychi backend | Apply the admission and credential-transport contract below. Check schema, renewal, and verification require agreement. |
| Daychi content API | Daychi backend | Daychi clients | Retain content ownership above. Apply Cabinet-issued bearer transport for native clients and identify which content calls require adaptation. |

The admission contract below owns the third row's failure behavior, removal
condition, and consolidation-ticket binding. Credential format and the executable
check contract remain open.

The first two rows share one provider. Identify the promises common to both
consumers and the requirements specific to Cabinet web or Daychi clients; do not
invent a second definition for a promise merely because it has another consumer.
For the Cabinet web seam, inventory the API surface used by its frontend and mark
which capabilities overlap Daychi's target needs. Cabinet-only promises keep their
definitions in Cabinet, with references here where they constrain a shared change.

### Accepted schedule access

Decision: the user, 2026-10-04. Cabinet provides the target schedule to Cabinet
frontend and Daychi clients. The schedule without Zoom connection details is
public. The schedule with Zoom connection details requires authentication.
Public responses must omit those details; hiding them only in the client does
not satisfy this contract. This decision does not select routes, date-window
parameters, or the mapping of existing Daychi identifiers.

### Accepted reminder selections

Decision: the user, 2026-10-04. The target reminder contract supports a one-off
reminder for a specific lesson date and recurring reminders for a selected
regular class. A one-off selection does not subscribe the user to future dates
and requires no unsubscribe action after that date.

Rationale: a person browsing the schedule can discover a lesson they want to
try and ask to be reminded before it starts. Regular reminders serve the
separate intention to keep attending the same class.

Decision: the user, 2026-10-04. For an authenticated user, Cabinet stores one
account-level selection of lesson dates and regular subscriptions. Cabinet web
and Daychi clients read and change that same selection; choosing a lesson in
one client does not require choosing it again in the other. Lead times and the
transition of existing local selections remain open.

### Accepted Daychi reminder delivery

Decision: the user, 2026-10-04. Daychi requests updated schedule and account
selections from Cabinet and reconciles local OS reminders from the received data.
Native server push is excluded from the agreed delivery scope. The user rejected
adding it as excessive for this work; the existing pull and local-delivery flow
can consume Cabinet's authoritative data without introducing another channel.

Freshness is bounded by the last successful refresh: a cancellation or transfer
cannot change a local reminder until the client receives the update. The existing
startup, foreground-return and periodic foreground refresh provide the starting
point. Preserve those existing refresh occasions unless integration demonstrates
a necessary adaptation. New polling or background-refresh capabilities are outside
the first-stage scope. Record stale-data behavior as a compatibility constraint.

### Accepted removal of per-date skips

Decision: the user, 2026-10-04. Remove Daychi's "skip this date" option from
the target product and do not require per-date skip exceptions in the shared
reminder contract.

Rationale: deciding not to attend does not give a person a useful reason to
open the app and record an exception. Avoiding a single notification provides
little benefit over dismissing it. The action does not notify a teacher or
release a reserved place. The hypothetical "I will miss next Tuesday" describes
the feature's mechanics, but does not establish why a person would use it.
Existing implementation alone is not a reason to preserve it in a shared contract.

The user requires the future ticket addressed to the Daychi agent to include
this explanation. Its scope must account for the option, related behavior and
existing saved exceptions. The disposition of those exceptions needs a migration
proposal; it is not decided here. The accepted one-off and recurring reminder
selections are unaffected by this removal decision.

### Accepted content admission

Decision: the user, 2026-10-04. Every admitted user receives the same Daychi content;
per-reader material permissions are not required. Cabinet owns user authentication
and the current admission decision. A separate gateway was not selected.

<straw-dog until="Cabinet serves Daychi content and unified admission is available to every supported client" ticket="docs/tickets/01-0010-daychi-backend-capabilities-in-cabinet.md">
Daychi backend requests the current admission decision from Cabinet before serving
protected content. Cabinet provides a narrow check using its authoritative session
and user-validity rules; Daychi consumes the decision without owning user accounts
or duplicating those rules. Invalid credentials produce an access refusal. Cabinet
unavailability produces a temporary service error, while clients retain their
stored session for recovery. Cached admission requires an explicitly agreed bound
on revocation delay; no cache policy is implied by this contract.
</straw-dog>

Decision: the user, 2026-10-04. Cabinet web uses a session cookie. Native Daychi
uses a Cabinet-issued bearer credential, presented to Cabinet and Daychi in
`Authorization: Bearer ...`. Daychi passes the presented credential to Cabinet's
admission check. Cabinet owns credential issuance and authoritative validation;
Daychi does not establish a separate account or session authority.

The authentication standard, credential format, acquisition and renewal, the
admission-check request/response, and verification remain open in the
[credential question](questions/q-0002.0008.0001-how-will-daychi-clients-obtain-and-present-cabinet-credentials.md).
The user requested a separate
[standardization question](questions/q-0002.0008.0001.0001-which-authentication-standard-should-cabinet-and-daychi-adopt.md)
on 2026-10-04; no particular protocol or token format is selected.
The current Cabinet cookie and Daychi bearer implementations are source evidence,
not deployed support for this target cross-project contract.
