# Native content reads using the Cabinet session

## Essential acceptance — 2026-10-21

Decision: the Workshop operator, 2026-10-21: remove everything unnecessary from
acceptance, following the explicit review of required outcomes and excess gates.
The operator reaffirmed preservation of existing implementation and staging;
the purpose is to remove unnecessary ceremony and clear integration closure.
This section governs current acceptance and closure of originals 15/16.

Only protected material and recording delivery require live proof: installed
Daychi in iOS Simulator, any suitable Daychi backend and real Cabinet staging.
Access refusal, revocation, session/account/issuer isolation, temporary-failure
recovery without credential loss, response validation and compatibility use
inspectable source and executed automated tests. No particular backend host,
physical device, Android, TestFlight or production release gates closure.
Ordinary users sharing Daychi's egress must be able to read; this does not
prescribe a per-grant budget, counter algorithm or throughput number.

Technical quotas and exact counter/window, restart, replacement or replica
behavior and exact retry-delay boundaries are not acceptance or closure
requirements.
Existing compatible API values, working protections and useful tests may remain;
no removal or reimplementation in recipient code is assigned. Invalid input
must still cause no unauthorized protected-content delivery.
No performance/stress target or expanded device/environment matrix is added.
Already credited evidence is reused; neither a new report format nor repeating
accepted builds, installation, account proof, CI or synthetic QA gates closure.

**Status: accepted boundary with essential acceptance narrowed 2026-10-21.
Existing implementation is preserved; joint content proof remains work.**

