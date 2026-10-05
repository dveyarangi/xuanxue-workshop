# Shared contract shape

A shared boundary contract defines the externally observable interface and its
guarantees for all affected providers and consumers. Internal implementation is
outside this shape. Each applicable dimension below has one agreed definition;
an inapplicable dimension has an explicit reason. Missing information is unresolved,
not permission for recipients to choose independently.

| Dimension | What must have one meaning across the boundary |
|---|---|
| Authority and scope | Provider, consumers, data owner, authoritative source, supported operations and explicit exclusions. |
| Operations and transport | Routes and methods; path, query and header parameters; media types, encoding and applicable transport/client requirements. |
| Requests | Field names, types, formats, units, required/optional fields, defaults, enums, null/omission meaning, validation and conflicting-parameter behavior. |
| Responses | Envelope and fields, types, formats, units, nullability, field meanings, derived values and metadata. |
| Identity and relationships | Identifier scope and uniqueness, relationships, deduplication keys and identity continuity through changes. |
| Time and intervals | Timestamp/date formats, offsets and timezone, calendar/DST rules, interval boundaries and which events fall within a requested window. |
| Data guarantees | Selection/filter semantics, source, coverage, completeness, ordering, duplicate handling, supported bounds, limits, pagination and empty-result meaning. |
| State and consistency | Snapshot/delta semantics, freshness and revision meaning, atomicity/concurrency guarantees, removals, retention, conflicts and isolation where applicable. |
| Access and exposure | Credentials and their permitted use, authorization, public/private fields, redaction and applicable lifecycle/revocation guarantees. |
| Failures and recovery | Status/error codes and bodies, validation failures, refusal/unavailability distinction, retryability, retained state and recovery behavior. |
| Effects and delivery | Mutation/side-effect meaning, idempotency, retry/duplicate behavior, ordering and delivery guarantees where applicable. |
| Evolution and compatibility | Exact contract revision, supported consumers, compatibility obligations and transition/retirement conditions. |
| Acceptance | Common request/response examples and expected outcomes, boundary/failure cases, conformance checks, supported test environment and version-bound evidence. |

Completeness does not add a guarantee the scope has not agreed. A best-effort
behavior, unsupported operation or absent guarantee is explicit where it affects
interoperability. An internal algorithm, module layout, storage choice or UI
presentation remains free unless its observable effects are part of the contract.

One accessible immutable contract reference is the authority for each boundary
version. Per-recipient issue text describes that recipient's action against it;
it is not a second contract definition. Examples and conformance outcomes belong
to the same reference and agree with its definitions.
