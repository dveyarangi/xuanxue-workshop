# Native account-session contract accepted — 2026-10-10

Session: `01a11a58-894d-7d52-af3b-008b2c32b221`, concluded on 2026-10-10.

## Decisions and their reasoning

The user accepted the complete
[native account-session contract](../contracts/native-account-session.md).
Browser/code-and-PKCE acquisition was already agreed; the user repeatedly
challenged requests to approve it again. The continuation therefore recovered
the accepted acquisition from its durable home and aligned only the remaining
shared choices. Acceptance of the final technical protocol was explicit:
"принимаем" on 2026-10-09.

The accepted lifetime is a 90-day bearer, renewable when older than seven days.
Renewal preserves the predecessor until its own expiry, avoiding a separate
refresh-token rotation and response-recovery mechanism. The copied-bearer renewal
tradeoff is documented. Each new login has its own grant; renewal retains that
grant. Local logout is immediate, with bounded best-effort grant-wide revocation,
no token retry queue, and an explicit incomplete-exit result if secure deletion
fails. Other native grants and browser sessions remain usable. Blocked accounts
retain their credential for authoritative recovery after unblock. A dispatched
initial exchange interrupted before durable credential installation requires a
fresh attempt while preserving any usable predecessor.

The user required "все, что получает веб самого кабинета", including email and
roles, then excluded phone: "телефон не надо". Native account read therefore
returns the full web `MeDto`, with the same optional-field and effective-role
meanings. An ID/name-only projection was rejected. Reading role data does not
grant staff operations. Current Daychi content consumers were checked before
describing what the new credential enables. This account-session slice preserves
legacy content access; the accepted eventual bearer transport to both backends
still needs the separate Cabinet-to-Daychi admission bridge.

The user rejected an extra Cabinet Continue/account-confirmation click and
requested that the hole be documented instead: "убери фрикшн — и просто пометь
эту дыру у нас в доках". A valid browser session now returns automatically;
necessary login also continues automatically after completion. The assistant's
claim that the button prevents app impersonation was corrected after the user
observed that another app could show the same button. A button requires user
action but does not authenticate an app. The accepted custom callback scheme
and public client identifier cannot prove native app identity; attacker-owned
PKCE attempts are a different case from interception of another initiator's
code. The contract owns the accepted risk and exact callback/PKCE protections.

An account-switching story and previous-grant cleanup were withdrawn as invented
scope: neither was established by the current application evidence. Joint proof
requires a real native build on one supported platform, with configuration and
client checks on both iOS and Android. The accepted wire fixes five operations,
DTOs/errors, a 60-second issued-code lifetime and a 900-second local attempt.

The user asked about non-browser alternatives. Native email-code entry, passkeys
and native Google Sign-In were explained as possible additional integrations.
The assistant initially omitted Google from that explanation, then corrected
it: Cabinet already has a Google browser-login implementation, which remains
compatible with the accepted handoff. A native Google SDK path would require
additional client/provider integration. On 2026-10-10 the user said "пока ничего
не меняем". No alternative replaced or reopened the accepted method.

## Work and verification

The contract, paired
[Cabinet brief](../assignments/native-session-cabinet.draft.md) and
[Daychi brief](../assignments/native-session-daychi.draft.md), architecture,
boundaries, migration delta and question summaries were reconciled to full
acceptance. The existing
[01-0008-native-cabinet-account-session](../tickets/01-0008-native-cabinet-account-session.md)
ticket now carries implementation delivery criteria separately from its completed
alignment criteria. No new breakdown or sibling implementation was performed.

The ticket's complete-profile verification records passing required harness,
rule-injection and mechanism checks, four validated ticket records, 29 validated
questions, 144 resolving local links/anchors, scoped whitespace checks and
straw-dog review. These results verify document alignment, not provider/client
implementation, deployment or actual native proof.

Earlier session-entry self-rechecking covered assignment timelines, source/CI
evidence and public runtime. The
[entry-review question](../questions/q-0002.0005.0002-does-ordinary-workshop-session-entry-invoke-and-exercise-assignment-review.md)
retains the limits: an additional 555-test shipped harness suite had one
ownership-fixture failure and two symlink skips; a proposed scoped environment
repair passed all 555 in memory. No unrelated repair or readiness acceptance is
claimed here. The current accepted harness comparison passed separately.

GitHub issues were read on 2026-10-10. No authentication assignments existed;
the prepared pair remained local drafts. The public schedule client
[issue 6](https://github.com/dveyarangi/xuanxue-workshop/issues/6) was open;
issues 1–5 were closed. No tracker writes were performed in this conclusion.

## Open questions and continuation

- [q-0002.0008.0001.0002 — How will native Daychi maintain a Cabinet account session without replacing its content access?](../questions/q-0002.0008.0001.0002-how-will-native-daychi-maintain-a-cabinet-account-session-without-replacing-its-content-access.md):
  the complete contract is accepted and alignment verified. Publication,
  provider/client implementation and joint native proof remain outstanding.
- [q-0002.0008.0001 — How will Daychi clients obtain and present Cabinet credentials?](../questions/q-0002.0008.0001-how-will-daychi-clients-obtain-and-present-cabinet-credentials.md):
  native account acquisition is settled; the separate content-admission bridge
  and wider migration remain open.
- [q-0002.0008.0001.0001 — Which authentication standard should Cabinet and Daychi adopt?](../questions/q-0002.0008.0001.0001-which-authentication-standard-should-cabinet-and-daychi-adopt.md):
  the accepted custom native profile does not establish full OIDC adoption;
  wider interoperability and admission caller trust remain open.
- [q-0002.0005.0002 — Does ordinary Workshop session entry invoke and exercise assignment review?](../questions/q-0002.0005.0002-does-ordinary-workshop-session-entry-invoke-and-exercise-assignment-review.md):
  self-recheck evidence is recorded; unrelated environment repair, independent
  grading and readiness closure are not completed by native-contract acceptance.

The next session resumes the paired authentication assignment preparation under
the existing ticket. Its first step is a fresh independent recipient reading
of the final accepted obligations, reusing unaffected earlier review evidence.
Publication requires the same accessible immutable full Workshop revision in
both briefs and direct dependency links. Current sources/tracker are checked
before writing. No new login decision is required. Live provider availability
and a real native build are integration-proof dependencies, not prerequisites
for preparing or publishing the assignments.

## Working-tree boundary

The native contract, briefs and related acceptance records remain local and
uncommitted. This conclusion adds the session account and question lean/end
updates. Pre-existing shared working-tree changes are preserved. Concluding
does not authorize a commit, publication or another delivery cycle. No new
general principle is proposed by this conclusion.
