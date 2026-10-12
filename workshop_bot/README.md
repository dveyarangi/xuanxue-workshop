# Local Workshop conversation

The first local stage of [telegram-workshop-access](../docs/tickets/01-0020-telegram-workshop-access.md)
answers questions from selected current Workshop records and can amend one passage
of prose in a selected existing ticket. Telegram transport is not connected.

## Run from the Workshop root

Requirements: Python 3.12+, Git, Windows for record writes, a native `codex.exe`
with local sign-in and support for the isolated execution options used by this app.
The executable is resolved from PATH or the locally installed Codex application.
No Telegram token is needed for this stage.

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
It is an operator JSON view, not a Telegram conversation interface.

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
continuations, a durable Telegram queue, delivery and live group acceptance remain
within the owning ticket's outstanding scope.

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
