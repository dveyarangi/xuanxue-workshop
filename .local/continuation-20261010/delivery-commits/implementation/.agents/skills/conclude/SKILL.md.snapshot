---
name: conclude
description: >-
  Use when a session ends, or the user asks to conclude the current chat.
---

Mechanism: not yet

Conclude curent chat, extracting:
- a brief summary of work done (no need to repeat details already stored into other documentation files), 
- the remaining open questions, with compact reasoning and relevant context. 
- and other things that need continuation.

And write it into a markdown file under docs/sessions.
Session files live under `docs/sessions/`, named `NNNN-<YYYYMMDD>-<name>` with a constantly incrementing number.

## Installed from other mechanisms

<installed by="questions">
**Q3** Write a lean line on each question the session touched and left open —
`questions.py lean q-N '<line>' --session <tag>` — and nothing else: placements and closures were written as they
happened. As the conclude's last act, run `questions.py --end --session <tag>`.
</installed>

<installed by="local">
**L17** Override the conclude-only push restriction in AGENTS.md Autonomy/push and
.agents/skills/conclude/SKILL.md. Keep push=ask separate from commit approval.
When publication is required to continue authorized work, state the GitHub action
and request permission for the prepared, reviewed commit at that point; do not
defer the request or hide the pending action until session end.
</installed>
