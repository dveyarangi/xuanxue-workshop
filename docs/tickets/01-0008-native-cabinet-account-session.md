# Native Cabinet account session

- **Status:** In progress (amended assignments published; recipient implementation and proof pending)
- **Type:** HITL
- **Responsible contributor:** Workshop agent under its operator; Cabinet and Daychi agents own their recipient contributions
- **Answers:** [q-0002.0008.0001.0002](../questions/q-0002.0008.0001.0002-how-will-native-daychi-maintain-a-cabinet-account-session-without-replacing-its-content-access.md)
- **Outcome:** Native Daychi signs in through Cabinet, securely restores and renews its session, reads the full current self-profile and signs out of that installation, with joint native proof and existing web/content behavior retained.

## Parent

The credential contribution in the [accepted migration delta](../migration-changes.md#changes-derived-from-accepted-contracts),
within the [first-stage scope](../stage-1.md). The user approved this one-outcome
breakdown and minting on 2026-10-06. Its
[post-impact assessment](../questions/q-0002.0002.0002-which-workshop-outcomes-should-the-remaining-reconciliation-pass-deliver.md#impact)
recommends a complete native account-session path separated from the broader migration.

The existing [credential agreement](../boundaries.md#accepted-content-admission),
[agreed native acquisition](../contracts/native-account-session.md#accepted-native-credential-acquisition)
and [sign-out scope](../boundaries.md#accepted-sign-out-scope) govern the result.
Cabinet remains the provider, account data owner and issuance/validation authority;
native Daychi is the consumer. Both projects retain their own operators and internal
design within accepted shared and security decisions. Workshop owns security
principles and protocol selection under
[Security authority](../agent-contract.md#security-authority).

## What to build

Implement the [accepted native account-session profile](../contracts/native-account-session.md)
through Cabinet's provider and Daychi's native consumer. Cabinet supplies browser
authorization, atomic code/PKCE exchange, bearer validation, full web-equivalent
self-profile, renewal and grant-wide revocation. Daychi supplies the registered
native callback, secure persistence/restoration, temporary-failure recovery and
installation-scoped logout. Valid browser sessions return automatically; necessary
sign-in has no extra Cabinet confirmation. The accepted impersonation risk remains
documented. Existing Cabinet web and Daychi invitation/content/schedule/reminder
behavior remain supported.

The user accepted the complete technical protocol on 2026-10-09 with "принимаем",
including code lifetime 60 seconds after issuance and attempt lifetime 900 seconds.
No shared wire choice remains for recipients to settle independently. This adds
no account-switching or profile-edit workflow and no phone field. The same Cabinet
account data and effective-role meanings apply to the full native self-profile.
Unified Daychi content admission remains a separate contract contribution.
The user accepted the current web `homeHiddenTiles` field on 2026-10-10.
Its required normalized value and N01 parity fixtures are defined in the same
native profile; no home-tile UI or preference editing/synchronization is added.
On 2026-10-10 the user accepted
[native credential protection](../contracts/native-account-session.md#accepted-native-credential-protection):
random 32-byte bearer credentials and SHA-256 hash-only storage. The user also
accepted database-backed pending authorization, browser binding, a fixed
900-second server deadline and atomic single-use completion, recorded in
[pending browser authorization protection](../contracts/native-account-session.md#accepted-pending-browser-authorization-protection).
The user subsequently accepted
[`/login/native` continuation](../contracts/native-account-session.md#accepted-native-browser-continuation-route).
All three relayed security/continuation choices are settled, document-verified and
published in the amended assignments. The settled public wire and earlier
product decisions remain binding.

The two recipient assignments are published against accepted Workshop revision
`3c98d4a5201710f8f777183dd7b61caefe47e2d5`:
[cabinet-native-account-session #7](https://github.com/dveyarangi/xuanxue-workshop/issues/7)
and [daychi-native-account-session #8](https://github.com/dveyarangi/xuanxue-workshop/issues/8).
Cabinet and Daychi implement and release under their own
operators; Workshop verifies the joint outcome. Acceptance of this contract is
not provider/client implementation, deployment or native proof.

## Acceptance criteria — delivery

- [x] Workshop settles native-token protection, pending-login protection and continuation.
- [x] Workshop verifies the full amended contract and both recipient assignments,
  including security authority and fresh independent recipient reconstruction.
- [x] Workshop publishes one updated immutable authority in both original recipient
  issues, with contract bytes, issue bodies, labels and dependency links read back.
- [x] Both recipient assignments cite the same accessible immutable accepted
  contract and common conformance cases, with their original issue channels recorded.
- [ ] Cabinet implements issuance, account read, renewal, revocation, errors and
  web compatibility; provider evidence covers its N01–N17 obligations.
- [ ] Daychi implements native handoff, full self-profile, secure persistence,
  restoration, recovery and local exit; client evidence covers its N01–N17 obligations.
- [ ] Joint N01/N11/N15/N16/N17 proof uses a real native build and a conforming
  reachable Cabinet provider, with controlled accounts, issuer and exact revisions.
  One supported platform supplies joint proof; both iOS/Android configurations
  and client checks are covered.
- [ ] /verify confirms the delivered contract behavior and retained Cabinet web,
  Daychi invitation/content and ordinary schedule/reminder behavior. No native
  proof or runtime acceptance is inferred from the contract's acceptance.

## Acceptance criteria — alignment exit

- [x] The user has accepted the complete native-session boundary contract, with
  authority, scope, operations, data shapes, credential lifecycle, access, failures,
  effects and compatibility settled; inapplicable dimensions have explicit reasons.
- [x] Common conformance outcomes cover successful sign-in/account read, restart
  restoration, expiry/renewal, current-user refusal, temporary failure and recovery,
  installation-scoped sign-out, cancelled/mismatched/replayed handoffs and interrupted
  persistence; existing web, native invitation and content-access paths remain supported.
- [x] Provider/client actions and joint native-runtime proof cover the same contract;
  recipient execution and integration dependencies are stated for their own activities.
- [x] Accepted decisions are in their authoritative home; this same ticket is rewritten
  with implementation acceptance criteria retaining the approved native proof and regressions.
- [x] /verify confirms the alignment result, contract completeness, ownership,
  compatibility, source references and the implementation-stage rewrite.

## Activity dependencies

Contract preparation/alignment can start without public-provider correction,
public-pilot native proof or Daychi installation. There is no dependency on
[cabinet-daychi-public-schedule-connection](./01-0007-cabinet-daychi-public-schedule-connection.md)
for this activity; existing queue order is preserved.

Implementation publication requires settled definitions, common cases and an
accessible immutable contract authority. Recipient implementation proceeds under
its operator; Workshop readiness and installation acceptance do not gate it.
Joint native proof additionally requires a reachable conforming auth provider,
controlled test account and actual native runtime, established by current evidence.

## Evidence baseline

The [refreshed source check](../current-system.md#native-account-session-source--2026-10-08)
records Cabinet `868a4edb09926a950b78e8daa3ce495c6e8e256e` and Daychi
`e1ab559c8d5db3dbd7db95aa7400941381ada12a`. Its linked primary sources own the
observations; no native auth runtime or deployment is claimed.
The [2026-10-10 scoped comparison](../current-system.md#assignment-and-native-profile-recheck--2026-10-10)
uses Cabinet `fee65f3b8004d4ecac6c2d3da668cf966be0d0f5` and Daychi
`0a3c824c1586eb7b3ca16ca0b3a365539076b025`. It retains unchanged auth/native
observations and identifies the web hidden-home-tile field now included in the
accepted native definition.

## Technical preparation — 2026-10-08

The user authorized technical preparation on 2026-10-08. The
[proposed shared profile](../contracts/native-account-session.md) specifies
browser authorization, PKCE/callback binding, code exchange, account read,
renewal, revocation, local persistence/failure recovery and common cases N01–N17.
The [Cabinet draft assignment](../assignments/native-session-cabinet.draft.md)
and [Daychi draft assignment](../assignments/native-session-daychi.draft.md)
derive their actions from that same proposal. These are reviewable preparation,
not published implementation assignments. The lifecycle and local sign-out decisions
and acquisition reaffirmation accept those parts, not the complete wire profile.

### Impact

Native account access crosses Cabinet issuance/account ownership and Daychi
browser handoff, secure persistence and restoration. Revocation requires Cabinet
to distinguish individual native grants while retaining web behavior; a header
substitution alone cannot meet installation-scoped sign-out.

### Hidden edges

A lost successful exchange consumes the code; recovery needs a fresh browser
attempt. A lost renewal response or failed local write must preserve a usable
predecessor. Offline local logout cannot establish server revocation. Callback
delivery on cold start, cancellation and issuer mixups affect session integrity.

### Leave alone

Content admission, legacy content credentials, account/reminder synchronization,
ordinary local choices/reminders, browser cookie policy and the public pilot.
No device fingerprint, gateway, background polling or backend retirement is added.

### Recommendation

The user accepted the native credential lifetime/renewal policy on 2026-10-08.
Its durable home is
[accepted credential lifetime and renewal](../contracts/native-account-session.md#accepted-credential-lifetime-and-renewal).
The decision includes predecessor validity for interrupted-renewal recovery and
the stated copied-bearer tradeoff. This policy is no longer a pending choice.

The same day's [acquisition reaffirmation](../contracts/native-account-session.md#accepted-native-credential-acquisition)
holds the browser/code-and-PKCE method fixed. The user also accepted
[local sign-out and failure policy](../contracts/native-account-session.md#accepted-local-sign-out-and-failure-policy):
immediate local exit, bounded best-effort remote revocation, no later token retry
queue and explicit incomplete exit if local deletion fails. Their provenance lives
in those contract sections. The user subsequently accepted
[account-block recovery](../contracts/native-account-session.md#accepted-account-block-recovery):
retain the credential while disabling account use; a successful authoritative
check after unblock restores access if the credential remains valid. The user also
accepted [the registered callback](../contracts/native-account-session.md#accepted-registered-callback)
`su.xuanxue.daychi:/oauth/cabinet`, with invitation compatibility and the stated
scheme-collision tradeoff. Exact endpoint/DTO/query definitions were accepted
with the complete technical protocol on 2026-10-09.
On 2026-10-09 the user accepted
[interrupted exchange recovery](../contracts/native-account-session.md#accepted-interrupted-code-exchange-recovery):
after a dispatched exchange without durable installation of the new credential,
start a fresh browser attempt while preserving any prior usable session.
Normal restoration applies if the new credential was durably installed.

The same day's acceptance of proposal items 3, 5 and 6 landed in
[session isolation and revocation guarantees](../contracts/native-account-session.md#accepted-session-isolation-and-revocation-guarantees),
[failure categories](../contracts/native-account-session.md#accepted-failure-categories)
and [joint verification scope](../contracts/native-account-session.md#accepted-joint-verification-scope).
These accept independent client sessions, grant-wide revocation including renewal
races, invalid/blocked/temporary distinctions, and real native proof on one platform
with configuration/client checks on both. Exact wire values were subsequently
accepted with the complete technical protocol on 2026-10-09.

The user challenged the extra Continue click, the omission of the bearer and
current content consumers from the account-payload explanation, and an unproven
account-switching story. [Current consumer evidence](../current-system.md#native-consumer-needs--2026-10-09)
records protected wiki/Zoom consumers and the accepted target bearer transport
to both backends. The account-session slice does not complete the admission bridge.
The proposed previous-grant cleanup for in-place replacement was withdrawn as a
requirement; no new account-switching UX is approved. Existing interrupted-acquisition
and secure-write protection remains binding. This slice's separation from the
unified content-admission bridge remains material to complete-profile acceptance.
The user subsequently required the complete web Cabinet self-profile, including
email and roles, rather than the proposed ID/name subset. Its durable home is
[accepted web self-profile parity](../contracts/native-account-session.md#accepted-web-self-profile-parity).
The accepted account response specifies the full checked `MeDto`, including
optional-email omission, linked-key/chat flags and effective roles/student mode;
N01 includes profile-parity cases. Cabinet owns the meanings; no Daychi profile-edit
UX or staff operations are added. The user subsequently excluded phone with
"телефон не надо". The same turn accepted
[automatic browser continuation](../contracts/native-account-session.md#accepted-browser-continuation-without-additional-confirmation)
without any additional Cabinet account/consent/Continue screen, retaining necessary
existing sign-in and all callback/PKCE bindings. The user accepted the
[native client-impersonation risk](../contracts/native-account-session.md#accepted-risk--native-client-impersonation)
and requested its documentation. N01 now covers automatic reuse of a valid browser
session and automatic continuation after necessary sign-in. These decisions do
not themselves approve the complete wire profile or establish deployed/native
behavior. The user subsequently accepted the complete wire profile with
"принимаем" on 2026-10-09; deployed/native behavior still requires implementation
and proof.

Use code/PKCE acquisition and one revocable native grant with a renewable bearer.
Implement the accepted lifetime/renewal policy through the accepted shared profile,
without adding refresh-token rotation/recovery machinery. Endpoint/DTO/callback-query,
exact revocation wire and other endpoint/DTO/timing values were accepted on 2026-10-09;
publication requires accepted shared meanings and an immutable accessible revision.

### Draft validation

Fresh independent Cabinet and Daychi recipient readers reconstructed their own
obligations from the brief, cited profile and their repository sources. Both found
coverage of all N01–N17 aspects. The Daychi reader found a callback URI ambiguity;
the profile now requires exact raw single-slash URI equality and decoded query
validation, and its affected independent re-read found no remaining substantive
gap. Cabinet's review prompted explicit renewal media/body validation and the
general duration formula. Exchange-dispatch durability and crash inputs make
interruption recovery explicit. These reviews establish draft readability and
compatibility, not implementation, accepted policy or native runtime behavior.

Initial draft checks passed: ticket validator, question validator, rule injection
and mechanism validation. The initial five contract, assignment, ticket and
question files had 33 resolving local links/anchors. Scoped straw-dog review
confirmed the candidate profile/briefs are bound to the open native question;
publication-placeholder references outside the wrappers describe draft state.
`git diff --check` passed. The required harness source comparison still fails
only on the pre-existing `.agents/skills/skill-up/SKILL.md` difference from
`goodwolf-harness@5871845`; its injection/shape checks pass. That unrelated
difference was not changed. No application test suite exists in Workshop;
provider/client checks and actual native proof await implementation.

After lifetime/renewal acceptance, the ticket and question validators passed
again (four ticket records, 29 questions, no diagnostics). Eight affected files
have 61 resolving local links/anchors; proposal wrappers are balanced and the
accepted policy is outside them. Scoped whitespace checks pass. The decision
accepts policy without changing the reviewed proposed operations or case outcomes.

### Complete-profile acceptance and verification — 2026-10-09

The user accepted the remaining technical protocol with "принимаем". The complete
contract is accepted; its proposal wrapper and the paired briefs' proposal
wrappers are removed. The briefs remain unissued drafts awaiting the same
accessible immutable authority. Architecture, boundaries, migration delta,
question summaries and this ticket now distinguish accepted wire from pending
implementation and proof. The existing ticket carries delivery acceptance
criteria; no new ticket split, publication or sibling implementation is claimed.

The required harness comparison passed against announced
`goodwolf-harness@8a512d3` (resolved
`8a512d39f47ec09c1e76750ce82de8aad0c35cfc`), with no source differences or
refusals. Its network-dependent clone required an approved escalation after the
restricted-network attempt failed. Rule injection and mechanism validation
passed with no diagnostics. Ticket validation covered four records and question
validation covered 29 entries, with no diagnostics. The nine scoped documents
have 144 resolving local links/anchors; scoped `git diff --check` passed.

Scoped straw-dog guesses describe accepted lifecycle conditions, explicit gateway
deferral, stable reminder constraints, source evidence or unissued assignment
state; none requires making the accepted native wire provisional again. Earlier
dated validation above records its original baseline and is superseded for the
current alignment result by this pass. There is no application test suite in
Workshop. Provider/client conformance, deployment and actual native proof remain
delivery criteria, not results of document verification.

The user's accompanying question about non-browser login is informational.
Explaining native email-code and passkey alternatives does not replace or reopen
the accepted browser/code-and-PKCE acquisition method.

## Recipient revalidation — 2026-10-10

Fresh independent Cabinet and Daychi readers reconstructed obligations from their
own brief, cited authority and relevant repository sources without Workshop
session history. Ownership, activity dependencies, internal freedom and N01–N17
coverage passed their scoped reading. Both found one publication blocker from
the [new source evidence](../current-system.md#assignment-and-native-profile-recheck--2026-10-10):
current web `MeDto` requires `homeHiddenTiles`, whereas the accepted native
field table, example and explicit N01 inputs omit its definition.

The concrete counterexample is a current web account with
`homeHiddenTiles: ["notice"]`. Projecting only the native table's listed fields
can satisfy that table while failing full-current-web parity. Returning the
additional field leaves the consumer's required-field/enum meaning unspecified
by the shared authority. The accepted full-profile requirement is retained;
its exact field definition and cases need reconciliation before immutable
publication. Reading this preference adds no tile UI, editing or synchronization
scope. The complete acquisition/lifecycle decisions remain accepted.

The user accepted the amendment on 2026-10-10 with "думаю надо добавлять".
Its durable home is the
[accepted self-profile parity](../contracts/native-account-session.md#accepted-web-self-profile-parity).
The contract now includes the current required normalized field, its six keys,
empty meaning and canonical order in the account definition/example, and compares
empty/populated/normalized values in N01. Both recipient briefs identify their
provider/client parity obligations against that same authority. The next action
was the affected recipient re-read and scoped verification; both passed below.
Both briefs still require one accessible immutable authority and direct issue
links; no auth issue has been published. The public-pilot review was handled in
the original assignments and does not gate this preparation.

The readers also identified older proposal/native-wire wording in current-system
and boundaries. The user authorized its repair on 2026-10-10. Current wording now
distinguishes the accepted native profile from its pending implementation/proof
and the separate unresolved content-admission check. Dated source observations
retain their provenance. Existing shared working-tree changes and sibling projects
were preserved.

Scoped record checks passed: four tickets and 29 question entries with no
diagnostics, 55 resolving local links/anchors across the three changed work/evidence
documents, balanced straw-dog wrappers and scoped whitespace validation. The
question validator's lexical-similarity suggestions do not collapse the separately
scoped native-session, content-consolidation and gateway questions. Published
fixture/progress responses were read back against their prepared bodies. These
checks establish record coherence, not accepted profile amendment, application
conformance or native runtime proof.

### Authorized drift repair — 2026-10-10

Scope: the maintained native-state wording in boundaries/current-system, its live
question references and the superseded body of Cabinet's original public-provider
assignment. The user authorized these repairs with "чини дрифт". Boundary summaries
now distinguish accepted public/native definitions from unresolved protected
schedule, reminder synchronization and content-admission integration. The acquisition
heading names its accepted status; all four live inbound references were updated.
Historical session/done records and dated source observations were preserved.

[Cabinet issue 5](https://github.com/dveyarangi/xuanxue-workshop/issues/5) now cites
the accepted `4aec5f8` authority, verified `868a4ed` provider and valid-only
omission/error-log behavior. Its obsolete all-or-error requirement and superseded
provider deviation are removed from the current brief. The published body was read
back exactly; the recipient label and accepted closed state are preserved. Remaining
fixture coordination stays in the original issue, with actual native proof in issue 6.

This is factual reconciliation under A1 and the issue body's current-assignment
requirement. No shared promise changed in that repair. The user's subsequent
acceptance of `homeHiddenTiles` lands separately in the native profile above.
The maintenance clock
reports no due local mechanisms, and declaration/rule-injection checks have no
diagnostics. Built-in mechanisms are outside this recipient's marking authority.

### Hidden-home-tile amendment verified — 2026-10-10

Both independent recipient readers re-read the changed profile/brief and found the
earlier counterexample resolved. Cabinet owns normalized provider parity;
Daychi requires the field/type/keys and proves the same account-read values.
Empty/populated/source-normalization cases match the exact captured Cabinet
definition. No additional shared wire, operation or UI choice was found; unaffected
earlier obligation/dependency coverage remains valid.

The required harness comparison passed against announced `8a512d3`, resolved to
`8a512d39f47ec09c1e76750ce82de8aad0c35cfc`, with no differences or refusals.
Rule injection and mechanism validation passed. Ticket validation covered four
records and question validation 29 entries, with no diagnostics. Nine scoped
documents have 147 resolving local links/anchors; both JSON examples parse,
the account example matches all 15 declared fields and the six tile keys match
Cabinet source. Scoped whitespace checks passed. Straw-dog candidates describe
accepted lifecycle conditions, the phone exclusion and unissued publication/proof
state; none makes the accepted field provisional. No application suite exists
in Workshop, and provider/client implementation or native runtime proof is not
claimed by these document checks.

The recipient pair is ready for an accessible immutable authority and direct
original-issue links. No auth assignment has been issued; the same existing
delivery criteria retain publication, implementation and joint native proof.

## Recipient publication — 2026-10-10

The user authorized sending the prepared commit and publishing both assignments.
Revision `b8ab296e2713580eb4b91155b0c333ea758a74ce` is available in GitHub;
the retrieved contract blob matches the committed file. Cabinet and Daychi source
heads remain `fee65f3b8004d4ecac6c2d3da668cf966be0d0f5` and
`0a3c824c1586eb7b3ca16ca0b3a365539076b025`, so the recipient readings remain
applicable. The published bodies match the reviewed briefs with pinned references
and direct issue links; both recipient labels and open states were read back.
The provider and client implementations, release and joint native proof remain
with their respective operators and these original issues. Publishing does not
complete this ticket or establish native runtime conformance.

## Security amendment — 2026-10-10

The user clarified Workshop's security authority after Cabinet asked about signed
versus random native credentials, pending authorization in a cookie versus the
database, and a `/login/native` resumption page. Visible interoperability alone
did not settle those security choices. The authority decision is recorded in
[Security authority](../agent-contract.md#security-authority); its reasoning and
source observations are in
[coordination evidence](../mechanisms/coordinate.evidence.md#native-recipient-implementation-questions--2026-10-10).

The user accepted the random-token/hash-only choice with "беседер". That decision
is landed in the native profile and local provider brief. The user subsequently
accepted pending-login protection with "принимаем": database-backed validated
transactions, browser binding, a fixed server deadline and single-use completion.
The user then accepted `/login/native` continuation with "хорошо". Workshop's
next action is to verify the amended contract and paired briefs, before publishing
one immutable amended authority through the existing paired issues.
Recipient implementation and joint native proof remain outstanding.

### Continuation URL diagnostic — 2026-10-10

The user asked why the continuation route had not been chosen before the security
authority clarification. The earlier criterion was dependence across Cabinet and
Daychi: Daychi constructs `/auth/native/authorize` and validates its native
callback, but does not construct `/login/native`. The earlier contract fixed
automatic continuation and cross-tab transaction isolation while leaving provider
routing unspecified. A browser-visible route is an interface to the browser;
its visibility alone does not make its exact pathname a shared Cabinet/Daychi
dependency. Deferring that pathname was consistent with project routing ownership.

The error was extending provider ownership of routing to security protocol choice,
and then describing selection of `/login/native` itself as a mandatory consequence
of the new security authority. That clarification requires Workshop to settle
transaction protection and authorization behavior, independently of the path name.
The user has now accepted this concrete route too; it is an explicit choice, not
evidence that all browser-visible paths require Workshop selection.

The independent /discover pass received only the functional native-app/browser
authorization flow, without this repository or decision history. Its material
follows unchanged; it is candidate context, not a verdict about the project.

#### Families

- **OAuth endpoint contract.** Mapping: native app → authorization endpoint → provider interaction → registered native callback. A continuation page is an intermediate provider step unless it also serves as an endpoint independently addressed by a consumer. OAuth’s exact-match requirement concerns the registered callback; it does not establish a continuation page’s pathname. Failure: confusing those addresses creates unnecessary coupling or incorrect redirect validation. **Confidence: high** on the distinction; the particular page’s role remains unknown. [RFC 8252, §§6–8.4](https://www.rfc-editor.org/rfc/rfc8252.html)

- **Public navigation interface.** Mapping: an independently maintained client or sign-in component constructs/configures `https://provider.example/continue?attempt=…`; the provider accepts that navigation and resumes the attempt. The URL’s agreed origin, route and parameter meanings form the interface. Choosing the literal address becomes shared when another component must ship, configure, register or validate that address independently. Failure: a route rename breaks deployed callers; inconsistent attempt identifiers resume the wrong transaction. **Confidence: high**, conditional structural inference.

- **Opaque continuation link.** Mapping: provider creates a continuation URL → browser or sign-in component carries it unchanged → provider resolves it. The shared promise can cover who supplies the link, how it is transported, its validity period and its resulting behavior while leaving pathname selection to the provider. Address changes become shared concerns when outstanding links must survive them. Failure: consumers reconstruct paths, strip parameters, or retain links beyond their promised lifetime. **Confidence: high** for URI opacity; **medium** for applicability without seeing link transport. [W3C Web Architecture, §§2.5, 3.5.1](https://www.w3.org/TR/webarch/)

- **Workflow continuation / capability.** Mapping: paused authorization attempt → URL carrying a reference or bearer authority → resume handler → callback dispatch. Reference and capability variants differ: possession might merely locate an attempt, or might authorize advancing it. The interface centers on attempt binding, replay, expiration and permitted transitions; its exact address matters only where another party relies on it. Failure: replay, cross-attempt substitution, or treating a locator as sufficient authority. **Confidence: medium**; these are conditional design deductions, not properties established by “continuation page.”

#### What the tasking smuggled in

“Two applications” conceals potentially separate native, sign-in, authorization and browser components. “Provider-owned” conflates hosting, route selection and compatibility responsibility. “Resume that attempt” presumes durable correlation. “Registered callback” does not establish that the continuation page itself is registered. “Page” presumes a rendered document where a redirect handler could suffice.

#### Nothing to take

No pathname follows from this shape alone. A browser-visible URL can be internally selected; an opaque URL can still carry shared behavioral obligations. I reject “microservice,” “event bus,” and “plugin interface” as families here: the task provides no service call, event delivery, or extension-registration structure to map them onto.

## Full security-amendment package verification — 2026-10-10

Workshop verified the complete contract and paired assignments against all 13
shared-contract dimensions and the accepted Security authority, rather than only
the three relayed questions. Fresh independent Cabinet and Daychi readers each
used its own prepared issue body, cited frozen authority and own repository,
without Workshop history or the other reader's findings. Both reconstructed the
same shared operations, formats, profile, timing, lifecycle, security, isolation,
failures and N01–N17 outcomes; neither found a semantic publication blocker or
unrelated implementation scope. Local schema/indexes, transaction mechanics,
libraries and presentation remain free within accepted guarantees. The
[independent review record](../../.local/native-security-20261010/independent-review.md)
retains input hashes, source limits and concrete implementation hazards.

The [current source check](../current-system.md#native-security-amendment-source-check--2026-10-10)
establishes Cabinet `f5036604a414f5e509ca3c9a73d5bcaaa72b3961`, unchanged relevant
source since the previous provider baseline, and unchanged public Daychi
`0a3c824c1586eb7b3ca16ca0b3a365539076b025`. The Daychi reader's local checkout is
older and cannot independently repeat that public comparison. Original issues
7 and 8 still contain the earlier `b8ab296` authority and have no comments;
no recipient native implementation report or deployment is inferred.

Required harness comparison passed at `goodwolf-harness@8a512d3`, resolved to
`8a512d39f47ec09c1e76750ce82de8aad0c35cfc`, with no differences or refusals.
Rule injection, mechanism validation, four ticket records and 30 question entries
passed with no diagnostics. Package checks validate resolving local/pinned-target
links, both JSON examples, all 15 account fields, N01–N17, token encoding/durations,
the PKCE control vector and frozen artifacts. The token example was corrected to
the accepted 32-byte/43-character encoding. The
[check result](../../.local/native-security-20261010/package-check.json) records
the final counts. Scoped straw-dog candidates concern accepted lifecycle conditions
and explicit implementation/proof status; they expose no unsettled contract choice.
Workshop has no application suite; recipient checks and actual native proof remain
delivery criteria.

At the verification handoff, document verification was complete and amendment
publication was prepared. Workshop's next action was to commit this reviewed package, make that revision
accessible and update the existing paired issue bodies to the same full SHA.
Commit and push require the user's per-change permission under L3; publication
retains original issue identities, labels and contribution channels. Prepared
[Cabinet issue body](../../.local/native-security-20261010/issue-7.body.md) and
[Daychi issue body](../../.local/native-security-20261010/issue-8.body.md) contain
revision placeholders for that mechanical substitution and are not published.
Recipient implementation and joint native proof remain outstanding.

## Security amendment publication — 2026-10-10

The user authorized commit, push and the prepared original-issue updates with
"поехали". Commit `3c98d4a5201710f8f777183dd7b61caefe47e2d5` was pushed to
`origin/master`. GitHub returned the contract bytes exactly as committed, with
blob `93aed52e5c55fa1310be2c4c2d0c388e6e2f2f5d`. Cabinet source remained
`f5036604a414f5e509ca3c9a73d5bcaaa72b3961` and public Daychi remained
`0a3c824c1586eb7b3ca16ca0b3a365539076b025`; original issues had no intervening
comments or edits before replacement.

Both original issue bodies now pin that full revision. Readback confirmed exact
reviewed text after revision substitution, unchanged titles, recipient labels,
open states and direct counterpart links. The
[publication receipt](../../.local/native-security-20261010/publication-receipt.json)
records the authority and body hashes. Preparation snapshots remain historical
review artifacts; the published bodies contain no revision placeholder.

Current stage: amended assignments published. Cabinet and Daychi agents, under
their respective operators, next implement their assigned provider/client work
and report evidence in the original issues. Implementation can proceed against
the accessible accepted contract; joint proof additionally needs the conforming
provider, controlled account and real native build. Workshop next reviews those
reports against the common cases. Publication establishes no recipient execution,
deployment or native proof, and the delivery ticket remains open.

## Out of scope

- Content-admission replacement and backend retirement: the
  [content-admission agreement](../boundaries.md#accepted-content-admission) and
  [consolidation deferral](../questions/q-0002.0009-should-cabinet-serve-daychi-content.md)
  retain their existing scope and bindings.
- Reminder synchronization and protected schedule cutover remain separate rows
  in the [migration delta](../migration-changes.md#changes-derived-from-accepted-contracts).
- Gateway implementation remains [deferred](../boundaries.md#accepted-gateway-deferral).
- New background polling and native server push remain outside the
  [first-stage scope](../stage-1.md#scope-limits).

## Parent scope addressed

The credential migration foundation for later authenticated schedule and account/reminder
work. The approved eventual result includes native sign-in, restoration, account read,
agreed expiry/renewal, refusal versus temporary failure and recovery, and local sign-out;
actual native proof and Cabinet web/Daychi ordinary-content regressions remain required.
It does not complete the broader migration or the public schedule connection.
