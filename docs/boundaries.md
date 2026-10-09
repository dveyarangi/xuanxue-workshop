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

<straw-dog question="q-0002.0009">
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
| Cabinet API for Daychi | Cabinet backend | Daychi clients | Provide schedule, identity, and reminder capabilities. The public lessons contract and native account-session profile define their accepted shapes; implementation and joint proof remain separately tracked. Protected schedule and account/reminder synchronization details remain unresolved. |
| Cabinet admission check for Daychi content | Cabinet backend | Daychi backend | Apply the admission and credential-transport contract below. The server-to-server check schema, caller trust and integration verification require agreement. Native account renewal is defined in the separate accepted profile. |
| Daychi content API | Daychi backend | Daychi clients | Retain content ownership above. Apply Cabinet-issued bearer transport for native clients and identify which content calls require adaptation. |

The admission contract below owns the third row's failure behavior, removal
condition, and consolidation-ticket binding. The
[native account-session profile](contracts/native-account-session.md) defines
native acquisition, bearer lifecycle and account access. The executable content
admission-check contract remains open; native account access does not complete it.

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
not satisfy this contract. Routes, exact query names and identifier encoding
remain in the provider's executable contract.

### Accepted schedule retrieval modes

Decision: the user, 2026-10-04. Support both count-limited retrieval and complete
retrieval of a supported bounded date window, selected through URL query
parameters. Preserve the current Cabinet frontend's count-mode behavior and
support Daychi's existing fourteen-day coverage in date-window mode. Count-mode
defaults and limits do not silently truncate a date-window result represented as
complete.

Cabinet owns the typed query and response definitions. Exact parameter names,
interval boundaries, supported bounds, mixed-parameter validation and any
pagination are executable-contract details to propose against both consumers.
The public/authenticated Zoom access rule applies to schedule retrieval regardless
of retrieval mode; this decision does not prescribe frontend presentation.

### Accepted first schedule connection

Scope reaffirmed by the user, 2026-10-05: the first Cabinet–Daychi application
connection is a public, read-only schedule path in native Daychi. It displays
actual Cabinet dated lessons for a complete fourteen-day window, without
credentials or Zoom fields, and reflects reschedules and cancellations after
refresh. Preserve the ordinary Daychi schedule, selections, cache and OS reminders
during this staged connection. Presentation and internal implementation remain
project-owned.

The earlier retirement applied to incomplete issue drafts, not this agreed scope.
Endpoint separation accepted by the user, 2026-10-05: add the public
`GET /api/public/lessons` read, using the user's suggested path, while preserving the existing authenticated
student endpoint. The public response contains only the public schedule, with no
Zoom links, Zoom passwords or authentication credentials. Supplying a session
does not broaden this public response. The future project assignment must carry
this explanation so a recipient can find the answer in its original ticket.

Response agreed by the user, 2026-10-05: return an array with the existing student
lesson fields and their types, excluding `zoomLink` and `zoomPassword`, and add
`classId: string` to each lesson. `id` identifies the dated occurrence; `classId`
identifies its Cabinet class. The pilot supplies this relationship in each item,
without introducing a separate class-ID list or reminder-settings operation.

