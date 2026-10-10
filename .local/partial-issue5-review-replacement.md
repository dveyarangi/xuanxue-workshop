Workshop review — 2026-10-06; policy follow-up — 2026-10-07

PR #562's merge fc2dee20d64d91122a58e57709c378c5fc91bae7 and all 19 final-head checks are verified. The production report is also verified: release workflow 37424107719 has successful backup/promotion jobs, release and tag prod-20261006-0630 point to that merge, and anonymous checks at 07:09 UTC found both staging and production running fc2dee2. The fourteen-date query returned 63/67 distinct lessons respectively, ordered by start with the allowlisted fields and no zoom substring. Invalid limit returns 400 invalid_input; protected /api/me/lessons without a session returns 401. Daychi #6's environment brief is being updated to this current deployment.

The user has amended the public pilot's failure policy. The [current Cabinet
amendment](CABINET_AMENDMENT_URL) and its immutable contract supersede this
review's whole-request-500 repair instructions. The previous public pilot is
not yet used; no version/legacy operation is required. Corrupt individual records
are omitted with an error log while valid records remain available. Genuine
operational failures still fail the read.

The [public mapper at fc2dee2](https://github.com/gregoryKot/xuanxue-cabinet/blob/fc2dee20d64d91122a58e57709c378c5fc91bae7/api/src/lessons/public-lesson.mapper.ts)
copied required lean values without runtime enforcement. Isolated counterexamples
showed missing duration omitted from serialized JSON and invalid class format
returned unchanged. These are pinned-source findings, not live corrupt-database
experiments. They remain invalid public data under the amended contract.

Keep valid public field enforcement; implement the omission/error-log and HTTP
cases specified in the newer amendment instead of whole-read failure on corrupt
records. Preserve empty strings, absent optional location, missing legacy tags
-> `[]`, public exposure boundaries and protected student behavior. Report code
and executed checks in this original issue.

Cabinet installation is [accepted in #1](https://github.com/dveyarangi/xuanxue-workshop/issues/1#issuecomment-6011474155).
Native evidence remains with [daychi-public-lessons #6](https://github.com/dveyarangi/xuanxue-workshop/issues/6)
and the combined connection. This review does not claim amended deployment or
acceptance.
