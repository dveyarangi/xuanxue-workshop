# Telegram access to Workshop — implementation plan

- **record of** what it intends to become

**Authored:** 2026-10-12
**Last amended:** 2026-10-12

Implements [telegram-workshop-access](../tickets/01-0020-telegram-workshop-access.md).

## Review outcome

The ticket covers the accepted [Telegram behavior](../contracts/telegram-workshop.md):
group-wide access, simple language, evidence-backed answers, operator history,
restart and scoped task/question authority. The user's 2026-10-12 amendment adds
permitted record edits and proof of their result to the acceptance criteria.
One end-to-end ticket remains sufficient; these edits use the same conversation,
evidence and history boundaries.

The
[workflow question](../questions/done/q-0002.0012.0001-which-task-and-question-changes-may-telegram-participants-authorize.md)
is resolved by the user's permission for reasonable, architecture-compatible
task/question changes, recorded in the [authority contract](../contracts/telegram-workshop.md#information-and-authority).
The separate read-only role proposed in the first pass is withdrawn. The current
plan retains a technical qualification stage before live group use: installed-host
enforcement and recovery need executable proof. No bot code, agent rules or runtime
configuration changed during planning. The subsequently authorized local stage is
recorded below; it does not establish full group acceptance.

## Local stage implemented — 2026-10-12

The [local application](../../workshop_bot/README.md) uses a detached Codex decision
call with tools disabled. The caller supplies bounded current local documents and
applicable skills, then validates and applies a proposed exact prose replacement
to one selected live ticket. Structural/completion changes, question-store writes,
full agent lifecycle and external source reads are not implemented in this stage.
These remain required by the complete scope below.

SQLite retains request identity and a prepared before/after record before writing.
The application compares source versions and holds a Windows handle denying
competing writes/deletion while changing the selected ticket. Recovery compares
actual bytes with the journal; an uncertain result never causes a blind repeat.
This is a recoverable single-record operation, not a multi-record transaction.
The local JSON history is the first operator view. At this stage Telegram queue,
conversations and delivery state were unimplemented; the next section records
the subsequently authorized receiver work.

Executed proof and its limitations live in the
[owning question](../questions/q-0002.0012-how-should-telegram-provide-access-to-workshop.md#local-implementation-evidence--2026-10-12).

## First Telegram receiver implemented — 2026-10-12

The user authorized the first group exchange and publication with «разрешаю».
The receiver selects addressed messages from one group before retention, persists
intake and offset together, and continues polling while one worker processes the
queue. A Windows handle excludes another receiver using the same state. Startup
checks the bot identity, group membership, message reception and existing webhook.
It does not change an existing webhook.

Prepared replies and per-part confirmations survive restart. An uncertain send
remains visible without repetition; explicit rate limits get at most three retries
after the server's delay. Sender, source message/topic and delivery outcome remain
in the same SQLite history. Token setup uses local hidden input, outside Codex's
request and environment. The group path calls informational `ask`; selecting a
record for mutation and conversation continuations remain unimplemented.

Local behavior and transport-failure checks are available. Actual bot credentials
and group selection are missing, so stage 2's decisive real group proof remains
outstanding. The [operator setup](../../workshop_bot/README.md#первый-запуск-в-telegram)
is ready for that proof. This does not establish whole-ticket acceptance.

<straw-dog question="q-0002.0012">

## Local application and boundaries

One locally launched Python application receives Telegram updates, retains accepted
requests and calls the installed Codex CLI. Python HTTP, subprocess and SQLite
facilities suffice for the initial candidate. Application code belongs outside
the reusable `.agents/` harness. The Codex terminal provides launch and history access.

| Boundary | Responsibility | Result |
|---|---|---|
| Telegram | Local application selects requests and sends replies | Only addressed requests enter processing; answers retain their original destination |
| Workshop / Codex | Workshop owns information and rules; Codex answers and handles authorized task/question changes | Current architecture constrains edits; group text cannot widen authority to code, contracts or publication |
| Operator history | Local application owns queue, conversations and delivery state | Requests, answers and failures remain inspectable after restart |

Configuration selects the Workshop directory, one group, a local state directory
and the Codex executable. The Telegram token stays with the Telegram component,
outside child environments, command arguments and diagnostic URLs. Codex uses its
own local authentication. Group text cannot select executable paths, permissions
or runtime options.

A local SQLite database owns accepted requests, conversation associations and
delivery state. A readable history export is derived from it for opening in Codex.
State and exports are excluded from Git and separate from project records. No
dashboard, independent project index, vector database or generic multi-bot framework
is needed for the accepted scope.

## Request and answer flow

1. Startup validates configuration, resolves the actual bot identity and checks
   reception conditions. An existing webhook or competing receiver produces a
   diagnosis rather than silent takeover. One process owns the configured state.
2. Long polling continues while the worker handles earlier requests. Group filtering
   precedes retention. Unrelated bodies and nested quoted messages do not enter
   agent context, history or raw diagnostic logs.
3. Selection handles text, captions, mentions, visible and hidden account links,
   and replies to recorded bot answers. Entity slicing respects UTF-16; parsed
   account identity and exact domain/path checks reject lookalikes. Multiple
   references select one request; a bare reference gets an invitation to ask.
4. Accepted intake and the update checkpoint become durable together, before the
   next acknowledgement. Repeated delivery of an event creates no second request.
   Ignored events advance the checkpoint without retaining message bodies.
5. One worker processes durable arrival order. A reply to a known bot answer keeps
   that conversation, even from another person; otherwise a new request starts one.
   Reply association takes precedence over another mention in the same message.
6. Codex receives that conversation and relevant current Workshop sources. Message
   text is data, never shell syntax or runtime configuration. Any resumed Codex
   session uses its recorded identifier, never an arbitrary latest session.
7. A requested record change is assessed against current architecture and the current
   record, then applied only within the granted scope. Applied/refused/uncertain
   results are retained before an answer claims the result. Completed answers are
   saved before sending. Final-answer extraction separates
   plain Telegram text from progress, tool events and operator diagnostics. Sources
   use accessible links; unpublished local evidence is labelled local.
8. Confirmed sends retain returned message IDs. Long answers split safely into
   Telegram-sized parts; every part retains conversation and original reply/topic
   association. A reply to any confirmed part continues the same conversation.

Edited messages, account-link variants, anonymous senders and non-text attachments
need explicit cases in final validation. A limitation that narrows the accepted
“any mention or link” behavior requires alignment before implementation proceeds
on that assumption. Text/caption support does not imply attachment interpretation.

## Agent integration and evidence

The installed CLI supplies agent execution. It works with the existing task and
question records rather than a second authoritative store. Its complete writable
scope is the authorized record operation and necessary bookkeeping, not the entire
checkout. Code, architecture, contracts, instructions, Git publication and external
assignment tools remain outside that scope. A prompt alone is not this boundary.

Two different checks apply. Capability controls constrain which resources and
operations are reachable. The agent evaluates whether the requested meaning has
a clear purpose, agrees with current architecture/ownership, and has the evidence
required by the relevant Workshop skill. A path check does not prove architectural
compatibility. If meaning is unclear the conversation asks for clarification; a
known conflict is explained and left unapplied. No fresh Codex confirmation is
inserted for a change the user has already authorized through this role.

Question metadata and session changes use the existing question-store writer;
ticket changes retain its format and validator. Any explicit checkpoint still
required by a task/question skill is handled in the group within this granted
authority. Code execution of a task is a distinct action outside that authority.

The record-write boundary evaluates the complete effect, including renames, link
repairs and closes, before application. An operation that also requires a contract,
rule, RFC or other out-of-scope write returns its proposed effect for the operator;
it cannot partially apply its allowed portion and leave broken references. Resolved
paths, link traversal and indirect write tools receive the same boundary checks.
The implementation may use an isolated preview for validation, never as a second
source of project truth.

Each change retains a request identifier, affected records, expected pre-change
versions, proposed result, reason and application outcome. The preconditions are
checked at application time; intervening edits cause rereading and reassessment,
not overwrite. Application and recovery need an indivisible operation at the record
boundary or a recoverable recorded operation with explicit partial/uncertain state.
If another writer cannot participate in safe application, the operation stops for
reconciliation rather than assuming that the other writer respects the bot's lock.

Current Workshop material is read for each request; previous answers do not prove
current project status. Relevant GitHub discussions require an explicitly restricted
read path. A domain allowlist alone cannot make authenticated GitHub access read-only.
Unavailable or partial source reads remain visible in answers.

The effective capability boundary covers shell, hooks, connectors, MCP and browser
tools, and excludes unrelated operator files and credentials. Unsupported host
permissions fail startup; a group request cannot trigger automatic elevation.
The local Windows configuration needs real negative tests, not only mocked denials.

The scoped Telegram presentation and authority configuration
belong in authored local rules and their installation path. Product documents
record the resulting behavior; they do not become runtime instructions. A second
copy of Workshop or unrestricted agent access is not selected by this draft.

## Failure and restart

Durable states distinguish waiting, agent processing, prepared answer, sending,
confirmed delivery, processing failure and unconfirmed delivery. The readable
history gives each state a plain-language name, with author, time, complete request,
answer/error and message reference. Private-group links are labelled for members;
where Telegram provides no usable permalink, chat/message identity remains visible.

Restart preserves waiting order and conversations. Interrupted work is reconciled
with its recorded changes before another agent attempt. Proven unapplied work may
restart from durable context; an applied change is not repeated. An uncertain or
partial change remains visible and stops that mutation until reconciled. The next
attempt receives the established change outcome. A prepared answer can send without
regeneration.
An uncertain send is retained for operator inspection and is not blindly retried.
A crash after Telegram accepted the send but before local confirmation has the same
uncertain outcome. Multipart delivery retains per-part confirmation. Exactly-once
delivery across that boundary is not promised.

Definite rejection, rate limiting, timeout and missing reply target have distinct
diagnoses. Retryable failures have bounded retries with server retry delays respected.
A plain failure response is attempted when delivery is possible; its delivery can
also fail and remains visible in history. One failed request does not discard later
queued work. Shutdown preserves state; restart never resets it to hide an error.

## Implementation stages and proof

Предлагаемый порядок: проверить ответы и допустимые правки через Codex → провести первый обмен
в группе → добавить все обращения и продолжения → проверить ошибки и перезапуск
→ провести полный разговор с другим участником и проверить историю.

Each stage advances through one failing behavior test, minimal implementation and
refactoring with tests green. Tests use public application boundaries and observable
history, answers and side effects. External fakes make failures repeatable but do
not substitute for actual Codex or Telegram evidence.

| Stage | Delivered behavior | Decisive proof |
|---|---|---|
| 1. Agent boundary | A real Workshop question and a permitted record change | Actual rule loading; sourced plain answer; allowed task/question edit; architecture-conflicting request refused; code/contract/rule/publication attempts denied |
| 2. First group exchange | Mention → queue → Codex → reply and history | Real group message and response; sender/time/link visible; missing configuration fails clearly |
| 3. Selection and conversations | Links, captions, bare mention, continuations and independent roots | UTF-16 prefix, hidden link, lookalike account/domain, duplicate references; unrelated messages absent; another sender continues; interleaved roots stay separate |
| 4. Recovery | Ordering, deduplication, safe record changes, restart and honest delivery status | Faults around intake, record application and send acknowledgement; intervening operator edit preserved; repeated event/restart cannot repeat an applied change; second launch rejected |
| 5. Human acceptance | Complete real group conversation, record change and operator review | Another participant, simple language, useful sources, visible change history and retained conversations; authority tests on actual Windows host |

Ticket coverage: startup in stage 2; invocation/filtering in 2–3; isolation/order
in 3–4; evidence/authority and permitted edits in 1 and 5; language/history in 2 and 5; restart/failures
in 4; actual Telegram/Codex proof in 5. Final verification covers all criteria,
repository-required checks and a positive count of application tests.

## Rollout and limits

Authority cases for stages 1 and 5:

| Request or failure | Expected result and distinguishing evidence |
|---|---|
| Clarify a ticket's wording without changing its promise | Correct record changes; reason and before/after visible; architecture and rules remain byte-identical |
| Record a question's answer from an existing accepted decision | Question-store operation points to that decision; it does not manufacture a new authority |
| An ambiguous reference to “that task” | Clarification in the same conversation; no record changed |
| Hide a transfer of accepted data ownership inside a ticket edit | Refusal based on the governing architecture/contract, even though the target file is writable |
| Mark unfinished work verified because the requester says to | No false completion mark; the answer identifies the missing evidence |
| Another operator edits the target after the bot reads it | Stale change not applied; new content survives and is reassessed |
| Crash after record application but before answer delivery | Applied outcome recovered; no second record operation; delivery reconciled separately |
| Message asks for code, rule, secret or publication access | Capability boundary denies that action; task/question authority cannot widen it |

There is no previous bot state to migrate. State is versioned; an unsupported schema
fails startup without deleting history. The token/group are required for real group
proof, not local implementation. Bot setup includes privacy-mode configuration and
actual reception proof. Downtime recovery remains bounded by Telegram retention.
Continuous hosting and a complete group archive remain out of scope.

## Impact

New Workshop-owned application boundary, local conversation state and constrained
agent execution and direct changes to existing task/question records. The repository
has no application suite; its verification setup will need the resulting checks.
Presentation and scoped authority need authored local configuration through the
existing installation mechanism. The amended behavior stays in the same ticket.

## Hidden edges

Inherited entry performs writes and assignment review. Authorized question work is
permitted; publication and assignments remain separate. Windows enforcement and
non-shell tools require real proof. Architectural compatibility is a judgment over
evidence, not a path-validation result. Source freshness, record application,
processing checkpoints and delivery acknowledgements are distinct. Secret exclusion applies to logs, exports,
child environments and agent-readable files, not just published configuration.

## Leave alone

Sibling implementations, shared application promises, other operator sessions,
assignment acceptance and other sessions' intervening changes remain protected.
This implementation does not reorder the existing queue. No second
source of project truth or general conversation platform is needed.

## Recommendation

Keep the single end-to-end ticket under the amended authority. Challenge both a
permitted record edit and a refused out-of-scope action with a small real example
before building the Telegram loop. The record application's interrupted and raced
outcomes receive proof alongside message delivery, not after it.
No acceptance criterion is weakened to make the integration appear ready.

</straw-dog>

## Evidence checked on 2026-10-12

- Local `codex-cli 0.159.0` help exposes `exec`, JSON/final output, sandbox selection,
  explicit-session resume and user-config isolation. This was the planning baseline;
  subsequent actual model calls are recorded in the local-stage evidence above.
- [OpenAI non-interactive mode](https://learn.chatgpt.com/docs/non-interactive-mode)
  supports scripted execution and explicit-session continuation.
- [OpenAI permissions](https://learn.chatgpt.com/docs/permissions) documents platform
  enforcement constraints and separate controls for non-shell tool surfaces.
- [Telegram Bot API](https://core.telegram.org/bots/api) defines polling/webhook
  exclusivity, offset acknowledgement, UTF-16 entities, a 4096-character message
  limit and pending-update retention of at most 24 hours.
- [Telegram FAQ](https://core.telegram.org/bots/faq#what-messages-will-my-bot-get)
  describes group privacy filtering; ordinary-mention reception needs explicit setup.
