# Local Workshop conversation

The [telegram-workshop-access](../docs/tickets/01-0020-telegram-workshop-access.md)
application passes group conversations to Codex. Codex reads relevant Workshop
documents with its own tools, keeps plain-text memory and returns an ordinary reply.
The separate local ticket operation can amend one selected passage. Complete group
task/question changes and whole-ticket acceptance remain outstanding.

## Run from the Workshop root

Requirements: Python 3.12+, Git, Windows for record writes, a native `codex.exe`
with local sign-in and support for the isolated execution options used by this app.
The executable is resolved from PATH or the locally installed Codex application.
Local `ask` and `history` commands need no Telegram token.

```powershell
uv run --offline --no-project python -m workshop_bot ask "Для чего нужен Workshop?"
uv run --offline --no-project python -m workshop_bot history
```

`ask` accepts `--target` with a live ticket's repository-relative path, `--sender`
and `--request-id`. Repeating an identifier with the same request returns its stored
outcome; using it for a different request fails. A requested edit takes effect in
the selected Workshop tree. Without `--target`, only the bot's memory is writable.

Global `--root` and `--state` options precede the subcommand. The default history
is `.local/workshop-bot/history.sqlite3`, excluded from Git. History includes author,
time, request and result. The selected-ticket operation also retains cited source
versions and changes before/after with reasons. It is an operator JSON view.

## Первый запуск в Telegram

