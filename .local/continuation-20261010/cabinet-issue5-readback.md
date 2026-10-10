## Recipient and outcome

Recipient: xuanxue-cabinet (`project:cabinet`). Cabinet supplies the school's public dated schedule through `GET /api/public/lessons`, with the agreed valid-only public projection, bounded-window selection and error behavior. Native Daychi consumes the staged pilot; the existing Cabinet student client remains supported.

**Provider contribution completed and accepted on 2026-10-08.** [Workshop acceptance](https://github.com/dveyarangi/xuanxue-workshop/issues/5#issuecomment-6052988637) identifies verified implementation, checks, published records and deployment limits. This closed provider assignment does not establish completion of [daychi-public-lessons #6](https://github.com/dveyarangi/xuanxue-workshop/issues/6) or the joint native connection. The existing fixture-coordination follow-up remains in this original issue.

## Expected / observed

Verified provider implementation: [PR #570](https://github.com/gregoryKot/xuanxue-cabinet/pull/570), merge `868a4edb09926a950b78e8daa3ce495c6e8e256e`, with [successful merge CI](https://github.com/gregoryKot/xuanxue-cabinet/actions/runs/37729360044). [The provider report](https://github.com/dveyarangi/xuanxue-workshop/issues/5#issuecomment-6052693441) and [Workshop review](https://github.com/dveyarangi/xuanxue-workshop/issues/5#issuecomment-6052906591) hold detailed source/check evidence. Workshop's reconciled records were published at [48ddb322c88d4df574f539c616bfce835344a6b9](https://github.com/dveyarangi/xuanxue-workshop/commit/48ddb322c88d4df574f539c616bfce835344a6b9).

| Boundary | Accepted promise | Verified disposition |
|---|---|---|
| Public schedule | Unauthenticated allowlisted lessons; count mode or uncapped bounded-window selection; invalid selected records omitted with error logs | Source and executed checks establish valid-only rows, per-occurrence omission logs, count without refill, uncapped windows, genuine whole-read errors and retained protected-route behavior. No remaining provider deviation was found within this assignment's accepted criteria. |

The earlier `fc2dee2` malformed-row review and all-or-error requirement are superseded by the accepted amendment and verified `868a4ed` contribution. Their timeline remains historical evidence.

Deployment observations at the 2026-10-08 acceptance: staging `https://staging.xuanxue.su` reported `868a4ed`, Mongo up and 63 valid public rows; production `https://xuanxue.su` reported `fc2dee2`. These are dated observations, not claims about the current deployment. Daychi later reported staging reads at `1ad7fb7` in #6; that report does not establish fixture authorization or a full provider re-audit. The configured origin excludes `/api`.

## Shared contract and conformance

Authority: [Public lessons contract and common conformance cases @ 4aec5f84130c2dd8df6875c30fd94c3cf2a5ec74](https://github.com/dveyarangi/xuanxue-workshop/blob/4aec5f84130c2dd8df6875c30fd94c3cf2a5ec74/docs/contracts/public-lessons.md), shared with Daychi #6.

This single immutable reference defines query modes and strict validation, the bare response array, field/identity meanings, selected-window coverage, valid-only best-effort results, omission logging, refresh/error semantics, compatibility and common cases. It adds no version selector, envelope or public completeness metadata. Cabinet owns executable definitions; internal implementation and release remain Cabinet's.

The public endpoint never exposes Zoom links/passwords, credentials or other non-allowlisted fields. A supplied session does not broaden its projection. The authenticated student endpoint retains its protected behavior.

## Provider obligations — implemented and accepted

- Supply the additive unauthenticated GET with exact declared query and error validation. Preserve per-occurrence `id` and `classId`, stable identities through moves/cancellation, scheduled/cancelled rows and start ordering; equal-start tie order is unspecified.
- Supply count mode with default 10 and limit 1–50, applying the limit before validation without refill. Supply a half-open window up to 28 UTC days, selecting all matching candidates without a current-time filter, row cap or pagination and returning their valid projections.
- Omit each selected occurrence with missing class metadata or invalid public data and emit an error-level operator log on that omission path with cause and available identifiers/request ID, without private source or credential leakage. Omit every affected occurrence of a bad shared class. Valid empty strings, absent optional location and missing legacy tags mapped to `[]` remain valid. All-invalid and truly empty selections both return `200 []`.
- Propagate failed lesson/class reads and unexpected code faults as whole-request errors; do not misclassify them as invalid rows or successful empty data.
- Preserve protected student access, existing web consumers and account/reminder behavior. Authentication integration, polling, push, gateway, source cutover and content consolidation remain outside this assignment.

## Execution dependencies and remaining fixture coordination

Recipient work proceeds under its own operator against the accessible settled contract. Workshop readiness, collaboration-installation acceptance and Planned/Ready wording add no implementation or release gate. [Installation #1](https://github.com/dveyarangi/xuanxue-workshop/issues/1) remains a separately accepted outcome.

Actual joint native proof in #6 needs a reachable conforming provider, its exact deployed/executable revisions, Cabinet-authorized controlled fixtures and Daychi's native runtime. A disposable development provider is sufficient. Cabinet owns fixture writes and deployment approval; Daychi stays read-only. No public mutation or clock-setting API is requested.

The [2026-10-10 fixture follow-up](https://github.com/dveyarangi/xuanxue-workshop/issues/5#issuecomment-6090400430) requests the responsible Cabinet operator, authorized environment/origin, fixture/class identities, timing and cleanup for creation, moves within/outside the window, cancellation/restoration, mixed invalid-row omission and repair recovery. Ordinary fixtures may use existing staff controls; corruption/repair cases use disposable development/test data. Production and shared staging data are not corruption targets. No operator reservation or controlled environment is established merely by provider acceptance or reported staging reachability.

## Acceptance evidence

The accepted report and review cover the provider's applicable common cases: 201-row uncapped windows, query/interval/count validation, public allowlisting with and without a session, mixed/shared-class corruption, omission logs, valid empty values, all-invalid empty results, source repair and genuine read failures, plus protected student regressions. No duplicate provider implementation report is required without changed relevant evidence.

Return the remaining fixture arrangement and any changed source/runtime or instruction evidence here with exact revisions and observable outcomes. Actual Daychi native observations and client evidence belong in #6. Provider-local or client-mock checks alone do not complete the joint connection. Workshop acceptance does not release either project.

## Reconciliation and communication

Use this original issue for fixture coordination, questions, changed evidence and follow-up. Existing provider acceptance and completed closure stand. Workshop reviews changed evidence against the same agreement and reconciles the shared records; unresolved shared promise changes return to coordination. No duplicate success issue, provider implementation assignment or Ready acknowledgement is required.
