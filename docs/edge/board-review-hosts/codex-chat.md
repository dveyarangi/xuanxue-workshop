# Current Codex chat — Board review hosts edge

## Integration

The host uses `.agents/scripts/gw/board.py`, the periodic review procedure in
`.agents/skills/review-assignments/PERIODIC.md`, and retained progress under
`.local/board-review/`. The same-chat scheduled task supplies recurrence. The local
computer, app and authenticated GitHub tools must be available during execution.

## Conformance

- **Discovery** — observed 2026-10-15; the authenticated gh adapter read all thirteen addressed issues, including closed cases, comments and timelines, with no primary-read failures. Linked evidence gaps remain explicit.
- **Review** — observed 2026-10-15; the current full agent supplied five representative evidence/acceptance/security/instruction-authority/closed-issue outcomes after reading the governing sources. The operator accepted all five on 2026-10-15; no actual contribution was accepted.
- **Delivery recovery** — observed 2026-10-15 on local HTTP and real GitHub; after explicit user approval, [control issue 14](https://github.com/dveyarangi/xuanxue-workshop/issues/14) received one studied answer. Interruption after remote acceptance left sending without a receipt; restart and repeat recovered comment 6180599165. Independent readback found one physical comment; closure was read back and studied. The local HTTP proof retained five comments across five cases.
- **Recurrence** — documented; configuration was changed to hourly and read back ACTIVE on 2026-10-15. Under the user's subsequent clarification, local L25 requires a short dated completion report for meaningful results, decisions or actionable failures; unchanged runs remain silent and wake does not repeat reports. Reports stay in this chat, renamed Workshop — дежурство по борде. Unattended invocation, tools/network access and conditional-report behavior remain unobserved.

### External trigger probe — 2026-10-15

The user requested a Desktop behavior check before deciding whether a mechanical
detector should replace hourly model activation. The installed Desktop package is
26.928.1915.0, with bundled codex-cli 0.159.0. The independently managed local daemon
and terminal CLI report 0.162.1. The Desktop child process uses its own stdio
app-server; the managed daemon is a separate process with a local control socket.

Read-only protocol clients initialized successfully against separate stdio servers
using both executable versions. They read this thread's correct identifier, title
and history. Native Desktop reported its current turn inProgress; the independent
server reported that same persisted turn interrupted and the thread notLoaded.
Those independent runtime fields cannot determine whether Desktop holds the chat.

| Desktop state before probe | external thread/resume result |
|---|---|
| Current chat active | both 0.159.0 and 0.162.1 refused: code -32600, already has an active writer |
| Existing chat idle but loaded | 0.159.0 refused with the same writer conflict |
| Existing chat notLoaded | 0.159.0 resumed successfully to idle |

Native readback retained active and idle respectively for the first two chats. The
unloaded control returned to notLoaded after the probe process exited; its latest
completed turn identifier was unchanged. Successful resume did update its recency
metadata from the historical completion time to the probe time in this installed
version. No turn/start, prompt, generated answer or issue publication was performed.
The probe processes were terminated after inspection. Two attempts through the
managed daemon's proxy received no initialization response before timeout; neither
attempt establishes access to the Desktop-owned backend.

Local evidence is retained under `.local/board-review/desktop-*-read-probe.json`
and `desktop-read-probe.py`. The protocol contract was checked against the
[official app-server documentation](https://learn.chatgpt.com/docs/app-server),
which distinguishes resume from starting generation. This observation establishes
the loaded-chat writer conflict, not impossibility of every external integration.
External generation and visibility of its result in Desktop remain unproven.
The accepted native heartbeat remains unchanged; no detector-first runner or
alternative Desktop transport was installed by this investigation.
