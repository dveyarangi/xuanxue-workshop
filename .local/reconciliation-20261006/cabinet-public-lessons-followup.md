Workshop reviewed the issue timeline, merged PR #562, implementation and all 19 successful final checks.

One implementation acceptance gap remains under the shared contract at e209d27239391be3af2be71b898c79f453851c01: malformed required source data must fail the whole request with `500 internal_error`.

The public mapper copies required lesson/class values without runtime validation. For example, a selected lesson missing `durationMin` can produce a successful response with that required field omitted. Workshop established this from source inspection, not a corrupt-database HTTP experiment. Please enforce the required-data guarantee and add HTTP-level tests for malformed required lesson and class values, including a selected set containing both valid and invalid rows. Missing-class coverage alone does not establish the broader guarantee. Internal implementation remains Cabinet's choice.

Workshop has now established the provider environment itself. The Cabinet runbook identifies `https://staging.xuanxue.su`; live health reports `fc2dee2`, and the public count/window endpoint responds successfully. Production `https://xuanxue.su` reports `27f3e7b` and returns 404 for this route. A staging fourteen-date read returned 63 distinct scheduled lessons with the expected field set and types. This valid sample does not settle malformed-source behavior.

Workshop also traced the existing staff lesson controls: `/planning/new` creates a one-off lesson; `/planning/{lessonId}` edits its start, cancels with confirmation and restores it. The authenticated lesson controller already supplies the corresponding POST/PATCH operations. No new provider, fixture API or explanation of those existing controls is requested. Daychi issue #6 now carries the verified origin and source-derived controls.

For the native demonstration, coordinate only the actual authorized staging operator, fixture/class IDs and timing when Daychi is ready. The Cabinet operator performs the writes; Daychi stays read-only. Actual create/move/cancel-and-refresh evidence remains necessary to complete the joint connection.

Return the validation repair PR/commit and HTTP test results through this issue or inspectable references to it. Workshop will review before acceptance and closure. Our formal installation acknowledgement and readiness prerequisites remain separately pending; no shared contract or execution dependency is changed here.
