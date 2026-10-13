# Cabinet session for web wiki

**Status: web-wiki shared-browser-session contract accepted, 2026-10-13.
Recipient implementation, coordinated access cutover and joint deployed proof
remain work. Acceptance is not a claim of deployed capability.**

## Accepted shared browser session

Decision: the user, 2026-10-12, replied "думаю да" to using Cabinet's shared
browser session after the common cookie, lifetime/logout and absence of wiki
reader credential storage were explained.

> Wiki использует общую браузерную сессию Cabinet. Срок входа и выход общие
> для Cabinet и wiki. Wiki не хранит токены или копии аккаунтов читателей в базе.

Cabinet owns user identity, session issuance, verification and current account
state. Daychi owns wiki delivery; its frontend/backend remain separate projects.
Every valid Cabinet-authenticated reader receives the same content. There is no
anonymous web reading, additional reader role or wiki-specific eligibility check.

The production browser namespace is `xuanxue.su` and its subdomains, treated as
one trusted session namespace. Cabinet's existing `session` cookie uses
Domain=xuanxue.su, Secure, HttpOnly, SameSite=Lax and Path=/. This scope includes
all matching subdomains, not only wiki. Issuance, renewal and expiration use the
same domain/path/name. Migration expires the old host-only cookie at Cabinet so
competing same-name values do not remain. A valid existing session can be reissued
at Cabinet; this acceptance adds no mandatory fresh login or new login method.

Protected reader API requests reach `wiki.xuanxue.su`, forwarding to Daychi's
internal backend if its hosting origin differs. Daychi receives the cookie and
asks Cabinet to validate the session and current existing active account before
returning content. Cabinet's signing secret remains at Cabinet. Cookie presence
or a frontend check alone does not authorize delivery, and a cached account result
cannot replace the current validation. Missing/invalid/expired sessions deny
reading; provider failure serves no protected content and is distinguished from
an authentication refusal. The accepted response/error wire is defined below.

