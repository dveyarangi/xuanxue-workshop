# Local Workshop conversation

The first local stage of [telegram-workshop-access](../docs/tickets/01-0020-telegram-workshop-access.md)
answers questions from selected current Workshop records and can amend one passage
of prose in a selected existing ticket. The first Telegram receiver is implemented;
an actual bot/group exchange has not been verified.

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
the selected Workshop tree. An answer without `--target` cannot edit records.

Global `--root` and `--state` options precede the subcommand. The default history
is `.local/workshop-bot/history.sqlite3`, excluded from Git. History includes author,
time, request, result, cited source versions and changes before/after with reasons.
It is an operator JSON view.

## Первый запуск в Telegram

1. Создайте бота через `/newbot` у [BotFather](https://t.me/BotFather), если его ещё нет.
2. В BotFather отключите privacy mode через `/setprivacy`, затем добавьте бота в
   выбранную группу. Если он уже был добавлен, удалите и добавьте его заново.
   Это позволяет получать обычные упоминания; приложение сохраняет только обращения.
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

В этом этапе доступны отдельные вопросы с упоминанием или ссылкой, в тексте и
подписи. Продолжение ответом без нового упоминания, изменённые сообщения, выбор
задачи для правки из Telegram и операции над вопросами ещё не реализованы.
Групповые запросы вызывают информационный вариант рабочего вызова; ранее
проверенная правка задачи доступна локальной командой `ask --target`.

## Current boundaries

The decision call has tools disabled and receives a bounded local source bundle,
applicable supplied skills and local question records. It cannot browse GitHub or
claim a complete question-store window. Its response proposes a change; the caller
checks the selected path, ticket format and source versions before applying it.
Semantic compatibility with architecture is assessed by the model, not guaranteed
by the path validator. The application rejects new ticket-validator diagnostics;
pre-existing unrelated diagnostics do not authorize additional violations.

Windows excludes concurrent writes to the selected file while application occurs.
A durable prepared change precedes the file write. Interrupted application is
compared with the recorded before/after content on the next request with that ID;
uncertain outcomes are retained without automatic repetition. This is recoverable
single-record application, not an atomic transaction across records.

The child environment omits arbitrary inherited credentials. Recognizable Telegram
tokens and API keys are redacted from input/output; this is not a general secret
detector. Runtime credentials do not belong in questions or Workshop documents.

Question mutations, ticket creation/closure, complete skill lifecycle, conversation
continuations and live group acceptance remain within the owning ticket's outstanding
scope. Sources in group replies are labelled local records; published-source links
remain part of the complete acceptance criteria.

## Verification

```powershell
uv run --offline --no-project python -m unittest discover -s tests -v
uv run --offline --no-project python -m tests.live_workshop_proof
```

The second command uses the signed-in Codex and creates an isolated copy under
`.local/workshop-bot/proof-*`. It applies a permitted prose amendment there and
checks refusals for an architecture conflict and a request to bypass authority.
Its `results.json` and SQLite history retain the evidence. Canonical project
records are checked for unchanged content. These checks do not prove Telegram
reception or delivery.
