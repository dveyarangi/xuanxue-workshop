# Telegram access to Workshop — implementation plan

- **record of** what it intends to become

**Authored:** 2026-10-12
**Last amended:** 2026-10-15

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
The initial receiver selected addressed messages from one group before retention, persisted
intake and offset together, and continues polling while one worker processes the
queue. A Windows handle excludes another receiver using the same state. Startup
checks the bot identity, group membership, message reception and existing webhook.
It does not change an existing webhook.

Prepared replies and per-part confirmations survive restart. An uncertain send
remains visible without repetition; explicit rate limits get at most three retries
after the server's delay. Sender, source message/topic and delivery outcome remain
in the same SQLite history. Token setup uses local hidden input, outside Codex's
request and environment. The group path calls informational `ask`; selecting a
record for mutation remained unimplemented; continuation/history support follows below.

Actual credentials and group selection were subsequently configured by the operator.
Live intake and an error reply exposed a source-catalog defect, repaired with a
successful actual Codex answer locally. This does not establish whole-ticket acceptance.

## Whole-group history amendment — 2026-10-12

The user explicitly selected «Всю переписку группы». Received group text/captions
are retained, while only mentions, account links and replies to confirmed bot
answers enter processing. Ordinary discussion is background across conversations;
reply associations identify the active exchange. The source group is filtered
before retention, and nested quoted bodies are not imported as additional history.
Existing SQLite history is extended without replacing records or delivery IDs.
Legacy requests retain independent roots because their old reply links were not captured.

Each call receives a retained snapshot of prior group messages and confirmed bot
reply parts preceding the current message. A 120,000-byte JSON history budget
prioritizes the direct reply target and conversation root, then newest discussion;
omission count is explicit. The complete received journal stays local. Attachment
contents, edited messages, pre-collection history and undelivered messages are not
claimed present. Missing attachment text has a visible marker. Current Workshop
sources are reread, and earlier bot answers do not establish current project state.

## Directed operator messages — 2026-10-15

The accepted amendment adds a Codex-only outgoing path into the configured group.
Impact is confined to local recipient registration, outgoing delivery/journal and
reply context. Project assignments remain in Workshop Issues; the detached group
worker gains no sending tool or recipient-registration authority. No sibling
implementation, dashboard or independent message service is needed.

A send resolves its scope from the Responsible operators table in
`docs/agent-contract.md`, with no local contact-registration command or memory
fallback. It takes a scope, UTF-8 message file and stable request ID, and uses the
documented username as an explicit mention.
Recipient identity and text are frozen in SQLite before the network operation.
Each request attempts delivery once; confirmed, rejected and uncertain results stay
inspectable. Duplicate/concurrent invocations return the existing result and changed
content under the same ID is rejected. A process lost during sending remains
uncertain. The receiver is not restarted or its processing states reset by sending.

Outgoing messages are single posts, at most 4,000 UTF-16 units including the prefix;
longer messages fail before delivery. Confirmed outgoing posts enter group context
and support replies without another mention. The decisive tests cover exact group
and recipient, no duplicate after restart/concurrency, failed or lost acknowledgement,
unknown recipients, escaped-as-text content, UTF-16 size boundaries,
reply continuation and absence of receiver-state changes during sender startup.
Actual group delivery requires a user-provided recipient and a real message need;
local transport tests cannot establish that live outcome.

## Direct Codex conversation and text memory — 2026-10-15

