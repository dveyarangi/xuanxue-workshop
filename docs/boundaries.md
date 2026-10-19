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

## Accepted Knowledge responsibility boundary

Decision: the user, 2026-10-12, accepted Knowledge's separate participation.

Knowledge owns source preparation, editorial review and its gated import tools.
Daychi retains the API, persisted content, access control and readers. Knowledge
prepares content for Daychi's provider-owned import definitions; separate project
participation changes no wire format, access protocol or content identity.
Existing content/semantics v1 remain active. Structured-article implementation and
integration acceptance stay in [original issue 9](https://github.com/dveyarangi/xuanxue-workshop/issues/9).
Accountability and addressing belong to
[the participant agreement](agent-contract.md#accepted-knowledge-participation--2026-10-12);
observed source and deployment claims belong to [current evidence](current-system.md#knowledge-reception-evidence--inspected-2026-10-12).

## Target connections

| Boundary | Provider | Consumer | Responsibility and unresolved contract |
|---|---|---|---|
| Cabinet API for its frontend | Cabinet backend | Cabinet frontend | Preserve existing school workflows. Identify which schedule, identity, access, and reminder promises are also consumed by Daychi, and which routes remain specific to Cabinet. |
| Cabinet API for Daychi | Cabinet backend | Daychi clients | Provide schedule, identity, and reminder capabilities. The public lessons contract and native account-session profile define their accepted shapes; implementation and joint proof remain separately tracked. Protected schedule and account/reminder synchronization details remain unresolved. |
| Cabinet session validation for Daychi content | Cabinet backend | Daychi backend | Apply the [native content check](contracts/native-content-session.md) and the separate accepted browser check. Wire, caller authority and per-grant native capacity are accepted; implementation and joint proof remain work. Native renewal remains in its account profile. |
| Cabinet sign-in for web wiki | Cabinet backend | Daychi backend and web wiki | Shared browser session, session check, automatic entry/return and Cabinet-site logout are accepted below; implementation, coordinated cutover and deployed proof remain work. |
| Daychi content API | Daychi backend | Daychi clients | Retain content ownership above. Apply Cabinet-issued bearer transport for native clients and identify which content calls require adaptation. |

The admission contract below owns the third row's failure behavior, removal
condition, and consolidation-ticket binding. The
[native account-session profile](contracts/native-account-session.md) defines
native acquisition, bearer lifecycle and account access. The separate
[native content-check contract](contracts/native-content-session.md) is accepted;
native account access alone does not establish its implementation or joint proof.

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

Decision: the user, 2026-10-19. Lesson reminders cover only explicitly chosen
recurring classes or individual lessons. A new account starts with no reminder
selections and receives no lesson reminders until a choice is made. This applies
to Cabinet and Daychi's shared account selection; there is no implicit all-classes
subscription. This decision concerns lesson reminders, not the scope of Cabinet's
other notification kinds.

<a id="accepted-offline-reminder-editing"></a>

### Accepted online-only reminder editing

Decision: the user, 2026-10-19. Changes to shared chosen classes, individual
lesson reminders and reminder lead time require a successful Cabinet save.
Offline shared editing is unavailable. A local draft is not confirmed shared
state. Cached viewing and already scheduled local reminders remain available
offline; Cabinet remains the owner of account settings.

Different choices remain independent: changing one class, lesson or lead time
does not replace unrelated choices. Cabinet determines the order of successful
saves; for the same choice, the last committed value wins. Device edit times
and client-clock tie rules do not determine the shared result.

If a save response is lost or the connection fails during a save, its outcome
can be unknown. Read Cabinet's current settings after reconnecting rather than
assuming success or failure, undoing server state or silently resending the
change. There is no durable offline-edit queue or automatic mutation replay.
Network or authentication failures preserve last confirmed cached settings and
active local reminders; they are not explicit sign-out.

Explicit sign-out clears transient local drafts/request state and cancels
account-owned local reminders. Old requests are not replayed into a later
sign-in or another account. Changes already accepted by Cabinet are retained;
local sign-out does not undo them. Existing account-session isolation and
late-response protections remain applicable.

This decision supersedes the 2026-10-04 offline-editing, pending-edit retention,
client latest-edit-time ordering and equal-time tie requirements. It retains
independent choices, shared account ownership and offline reading/delivery.
The [synchronization question](questions/q-0002.0007.0002-how-should-daychi-reconcile-local-edits-with-cabinet-account-state.md)
holds the history and remaining executable-interface/delivery preparation.

### Accepted reminder lead times

Decision: the user, 2026-10-04. The shared reminder lead-time setting supports
0, 15, 30, 60 and 120 minutes, plus the school default. Zero means notification
at the lesson start. Cabinet web and Daychi honor the same account setting.
The supported options preserve the explicit lead times available in either
existing client.

Decision: the user, 2026-10-19. Lead-time changes follow the
[online-only editing agreement](#accepted-online-only-reminder-editing),
independently of lesson-date and recurring-class choices. This supersedes the
4 October offline lead-time, client timestamp and equal-time reconciliation rule;
the supported lead-time options remain unchanged.

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
after a successful refresh. The 19 October online-only decision retains cached
settings and offline delivery without a pending-edit queue or automatic replay.
This preserves offline usefulness while accepting
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
protected content. Cabinet provides the accepted native/browser checks using its authoritative session
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
The full profile is published at `c9c69c3`; implementation and native proof remain
separate from acceptance of that wire. On 2026-10-16 the user reaffirmed the
already accepted equal-content/current-session rule and approved completing the
[native content-check contract](contracts/native-content-session.md): existing
native GET me, presented-bearer caller authority, fixed matching issuer, per-read
validation and grant-isolated capacity. This adds no separate reader entitlement.
The connection is accepted, with implementation and integrated proof remaining
in [original coordination issue 11](https://github.com/dveyarangi/xuanxue-workshop/issues/11).
The user requested a separate
[standardization question](questions/q-0002.0008.0001.0001-which-authentication-standard-should-cabinet-and-daychi-adopt.md)
on 2026-10-04; the accepted native profile does not establish full OIDC adoption
or substitute for the separately accepted content-validation connection.
The current Cabinet cookie and Daychi bearer implementations are source evidence,
not deployed support for this target cross-project contract.

### Accepted web-wiki reader access

Decision: the user, 2026-10-12, clarified: "все и только вошедшие в кабинет так же
получают доступ к вики".

Reading web wiki requires a valid Cabinet-authenticated account session. Every
such user receives the same wiki content. Anonymous visitors cannot read wiki.
The separate [public homepage graph overview](contracts/web-wiki-session.md#accepted-public-homepage-graph-overview)
was accepted by the user on 2026-10-14: section names, node counts and anonymized
structure only, with no protected material/subtopic text or identity, dates,
source/recording links or credentials. Its canonical allowlist and proof are in
the contract; web-wiki reading still requires the Cabinet session.
There is no separate wiki admission status, reader role or per-material entitlement.
For this web consumer, the existing admission obligation means authoritative
validation of the Cabinet-authenticated session and account, not an additional
wiki-specific eligibility decision.

Cabinet remains the account/session authority. Wiki uses the
[accepted shared browser session](contracts/web-wiki-session.md#accepted-shared-browser-session).
The [current-session check](contracts/web-wiki-session.md#accepted-current-session-check)
defines the accepted backend validation wire; a cookie or frontend check alone
does not authorize protected reader delivery.

### Accepted web-wiki shared browser session

Decision: the user, 2026-10-12, replied "думаю да" after reviewing the simpler
shared-cookie alternative and its common lifetime/logout and no wiki credential
storage consequences. The authoritative home is the
[shared browser-session contract](contracts/web-wiki-session.md#accepted-shared-browser-session).
Cabinet issues the existing session cookie for xuanxue.su and its subdomains;
Daychi validates the presented session/current account through Cabinet before
serving protected wiki content. The websites retain separate frontends/backends.
Cookie lifetime, renewal and browser logout are common. Wiki reader authentication
requires no persisted token, local session or account replica in the wiki database.

This replaces the earlier separate wiki-session direction and its associated
client secret, code exchange, independent exit and 90-day renewal/storage policies.
Native bearer/session contracts and other client installations retain their scope.
The user accepted the [narrow validation interface](contracts/web-wiki-session.md#accepted-current-session-check)
with "отлично" on 2026-10-12. On 2026-10-13 the user accepted
[Cabinet-site logout](contracts/web-wiki-session.md#accepted-cabinet-site-logout)
and explicitly affirmed the [automatic original-page return](contracts/web-wiki-session.md#accepted-browser-entry-and-migration).
Recipient changes, coordinated access cutover and joint deployed proof remain
work; no sibling implementation is authorized by this record.

### Accepted web-wiki environment separation

Decision: the user, 2026-10-13, accepted staging wiki at
`wiki.staging.xuanxue.su` and a distinct staging cookie. The
[environment profile contract](contracts/web-wiki-session.md#accepted-production-and-staging-separation)
owns fixed matching origins, cookie names/domains, signing-key/account isolation,
legacy staging cleanup and independent lifecycle proof. Production credentials
still reach trusted staging hosts; staging ignores them. Recipient implementation,
DNS/HTTPS provisioning and deployed proof remain work.

### Accepted web-wiki sign-in handoff

The earlier separate code-and-PKCE handoff was superseded on 2026-10-12 by the
[shared browser session](contracts/web-wiki-session.md#accepted-shared-browser-session).
Its [former profile](contracts/web-wiki-session-separate-history.md) is historical.

### Accepted web-wiki consumer authentication

The earlier confidential wiki-consumer/code-exchange secret was superseded by the
[shared browser session](contracts/web-wiki-session.md#accepted-shared-browser-session).
The current direction requires Cabinet's authoritative validation of the
presented browser session, with no separate wiki grant-issuance client secret.

### Accepted web-wiki explicit sign-out

The earlier independent wiki exit was superseded by the
[shared browser-session logout](contracts/web-wiki-session.md#accepted-shared-browser-session).
Cabinet and wiki now share this browser session's exit; native clients and other
browser installations are not signed out by that operation. The user accepted
[Cabinet-site logout](contracts/web-wiki-session.md#accepted-cabinet-site-logout)
on 2026-10-13: wiki links to the Cabinet `/logout` page, with no wiki logout API
or proxy. The action uses Cabinet's existing POST, clears the shared browser
cookie and retains Cabinet's completion/error/retry behavior. Implementation
and joint deployed proof remain work.

### Accepted web-wiki lifetime and renewal

The earlier independent wiki 90-day/seven-day lifecycle and predecessor recovery
were superseded by the [shared browser session](contracts/web-wiki-session.md#accepted-shared-browser-session).
Wiki follows Cabinet's existing browser-session lifetime and renewal. This does
not change the separately accepted native credential lifetime/renewal.

### Accepted sign-out scope

Decision: the user, 2026-10-05; shared Cabinet/wiki browser scope amended by the
user on 2026-10-12 at the [shared browser-session contract](contracts/web-wiki-session.md#accepted-shared-browser-session).
Explicit sign-out ends authenticated use in the current client installation.
Cabinet and web wiki share that browser-session exit; other browser installations
and native clients remain signed in;
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
