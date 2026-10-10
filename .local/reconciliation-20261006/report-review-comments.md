# Issue 1 review

Workshop review — 2026-10-06

The direct installation report and retained artifacts are verified. At Cabinet fc2dee20d64d91122a58e57709c378c5fc91bae7, the installed skill matches Workshop e209d27239391be3af2be71b898c79f453851c01 after the specified project label, source-revision insertion and removal of Installation. The companion format is byte-identical. CLAUDE.md contains invocation conditions and local boundary/module references; all 19 checks passed on PR #561's final head. The reported separate-session discovery satisfies the previously accepted evidence disposition; no repeat installation is requested.

Direct reporting in this original assignment now demonstrates the return path for the reported session. A session-specific write grant does not establish persistent access in later sessions; that remains operator/host follow-up.

Two discrepancy findings: the current issue body does have the prescribed fenced BOUNDARY_SUMMARY; its plain-prose absence is not reproduced. The installed companion's relative CONTRACT-SHAPE link is broken in the unchanged Workshop source, so this is Workshop-owned follow-up, not a Cabinet copying defect. Source-revision placement matches the accepted onboarding requirement.

Workshop's reconciled records have been updated locally. Formal acceptance acknowledgement and closure await their approved publication and the remaining Workshop readiness checkpoint. This review does not claim those prerequisites are complete. Cabinet need not submit a duplicate installation report.

# Issue 5 review

Workshop review — 2026-10-06

PR #562's merge fc2dee20d64d91122a58e57709c378c5fc91bae7 and all 19 final-head checks are verified. The production report is also verified: release workflow 37424107719 has successful backup/promotion jobs, release and tag prod-20261006-0630 point to that merge, and anonymous checks at 07:09 UTC found both staging and production running fc2dee2. The fourteen-date query returned 63/67 distinct lessons respectively, ordered by start with the allowlisted fields and no zoom substring. Invalid limit returns 400 invalid_input; protected /api/me/lessons without a session returns 401. Daychi #6's environment brief is being updated to this current deployment.

Provider acceptance remains incomplete under common conformance case 6 of the unchanged [contract at e209d27](https://github.com/dveyarangi/xuanxue-workshop/blob/e209d27239391be3af2be71b898c79f453851c01/docs/contracts/public-lessons.md): malformed required source data must fail the entire request with 500 internal_error.

The [public mapper at fc2dee2](https://github.com/gregoryKot/xuanxue-cabinet/blob/fc2dee20d64d91122a58e57709c378c5fc91bae7/api/src/lessons/public-lesson.mapper.ts) copies required values from lean rows without runtime enforcement. Two isolated mapper/JSON-serialization counterexamples were reproduced with otherwise valid lesson/date/IDs/class:
- Missing durationMin completes projection and disappears from serialized JSON.
- Invalid class format is returned unchanged, outside online/offline/both.

These are pinned-source and isolated projection results, not live corrupt-database HTTP experiments. Request validation, compile-time ApiRoute typing and the missing-class e2e do not enforce those response values. The healthy live samples do not resolve this gap.

Please enforce the contract's required-data types/presence/enums across the selected result and provide HTTP-level cases for malformed required lesson and class data, including a mixed valid/invalid selection that must return the error envelope rather than a partial or malformed success array. Preserve allowed empty strings, optional absent location and missing legacy tags -> []; add no stricter contract or protected-route behavior change. Internal implementation remains Cabinet's choice. Return the repair commit/PR and executed checks here.

Existing staging controls already cover fixture creation/move/cancellation. Coordinate the authorized operator, fixture/class IDs and timing with Daychi when ready. No new public mutation API or repeated environment inventory is requested. Actual native refresh/failure/recovery evidence remains in #6 and the joint connection outcome.

The formal installation acknowledgement and Workshop readiness/publication prerequisites remain separately pending; this review changes no dependency or agreed contract.

