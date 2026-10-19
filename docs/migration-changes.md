# Migration compatibility

Accepted behavior is owned by [boundaries](boundaries.md) and its linked contracts;
observed implementations and proof are owned by [current-system](current-system.md).
This record holds compatibility consequences across those agreements. Delivery
scope, recipient actions and acceptance evidence are owned by the existing tickets
and original issues; the [queue](tickets/README.md#queue) holds work order.
The [first-stage goal](stage-1.md) bounds the migration.

## Changes derived from accepted contracts

| Cross-contract concern | Compatibility consequence | Governing agreements |
|---|---|---|
| Schedule identities and reminder choices | Replacing a schedule source also changes the identities joined by selections and reminders. A working public display alone does not establish compatibility of the ordinary account calendar, Mine or reminder path. | [Source cutover](boundaries.md#accepted-schedule-source-cutover), [public pilot isolation](contracts/public-lessons.md#state-refresh-and-effects), [account calendar](contracts/reminder-sync.md#sign-in-guest-state-and-delivery-compatibility) |
| Calendar availability and saved choices | A dated window and saved account choices have different lifetimes. Replacing a successful best-effort window can remove a displayed occurrence and its pending notification without deleting its saved selection; a failed read instead preserves the last confirmed plan. | [Public refresh semantics](contracts/public-lessons.md#state-refresh-and-effects), [reminder calendar reconciliation](contracts/reminder-sync.md#sign-in-guest-state-and-delivery-compatibility) |
| Calendar, reminders and protected access | Public calendar reads, account settings and protected content use different access boundaries. Connecting their clients does not make private meeting details public, turn reminder choices into access rights or merge the native and browser credential lifecycles. | [Schedule access](boundaries.md#accepted-schedule-access), [native account profile](contracts/native-account-session.md), [reminder authority](contracts/reminder-sync.md#accepted-behavior-and-contract-authority), [browser session](contracts/web-wiki-session.md) |

## Compatibility evidence

The [boundary comparison](reconciliation-20261004.md#boundary-comparison) and
[current source evidence](current-system.md) hold the inspected application seams
and their provenance. The [accepted source-cutover condition](boundaries.md#accepted-schedule-source-cutover)
owns the retirement obligation. The contracts' common cases own its applicable
behavior and proof requirements; this comparison supplies no independent work status
or additional contract decision.

## Proposed contribution breakdown

The withdrawn broad investigation pair and its impact assessment are historical
in the [original disposition](reconciliation-20261004.md#withdrawn-contribution-proposal--2026-10-05).
The [owning work records](tickets/README.md#queue) carry delivery scope; this record
contains no parallel contribution or status inventory.

## Impact assessment of the contribution split — refreshed 2026-10-05

The [historical assessment](reconciliation-20261004.md#withdrawn-contribution-proposal--2026-10-05)
preserves the proposal and its disposition at that time.
