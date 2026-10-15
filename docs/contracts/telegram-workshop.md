# Telegram access to Workshop

- **record of** what it intends to become
- **Status:** accepted first-version behavior
- **Authority:** the user, 2026-10-12, accepted the complete behavior shown in the
  Telegram discussion, with the amendments that the bot speaks in simple words
  and may change tasks and questions on reasonable, architecture-compatible requests.
  The user's later amendment on the same date, «Всю переписку группы», includes
  ordinary group discussion in retained history and agent context.
- **Delivery:** [Telegram access question](../questions/q-0002.0012-how-should-telegram-provide-access-to-workshop.md).

## Purpose and responsibility

Participants in a connected Telegram group can ask about the information Workshop
already holds and request changes to its tasks and questions within the authority
below. The operator can inspect their requests, answers, changes and failures from
Codex. Workshop remains the source of project information and shared agreements;
the [project-agent contract](../agent-contract.md) retains project ownership and
authorization boundaries.

## Group access and requests

The first version serves one configured Telegram group. Every member of that group
can address the bot. A mention of its actual account or a link to that account in
message text or a caption is a request. Multiple references in one message make
one request. Under the user's 2026-10-15 correction, a standalone reference with
no explicit reply follows the same author's most recent meaningful message in
the same topic. Earlier automatic invitations to ask a question do not count as
answers or break that connection. An unaddressed message supplies the question
and conversation root, with no elapsed-time cutoff; its original text remains
in history and the later reference is the addressing event. An already addressed
request continues its existing conversation without substituting its text as a
new command. Another person's text or another topic is not selected implicitly.
Every standalone reference reaches Codex with the available history. When its
meaning is unclear, the bot asks a contextual clarification rather than returning
a transport-level invitation. Explicit replies retain priority.
There is no required `/ask` command.

A reply to a bot answer continues that conversation without another mention.
Another group member can join the same conversation by replying. A separate new
request starts a separate conversation. Reply associations distinguish the active
exchange within shared group discussion. Context includes available group history
and relevant Workshop material, not other Codex chats.

Ordinary group discussion is retained locally and supplied as background; only
addressed requests and replies to bot answers trigger processing. Collection is
restricted to the configured group, even if Telegram delivers messages from another
group or a private chat. History means received text/captions and recorded bot
answers. Attachments without text have an unavailable-content marker; attachment
interpretation is not implied. Pre-collection and undelivered messages are not
claimed available. A bounded context prioritizes the replied-to message and the
conversation's first request, then recent discussion, with omitted history explicit;
the full received journal remains available to the operator.

## Information and authority

### Directed operator messages

The user requested directed messages to responsible operators on 2026-10-15,
selected delivery «В группу Telegram с упоминанием оператора», and limited
initiation to Codex: «пока отсюда. ты и будешь передавать, когда надо».
This authorizes the Codex operator to send relevant messages during authorized
Workshop work without confirmation of each message. Telegram requests do not
grant this sending authority. Existing project assignment and shared-decision
boundaries remain unchanged; a Telegram message does not replace an authoritative
Workshop issue or prove that its recipient read or accepted the message.