1. Создайте бота через `/newbot` у [BotFather](https://t.me/BotFather), если его ещё нет.
2. В BotFather отключите privacy mode через `/setprivacy`, затем добавьте бота в
   выбранную группу. Если он уже был добавлен, удалите и добавьте его заново.
   Это позволяет получать упоминания и сохранять переписку выбранной группы.
   [Описание режима Telegram](https://core.telegram.org/bots/features#privacy-mode).
3. Напишите в группе `/start@имя_бота`, чтобы настройка увидела группу.
4. В терминале Codex, открытом в Workshop, выполните:

```powershell
uv run --offline --no-project python -m workshop_bot telegram-setup
uv run --offline --no-project python -m workshop_bot telegram
```

Настройка запрашивает токен скрытым вводом и показывает группы на выбор.
Токен вводится только в локальном терминале. Он хранится в
`.local/workshop-bot/telegram.token`, группа — в `telegram.json` рядом с ним;
оба файла исключены из Git. Токен не входит в параметры запуска Codex или его
окружение. При известном ID доступна настройка `telegram-setup --group -100…`.

Для первого разговора подходит сообщение `@имя_бота Для чего нужен Workshop?`.
Просмотр запросов и ответов в другом терминале:

```powershell
uv run --offline --no-project python -m workshop_bot telegram-history
```

В истории видны автор, время, сообщение, ответ, состояние доставки и ссылка для
участников супергруппы; обычная группа сохраняет пару chat/message ID. Длинный
ответ делится на части, подтверждения сохраняются отдельно. Ctrl+C останавливает
бота. `telegram --once` обрабатывает один доступный пакет и готовую очередь.
Существующий webhook, недостаточные права и второй приёмник дают ошибку.

Полученные тексты и подписи всей группы сохраняются локально. Бот отвечает на
упоминания, ссылки и ответы на свои подтверждённые сообщения, включая ответы
других участников после перезапуска. Обычная переписка служит фоном и не запускает
ответ сама по себе. Вложения без текста отмечаются как недоступное содержимое.
В один вызов передаётся до 120 КБ истории: сначала сообщение, на которое отвечают,
и начало разговора, затем свежая переписка. Число пропущенных сообщений передаётся
агенту; полный полученный журнал остаётся в SQLite. История до начала сбора и
сообщения, которых Telegram не доставил, автоматически не восстанавливаются.
Изменённые сообщения, выбор задачи для правки из Telegram и операции над вопросами
ещё не реализованы.
Групповые запросы вызывают Codex с чтением документов и записью своей памяти;
правка выбранной задачи доступна локальной командой `ask --target`.

## Память и направленные сообщения

Память бота — обычный Markdown-файл `.local/workshop-bot-memory.md`.
Codex сам читает нужные материалы Workshop и редактирует этот файл штатными
инструментами. У памяти нет JSON-схемы, ключей фактов или специального протокола.
Оператор может читать и редактировать тот же документ; изменения лучше делать
между обращениями, чтобы не пересекаться с записью бота.
Ответственные и их Telegram-контакты находятся в
[общем договоре](../docs/agent-contract.md#responsible-operators).

```powershell
uv run --offline --no-project python -m workshop_bot memory
uv run --offline --no-project python -m workshop_bot telegram-send --to cabinet --message-file .local/workshop-bot/message.txt --request-id cabinet-question-20261015
uv run --offline --no-project python -m workshop_bot telegram-outbox
```

`telegram-send` берёт адресата из таблицы общего договора; неизвестный или
неоднозначный адресат останавливает отправку. Это локальная команда оператора
Codex, недоступная рабочему вызову из Telegram. Текст читается из UTF-8 файла и
публикуется в настроенной группе с точным @username из договора. Один текст
с префиксом занимает до 4 000 единиц UTF-16; более длинный требует сокращения.
Текст не интерпретируется как HTML или Markdown. Упоминание не доказывает членство
адресата в группе, получение уведомления или прочтение сообщения.

Один идентификатор поручения соответствует одной попытке отправки. Повтор той же
команды возвращает прежний результат; иной текст или адресат с тем же ID запрещён.
При потере подтверждения результат остаётся неопределённым без автоматического
повтора. Новый ID после определённого отказа означает новую явную попытку.
Подтверждённое сообщение имеет Telegram ID и ссылку для супергруппы. Ответ на него
продолжает разговор с ботом; текст исходного сообщения входит в контекст.
Отправка совместима с работающим приёмником и не сбрасывает его очередь.

## Current boundaries

Ordinary conversations invoke Codex with file tools and plain final text. The bot
supplies the repository location, group background and current request; Codex chooses
what to read. Codex starts in the Workshop root and loads its `AGENTS.md` and local
skill catalog through native project discovery. Missing entry or skill directory
fails before a model call. The Telegram instruction supplements that harness with
role permissions and plain language. Direct writes are limited to the memory file by a named permissions
profile. Private bot state and operator Codex/SSH/AWS directories are denied to tool
reads, except the two global Codex entry paths (`AGENTS.md` and `AGENTS.override.md`)
needed by native instruction discovery. Network commands, inherited connectors/hooks, browsers and delegation are
disabled. The Windows sandbox requires root read access; this is not repository-only
read isolation. Architecture and other project documents are read-only in this route.
Session-writing hooks stay disabled. The bot entry in `agent.rules.md`, authored
as L22 in `local.rules.md`, replaces operator registration and debug presentation.
Every addressed request checks the existing board script's retained status. Completed
applicable reviews are reused; otherwise the bot uses recall and assignment review.
Shared principles and applicable skills remain available, including question records.
Unavailable external evidence is disclosed. Operator session bookkeeping and
general publication authority are not inherited by the group worker.

The Telegram route exposes scoped host tools through a required stdio MCP server:
board status/discovery, paged issue evidence and fresh GitHub reads, published
document links, public HTTPS checks, a separate review notice, original-issue
follow-up and operator requests. The existing board script owns discovery, leases
and publication recovery. Its retained snapshots are not described as freshly read
GitHub data; current facts can be checked with fresh reads. The model selects
relevance and reuses completed reviews where their basis still holds.

Read tools are classified as read-only; the three granted write tools (notice,
request log and compatible issue follow-up) have explicit approval configuration.
This does not enable general shell network or file writes. Public site checks
use HTTPS hosts named in README, current-system or boundaries, reject credentials,
query parameters and private addresses, and do not follow redirects. Authenticated
staging checks require separately supplied access and an approved capability.

New relevant evidence produces one short notice before the main answer. Notice
delivery is journaled separately; an uncertain send is not repeated. Replies to
confirmed notices preserve the conversation. Evidence seen by the group is retained
across independent requests, so unchanged evidence does not produce another notice.

Mechanism, access and agreement requests are appended to `docs/requests/telegram.md`
with trusted message provenance and pending status. L26 in local.rules.md reaches
operator recall through the normal installer. Recording a request never approves
implementation. Bot memory remains ordinary text; MCP and private routing files
are transport state, not a structured memory protocol.

Each Telegram conversation root has a persistent Codex session, indexed by group
and conversation ID in SQLite. Replies from any participant resume that exact
session across receiver restarts; independent addressed requests start new ones.
Codex stores its own conversation history. Each turn also receives the bounded
group snapshot, which can overlap earlier background; native compaction may reduce
old context. Standalone local requests remain ephemeral.
Conversations received before this upgrade acquire a persistent session on their
next addressed turn, using the retained Telegram background; former ephemeral
Codex sessions cannot be resumed.

Session identity is saved as soon as Codex announces it. An unavailable saved
session is not replaced automatically. A start without a confirmed identity or
a receiver crash during an active call requires operator review of the retained
request and session state before that conversation can continue. No arbitrary
latest operator session is resumed. Every resume reasserts the bot permissions.

An interrupted conversation may already have changed memory, recorded a request or
published a follow-up. Failed answers report that uncertainty; the same request is
not automatically executed again.

The separate local `ask --target` operation still uses a bounded source bundle and
one proposed ticket passage. The caller checks the selected path, format and source
versions before applying it. Semantic compatibility is assessed by the model.

Windows excludes concurrent writes to the selected file while application occurs.
A durable prepared change precedes the file write. Interrupted application is
compared with the recorded before/after content on the next request with that ID;
uncertain outcomes are retained without automatic repetition. This is recoverable
single-record application, not an atomic transaction across records.

The child environment omits arbitrary inherited credentials. Recognizable Telegram
tokens and API keys are redacted from input/output; this is not a general secret
detector. Runtime credentials do not belong in questions or Workshop documents.

Question mutations, ticket creation/closure, complete skill lifecycle
and live group acceptance remain within the owning ticket's outstanding
scope. Group replies use verified published links or omit references. When a person
must act, the answer explains how, or points their agent to an existing assignment.

## Verification

During answer preparation the receiver renews Telegram's typing status every two
seconds, accounting for network-call duration and respecting Telegram retry delays.
Its stderr log records accepted updates and failures without message text or credentials.
This is independent of the separate notice about new board evidence; Telegram clears
typing when a bot message arrives, and the next update restores it.
Local operation requires a running receiver process. Its lifetime is not guaranteed
by a temporary Codex command handle; a hidden Windows launch can retain stdout/stderr
logs outside that handle. Computer shutdown still stops the receiver.

```powershell
uv run --offline --no-project python -m unittest discover -s tests -v
uv run --offline --no-project python -m tests.live_workshop_proof
uv run --offline --no-project python -m tests.live_harness_proof
uv run --offline --no-project python -m tests.live_bot_tools_proof
uv run --offline --no-project python -m tests.live_bot_requests_proof
```

The second command uses the signed-in Codex and creates an isolated copy under
`.local/workshop-bot/proof-*`. It applies a permitted prose amendment there and
checks refusals for an architecture conflict and a request to bypass authority.
Its `results.json` and SQLite history retain the evidence. Canonical project
records are checked for unchanged content. These checks do not prove Telegram
reception or delivery.

The third command exercises the bot entry and implicit skill selection, retains a
conversation-only value across separate worker processes, verifies the memory/document
write boundary on resume and checks a separate conversation cannot recall that value.
It also asks an ordinary ownership question against Workshop. Evidence includes native events and answers under the
denied private proof directory; no Telegram message is sent.

The tools proof reads a real GitHub control issue through the scoped MCP tools and
captures a separate notice without sending it to Telegram. The requests proof
records a mechanism proposal in an isolated fixture, checks recall/review fallback,
then starts a fresh operator process and verifies recall discovers the pending
request. Neither proof publishes to GitHub or the real Telegram group.