Cabinet's existing browser lifetime, renewal and browser logout govern both
websites. Wiki has no separate 90-day credential, renewal lifecycle or independent
authenticated server session. Browser logout affects this shared browser session;
other browser installations and native bearer grants retain their own scope.
Logout follows the [accepted Cabinet-site operation](#accepted-cabinet-site-logout).
Its page and shared-cookie expiration still require recipient implementation.

Daychi holds the presented cookie and validated account result only while handling
the request. Reader authentication needs no credential/user record in the wiki
database: no encrypted token, separate wiki session, reader registration or account
replica. Credentials are not persisted in logs or content records. No wiki code
exchange, PKCE, client secret, stored wiki grant or credential-encryption key is
required for this direction. User-owned content or editorial/native authority is
a separate business scope; this agreement does not authorize deleting its records.

## Compatibility and transition

This acceptance supersedes the former separate wiki handoff, confidential consumer,
independent exit/failure handling, 90-day/seven-day renewal, predecessor recovery
and encrypted server credential storage policies. Their [historical snapshot](web-wiki-session-separate-history.md)
retains provenance. The accepted native account-session protocol is unchanged.

The web access transition still closes anonymous reader delivery across exposed
origins, direct paths and controlled delivery caches. New no-store headers alone
do not remove old public cache entries. Static login/application assets may be
public when they contain no protected content. Native private invitation/content
and owner/import/Knowledge authority retain their existing scope and cannot be
used as alternate web-reader authentication. The breaking anonymous-access change
remains coordinated through original issue 9; this acceptance publishes no issue
assignment and changes no recipient source or deployment.

## Browser operations and proof

### Accepted browser entry and migration

Decision: the user, 2026-10-13, explicitly accepted "Автоматически открывать
исходную страницу wiki после входа в Cabinet. - да", clarifying the immediately
preceding refusal. This is the operative return decision.

> После входа в Cabinet пользователь автоматически возвращается на исходную
> страницу wiki.

Production sign-in entry is a top-level browser navigation to
`GET https://xuanxue.su/wiki?returnTo=<encoded wiki-relative destination>`.
With an already valid shared cookie, normal wiki reads use the accepted session
check directly; they need no entry navigation. The entry is used when sign-in is
initiated, including migration of a still-valid legacy Cabinet host-only cookie.
It returns no authorization code or user token in its URL.

`returnTo` is optional, defaults to `/`, and is the only query field. Its decoded
UTF-8 value is at most 1024 bytes and contains a wiki-relative path with optional
query/fragment, starting with one `/`. Duplicate/unknown fields, invalid percent
encoding, absolute/scheme-relative URLs, backslashes and control characters
return 400 without redirecting. Parsing/resolution against the fixed origin
`https://wiki.xuanxue.su` must retain that exact origin. The destination's path,
query and fragment are preserved; it cannot choose a different site.

| Cabinet entry state | Browser outcome |
|---|---|
| Existing valid session and current unblocked account | 303 to the exact wiki destination, after sharing the cookie and expiring the old Cabinet host-only value |
| Missing/invalid/expired session or deleted account | 303 to Cabinet's existing `/login` with an internal return destination of `/wiki?returnTo=...`; ordinary Cabinet sign-in then resumes that entry |
| Blocked account | 403, no redirect back into login |
| Validation/provider failure | 503, no redirect into login and no claim that the session ended |

Cabinet's new login `returnTo` query support accepts this validated internal wiki
entry path and feeds its existing per-tab return mechanism. The login screen and
Telegram/Google/email methods are reused. Resuming `/wiki` is an actual full-page
Cabinet browser request so its cookie headers and outward redirect execute;
client-only route navigation is insufficient for this entry. The explicit wiki journey returns to
its own entry; unrelated/stale native continuation state cannot commandeer it.
Ordinary Cabinet deep links and the native profile retain their existing behavior.
When email sign-in completes in another tab, refocusing/reopening the originating
login tab rechecks Cabinet's session and resumes its retained entry. Return paths
are nonsecret per-tab navigation state, not reader records or credentials in wiki.
If that navigation state cannot be retained, the existing Cabinet home fallback
applies; authentication still succeeds and reopening wiki uses the shared cookie.

The entry's authenticated 303 carries separate Set-Cookie fields: expiration of
`session` with Path=/ and no Domain on the Cabinet host, and the shared `session`
with Domain=xuanxue.su and the accepted Secure/HttpOnly/Lax/Path=/ flags. Both apply
before the redirect. Before the existing renewal threshold, the same signed token
and original expiry are retained, with remaining Max-Age; eligible rolling renewal
uses Cabinet's current policy. Sharing itself does not start a new 90-day clock.
Login/renewal/logout issuance must not recreate a legacy host-only credential
after this migration. Entry and login-continuation responses use no-store.

Common entry proof covers legacy-session reuse without fresh sign-in, existing
login methods, original destination/query/fragment, malformed destinations,
native/ordinary return compatibility, another-tab email completion, per-tab
isolation/fallback, both cookie fields before redirect and preserved/renewed expiry.
This entry routing implements the accepted return decision. Recipient
implementation and deployed proof remain work.

### Accepted Cabinet-site logout

Decision: the user, 2026-10-13, replied "хорошо" to the wiki navigation link to
Cabinet's `/logout` page, keeping the logout action and existing POST at Cabinet.

Logout belongs to the Cabinet website. Wiki provides no logout API, proxy,
cross-origin POST or local authenticated-session exit. It offers a navigation
link to `https://xuanxue.su/logout`, a Cabinet page exposing its existing logout
action. GET loads the page; the user's logout action on Cabinet invokes its
existing `POST /api/auth/logout` with Cabinet's existing mutation binding. The
page is an addition, not an already verified source capability. No GET link is
defined to invoke the POST API directly or mutate the session on page load.

Cabinet's confirmed 204 expires the shared session cookie with Domain=xuanxue.su,
Path=/, Secure, HttpOnly, SameSite=Lax and Max-Age=0; it also expires any legacy
Cabinet host-only value at that same origin. The operation remains usable with
an absent/expired session. The Cabinet website owns completion/error/retry
behavior; failure or a lost response is not reported as confirmed logout. An
idempotent retry can clear cookies even if the previous request already succeeded.
No wiki endpoint, credential queue, separate local-session invalidation or
mandatory return to wiki is required. The normal Cabinet post-logout destination
is its login page. Other browser installations and native bearer grants remain
unaffected. Wiki loses authentication on its next protected request and removes
protected reader content then; cross-tab UI notification remains project-owned.
The accepted shared-cookie response ordering remains unchanged.

Logout proof covers Cabinet-site logout reached directly or through wiki navigation,
missing/expired session logout, no wiki logout endpoint, no mutation on the
logout page GET, existing Cabinet mutation binding, lost-response retry and
provider failure. The earlier simulated wiki logout proxy is not implementation
evidence or a requirement of this accepted logout scope. The page/expiration
implementation and deployed joint proof are not established by acceptance.

### Accepted current-session check

Decision: the user, 2026-10-12, replied "отлично" to the proposed one-endpoint
interface, its response meanings and relaying Cabinet's renewed cookie.

Daychi checks each protected reader request using exactly
`GET https://xuanxue.su/api/auth/session` over HTTPS, with
`Cookie: session=<the value presented to wiki>`. It forwards only the session
cookie, not the complete browser Cookie header. There is no query, request body,
Bearer credential, client secret or account-ID input. A missing session is refused
locally by Daychi without a provider call. Ambiguous duplicate session values are
refused; neither participant chooses a first/last value for this interface.

Illustrative request; the placeholder is the actual signed cookie value, not a
new token type:

```http
GET /api/auth/session HTTP/1.1
Host: xuanxue.su
Cookie: session=<existing browser-session value>
```

Success without rolling renewal:

```http
HTTP/1.1 204 No Content
Cache-Control: no-store
```

Cabinet uses its existing browser AuthGuard verification/current-account rules,
without a wiki role or eligibility check. The endpoint does not call the full
self-profile mapper or return account/role/contact data. It is not a new session
issuer or alternate account authority.

| Cabinet response | Meaning and Daychi reader outcome |
|---|---|
| 204, empty body | Session is valid and its current account exists and is not blocked; Daychi may deliver the requested protected content |
| 401 | Missing, malformed, invalid-signature or expired session, or deleted account; Daychi refuses the read with 401 and permits the existing Cabinet sign-in path |
| 403 | Current account is blocked; Daychi refuses the read with 403; no additional wiki eligibility is implied |
| 429 | Provider rate limit; Daychi returns temporary unavailability (503) and serves no protected content |
| 5xx, transport/TLS failure, timeout, redirect or any unexpected status/body | Daychi returns temporary unavailability (503) and serves no protected content; it does not classify the reader as signed out |

All check responses use `Cache-Control: no-store`. Daychi follows no redirects,
uses a total five-second provider deadline and does not automatically retry this
check within the reader request. Failure/refusal bodies are not part of the shared
interface and are not copied into the reader response. Only an empty 204 authorizes
content; a 200 profile/HTML body is not a successful check. Failure/refusal does
not expire or replace the shared cookie, so a late refusal cannot delete a newer
valid browser session. There is no positive authorization cache or persisted
reader state; the next reader request rechecks current Cabinet authority.

The endpoint retains Cabinet's existing rolling-cookie renewal. On successful
validation Cabinet may supply the renewed `session` via Set-Cookie, using the
accepted shared Domain/Path/Secure/HttpOnly/SameSite attributes. Daychi forwards
that session Set-Cookie to the browser with its reader response; unrelated cookies
are not relayed. Any session Set-Cookie emitted by this operation is the accepted
shared renewal value; Cabinet host-only session expiration is not emitted by this
operation. Legacy-cookie expiration belongs to Cabinet's browser migration,
login/renewal and logout responses. Invalid renewal-cookie attributes are an
integration failure,
not permission to issue a local replacement. A separate wiki renewal request,
expiry calculation or stored credential is unnecessary. Normal browser last-response
ordering remains Cabinet's shared-session behavior; this check adds no independent
wiki-grant invalidation or stronger logout-race guarantee.

Protected wiki API replies also use no-store. Content DTOs and Daychi's reader
error representation remain its owned API; the success/refusal/unavailability
status meanings above are shared. Current Cabinet browser limits distinguish
verified sessions from unauthenticated IP traffic; the implementation and common
proof must preserve usable multi-reader checks behind one Daychi backend rather
than importing the native IP-only lifecycle budget.

Common proof covers valid/missing/forged/expired cookie, deleted/blocked/unblocked
account, duplicate cookie, empty 204 versus unexpected 200/redirect, provider
429/5xx/deadline failure, original-age renewal boundary and renewed shared cookie
reaching the browser without Cabinet-host legacy-expiration headers in the check,
no user-data/credential persistence, multiple readers behind
one backend and anonymous reader paths. Both recipients use this same definition.
This interface is accepted; no endpoint implementation or deployed joint proof
is established by that acceptance.

The [web sign-in decision](../questions/done/q-0002.0008.0001.0001.0001-how-should-web-wiki-reuse-an-existing-cabinet-sign-in.md)
holds provenance and bounded source/browser evidence. Shared session, entry/
migration/return routing, Cabinet-site logout, validation request/response,
refusal/failure meanings and renewal-cookie relay are accepted above. Recipient
assignments and coordinated access cutover remain separate work; none is created
or published by this acceptance.

Browser cookie delivery was executed in an isolated Chrome 154.0.8037.99 context
with reserved HTTPS fixtures and a simulated reader endpoint. The
[scoped evidence](../questions/done/q-0002.0008.0001.0001.0001-how-should-web-wiki-reuse-an-existing-cabinet-sign-in.md#browser-delivery-evidence)
establishes shared delivery and expiration, not production Cabinet/Daychi proof.
Joint proof still needs actual issuance/migration, renewal, current account and
expiry/refusal/failure validation, logout from either site, both delivery paths
and closure of anonymous bypasses, including controlled caches. Source versions,
the agreed interface and the deployed configuration must match that proof.

## Superseded policy references

### Accepted renewal recovery policy

Superseded by the shared browser session above. The earlier separate-grant
[recovery policy](web-wiki-session-separate-history.md#accepted-renewal-recovery-policy)
is historical and is not required for wiki implementation.

### Accepted credential storage protection

Superseded for web-reader credentials: no reader credential is stored by wiki.
The earlier [storage policy](web-wiki-session-separate-history.md#accepted-credential-storage-protection)
is historical; it does not require a wiki credential database or encryption key.

### Accepted local sign-out and failure policy

Superseded by Cabinet's common browser-session logout. The earlier independent
[wiki exit policy](web-wiki-session-separate-history.md#accepted-local-sign-out-and-failure-policy)
is historical; it does not establish an independent wiki session or exit marker.
