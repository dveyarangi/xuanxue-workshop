# Superseded separate wiki-session proposal

**Historical snapshot, 2026-10-12. Not the operative web-wiki contract.**
The user subsequently accepted the [shared Cabinet browser session](web-wiki-session.md).
The formerly accepted separate-session policies and unaccepted wire below are
retained for decision provenance. They no longer prescribe web-wiki behavior.
The snapshot is not implementation or deployment evidence.

---

# Cabinet session for web wiki

**Status: web-wiki v1 draft under reconsideration, 2026-10-12; simpler shared-cookie alternative unaccepted.**
Reader access, browser handoff, confidential
consumer authentication, explicit exit, exit failure policy, credential storage
protection, renewal recovery and 90-day/seven-day lifetime are accepted at their linked homes below. The remaining
protocol below is unaccepted. It is not an implementation assignment, published
contract revision or deployed capability. The
[web sign-in question](../questions/done/q-0002.0008.0001.0001.0001-how-should-web-wiki-reuse-an-existing-cabinet-sign-in.md)
holds the profile; remaining wire and application-secret rotation are proposed
below. The conditional browser-account finding below does not establish a
mandatory cookie migration or an additional acceptance blocker.
Workshop owns shared/security choices; Cabinet owns account
and grant authority; Daychi owns web sessions, frontend and content delivery.

