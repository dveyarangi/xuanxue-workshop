# Current Codex chat — Board review hosts edge

## Integration

The host uses `.agents/scripts/gw/board.py`, the periodic review procedure in
`.agents/skills/review-assignments/PERIODIC.md`, and retained progress under
`.local/board-review/`. The same-chat scheduled task supplies recurrence. The local
computer, app and authenticated GitHub tools must be available during execution.

## Conformance

- **Discovery** — observed 2026-10-15; the authenticated gh adapter read all thirteen addressed issues, including closed cases, comments and timelines, with no primary-read failures. Linked evidence gaps remain explicit.
- **Review** — observed 2026-10-15; the current full agent supplied five representative evidence/acceptance/security/instruction-authority/closed-issue outcomes after reading the governing sources. Operator grading remains pending; no actual contribution was accepted.
- **Delivery recovery** — observed 2026-10-15 on local HTTP only; a stored comment survived loss of its HTTP response and was recovered on restart without another comment. Five cases produced five physical comments. Real GitHub publication is unobserved after automatic approval review rejected creation of the controlled issue.
- **Recurrence** — documented; automation workshop-board-review targets this chat every fifteen minutes and is PAUSED. No unattended invocation or real GitHub publication is claimed.