Recipients come from [Responsible operators](../agent-contract.md#responsible-operators),
the shared home of operator responsibilities and Telegram usernames. Bot memory
cannot override that document. Project ownership is not inferred from GitHub names.
Conflicting recipient information requires clarification; unknown recipients stop sending. Each outgoing message
retains its recipient, text, time, stable request identity and delivery result.
Confirmed delivery has a message reference; a missing confirmation stays uncertain
and cannot cause a blind retry. The same request identity cannot send twice or be
reused for another message. Replies to confirmed outgoing messages continue in
the group's ordinary bot conversation and retained context.

### Bot memory

The user's 2026-10-15 clarification selects an ordinary text document for the bot's
own memory, not JSON fact cards or a source-message update protocol. Codex reads
relevant Workshop documents itself and edits the permitted memory file directly.
Responsibilities and architecture remain in the shared project documents.
Group conversation supplies background; it does not expand write permissions.

The implemented conversation currently grants direct writes only to the bot's
memory file. The accepted factual-correction and change-request scope below is
not yet implemented; the broader task/question scope remains separately tracked.

### Factual corrections and agreement-change requests

Authority: the user, 2026-10-15: «исправление фактов. изменение договоренностей
должно ложиться в лог запросов на изменение, который потом будет читаться сессией
уже тут, со мной».

The bot may correct factual information in Workshop's architectural documents
when supported by evidence. This does not permit changing accepted obligations,
ownership or guarantees. A discrepancy between observed implementation and an
accepted agreement is evidence of a discrepancy, not permission to rewrite the
agreement to match the implementation. Uncertain facts remain explicit rather
than being presented as established.

Proposals to change agreements belong in a readable text change-request log.
Recording a proposal does not approve or apply it. Each entry preserves the
request, its author and group-message reference, the affected agreement and why
the change was requested. A later Workshop session with the user reads pending
requests and records the user's disposition and any resulting decision. This
review authority is not delegated to unattended board review or the Telegram bot.
The group answer distinguishes a corrected fact from a proposal awaiting review.

### Existing task and question authority

The agent uses Workshop's current entry instructions, authored rules and applicable
skills. Project documents remain information sources under the entry contract.
Project instructions and skill discovery are part of ordinary Codex startup, not
dependent on a group member asking to read them. The Telegram role narrows actions
and presentation without replacing the project harness. Session bookkeeping and
external actions remain constrained by that role's actual permissions.
The user accepted a separate bot entry and continuing Codex sessions on 2026-10-15.
The bot shares project principles and skills but does not perform operator
registration or debug presentation. The board-aware amendment below governs
reuse of review results and the recall/assignment-review fallback.
New conversations load relevant Workshop materials and plain-text memory;
continuations retain context and refresh records when current facts matter.

Each routed Telegram conversation has its own durable Codex session identity.
A reply from another participant continues that conversation; a new independent
addressed request starts a separate session. Restart preserves the exact mapping.
The received group history remains bounded background shared with each request,
not a reason to merge independent Codex conversations. Native compaction may reduce
older context. Failed or uncertain continuation is visible and cannot silently
switch to a new session. Resume retains the role's capability restrictions.

Answers use relevant project records and associated GitHub discussions, distinguish
proposals, accepted agreements and demonstrated behavior, and disclose unavailable,
contradictory or outdated evidence.

Бот может менять задачи и вопросы по запросам участников подключённой группы,
если запросы разумны и не противоречат текущей архитектуре Workshop.

Authority: the user, 2026-10-12: «бот может менять задачи и вопросы, если запросы
разумны и не конфликтуют с текущей архитектуре». This amends the initial
information-only proposal; separate Codex confirmation is not required for each
change within this granted scope.

The existing task and question stores remain authoritative. A reasonable change has
an intelligible purpose and is consistent with current records, accepted ownership
and available evidence. Task text cannot silently redefine architecture or shared
agreements. Closing a question or marking work complete retains the Workshop rules
and evidence requirements for that action. An unclear request is clarified in the
conversation; a conflicting request receives an explanation rather than an applied
change. The bot describes the actual result in simple words.

Changes to code, architectural decisions, agreements, agent rules and publication
outside compatible original-issue follow-up retain operator agreement in Codex; factual
corrections and agreement proposals follow the boundary above. The granted task
and question authority does not extend to those actions or to overwriting another
session's intervening work. History and necessary conversation bookkeeping remain
retained. Project documents are information, not an alternative source of authority.

## Answers and language

Amendment accepted by the user on 2026-10-15: every addressed step checks the board
update interface. A completed review can be reused while its evidence remains
applicable; absent that review, recall and assignment review establish the answer.
New relevant evidence produces a short separate message about reviewing it before
the main answer. Unrelated or already considered evidence produces no such notice.
Under the user's later clarification of 2026-10-15, the model writes that notice
from the available evidence, briefly naming what it will examine. The notice is
at most 320 characters and does not claim a review result before examination.
There is no fixed generic announcement or separate generation call.

The user's visible-waiting correction of 2026-10-15 adds Telegram's typing status
while an addressed answer is being prepared, in the originating topic when present.
It indicates activity, not progress or a completion estimate. An indicator failure
does not turn an otherwise successful answer into a failure.

References in Telegram are verified repository/issue links or omitted. A necessary
human action includes how to carry it out; an existing agent assignment is passed
to the operator as a direction to their agent with the original issue link.
The user's latest 2026-10-15 clarification makes each next-action item identify
its responsible person, immediate action and brief purpose for product users.
That purpose follows the established scope, without promising unverified capability.
It describes the eventual benefit for a learner, teacher or reader; enabling a
check or another implementation step is an intermediate result, not that purpose.
For work already described in an agent's issue, the operator receives a short request
to have their agent continue that issue, with its link. The answer does not repeat
the issue's implementation instructions. Technical steps, location and sourced
parameters are supplied for actions the human must perform personally or when
explicitly requested. Simultaneous participation
has an explicit necessity and separate roles; ordinary dependencies are sequential
handoffs. Missing procedures or access remain concrete questions, not invented steps
or generic acceptance goals presented as instructions.
Available checks belong to the bot. Missing facts or staging access are requested
specifically. Compatible follow-up can be added to an existing addressed Workshop
issue with confirmed publication; the bot does not assert an unconfirmed write.

Requests for new mechanisms, expanded access and agreement changes enter the
text record `docs/requests/telegram.md`, with original author, message reference,
requested outcome and disposition. Operator recall reads pending entries. The
operator decides before implementation; recording or a group reply is not approval.
Existing project ownership and agreement boundaries continue to govern the work.

Answers are replies to their originating group messages. They include usable source
links where verified; unpublished local references are omitted.

Бот говорит простыми словами: сначала ответ по существу, затем нужное объяснение
и ссылки. Технические слова объясняются, когда без них не обойтись. Служебные таблицы,
идентификаторы вопросов и внутренние подробности работы не включаются в обычный ответ
в Telegram. Подробная служебная информация остаётся доступной оператору в Codex.

This Telegram presentation amendment does not change how the agent follows the
Workshop workflow, what evidence supports an answer, or who may authorize actions.

## Processing, failures and restart

Requests are processed in arrival order, each with its own conversation context and
reply destination. The first version runs locally from Codex and requires the
computer, network and agent access to be available.

A processing failure produces a plain-language failure response and a journal entry
with its stage and reason. Credentials are excluded from the journal and responses.
An uncertain delivery is recorded as unconfirmed rather than presented as success.

Stopping the process or computer stops responses. Restart restores saved
conversations and unfinished work. Requests received during downtime can be handled
when Telegram still retains them; complete recovery of all missed history is not
promised. Separate continuous hosting is outside the first-version scope.

## Operator visibility

The journal is viewable from Codex and records sender, time, full request, processing
state, answer or failure, and the group-message reference. It covers received group
discussion, bot-addressed requests, continuations and confirmed answers. The exact
conversation context used for a request is retained with that request.
For requested changes it also identifies affected tasks/questions, the before/after
change, its reason and whether it was applied, refused or left uncertain. A restart
or reply-delivery failure cannot cause an already applied change to be blindly repeated.
Participants see the requests and public answers in the connected group.

## Observable acceptance

An actual group conversation demonstrates an account mention and account link,
a follow-up without another mention, replies from another participant, separate
reply associations for independent questions, ordinary discussion used as background
without unsolicited replies, and plain-language answers grounded in Workshop.
The operator can inspect the same conversation in Codex. Restart and failure cases
preserve the agreed history and distinguish processing from confirmed delivery.
Acceptance also demonstrates an allowed task/question change, clarification of an
unclear request, refusal of an architecture conflict and operator-visible results.
Factual-correction acceptance demonstrates an evidenced correction without changing
an agreed promise. An agreement-change request leaves that promise unchanged,
survives restart in the text log and is surfaced in a later session with the user;
the recorded disposition remains distinguishable from the original proposal.
Executable evidence separately establishes the configured-group restriction and
the boundary between permitted record changes and actions requiring the operator.