The user reaffirmed the already accepted content-access rule and approved the
per-read validation plan on 2026-10-16 in response
to [one-cabinet-login #11](https://github.com/dveyarangi/xuanxue-workshop/issues/11).
The [existing access decision](../boundaries.md#accepted-content-admission) owns
Cabinet authority and equal content access; this contract completes its native
server-consumer connection. It is a compatible, coexisting addition, not a
retirement of legacy readers or a new content entitlement.

Daychi validates the presented Cabinet native bearer with Cabinet before each protected native content read. A valid current Cabinet session is sufficient; no additional reader role, invitation or material entitlement is required. Refusal denies the read; temporary failure preserves the credential for recovery.

## Authority and scope

Cabinet provides current native credential, grant and account validation and owns
those records. Daychi's retained backend consumes that decision for its protected
native wiki content, including recording links. The native app presents its
existing Cabinet bearer to Daychi through one Authorization header. Daychi owns
its content, API/client integration, internal routing and error text. Knowledge
retains editorial/import ownership and has no implementation action in this slice.

The immutable native wire baseline is the
[full profile at c9c69c3](https://github.com/dveyarangi/xuanxue-workshop/blob/c9c69c3ebb039ca0962de065909542030a4f5c63/docs/contracts/native-account-session.md).
Its acquisition, credential syntax, complete account/session schema, lifetimes,
renewal, revocation and native error wire remain binding. This contract extends
the permitted use of that bearer to Daychi's native content check; it adds no
scope string, token type, service secret, account replica or grant store.

The browser cookie check and browser exposure transition remain governed by the
[web-wiki contract](web-wiki-session.md), independently of this bearer connection.
Owner/import/write operations, meeting/Zoom credentials, schedule and reminders
retain their existing authority. Backend consolidation and gateway work remain deferred.

## Operation and issuer binding

For each protected native Daychi read, use exactly:

```http
GET /api/auth/native/me HTTP/1.1
Host: staging.xuanxue.su
Authorization: Bearer <the credential presented to Daychi>
Accept: application/json
```

The fixed issuer is `https://staging.xuanxue.su` for staging or
`https://xuanxue.su` for production. Daychi configures one matching profile for
each consumer deployment and app configuration. A request, token, account ID,
redirect, content link or forwarded host cannot select or override the issuer.
There is no fallback between issuers. Network traffic is HTTPS with certificate
and hostname verification. Follow no redirects, including same-origin redirects.

The request has no query and no body. Forward exactly one presented native bearer,
not cookies, the complete incoming headers, legacy content credentials or user IDs.
Do not attach a browser cookie, service credential or client secret. Missing,
duplicate, malformed or out-of-profile bearer input refuses locally with 401,
without a Cabinet request. Cookies cannot rescue that refusal. Token syntax and
bounds are those of the pinned native profile; Daychi treats its value as opaque.

One incoming protected read makes at most one Cabinet check. The total deadline
is five seconds across DNS, connection, TLS and response consumption. There is no
automatic retry or hedged request within that read. A later explicit read can
try again, respecting a supplied rate-limit delay.

## Response and downstream result

Cabinet retains `GET me` from the pinned profile: HTTP 200 UTF-8 JSON with the
complete required `account` and `session` fields, reading current credential,
grant and account state. The native profile defines field types, required versus
optional fields, enums, ID syntax and whole-second durations. A success requires
`account.status="active"` and `session.expires_in > 0`; JSON booleans are not
numeric durations. Unknown additive fields may be ignored, never used as authority.
Missing or mistyped required fields, null instead of a required value, unknown
enum values, invalid IDs, negative durations and a blocked success profile are
malformed provider success, not authentication refusal.

Daychi validates the response and discards the profile/session data after the
decision for this read. It neither persists that data nor returns it in content
responses or diagnostics. No local account/role check can grant or deny additional
wiki eligibility. A student with empty roles and a staff account have equal access.

| Cabinet outcome | Daychi protected-read outcome |
|---|---|
| 200 with the valid native response above | Deliver the requested content under Daychi's existing content semantics |
| 401 `invalid_token` | 401 refusal; expiry, deletion and grant revocation remain Cabinet decisions |
| 403 `account_blocked` | 403 refusal; retain the credential for later unblock recovery |
| 429 `rate_limited` | 503 temporary unavailability; retain credential; respect the valid integer `Retry-After` |
| 400, other 4xx, 5xx, TLS/transport failure, five-second deadline, redirect, unexpected status/media type, malformed success or mismatched refusal code | 503 temporary unavailability; retain credential and serve no protected content |

Cabinet refusal bodies/headers follow the pinned native profile. A malformed or
missing failure body cannot become evidence of a valid session; if it does not
match the 401/403/429 codes above, use temporary unavailability. Daychi's content
error body/text is project-owned; it does not relay Cabinet bodies, profile fields,
raw transport errors, cookies or Set-Cookie. Cabinet checks and Daychi protected
content replies use `Cache-Control: no-store`; native checks emit no Set-Cookie.
Neither participant implicitly renews a credential during this read.

For a valid provider 429, Daychi supplies the integer `Retry-After` on its 503.
A missing or invalid provider delay uses 60 seconds for retry scheduling; it is
never an immediate retry. Other temporary failures introduce no mandatory retry
interval. Preserve the native profile's rule: a 401 can clear only the matching
current Cabinet credential, never a newer replacement or the legacy credential.
Blocked and temporarily unavailable results do not sign the user out.

## Capacity and identity

The 21 October operator decision removes the former mandatory 60-successful-
checks-per-grant rolling-60-second budget and all quota counter, credential-
sharing, exact-window, restart, replacement and concurrent-replica acceptance
requirements. The older restart-reset exception is subsumed by this removal.
No new limiter, persistence or distributed counter work is required.

Ordinary authenticated readers sharing Daychi's egress must remain usable.
Cabinet's current working resource protections may remain; they are not a new
shared throughput promise. The refusal/unavailability wire and credential
retention rules above remain compatible, including recoverable provider 429.
No service secret, caller-selected authority or identity trust is introduced.

Account and grant identifiers retain the native profile's scope and continuity.
Daychi does not infer them from the opaque token. This operation validates one
request; it adds no pagination, ordering, calendar or synchronization protocol.

## Consistency, effects and coexistence

There is no positive authorization cache, persisted allow flag or stale-success
fallback. Each new protected read rechecks Cabinet, including after a previous
successful read. A check begun after successful grant revocation must refuse;
blocking/deletion and later unblock/provider recovery are observed on the next
check. A check already in flight may observe the earlier valid state; this adds
no cancellation of content already delivered or guarantee of erasing third-party
recording URLs already learned by a reader. A failed check cannot authorize a
new content response from previously cached authorization or content.

Daychi explicitly selects Cabinet-authenticated native content within its owned
app/API transport. The wire selection within Daychi is its internal design, but
the observable behavior is fixed: a Cabinet bearer never goes to a legacy
credential validator or issuer chosen by token guessing, and a failed Cabinet
check never falls back to legacy/public authorization. Existing legacy native
clients and credentials continue their existing APIs and content formats until
an independently coordinated transition; they are not retired by this contract.
The canonical browser-wiki host still applies its cookie-based reader policy;
the native path cannot bypass it by sending a header to browser reader routes.

The request reads current state only. It issues, renews and revokes no credential,
changes no account/content and creates no reader membership. Retry idempotency,
delivery ordering and content writes therefore add no new cross-project meaning.
Raw bearers, account/profile responses and recording links are not included in
logs, issue reports or conformance artifacts. Synthetic credentials below are
nonsecret test inputs; real account/status/deletion/fixture operations require
their owners' authorization. Operator approval of this contract is not deployment
or permission to modify recipient accounts or fixtures.

## Common conformance outcomes

Both recipients use these cases against the same immutable revision. Cabinet
proves provider access outcomes; Daychi proves downstream behavior and
absence of protected content on every refusal/failure. Project-owned test code
may differ; two local green suites alone do not establish joint acceptance.

| Case | Input or transition | Required common outcome |
|---|---|---|
| C01 | Valid active student with empty roles; valid staff account | Valid native 200; same protected content eligibility, no extra entitlement |
| C02 | Missing, malformed, duplicate or out-of-profile bearer; browser cookie present | Local Daychi 401 without provider call; cookie grants no native access |
| C03 | Unknown/expired credential, deleted account or revoked grant | Provider 401 invalid_token; Daychi 401, no protected fields/recording links |
| C04 | Valid credential for blocked account, then unblock | Provider/Daychi 403 while blocked; same retained credential can succeed after unblock |
| C05 | Valid response followed by completed revocation, then a new read | Earlier success is not cached; new provider/Daychi read refuses |
| C06 | Provider rate refusal with valid or invalid delay | Temporary unavailability, no protected content or credential loss; no immediate retry loop. Exact delay/counter boundary proof is not a closure gate |
| C07 | 500/503, connection/TLS failure, response exceeding five seconds | Daychi 503, no protected content, one attempt; later healthy read can succeed |
| C08 | Redirect, unexpected 204/HTML 200, malformed JSON, invalid/missing required field, bool duration, blocked 200 or mismatched 401/403 error | Daychi 503, no fallback, renewal, cookie relay or credential loss |
| C09 | Ordinary authenticated reads by different users behind one Daychi egress | Both can read; no prescribed numeric quota, grant counter or stress-test threshold |
| C12 | Invalid bearer or caller-supplied account/grant identity | No unauthorized read or caller-selected authority |
| C13 | Staging credential against production-selected consumer, or request-supplied issuer | Only the fixed configured issuer is contacted; unknown credentials refuse; no issuer override or fallback |
| C14 | Credential replaced while earlier read returns 401/503; explicit native sign-out | Late outcome cannot delete replacement/legacy credential; native grant-scoped logout retained |
| C15 | Existing native/owner/import/public content consumers and browser-wiki routes | Existing authority/content behavior retained; native addition cannot bypass browser cookie policy |
| C16 | Account/profile/contact data, cookies and provider errors during every outcome | No profile/credential persistence, downstream leakage, Set-Cookie or sensitive logs |

Joint proof uses real Cabinet staging, any selected Daychi backend and an
identified installed Daychi iOS Simulator build/source mapping under owner
authorization. Its live scope is protected material/recording delivery under the
accepted evidence split below. Executed automated checks cover
next-read refusal after grant revocation, other native/browser sessions remaining
usable, blocked/unblocked recovery, provider failure/recovery without credential
loss, expiry and deletion. No live status, outage, revocation,
aging or deletion fixture is required. Existing accepted N11 evidence can be reused
where its revisions and observations establish the applicable content outcome.

## Accepted acceptance-evidence split — 2026-10-20

Decision: the Workshop operator, 2026-10-20.

Live joint proof for originals 15/16 requires protected material and recording
delivery using Cabinet staging under the accepted runtime below. All remaining
cases, including revocation/next-read refusal, session isolation, block/unblock,
provider failure/recovery, expiry
and deletion, use inspectable source and executed automated
tests; no separate live run is required.

The essential-acceptance section removes quota/counter obligations; other shared
behavior and existing valid evidence remain. This
decision does not establish completed proof.

## Accepted joint-proof runtime — 2026-10-20

Decision: the Workshop operator, 2026-10-20.

Installed Daychi in iOS Simulator is sufficient for current acceptance and closure
of originals 15/16, using any Daychi backend and real Cabinet staging.

No particular Daychi backend hosting environment is required. Physical hardware,
Android and TestFlight delivery do not block acceptance or closure. The live reads
exercise the native content path through the selected Daychi backend and Cabinet
staging; the client/backend/source mapping is reported.

Only protected material and recording delivery require live proof; all remaining
cases use executed automated tests. Existing behavior and accepted evidence remain
binding; this decision does not establish that the actual reads have passed.

Implementation and synthetic proof can proceed against the accessible contract
under each recipient's operator. Actual integrated activation requires provider
access/source/check evidence, Cabinet staging native/account access and a
Daychi client/backend runtime under the accepted scope above; release and
production cutover remain with the recipient owners. Reports return through the
linked contributions in original coordination issue 11.