Query and validation agreed by the user, 2026-10-05: retain Cabinet's count and
date-window conventions, with complete windows free of count truncation. Daychi
requests fourteen school calendar dates in `Asia/Jerusalem`, including earlier
lessons today and each bound's actual timezone offset. The
[public lessons contract](contracts/public-lessons.md#operation-transport-and-request)
owns the exact parameters, defaults, bounds, membership and invalid-input rules.

Failure and recovery amended by the user, 2026-10-07: public pilot reads return
valid available lessons while omitting individual malformed records with
error-level operator logs. Availability of the remaining schedule takes priority
over complete delivery. The prior public pilot contract is not yet used, so its
guarantee is replaced directly without a version selector or completeness metadata.
The client cannot distinguish an omitted invalid record from an absent record.
Failed retrieval or unreliable processing of the selected set still fails the
read using Cabinet's error conventions, without exposing private schedule data.
The [failure contract](contracts/public-lessons.md#failures-and-recovery) owns the
exact status/code/body definitions.

On a network failure, non-success HTTP response or invalid success body, the
pilot retains its last successful Cabinet result and makes the failure visible.
With no previous result it shows unavailability rather than an empty schedule.
Ordinary Daychi cache, selections and OS reminders remain unaffected. This is
ordinary failure handling. A valid best-effort result is a successful read,
not a failed refresh; it needs no new completeness or warning state.

Successful refresh follows the already accepted complete-window/current-schedule
requirement, clarified by the user, 2026-10-05. The pilot displays the returned
list for the requested dates. A lesson moved within those dates keeps its ID and
uses its updated start; one moved outside them is absent from that window.
Cancellation is represented by `status: cancelled` while the lesson remains in
the window. A successful empty list clears the previous displayed result,
including when all selected rows were invalid; it means no valid rows available
and does not prove the source contains no lessons. Repairing records restores
them on a later successful read. This pilot display does not infer reminder or
account mutation from absent rows.

The [public lessons contract](contracts/public-lessons.md) owns the consolidated
wire definition, exact field meanings, request/response examples, identity and
ordering conventions, and common conformance outcomes. These complete the
already-agreed target; consolidation is not a new approval of its behavior.
Published implementation assignments share this complete definition and examples
through the same immutable revision. This scope does not establish implementation or deployment,
release recipient execution, or replace the eventual source-cutover obligations.

Environment selection clarified with the user, 2026-10-06: the native pilot uses
Cabinet's existing staging environment. Production remains a separate deployment;
supplying its address does not establish that it serves the pilot route. The
[environment evidence and existing fixture controls](current-system.md#cabinet-public-schedule-environments--checked-2026-10-06)
identify the concrete origins, observed versions and remaining native-test limits.
The configured origin is environment data; the immutable public wire contract
is unchanged. Cabinet's operator performs controlled lesson writes through its
existing staff functionality; Daychi remains the read-only consumer.

Decision: the user, 2026-10-06. Cabinet is to serve the same
agreed public lessons API at `https://xuanxue.su/api/public/lessons`, using
`https://xuanxue.su` as Daychi's configured production origin. Actual availability
is recorded in the environment evidence. Staging is sufficient for current
native pilot acceptance; Cabinet's operator owns production deployment.

### Accepted schedule source cutover

Decision: the user, 2026-10-04. Remove Daychi's direct school-website HTML
schedule source when its Cabinet schedule integration is verified. After cutover,
fresh schedule data comes from Cabinet; a failed refresh retains the cached
Cabinet schedule and active reminders under the delivery contract below.

Verify the accepted public/authenticated access, complete fourteen-day retrieval,
lesson identity through rescheduling, received cancellations and failed-refresh
behavior before removing the source. The implementing projects supply the
executable checks and evidence. A client with no cached Cabinet schedule cannot
obtain a schedule during a Cabinet outage.

Rationale: the school-website parser reconstructs a weekly timetable without
verifying dated exceptions. It cannot serve as a competing live source for
Cabinet's cancellations, rescheduled occurrences and shared reminder identities.
This is an accepted cutover obligation, not evidence of completed integration.

### Accepted reminder selections

Decision: the user, 2026-10-04. The target reminder contract supports a one-off
reminder for a specific lesson date and recurring reminders for a selected
regular class. A one-off selection does not subscribe the user to other occurrences
and requires no unsubscribe action after that occurrence.

Decision: the user, 2026-10-04. A one-off selection follows the same lesson
occurrence if its scheduled date or time changes. Its identity survives the move;
the reminder uses the updated start time once received. Moving that occurrence
does not turn the selection into a recurring class subscription. Cabinet's
existing identity model is the reference; the one-off reminder capability is an
extension to its current class-based notification selection. This decision does
not prescribe frontend presentation or identifier encoding.

Rationale: a person browsing the schedule can discover a lesson they want to
try and ask to be reminded before it starts. Regular reminders serve the
separate intention to keep attending the same class.

Decision: the user, 2026-10-04. For an authenticated user, Cabinet stores one
account-level selection of lesson dates and regular subscriptions. Cabinet web
and Daychi clients read and change that same selection; choosing a lesson in
one client does not require choosing it again in the other.

Decision: the user, 2026-10-04. On sign-in, Daychi pulls account data from Cabinet.
Ongoing reconciliation follows the accepted rules below; ordering details remain open.

### Accepted offline reminder editing

Decision: the user, 2026-10-04. Signed-in Daychi users can change reminder
selections offline. Preserve pending user changes through refreshes, connection
failures and retries; receiving Cabinet state must not silently discard them.
Cabinet remains the owner of shared account state. Reconciliation must preserve
as much user intent as possible.

Decision: the user, 2026-10-04. Explicit sign-out discards unsynced reminder
selection and lead-time edits for the signed-out account. They are not replayed
on a later sign-in to that account or applied to a different account. This does
not remove changes already accepted by Cabinet. Connection failures and retries
continue to preserve pending edits; they are not explicit sign-out.

Decision: the user, 2026-10-04. Reconcile each reminder choice independently.
Preserve edits to different choices: adding lesson A offline and removing lesson B
in Cabinet preserves both changes. For conflicting edits to the same choice, the
latest edit wins. A removal is an edit and participates in the same ordering;
merging selections must not discard a winning removal. This rule applies to
one-off lesson-date choices and recurring class subscriptions.

Decision: the user, 2026-10-04. When conflicting edits have exactly equal update
times, retain Cabinet's stored value. Apply this tie rule to reminder choices,
including removals, and to the lead-time setting; clients apply the resolved
account state.

Clock handling, pending-edit
tracking, retry behavior and verification remain open in the
[synchronization question](questions/q-0002.0007.0002-how-should-daychi-reconcile-local-edits-with-cabinet-account-state.md).

### Accepted reminder lead times

Decision: the user, 2026-10-04. The shared reminder lead-time setting supports
0, 15, 30, 60 and 120 minutes, plus the school default. Zero means notification
at the lesson start. Cabinet web and Daychi honor the same account setting.
The supported options preserve the explicit lead times available in either
existing client.

Decision: the user, 2026-10-04. Daychi allows offline changes to the reminder
lead-time setting and preserves pending changes under the offline-editing rule.
Reconcile this setting independently of lesson-date choices and recurring
subscriptions; its latest edited value wins, with equal times resolved by the
Cabinet-value rule above. Timestamp mechanics remain open in the synchronization
question above.

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

Decision: the user, 2026-10-04. When a schedule refresh fails, keep the cached
schedule available and leave local reminders active. Reconcile received cancellations and transfers
after a successful refresh. Failed refreshes do not discard pending reminder
selection or lead-time edits. This preserves offline usefulness while accepting
that an unseen cancellation or transfer can leave a reminder based on older data.
Presentation of freshness and refresh failures belongs to Daychi under the
[scope-of-authority contract](agent-contract.md#boundary-scope-and-product-language).

Decision: the user, 2026-10-04. Cabinet and Daychi may both deliver a reminder
for the same lesson to the same account through their existing delivery channels.
Cross-client duplicate notifications are allowed; this integration requires no
shared deduplication or exclusive delivery-channel guarantee. Each project owns
its delivery implementation while consuming the shared account selections and
lead-time setting.

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
this explanation. Its scope must account for the option and related behavior.
The accepted one-off and recurring reminder selections are unaffected by this
removal decision.

### Accepted content admission

Decision: the user, 2026-10-04. Every admitted user receives the same Daychi content;
per-reader material permissions are not required. Cabinet owns user authentication
and the current admission decision. A separate gateway was not selected.

<straw-dog question="q-0002.0009">
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

The [native account-session profile](contracts/native-account-session.md) defines
the accepted native credential, exact renewal wire and common conformance cases.
Publication, implementation and native proof remain outstanding. The separate
content-admission check's request/response, caller trust and integration verification
remain open in the
[credential question](questions/q-0002.0008.0001-how-will-daychi-clients-obtain-and-present-cabinet-credentials.md).
The user requested a separate
[standardization question](questions/q-0002.0008.0001.0001-which-authentication-standard-should-cabinet-and-daychi-adopt.md)
on 2026-10-04; the accepted native profile does not establish full OIDC adoption
or settle the separate admission protocol.
The current Cabinet cookie and Daychi bearer implementations are source evidence,
not deployed support for this target cross-project contract.

### Accepted sign-out scope

Decision: the user, 2026-10-05. Explicit sign-out ends authenticated use in the
current client installation. Other Cabinet and Daychi clients remain signed in;
ordinary sign-out does not terminate every session of the account. The accepted
discard of that installation's unsynced reminder and lead-time edits still
applies; Cabinet's already-accepted account state remains. The user accepted native
local exit and network/storage failure behavior on 2026-10-08; its authoritative
home is [local sign-out policy](contracts/native-account-session.md#accepted-local-sign-out-and-failure-policy).

### Accepted native credential lifetime and renewal

Native account credential lifetime and renewal were accepted by the
user on 2026-10-08. Their authoritative definition is
[accepted credential lifetime and renewal](contracts/native-account-session.md#accepted-credential-lifetime-and-renewal);
the full native wire profile was accepted by the user on 2026-10-09.
Implementation and native proof remain pending.

### Accepted gateway deferral

Decision: the user, 2026-10-05. A shared gateway is deferred until project
contributions demonstrate a concrete client or deployment requirement that the
accepted direct connections cannot satisfy. Daychi clients reach Cabinet for
schedule and account/reminder state, and Daychi's retained backend for content.
Cabinet retains account, issuance and admission authority. The native sign-in
method below was reaffirmed for native-session delivery on 2026-10-08. Gateway
deferral is separate from the accepted native wire profile and does not authorize
gateway implementation.

### Accepted native credential acquisition

Decision: the user, 2026-10-04, accepted the shared Cabinet sign-in handoff for
the initial migration, as a straw dog pending the
[gateway question](questions/q-0002.0010-should-clients-reach-cabinet-and-daychi-through-a-shared-gateway.md).
That provisional disposition records the initial agreement. On 2026-10-08 the
user reaffirmed the existing browser/code-and-PKCE method and corrected a repeated
approval request. Its operative home is
[accepted native credential acquisition](contracts/native-account-session.md#accepted-native-credential-acquisition).
The method and full native wire profile are accepted; the separate admission-check
schema remains unresolved. Gateway deferral remains unchanged.
