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
Session-writing hooks stay disabled; the bot follows entry and applicable skills
through their available read-only work, including inspecting existing question records.
Unavailable external evidence is disclosed. Operator session bookkeeping and
publication are not inherited by the group worker.

An interrupted conversation may already have changed memory. Failed answers do not
claim that it was unchanged; the same request is not automatically executed again.

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
scope. Sources in group replies are labelled local records; published-source links
remain part of the complete acceptance criteria.

## Verification

```powershell
uv run --offline --no-project python -m unittest discover -s tests -v
uv run --offline --no-project python -m tests.live_workshop_proof
uv run --offline --no-project python -m tests.live_harness_proof
```

The second command uses the signed-in Codex and creates an isolated copy under
`.local/workshop-bot/proof-*`. It applies a permitted prose amendment there and
checks refusals for an architecture conflict and a request to bypass authority.
Its `results.json` and SQLite history retain the evidence. Canonical project
records are checked for unchanged content. These checks do not prove Telegram
reception or delivery.

The third command exercises native project instruction loading and implicit skill
selection using values absent from the user request, verifies the memory/document
write boundary, then sends an ordinary status question against Workshop. Its local
evidence includes Codex tool events and answers; no Telegram message is sent.
