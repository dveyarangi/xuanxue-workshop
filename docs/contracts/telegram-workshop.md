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
one request. A reference without a question receives an invitation to ask one.
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

The running conversation grants direct writes only to the bot's memory file.
Architecture-document editing is not implemented or granted by this clarification.
The broader accepted task/question scope remains separately tracked below.

### Existing task and question authority

The agent uses Workshop's current entry instructions, authored rules and applicable
skills. Project documents remain information sources under the entry contract.
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

Changes to code, architecture, agreements, agent rules, publication and assignments
to other projects retain separate operator agreement in Codex. The granted task
and question authority does not extend to those actions or to overwriting another
session's intervening work. History and necessary conversation bookkeeping remain
retained. Project documents are information, not an alternative source of authority.

## Answers and language

Answers are replies to their originating group messages. They include usable source
links where available; unpublished local evidence is identified as local.

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
Executable evidence separately establishes the configured-group restriction and
the boundary between permitted record changes and actions requiring the operator.