The [memory clarification](../contracts/telegram-workshop.md#bot-memory) replaces the
structured fact store. A normal conversation invokes Codex with the request, group
background, repository location and memory path. Codex reads project files with its
own tools and returns plain final text. It edits `.local/workshop-bot-memory.md`
directly; no memory schema, source-ID protocol or fixed document bundle participates
in this route. The existing selected-ticket local operation remains separate.

A named Codex permission profile grants filesystem reads and only the memory file
write access. Private bot state and the operator's Codex, SSH and AWS credential
directories are denied to tool reads. Network commands, inherited connectors, hooks,
browser and other-agent tools are disabled; approvals are never escalated by a group
request. The installed Windows sandbox requires root read access. Native checks must
prove permitted reads/writes and refused out-of-scope writes/private reads.

Memory is an ordinary mutable document. An interrupted Codex turn may have edited it;
a failed reply is not proof of unchanged memory. The journal prevents automatically
rerunning the same request. The group receiver continues to serialize conversations.

### Impact

The conversation call, prompt, memory storage and outgoing recipient lookup change.
Telegram intake, journal, reply association and delivery recovery retain their contracts.

### Hidden edges

Actual Windows permissions, plain final-text extraction and direct file editing need
real-host evidence; a mocked successful process does not establish these capabilities.
Memory must remain outside the denied private-state directory.

### Leave alone

Sibling projects, architectural write authority and the local ticket application path
are unchanged. Stored conversation/delivery data is not agent memory.

### Recommendation

Use the existing Codex file tools and one Markdown file. Remove the structured-memory
module and contact-registration command; keep ownership in the shared contract.

## Project harness integration — 2026-10-15

The user authorized connecting the existing harness to ordinary bot invocation.
The earlier temporary working directory and zero project-document limit prevented
native project instruction discovery. File readability alone did not prove entry
or skill application. `--ignore-rules` affects command execution policy files,
not `AGENTS.md`; it remains separate from project-instruction discovery.

The conversation now starts at the supplied Workshop root with a 64 KiB project
instruction budget and native skill discovery. Missing `AGENTS.md` or `.agents/skills`
fails before invocation. The authored Telegram role supplements the project entry;
no copied harness, generated skill index or fixed source bundle is introduced.
The existing permission profile still grants only the memory file for direct writes.
Native discovery also checks the global Codex entry. Its two entry-file paths are
readable exceptions within the denied Codex profile directory; authentication and
configuration files remain denied. A native start exposed this requirement even
with an empty global `AGENTS.md`.

Session-writing hooks remain disabled. The Telegram role follows applicable read-only
skill work, reads existing questions and reports inaccessible external
evidence. Registration and question-store mutations remain with the operator
session; the bot does not acquire publication, connector or network authority.
At this stage, factual edits and the agreement-request log were unimplemented.
The board-aware amendment below implements the request log and scoped original-issue
follow-up; factual document edits remain separate. Loading instructions alone does
not establish those capabilities.

The initial native proof used a normal ownership question, an entry-only marker
and an implicitly selected skill whose answer is absent from the request and README.
It also exercised memory writing while preserving another document, then asked an
ordinary Workshop status question and observed recall and assignment-review skills.
That automatic operator entry is superseded by the accepted continuing-conversation
amendment below. Its updated native proof retains implicit skill discovery and write
scope while verifying the bot-specific entry and context across worker processes.

<straw-dog question="q-0002.0012">

## Factual corrections and agreement proposals — next implementation

The user's 2026-10-15 [authority amendment](../contracts/telegram-workshop.md#factual-corrections-and-agreement-change-requests)
permits evidenced factual corrections and defers agreement changes to a later
session with the user. Direct factual-document edits remain unimplemented. The
board-aware amendment below implements the separate request-log path. This section
supersedes earlier blanket architecture-write exclusions for factual corrections only.

The candidate uses Codex's existing file tools and a Markdown request log, not
structured memory updates or a separate classifier. The write boundary must
distinguish allowed documentation from code, rules and publication; permission to
write a document does not establish authority to change a promise within it.
Evidence of implementation drift is recorded as drift, not an amended contract.

The implemented log at [Telegram requests](../requests/telegram.md) retains the
proposal and group-message reference, author, kind and pending disposition. Operator
recall discovers it under local L26. Review records the user's decision without
erasing the proposal. The unattended board-review route does not accept these
changes on the user's behalf.

Proof covers a supported factual correction, an agreement change disguised as a
factual correction, an uncertain fact, a repeated request, a concurrent document
edit, interrupted application and discovery of the pending proposal in a later
session with the user. Existing delivery uncertainty must not trigger a second edit.

The [two-pass astrobot study](../questions/q-0002.0012-how-should-telegram-provide-access-to-workshop.md#astrobot-study--2026-10-15)
adds candidates for visible waiting, explicit current time and useful operator
diagnostics. They are recommendations, not already implemented capabilities or
new acceptance gates. A separate feedback classifier, remote prompt platform and
automatic regeneration after failure are unnecessary for this scope.

## Local application and boundaries

One locally launched Python application receives Telegram updates, retains group
discussion and calls the installed Codex CLI for addressed requests. Python HTTP, subprocess and SQLite
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
   precedes retention. Received group discussion is background; other chats and
   nested quoted bodies do not enter agent context, history or raw diagnostic logs.
3. Selection handles text, captions, mentions, visible and hidden account links,
   and replies to recorded bot answers. Entity slicing respects UTF-16; parsed
   account identity and exact domain/path checks reject lookalikes. Multiple
   references select one request; a bare reference first resolves the accepted
   follow-up-addressing case and always reaches Codex with available history.
4. Accepted intake and the update checkpoint become durable together, before the
   next acknowledgement. Repeated delivery of an event creates no second request.
   Ignored events advance the checkpoint without retaining message bodies.
5. One worker processes durable arrival order. A reply to a known bot answer keeps
   that conversation, even from another person; otherwise a new request starts one.
   Reply association takes precedence over another mention in the same message.
6. Codex receives that conversation, available group background and current Workshop sources. Message
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
| 3. Selection and conversations | Links, captions, bare mention, continuations and independent roots | UTF-16 prefix, hidden link, lookalike account/domain, duplicate references; ordinary discussion is background without replies; other chats absent; another sender continues; interleaved roots retain reply associations |
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

## Continuing conversations — accepted 2026-10-15

The user accepted a bot-specific entry into the same harness and one persistent
Codex session per Telegram conversation. Native project discovery remains enabled;
the role replaces automatic operator wake/recall/assignment review with reading
the request's relevant materials. Later turns refresh facts as needed.

### Impact

The existing SQLite state owns the mapping from group and routed conversation root
to an exact Codex session UUID. A new independent mention starts a new session;
replies, including another participant's replies, resume that session after restart.
Local requests without a Telegram conversation remain standalone. Session content
is stored by Codex; the bot database holds routing and execution state, not a second
memory format. Text memory remains the shared writable note.

### Hidden edges

Session identity is saved on the native thread-start event, before the turn completes.
An unknown start, an interrupted active call, or an unavailable saved session cannot
silently create a replacement. Exact request deduplication remains independent of
session continuation. Every launch reasserts the same restricted capabilities.
The bounded group snapshot is supplied as background on each turn; it may overlap
earlier context. Native compaction and bounded snapshots do not promise unlimited recall.

### Leave alone

Group routing, operator outbox, selected-ticket edits, factual-correction authority,
agreement-change review and sibling projects retain their existing boundaries.
No copied harness, extra skill catalog or general session service is needed.

### Recommendation

Implement within the existing ticket. Prove context remembered across actual worker
processes, exact UUID reuse, independent roots, unchanged permissions on resume and
absence of automatic operator entry. Exercise failed starts and duplicate requests
with deterministic tests, then restart the receiver after its queue is idle.

Verification on 2026-10-15: 59 application tests passed, including six continuation
cases. Four native calls passed in separate worker processes: implicit skill use;
exact-session continuation recalling a conversation-only value with permitted memory
write and refusal of another write; independent-root isolation; and Workshop ownership
lookup without automatic recall or assignment review. Local evidence is retained at
`.local/harness-proof-20261014-235748/private/`. Required harness, installed-rule,
mechanism, question and ticket checks passed. This proves the scoped amendment,
not the remaining factual-edit/log capability or whole-ticket group acceptance.

## Board-aware answers and operator requests — accepted 2026-10-15

Implements the [answer amendment](../contracts/telegram-workshop.md#answers-and-language)
in the existing ticket. The user specified that mechanism requests reach the next
operator wake rather than granting implementation authority inside Telegram.

### Impact

The host checks the existing board script before each addressed request, reuses its
snapshots and completed review notes, and exposes scoped tools to the Codex worker.
Those tools provide paged board evidence, fresh GitHub reads, public site checks,
one short review notice, recoverable original-issue follow-up and append-only
operator requests. The agent chooses relevance and performs the existing skills
when no applicable review exists. The same plain-text role is reasserted on resume.

### Hidden edges

A fetched snapshot is not a completed review. Monitor leases and uncertain
publication state remain authoritative. A notice has separate delivery state from
the main answer; failure or restart cannot resend it blindly or confuse its reply
association. Tool credentials remain in the host. Shell network and direct code
writes stay unavailable; scoped tools do not transfer arbitrary host permissions.
Public checks cannot establish authenticated staging behavior. Requests preserve
trusted intake provenance and reach recall without authorizing themselves.

### Leave alone

The board reviewer, its existing script and active work remain owned by that
reviewer. Reuse its publication recovery instead of building another comment
sender. No duplicate board database, automatic code execution, copied harness or
structured bot memory is introduced. Existing fact-edit work remains separate.

### Recommendation

Implement the scoped tools and durable notice delivery, then exercise changed,
unchanged, absent and partially unavailable board evidence; original-issue
publication recovery; request deduplication and next-wake discovery; and native
Codex tool use. Live proof uses reads and isolated fixtures, not synthetic posts
to the real group or project issues.

### Verification on 2026-10-15

Native Codex used the scoped tools to read current GitHub issue 14 and supplied a
separate review notice before its answer with real issue/comment URLs. Evidence:
`.local/harness-proof-tools-20261015-003153/private/`. An isolated native conversation
recorded a mechanism request, actually read recall and review-assignments when the
fixture lacked a completed review, and a fresh operator Codex process discovered
that pending request through recall. Evidence:
`.local/harness-proof-requests-20261015-003443/private/`.

Host probes verified a published document URL, public staging health HTTP 200 and
a DNS failure for the documented wiki staging host. They do not establish authenticated
access. Tests cover original-issue follow-up recovery, changed evidence and reviewer
conflicts, notice delivery/restart, missing monitor output and request provenance.
No synthetic message or comment was posted to the real group or GitHub issues.
The full standard-library suite passed 82 tests; harness, installed-rule, mechanism,
question and ticket validation passed. The scoped provisional-text scan found no
unbound candidate introduced by this amendment.

## Silent receiver and typing correction — 2026-10-15

The user reported missing answers and no visible typing activity. Inspection found
no running receiver and no newly received messages in the local journal; its former
execution handle no longer existed. The cause of that process exit was not retained.
The transport also had no sendChatAction implementation.

The worker sends typing before preparing an addressed answer and renews it every
two seconds in the same topic, measured from the start of each network call rather
than its completion. It stops renewal before sending the answer, respects
Telegram retry delays and isolates indicator failures. The action uses a short HTTP
timeout. Ordinary group background messages do not start it. Tests exercise renewal,
topic routing, cleanup and failure isolation through the group processing boundary.

The local receiver was restarted as a hidden Windows process with separate retained
stdout/stderr logs under its private runtime directory. This is a local launch, not
automatic startup after reboot or a continuous-hosting guarantee.

Verification: 90 tests passed, including both typing cases; the declared harness,
installed-rule, mechanism, ticket and board-report checks passed. The restarted
receiver recovered group message 43 and delivered a substantive answered result,
with no processing or delivery error. Its separate process remained running on
subsequent inspection. Telegram client rendering of the indicator was not observed
directly; renewal and request parameters were verified through transport tests.

The later 2026-10-15 report of disappearing typing occurred while message 57 was
still processing; that request subsequently reached confirmed delivery. Telegram's
indicator expires after at most five seconds and is cleared by a bot message,
including a review notice. The previous four-second completion-based interval left
little tolerance for network latency. Three live diagnostic actions succeeded in
0.26–0.33 seconds, so the particular disappearance is not proven to be a network
failure. The two-second start-based cadence increases that tolerance; safe local
logs retain message ID, accepted calls and duration, or error code/retry delay,
without message bodies, API URLs or credentials. Failure to refresh does not stop
the answer. Telegram rate limits, network failures and client rendering can still
interrupt the indicator; it is not a guarantee of continuous display.

Verification of this amendment: 95 tests passed against the committed baseline
plus these changes, including delayed-action cadence and safe failure logging.
The shared 102-test run encountered a separate in-progress board transport
expectation mismatch; its changes are excluded from this slice. The declared
harness, rule, mechanism, board-report and ticket checks passed. Four actual
sendChatAction calls were accepted at 14:10:46/48/50/52 Jerusalem, with no message
sent by that diagnostic. The idle receiver was restarted at 14:12 with stderr
logging enabled; Telegram-client rendering remains unobserved.

## Executable next steps — 2026-10-15

The user supplied a second vague Telegram answer: named owners and issue links
still left DNS configuration and a joint browser check as goals rather than steps.
The local conversation rule now defines the presentation of an executable action,
copy-ready direction to an already assigned agent, sequential result handoff and
explicit missing prerequisites. It changes neither issue ownership nor permissions.

Two real Codex answers in one continuing conversation were inspected at
`.local/bot-actions-proof-20261015-102723/private/`. The first retained the exact
CNAME target and private TXT handoff from issue 12, separated the DNS actor from
recipient agents, supplied copy-ready agent requests and identified available versus
blocked work. The follow-up on renewal requested a Cabinet-prepared eligible test
session, refused to invent a waiting interval, and described the request, response,
cookie forwarding and subsequent read that distinguish renewal from a simple reload.
It explained why simultaneous owner participation was unnecessary. These are observed
prompt outcomes, not evidence that the DNS or browser work was performed.

Both answers completed in the same native session. No group message, issue comment
or recipient mutation was made by the proof. Harness integrity, installed rules and
mechanism validation passed. The running bot reads the amended role on its next turn.

## Follow-up addressing — 2026-10-15

The user corrected the two-message interaction: a question without a mention,
followed two minutes later by a standalone bot mention, refers back to that question.
The former bare-reference shortcut returned an invitation before Codex saw the
question. Its first repair still failed on the live history: previous invitations
masked the question and a five-minute cutoff excluded subsequent attempts. The
user reported that failure at 13:44. The shortcut and cutoff are removed.
Intake skips stored legacy invitations, then selects the most recent meaningful
same-author/same-topic message; explicit replies retain priority. Identity uses
Telegram IDs, not display names. Every standalone reference reaches Codex, including
one with no selected antecedent, so clarification can use the available context.

A nullable addressed-message reference preserves both original journal entries.
The later mention supplies the request identity and delivery target; the preceding
message supplies the question and conversation root. Existing history gains the
nullable field on startup. Duplicate updates retain one request. An already
addressed predecessor supplies its existing conversation root, but never replaces
the new mention with the old command. Conversation messages include request status;
the bot's role forbids repeating completed work because of a repeated mention.
No old delivered invitation is automatically reprocessed.

Regression coverage includes the original wording, the legacy persisted question
50 and invitations 51/53/55 at their actual time gaps, restart, duplicate intake,
agent input and delivery. Other cases cover sender/topic isolation, explicit reply
precedence, unavailable attachment text, continuation in every delivery state and
typing before even an empty-history mention reaches the agent. The legacy fixture
is inserted as the old receiver wrote it, not generated by the repaired receiver.

Verification: all 94 tests passed in the committed baseline plus this scoped
change. The shared working tree's 100-test run encountered an unrelated in-progress
board migration fixture error (ten columns, eleven placeholders); that work is not
included here. Harness integrity, installed rules, mechanism, ticket and board-report
validation passed. On a private copy of the live journal, a new reference selected
message 50 through invitations 51/53/55 and a native Codex call produced concrete
next steps. Evidence is retained privately under
`.local/bot-followup-proof-20261015-105307/private/`; Telegram delivery was simulated,
with zero real group sends. The idle receiver was replaced at 13:58 Jerusalem;
the new process remained running with no startup error. Previously sent invitations
remain historical records, not requests retroactively answered by this proof.

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
