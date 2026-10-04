# Backend consolidation horizon

[daychi-backend-capabilities-in-cabinet](tickets/01-0010-daychi-backend-capabilities-in-cabinet.md)
is a blocked HITL horizon record, accepted as the admission straw dog's binding on
2026-10-04. Its membership is one end-to-end consolidation outcome; no implementation
split, contributor dispatch, or application change is authorized by that binding.

## Impact

Consolidation transfers content ownership, persistence, API behavior, imports, and
operations across Daychi and Cabinet. Inspection found four protected read routes,
four conditional public read routes, and two administrative import/status routes.
The content core spans 528 lines in four Python modules, with 16 existing backend
regression scenarios. Both the mobile client and the separate web wiki consume it;
Cabinet's existing library must retain its behavior. Authentication unification is
also a dependency of the already accepted user-ownership direction.

## Hidden edges

Client bookmarks refer to stable material IDs; Cabinet's existing materials use
Mongo ObjectId. Search must account for Cabinet's encrypted material titles.
Annotation storage preserves source bindings, revisions, and atomic replay-safe
imports. The importer uses Daychi's administrative session and CSRF contract.
Public content projections exclude protected connection data. The source index,
identity database, and annotation database are outside this checkout, so actual
record counts, collisions, and cutover duration are unmeasured. Full service
retirement also covers access flows, feedback, schedule/Zoom, hosting, and downloads.

## Leave alone

Existing client design, stable references, local reminders, Cabinet-only workflows,
external media hosting, and separate content-preparation scripts. The consolidation
record requires explicit disposition of remaining service duties rather than
silently discarding them.

## Recommendation

Narrow execution to an agreed scope after data inventory and compatibility/rollback
assessment. Retain one coarse horizon record for the end-state; defer its internal
split to that assessment. Creation of the record only supplies the named successor
required by the accepted straw dog.
