# Windows user task — Board review hosts edge

## Integration

The current-user task WorkshopBoardReview invokes windowless Python directly,
with the controller's absolute path, Workshop working directory, explicit repository,
recipient labels and shared report. It repeats hourly while the computer is running
and the user is signed in. Task policy ignores overlapping starts; an OS-backed
controller lock excludes cooperating external invocations through completion.
Desktop is not a prerequisite. The old same-chat heartbeat is PAUSED.

The active task invokes full review after available discovery. Authentication stays
at the host behind per-run MCP capabilities: selected-issue mutations and allowlisted
repository reads. The shared report exposes meaningful results and failures to wake
and bot readers without automatic Telegram distribution.

## Conformance

- **Discovery** — observed 2026-10-15; the actual Windows task completed a real-board pass at 00:37:01Z with exit 0, candidates 1–13, no read errors and no reviewer invocation. These are the unprocessed baseline, not thirteen newly arrived reports. A second real controller process returned busy while the task held the lock.
- **Review** — observed 2026-10-15 for controlled standalone report handling: a real Codex process read and replaced a test report, preserving its open matter. The actual bot role read the shared report and returned its date and an open matter. Full semantic review was graded separately under the existing proof. Direct sandbox GET user returned HTTP 401; the bounded host alternative then passed a real standalone identity (dveyarangi) and control-issue read, with no raw token transfer. These read/report observations do not establish a completed unattended board batch.
- **Delivery recovery** — documented; the controller retains execution receipts and leaves board progress to the reviewer. Existing issue-publication recovery was independently tested and proven on real GitHub under the prior host. No authenticated standalone publication is claimed.
- **Recurrence** — observed 2026-10-15; the limited current-user interactive task is registered hourly and its manually triggered scheduled discovery completed successfully. Windowless Python avoids the system PowerShell script-policy restriction. The full task is enabled with next run 2026-10-15T05:02:27+03:00. An authenticated controlled standalone invocation passed; the first autonomous hourly tick remains unobserved.