The user subsequently asked to replace the separate web mechanism with Cabinet's
existing browser cookie. The [shared-browser-session alternative](../questions/done/q-0002.0008.0001.0001.0001-how-should-web-wiki-reuse-an-existing-cabinet-sign-in.md#simpler-shared-browser-session-alternative--2026-10-12)
uses a domain-scoped Cabinet cookie and current-account validation instead of
separate wiki grant machinery. It changes the accepted independent lifetime/exit
semantics and remains unaccepted. The earlier code/token draft below is retained
as the previous candidate; it is not the only possible architecture or an
implementation prerequisite.

## Held decisions

The durable homes are [reader access](../boundaries.md#accepted-web-wiki-reader-access),
[handoff](../boundaries.md#accepted-web-wiki-sign-in-handoff),
[consumer authentication](../boundaries.md#accepted-web-wiki-consumer-authentication),
[explicit exit](../boundaries.md#accepted-web-wiki-explicit-sign-out),
[lifetime/renewal](../boundaries.md#accepted-web-wiki-lifetime-and-renewal),
[local sign-out failure policy](#accepted-local-sign-out-and-failure-policy) and
[credential storage protection](#accepted-credential-storage-protection) and
[renewal recovery](#accepted-renewal-recovery-policy), all
accepted by the user on 2026-10-12. Every valid Cabinet-authenticated reader has
the same wiki content; no anonymous reading or separate reader eligibility exists.
Wiki has its own cookie session; signing out leaves Cabinet and other clients
signed in. Those choices are fixed while this draft resolves their consequences.

## Proposed registration and common representation


The consumer is exactly `daychi-wiki`; its requested scope is exactly `account:read`.
The protocol identifier is `web-wiki-v1`; no version-selection request parameter
is added. Both ends use the same pinned accepted revision for this identifier.
This scope names current-account validation, not a reader role, staff permission
or content entitlement. A wiki grant is accepted only by the web lifecycle
operations below; native and Cabinet browser operations reject it. Native grants
cannot pass the web operations or create a wiki cookie. The accepted native
profile and its own scope remain unchanged.

Every wiki grant belongs to one configured issuer. A matching client ID alone
does not make a foreign issuer's token valid: session validation rejects it and
revocation ignores it, including when storage is shared. Issuer binding survives
renewal. The existing native/browser profile retains its own accepted semantics.

The production tuple is issuer `https://xuanxue.su`, wiki origin
`https://wiki.xuanxue.su`, callback
`https://wiki.xuanxue.su/auth/cabinet/callback`. Issuers/origins have no trailing
slash or `/api` suffix. Callback matching is exact, with no query, fragment,
userinfo, wildcard or normalization alternatives. Every environment has an
independent registration and secret; production does not accept staging tokens.
This v1 production registration does not define a staging wiki deployment or
infer a staging DNS name. Staging web registration is outside this version's
deployment scope; Cabinet's existing staging/native profile is unchanged.
The isolated conformance tuple is issuer `https://cabinet.test`, wiki origin
`https://wiki.test`, callback `https://wiki.test/auth/cabinet/callback`, with its
own fixture secret. These are controlled fixture addresses, not deployment claims.
Only these exact tuples are supported by this version; a different deployed
tuple is a shared registration change, not an independently chosen callback.

Cabinet and Daychi server POSTs use HTTPS, UTF-8 form encoding and exactly one
`Authorization: Basic ...` header. Its username is `daychi-wiki`, password is the
registered application secret; each is form-encoded before joining with `:` and
base64 encoding, as in [RFC 6749 §2.3.1](https://www.rfc-editor.org/rfc/rfc6749.html#section-2.3.1).
No secret in request bodies, bearer Authorization header, query credential or
Cabinet browser cookie substitutes for this authentication. Claimed client ID is
not authenticated identity. Missing, malformed, duplicate or wrong Basic headers
return `invalid_client`. Provider authentication precedes user-account results.

The proposed secret, code, PKCE verifier, state, Cabinet credential and browser
opaque session IDs each use 32 cryptographically random bytes encoded as
43-character unpadded base64url. S256 is SHA-256 of the ASCII verifier, likewise
base64url encoded. Storage protection follows
[accepted credential storage protection](#accepted-credential-storage-protection).
Grant `session_id` is an opaque, case-sensitive `[A-Za-z0-9_-]{16,128}` string;
Cabinet account `id` is a stable, case-sensitive `[A-Za-z0-9_-]{1,128}` string.
Daychi never decodes credentials or IDs to infer identity or permission.

Form/query names are case sensitive and percent-decoded once as UTF-8. Malformed
encoding, duplicate decoded names, unknown fields, empty values and wrong types
are rejected. Server forms are bounded to 4096 bytes; server POSTs have no query
parameters. JSON responses are UTF-8 `application/json`, `Cache-Control: no-store`
and `Pragma: no-cache`; successful responses have the complete required field
sets below, no nullable fields. Requests cannot substitute a JSON body for form
encoding; content type must be `application/x-www-form-urlencoded`, with omitted
charset or UTF-8. Nonempty query/body inputs to an operation that excludes them,
malformed/oversized forms and wrong media types return 400 `invalid_request`.
Consumers validate required fields/types and
ignore additional response fields. Durations are integer seconds. Server time
uses whole epoch seconds; expiry is exclusive (`now < expires_at`). `expires_at`
is the returned credential's absolute expiry as an integer Unix timestamp in
seconds, not milliseconds; `expires_in=expires_at-now` describes the same
operation snapshot. UTC epoch arithmetic has no calendar/DST adjustments. Account
IDs are unique within an issuer; identity is the pair `(issuer, account.id)`.
Grant IDs are unique within an issuer and retain the issuing consumer/account
through renewal. Dates,
pagination, ordering and content selection do not apply to these session objects.
No authorization URL, callback query, secret, cookie or credential enters logs,
analytics, error reports or persistent browser navigation.

## Proposed browser authorization and code exchange


Daychi durably establishes a browser-bound attempt before handoff. It stores
issuer, callback, state, verifier, safe wiki destination, creation/deadline and
current/cancelled/exchange-dispatched state server-side. An opaque Secure,
HttpOnly, SameSite=Lax host-only binding cookie identifies the browser attempt;
its name starts with `__Host-Http-`, with Secure, HttpOnly, Path=/ and no Domain.
neither the verifier nor Cabinet credential is exposed to frontend JavaScript.
Only one attempt is current per browser binding. Replacement and completed exit
invalidate earlier attempts and late results. The attempt expires 900 seconds
after creation, without extension by sign-in; uncertain/missing context fails
closed. Database cleanup never substitutes for deadline enforcement.

The destination is a relative path/query/fragment within the configured wiki
origin, validated after URL resolution; external origins, userinfo, protocol-
relative URLs, backslashes and control characters are rejected. It is stored at
start, never taken from the callback. The callback ends with a 303 to this safe
destination without code/state/issuer in the resulting URL. Responses carrying
callback information use `Referrer-Policy: no-referrer` and no cache.

`GET /auth/wiki/authorize` accepts exactly `response_type=code`,
`client_id=daychi-wiki`, `redirect_uri=<registered callback>`,
`scope=account:read`, `state=<43-character state>`,
`code_challenge=<43-character S256 digest>` and `code_challenge_method=S256`.
It reuses Cabinet's existing login methods and automatic browser continuation.
Cabinet's internal continuation retains this exact stored transaction, its
opaque browser binding and a nonextending 900-second provider deadline. A login
email completed in another tab resumes the original valid transaction or offers
a fresh attempt; it never selects a different tab's transaction. No consent or
additional confirmation is introduced for successful continuation.

Success redirects with exactly `code`, `state`, `iss`. Code lifetime is 60 seconds
from issuance, single-use, bound to issuer/client/callback/S256/account. Once
client, callback and well-formed state are established, errors redirect with
exactly `error`, `state`, `iss`; allowed errors are `invalid_request`,
`unsupported_response_type`, `invalid_scope`, `access_denied`,
`temporarily_unavailable`, `server_error`. An invalid client/callback/state returns
a Cabinet-local 400 page without redirect. Callback queries have exactly the
success or error field set. Code/state must have their declared 43-character
syntax, issuer must be the exact configured issuer, and errors must be in the
allowlist. Empty/extra/duplicate fields, malformed encoding and callback path/
authority/fragment alternatives are rejected before exchange. Daychi checks origin/path, state, issuer and its
current browser-bound attempt before any exchange; a wrong/expired/late callback
has no credential effect.

`POST /api/auth/wiki/token`, authenticated with Basic, accepts exactly
`grant_type=authorization_code`, `client_id=daychi-wiki`,
`redirect_uri=<registered callback>`, `code`, `code_verifier`. The body client
must match the authenticated client, or return 400 `invalid_request`. Correct
exchange atomically consumes the valid code; only that successful claimant may
issue a grant for the consumer and the still-existing active account.
Wrong bindings do not consume another valid transaction. At most one concurrent
exchange succeeds. Consumption and grant/credential writes need not be one
multi-document transaction: an interrupted exchange after consumption returns
failure or loses its response, and requires a fresh attempt, never replay of the
consumed code. A 200 is sent only after the issued grant/credential are durably
available. Its 200 response is:

```json
{"access_token":"AAECAwQFBgcICQoLDA0ODxAREhMUFRYXGBkaGxwdHh8","token_type":"Bearer","expires_at":1799582400,"expires_in":7776000,"scope":"account:read","session_id":"wikigrant1234567","renew_after":604801}
```

Daychi durably marks an attempt nonretryable before dispatch. A lost exchange
response or restart before durable credential installation requires a fresh
browser attempt; the same code is not resent. A successful credential is validated
using the session operation below, then durably linked to the Cabinet account and
grant before the new wiki cookie is installed or successful sign-in is reported.
Storage failure preserves any prior usable session; a late result cannot install
after replacement/exit. No refresh token, ID Token, account picker or full OIDC
profile is introduced.

## Proposed session validation, renewal and revocation


`POST /api/auth/wiki/session`, authenticated with Basic, accepts exactly the form
field `token=<Cabinet wiki credential>`. It validates credential expiry, expected
consumer, nonrevoked grant and current existing active account. It returns the
current account ID and the same credential when age is at most 604800 seconds;
when age is greater, it renews through the shared core and returns a new credential
for the same grant/account, with another 7776000 seconds from issuance. Combining
validation and eligible renewal is a proposed web adapter, not a change to native
operations. It avoids a separate provider renewal call during a protected read.

The 200 response has exactly the exchange fields plus `account: {"id": "..."}`.
`session_id` remains stable through renewal; a validated account ID cannot change
for the existing grant/local session. `renew_after=max(0, issued_at+604801-now)`;
`expires_at` and `expires_in=expires_at-now` describe the credential returned.
Daychi persists absolute expiry and never creates a later expiry by adding the
duration to a delayed response's receipt time. Daychi must not assume
synchronized Cabinet/Daychi/browser clocks. Cookie Max-Age is
bounded conservatively by the returned remaining duration minus elapsed request
time and one second for whole-second rounding. Local clock uncertainty cannot
extend a session or substitute for provider validation. Account/grant metadata
are coherent within that operation; separate operations need not share a snapshot.
The new credential
example is:

```json
{"account":{"id":"cabinet-account-id"},"access_token":"AAECAwQFBgcICQoLDA0ODxAREhMUFRYXGBkaGxwdHh8","token_type":"Bearer","expires_at":1799582400,"expires_in":7776000,"scope":"account:read","session_id":"wikigrant1234567","renew_after":604801}
```

Lost-response recovery, predecessor validity and concurrency follow the separate
[accepted renewal recovery policy](#accepted-renewal-recovery-policy).

Every protected web read invokes session validation. No positive result is reused
to authorize a later read, and local expiry or cached identity never grants access.
The validity result applies at that operation; it is not a distributed lock through
content delivery or a promise to retract content already returned. Timeouts,
provider failures and malformed success responses supply no content. Rate limits
must account for all readers behind the Daychi backend: authenticated web-client
traffic does not inherit the native/global browser IP-only budget. Cabinet owns
web budget sizing and returns the exact temporary error below when a bound is
exceeded. Unverified claimed client IDs never select a trusted-client budget.
This version defines no throughput or latency SLA. Joint proof records the
provider's configured web budget and exercised multi-reader traffic, including
more than 60 calls/minute behind one backend IP below the configured web budget,
and verifies both valid traffic and explicit over-budget 429 behavior. These are
runtime proof inputs, not extra shared request fields or recipient-selected
protocol meanings. Single-user/native/browser limits remain under their own scope.

`POST /api/auth/wiki/revoke`, authenticated with Basic, accepts exactly
`token=<wiki credential>`, and optional `token_type_hint=access_token`.
It revokes the presented credential's entire wiki grant, including predecessors
and concurrently issued credentials. An expired credential with a retained known
association may revoke its grant. Unknown/already revoked/other-consumer tokens
return the same 200 empty body and cannot revoke another grant. Revocation is
idempotent, cannot target an arbitrary account, and retains its effect for as long
as any associated credential could otherwise be accepted. After acknowledgement,
no concurrent issuance result for that grant is usable.

## Proposed failures and server custody


All server POST failures have exactly `{"error":"<code>"}`. Application
authentication failure is 401 `invalid_client`, with
`WWW-Authenticate: Basic realm="cabinet-wiki"`; it is distinct from reader refusal
and does not erase a reader credential. Malformed forms are 400 `invalid_request`;
unsupported token grant type is 400 `unsupported_grant_type`. Code expiry/replay,
wrong bindings or a deleted/blocked account at exchange are 400 `invalid_grant`.
Session validation returns 401 `invalid_token` for unknown/expired/revoked/wrong-
consumer tokens or deleted accounts, and 403 `account_blocked` for a valid grant
whose current account is blocked. Invalid-token testing precedes account status.
Neither response accepts a Cabinet browser cookie as replacement authority.

429 `rate_limited` includes an integer `Retry-After` of 1–3600 seconds;
503 `temporarily_unavailable` and 500 `server_error` are temporary. Daychi retains
the credential on these failures and on invalid-client, transport or malformed
response failures, and serves no protected content. A blocked account retains its
credential for recovery after unblock; invalid-token removes only the matching
current local credential/session. No failed operation automatically signs the user
out of Cabinet. New sign-in is deliberate while explicit exit remains in force.

Unexpected statuses/error codes, malformed JSON, missing/wrong required fields,
wrong response scope, or account/grant identity changes are integration failures:
retain prior durable state, serve no content and report service failure. A stale
invalid-token response cannot erase a newer/current session. Retries respect
429 Retry-After; no background polling or persistent retry queue is required.

Daychi holds recoverable credentials/verifiers in private server storage, separated
by issuer and from native invitations/owner configuration. Only the server session
holder requires recoverability; Cabinet's credential records are hash-only.
Durable credential installation/renewal precedes reported completion. Local
credential writes never resurrect an invalidated session; failures are explicit
local failures, with no protected content served by that request. Restarts
restore only durable current state, and still validate
with Cabinet before content. Reader cookies are host-only, Secure, HttpOnly,
SameSite=Lax, Path=/ and contain opaque references, not Cabinet credentials.
Reader/binding cookie names start with `__Host-Http-`; deletion uses the same
name, Secure, HttpOnly, Path=/, no Domain and Max-Age=0. Duplicate occurrences of
the expected cookie name are refused rather than selecting a first/last value.
This prevents a sibling subdomain from shadowing those cookies on browsers
enforcing the `__Host-` constraints; supporting browsers must enforce these
constraints and the Secure/HttpOnly flags. Lax permits top-level navigation and
cross-site fixture callbacks; mutations still require exact Origin/custom-header
protection. Exact suffixes remain Daychi's local names and do not collide with
owner cookies. These are proposed web-cookie requirements, not changes to the
existing Cabinet account cookie.
Cookie/session expiry tracks confirmed credential expiry; ordinary requests do
not extend it. Protected-at-rest storage is accepted below; application-secret
rotation follows the proposed lifecycle below, under Workshop security authority.

Daychi owns its local start/callback/status/exit route layout and frontend DTOs.
Same-origin mutation requests require exact configured Origin and a non-simple
custom header; no permissive cross-origin credential access is enabled. Callback
is a distinct browser navigation protected by the attempt binding/state/S256.
Session fixation is prevented by fresh opaque local-session issuance after login.
Raw credentials never enter frontend storage or content DTOs. Protected reader
responses are no-store; a service worker/browser cache supplies no offline
authenticated wiki reads. The exit failure policy is held separately below.

The wiki reader cookie has no authority on Daychi's legacy access-session,
invitation, standalone Zoom, owner/admin or import routes. Reusing the existing
authorizer seam is scoped to wiki-reader delivery; the general Daychi bearer
authorizer is not replaced by a broadly valid wiki cookie. Material/article DTO
and recording/source protections retain their existing contract.

Late HTTP responses can still affect the browser cookie jar; JavaScript cannot
conditionally undo a HttpOnly Set-Cookie header. The required guarantee is that
such a reference cannot recreate/use an invalidated server session, never that
all late cookie writes are physically prevented. A stale dead reference supplies
no content and may require another handoff. Delayed read/renewal/exit/callback
responses are included in proof; server identity checks and exit-intent suppression
apply before any restored UI or new content read.

## Conditional browser-account protection finding

If an attacker controls a sibling HTTPS origin, the existing Cabinet cookie
name/selection can let a sibling-domain cookie select another valid account for
the handoff. That deployment premise has not been established. Code/state/
S256 and backend client authentication preserve that selected account; they do
not determine which same-name browser cookie Cabinet should trust.
The source counterexample and unaccepted hardening option are held in
[browser-account protection](../questions/done/q-0002.0008.0001.0001.0001.0008-how-should-cabinet-protect-the-browser-account-inherited-by-wiki.md).
The earlier mandatory-migration conclusion is withdrawn. Cabinet can reuse its
existing cookie to authenticate the browser for this handoff; wiki still receives
the code and establishes its own cookie. The previously accepted reader, lifetime,
renewal, storage and wiki-exit policies are unchanged. Browser-cookie hardening
remains a separate unaccepted option, not a prerequisite established by this review.

## Proposed application-secret lifecycle


Cabinet and Daychi operators provision the same confidential-client secret for
the exact environment tuple through their deployment secret configuration.
One secret is active per tuple; raw values are exchanged privately and are absent
from Workshop records, issues, source, images, logs and browser storage. Cabinet
verifies the client secret before disclosing reader/account outcomes; no arbitrary
account or token-inspection operation is added by possession of this secret.

This v1 has no dual-secret overlap. Rotation replaces Cabinet's registered secret
and Daychi's calling secret through a coordinated operator change. While values
mismatch, provider calls return `invalid_client`; Daychi treats it as service
unavailability to the reader, retains local credentials and serves no content.
It does not report that the reader signed out or erase the session. When both
ends use the new value, existing grants resume validation/renewal without fresh
user login; grants are bound to the consumer, not a secret generation. The
tradeoff is a possible brief interruption during rotation, rather than another
overlap/deadline mechanism. Old secrets are rejected after provider replacement.

Rotation changes no encryption key, account authority, grant identity or native
registration. Operator rollback restores a consistent pair or keeps protected
reading unavailable; it never opens anonymous access. Revoking compromised user
grants remains separate from replacing the application's secret. Joint proof
includes mismatch, retention, rejection of the replaced secret and recovery with
the matching new pair. This lifecycle is proposed as part of final wire acceptance.

## Accepted renewal recovery policy

Decision: the user, 2026-10-12, replied "хорошо" to predecessor retention and
recovery after a lost renewal response. This accepts the policy below without
accepting the remaining web wire draft.

Renewal keeps the same Cabinet wiki grant and account identity. It issues a new
credential with 90 days from its issuance; the predecessor remains valid only
until its original expiry while the grant/account remain eligible. Its lifetime
is not extended by that renewal. Revoking the grant invalidates every associated
credential, including predecessors and concurrently issued renewal credentials.
No issuance racing with acknowledged revocation may leave a usable credential.

Daychi durably installs the received replacement before reporting renewal complete
or extending local-session/cookie expiry. A lost response, failed durable write or
restart before installation retains the previously stored credential and its
existing expiry. The failed request serves no protected content. A later attempt
may validate and renew using that still-valid stored predecessor. Once it has
expired, it cannot be renewed; a fresh Cabinet handoff is required. Temporary
provider/storage failure never creates a new expiry or an independently valid
local authentication fact.

Concurrent renewal may issue several credentials for one grant; no exactly-once
renewal or recovery of a particular lost token is promised. Daychi serializes
updates to its current local session and discards superseded results. Late results
after exit, cancellation or replacement cannot install a credential, change
identity or recreate a local session. All successful reads/renewals still check
the presented credential, expected consumer, grant and current Cabinet account.

This reuses the existing grant lifecycle and predecessor model; no refresh-token
type or persistent recovery queue is added. The tradeoff is several simultaneously
valid credentials for a grant. Renewal alone does not detect theft. A copied valid
wiki credential plus this application's secret could continue using/renewing
that grant until revoked, expired or refused. The encrypted server custody and
confidential-client authentication remain required; retaining a predecessor does
not relax them or authorize native/browser use of a wiki credential.

Common proof covers a provider-success response lost in transit, failed durable
replacement write, restart before installation, concurrent renewal, original
predecessor expiry, independent account/grant refusal, acknowledged revocation
with an in-flight renewal, and a late response after completed local exit. It
shows recovery without a new login only while the stored predecessor remains
valid, with no false renewal completion. These are accepted outcomes; web
implementation and runtime proof remain pending.

## Accepted credential storage protection

Decision: the user, 2026-10-12, replied "согласен" to hash-only issuer/reference
storage and authenticated encryption of Daychi's recoverable values with a
separate server key. This accepts the protection, failure, key-lifecycle and
restore guarantees below; it does not accept the remaining protocol draft.

Cabinet persists only SHA-256 hashes of the random wiki credentials, authorization
codes and opaque browser bindings, with their grant/transaction associations and
deadlines. It does not need to recover these presented secrets. Daychi likewise
persists only hashes of its opaque reader-session and attempt-cookie references.
This reuses the existing random-token/hash model rather than adding signatures.

Daychi needs to recover the Cabinet credential and pending PKCE verifier. Those
values are encrypted before durable storage using AES-256-GCM through a maintained
cryptographic library. Each encryption uses a unique 96-bit nonce under that key;
the implementation enforces the mode's per-key usage/nonce limits. Authenticated
context binds the encrypted value to its issuer, registered wiki consumer, local record
identity and value kind, preventing transplantation into another session/attempt.
Exact database schema and binary encoding are local Daychi implementation choices.
Raw credentials/verifiers are absent from database files, journals, snapshots and
backups; only the service may decrypt them for the accepted server operations.

Each issuer environment has its own random 256-bit storage key, separate from
the confidential-client secret. Daychi's operator owns it; Cabinet does not need
it. It is supplied from operator-controlled deployment secret configuration,
kept outside the session database/volume and its backups, and absent from source,
container images and logs. The configuration's actual access/injection protection
requires deployment evidence; this choice does not promise protection against
compromise of the running service or its complete secret configuration.
No additional key-management service is required by this decision.

Records identify the encryption key used. A new active key encrypts new writes;
old keys remain available only while retained records require them. Rotation
re-encrypts or discards those records before retiring the old key, with recoverable
keys protected separately from any retained backup ciphertext. Client-secret
rotation is independent; it does not force re-encryption of reader credentials.
Missing keys, authentication-tag/context failures and storage failures supply no
protected content and are explicit local failures, never plaintext fallback or
evidence that the account was deleted. Existing ciphertext is retained for key
recovery; permanent loss requires a new wiki sign-in, not a Cabinet account reset.

Private files/backups retain service-only access. Restoring an older database
backup discards its reader sessions and pending sign-in attempts before serving
requests, so a restore cannot resurrect a session whose local exit was completed.
Ordinary restart keeps durable current sessions and still validates with Cabinet.
These guarantees do not migrate native content credentials or owner sessions.

Proof covers database/journal/backup inspection without plaintext credentials,
hash-only cookie-reference storage, wrong/missing key, modified ciphertext or
context, cross-issuer substitution, restart, key rotation and old-backup restoration.
Reader/account/consumer validation remains required after decryption. Storage
acceptance is separate from acceptance of the remaining wire draft; no key has
been provisioned and no recipient storage implementation is established here.

## Accepted local sign-out and failure policy

Decision: the user, 2026-10-12, replied "принимаем поведение при обрыве связи"
to the proposed immediate suppression, incomplete-exit indication and retried
local cleanup. This accepts the failure policy below, not the remaining wire
draft. It preserves the accepted ordinary exit and independent client sessions.

On explicit exit, wiki immediately stops authenticated reads and renewal, clears
rendered/cached reader content it controls, and disregards pending sign-in/read
responses. It persists a nonsecret sign-out intent when browser storage permits;
all same-origin wiki tabs suppress automatic entry and restored authenticated UI.
This intent carries no reader credential and grants no access. Reload/reopen
respects it before session restoration or content fetches.

Wiki reports local sign-out complete only after the sign-out intent is durably
persisted and Daychi acknowledges durable invalidation of that browser's current
local session and pending sign-in attempts, and sends the session-cookie expiration
response. Backend invalidation is atomic against credential installation/renewal:
late results cannot recreate a usable local session. Other wiki installations,
native grants and Cabinet browser sessions remain intact.

When Daychi is unreachable, cleanup fails, or its acknowledgement is lost, wiki
shows sign-out pending/incomplete and continues suppressing reads and automatic
entry. It retries the idempotent local cleanup when connectivity returns or wiki
reopens, before any session restoration or deliberate new sign-in. It does not
claim that a browser marker has revoked server access. If marker persistence
fails, suppression is guaranteed only in the running frontend; sign-out remains
incomplete even if server cleanup succeeded, because remaining signed out after
restart is unconfirmed. Successful retry establishes both conditions before
reporting completed local exit.

Once local invalidation is durable, Cabinet grant revocation is attempted with
the captured credential within the configured request timeout. Failure of this
remote attempt does not undo completed local exit; remote revocation is confirmed
only by Cabinet acknowledgement. No persistent revocation queue is added. If
local invalidation succeeds but its response is lost, retry still returns a
successful cookie-expiration response. No late callback/response may restore
the completed local session, and a deliberate new sign-in starts a new attempt.

Common proof covers request not delivered, lost success response, failed server
deletion, unavailable Cabinet after successful local deletion, failed browser
marker storage, reload/reopen, two wiki tabs, stale callback/renewal response and
deliberate new sign-in after confirmed cleanup. A copied old cookie is rejected
after acknowledged local cleanup; before acknowledgement that rejection cannot
be asserted. These are acceptance requirements, not executed web runtime evidence.

## Proposed transition and common proof


All reader delivery reachable through the configured web-wiki origin requires the
Cabinet-backed wiki session, including article/semantic/catalog/material/graph/
recent APIs, downloads and direct URLs. Static application assets/login shell may
be public only when they expose no protected text/content. Existing public reader
APIs cannot remain an anonymous bypass, including public reader endpoints exposed
on another backend origin. Native invitation credentials and owner
credentials do not create or replace a web-reader session.

Cutover also closes cached anonymous delivery: Daychi's operator invalidates or
disables shared cached reader responses and retires cached public content assets/
URLs it controls. New no-store headers alone do not invalidate an old fresh
public cache entry. Access checks precede conditional/304 responses, and no shared
cache may serve protected content without the current reader check. Proof primes
the old anonymous paths/cache before cutover, then requests them unauthenticated
and conditionally after cutover through exposed origins and their delivery caches.
Previously downloaded copies/screenshots are not remotely retractable; the
guarantee concerns controlled delivery after cutover.

Closing published anonymous reads is a breaking access migration. Article,
semantic and content DTOs/data remain unchanged; owner imports and Knowledge's
editorial contract retain their authority. Existing native invitation/content
access remains outside this web slice on its existing native API surface; the
web origin must not expose that compatibility path as an alternate reader
authentication route. This scoped exception does not claim global retirement of
every legacy content channel. Daychi owns route/deployment isolation and its proof.
The delivery transition has one shared outcome: Cabinet first supplies the
additive web profile while preserving the existing native/browser contracts. Daychi
then installs and proves the web adapter/reader gate against that provider;
Workshop reviews the joint proof and records the breaking access cutover in
original issue 9. This does not retroactively declare the earlier anonymous-
publication result defective. After cutover, rollback may restore a conforming
protected version or return temporary unavailability; it cannot reopen anonymous
reader APIs. The native private content compatibility exception and owner/import
authority remain explicit through both transition and rollback.
Both implementations may be prepared independently against the same profile and
isolated fixtures; a live conforming provider is required for activating and
proving the production handoff, not for starting recipient implementation.

Final technical acceptance fixes this complete v1 shape, including production
registration and isolated fixtures. An accepted profile must be pinned to an accessible immutable Workshop
revision, with both recipient briefs deriving from it. No assignments are created
by this draft. There is no extra account synchronization, role service, JWT system,
shared subdomain cookie, full OIDC adoption or general token-introspection service.

| Case | Observable outcome |
|---|---|
| W01 Active/no Cabinet browser session; email login in another tab | Existing login reused; automatic continuation and original wiki destination, exact current attempt |
| W02 Wrong state/issuer/callback/S256, extra or duplicate fields, replay/concurrent exchange | No unauthorized credential installation; at most one valid exchange; invalid client/callback never redirects |
| W03 Missing/wrong application secret; valid Cabinet cookie supplied instead | Application rejected independently of reader credentials; no account disclosure |
| W04 Native credential on every web operation and web credential on every native/browser operation | Consumer isolation, including renewal/revocation; other grants/browser remain valid |
| W05 Age 604800/604801; expiry boundary; renewed/predecessor credentials | Exact threshold/90-day durations, no local activity extension; grant-wide revocation |
| W06 Lost exchange/renewal response, failed durable write, restart, concurrent/late response | Fresh attempt for uncertain code exchange; predecessor recovery for renewal; no resurrection |
| W07 Block/unblock, deletion, revocation, provider transport/500/503/429, malformed 200 | Current-account outcomes; no content on failure; retained/discarded credentials and Retry-After as specified |
| W08 All web reader API/direct/public paths without cookie, with invitation/owner cookie, with Cabinet cookie only | No anonymous/alternate web-reader path; authenticated content DTOs preserved |
| W09 CSRF, sibling origin, session fixation, logs, caches and server restart | Same-origin mutation binding; server-only credentials; no protected cache/log exposure; durable restoration still validates |
| W10 Explicit exit, reload/reopen, two tabs, delayed callback/renewal, deliberate entry | Accepted normal suppression and local sign-out failure policy; no premature completion or stale restoration |
| W11 Native/owner/import/Knowledge compatibility and published anonymous route cutover | Existing contracts retain their scope; breaking web-reader access transition explicit |
| W12 Concurrent web readers behind one backend, explicit over-budget traffic; application-secret mismatch/rotation; foreign issuer | Recorded web budget supports multi-reader proof without inheriting native IP-only throttling; 429 honors Retry-After; mismatch retains reader credentials; old secret and foreign tuples rejected |
| W13 Database/journal/backup disclosure, key loss/tampering, context substitution, key rotation and old-backup restore | Accepted storage protection: no recoverable plaintext without the key, explicit failed decryption and no resurrected sessions |
| W14 Sibling-domain/path cookie shadowing and duplicate protected cookie names; protected cookie expiration | Browser cookie origin protection and duplicate refusal; expiration header is valid for the protected name; Cabinet account-cookie migration is decided separately |
| W15 Old public cache primed, cache hit/conditional request after cutover, public content assets | No controlled anonymous delivery bypass, including 304 reuse; no claim to retract already downloaded content |
| W16 Wiki cookie alone on legacy access/Zoom/admin/import; delayed HttpOnly cookie responses | No broader Daychi authority; dead references cannot resurrect/use exited sessions |

These are proposed common outcomes, not executed runtime evidence. Exact
request/response examples above use illustrative random values and IDs; both
success examples use issuance time `2026-10-12T12:00:00Z` and expiry
`2027-01-10T12:00:00Z` to demonstrate 7776000 seconds. Each
recipient supplies version-bound source/check evidence; joint browser/API proof
uses the same pinned profile, the declared production tuple and controlled test
account. Fixture conformance does not claim production runtime proof. Cookie
flags, consumer isolation and public-route closure require joint
proof, not two independent success claims.

Extra response fields are compatible because consumers ignore them after required
validation. New request fields, changed identifiers/semantics or guarantees,
different deployment tuples and access-policy changes require coordinated
revision; strict request validation is not silently relaxed. Article/content/
semantic DTO versions retain their existing contract independently of this
session transport. The web-reader access cutover is explicitly breaking.

## Source basis and draft limits

The [minimum-adaptation investigation](../questions/done/q-0002.0008.0001.0001.0001-how-should-web-wiki-reuse-an-existing-cabinet-sign-in.md#minimal-adaptation-investigation--2026-10-12)
pins Cabinet `67d5cbd0041daa13c6973b657479e45a6716486f` and Daychi
`d2cde6b93ef79734e4de0438ddc2e138698214af`. Its current core supports the proposed
reuse, but no web implementation is verified. Cabinet's existing
[native throttle](https://github.com/gregoryKot/xuanxue-cabinet/blob/67d5cbd0041daa13c6973b657479e45a6716486f/api/src/auth/login-throttle.ts)
limits native requests to 60/minute per IP; its rare native lifecycle workload
cannot establish suitability for server-aggregated wiki reads. The v1 proposal
fixes registration, application-secret lifecycle and proof semantics above;
staging wiki deployment is excluded from this version, and budget sizing is a
provider operating choice with explicit common proof. Actual implementation,
secret/key provisioning, host routing and production joint proof remain work to
be demonstrated by their owners. No source, check or runtime claim in this draft
establishes that the target already operates.
