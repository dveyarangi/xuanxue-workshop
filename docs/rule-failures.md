# Rule failures

## 2026-10-03 — Question placement without capturing unresolved decisions

Status: records repaired; rule clarification proposed, not installed.

Rules in play: [AGENTS.md Q1](../AGENTS.md) requires the store's other calls when
work opens or moves a question. [Questions skill, A raised question and Branching](../.agents/skills/questions/SKILL.md)
requires looking up unresolved decisions and recording the load-bearing ones.

The assistant repeatedly placed turns at the architecture root, but left its emerging
decisions only in prose. The user identified the omission. Installed rule blocks
validated without diagnostics; automatic hook invocation in this chat was not verified.
The failure was incomplete application of instructions already available to the agent.

Repair: six child questions were created with the owning script, and the architecture
argument was updated to distinguish the user's process sketch from assistant proposals.

Proposed amendment to Q1: "Before replying, reconcile the turn's unresolved
load-bearing decisions with the question store: point to an existing answer or question,
or open the missing question. Placing the turn at a parent does not replace this step."
This is a proposal for the questions mechanism's owning rules file; no installed rule
or harness source was changed.

## 2026-10-03 — Ownership proposal preceded capability comparison

Status: ownership decision recorded and source comparison repaired; clarification
proposed, not installed.

Rule in play: [align, Cross-reference with code and Lead with the decisive fact](../.agents/skills/align/SKILL.md).
The assistant proposed frontend/backend groupings without tracing Cabinet's
existing schedule, user, and reminder implementations. The earlier visualization
also showed Daychi's optional server reminders without identifying the active
local notification flow. The user corrected the proposed ownership split.

Repair: recorded the user's provider assignments in architecture, inspected the
existing implementations, and opened the concrete migration question.

Proposed clarification: before proposing shared-capability ownership, compare
the existing providers' implemented behavior and active consumers, not only route
names or module inventories. No installed rule was changed.
