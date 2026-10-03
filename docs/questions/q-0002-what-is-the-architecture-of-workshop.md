# q-0002 What is the architecture of Workshop?

- **state** open
- **lean** Cabinet ownership of schedule, users, and reminders is accepted; Daychi retains content. Workshop contract, tracker, onboarding, operations, and migration mechanisms remain open.
- **struck** 0, last 2026-10-03T10:43Z

## Direction and evidence

The user rejected a mandatory agreement PR approved by both project owners as too
cumbersome for the current projects (2026-10-03). Their alternative is an idea to
evaluate: a client-domain agent requests an API change through a Workshop ticket;
a backend-domain agent publishes a change and requests consumer migration through
a ticket. The specific flow has not been accepted as architecture.

Inspection of the current local checkouts found:

- Cabinet's api and web share typed route contracts, checked by TypeScript and
  route-registration e2e tests. See [ADR-0148](../../../xuanxue-cabinet/docs/adr/0148-api-route-map-in-shared.md)
  and [the route map](../../../xuanxue-cabinet/shared/src/api-routes.ts).
- Cabinet's agent completes and merges its own green PR to staging; production
  release requires the owner's instruction. See [CLAUDE.md, process 1a](../../../xuanxue-cabinet/CLAUDE.md).
  A new cross-project approval ceremony would add to this existing workflow.
- Cabinet's shared package is private, and its response version header identifies
  a build commit. These do not establish a separately published API compatibility
  version. See [the package](../../../xuanxue-cabinet/shared/package.json) and
  [the version header](../../../xuanxue-cabinet/api/src/common/app-version-header.ts).
- Daychi's mobile schedule, access, and wiki calls currently target its own
  services. See [schedule loading](../../../daychi/apps/practice-app/src/features/schedule/load.ts),
  [access calls](../../../daychi/apps/practice-app/src/features/access/session.ts),
  and [the schedule API](../../../daychi/practice_api/schedule_app.py).
  A domain can therefore be part of a repository; the repository name alone
  does not identify the responsible client or backend.

## Earlier candidate architecture

Historical proposal: the accepted provider assignments now live in
[architecture](../architecture.md). The generic domain directory below does not
override the decision to move schedule, users, and reminders to Cabinet.

Workshop holds a directory of domains and their interface sources, requests between
domains, and change announcements linked to consumer migration work. Interface
definitions and implementation checks remain with the providing project.

A client request names the target domain, missing behavior, affected interface,
and what would unblock the caller. The provider responds on that request with
the implementation reference and its availability. The consumer verifies its use
before the request is considered fulfilled.

A provider-led change announces what changed, its exact revision, compatibility,
and where it is available. Migration tickets are created for consumers that have
work to do. For a breaking change, announce the candidate while the existing
behavior is still supported; consumer migration precedes retiring that behavior.

Use exact source revisions as initial references. A version reference alone does
not imply a deployed endpoint. Agents discover work addressed to their domain when
starting or resuming a task; notification and scheduling machinery remain undecided.

Still to resolve: where shared tickets are authoritative across separate clones,
how domain addresses and claim ownership work, and how published interface changes
and consumer adoption are recorded. This proposal does not choose those mechanisms.

## User process sketch, 2026-10-03

Workshop should extract responsibility boundaries, identify duplication, and reuse
APIs where appropriate. It should hold and maintain the boundary contracts, while
each project's internal architecture stays local. Agents should install the relevant
rules in their own environment, document their boundaries locally, and coordinate
boundary work through Workshop's tracker. Workshop should enforce visibility and
error monitoring through addressed project work. Project agents should periodically
check for tickets addressed to them.

This direction supersedes the earlier candidate's implication that a directory of
interface sources alone is sufficient. The division between Workshop's authoritative
agreement and executable schemas in provider repositories remains an open decision.

The assistant suggested consultation on boundary-related work, tickets when promises
or cross-domain work change, compatibility and migration evidence, verified onboarding,
defined polling occasions, and stable domain ownership with a human fallback. These
are recommendations, not accepted decisions.

The six child questions now hold the unresolved decisions about ownership and reuse,
contract maintenance and checks, change coordination, tracker storage and responsibility,
agent onboarding and discovery, and operational obligations. They were reconstructed
on 2026-10-03 after the user pointed out that the discussion had not been branched.

## Provider ownership decided, 2026-10-03

The user assigned schedule, users, and reminders to Cabinet backend and retained
Daychi videos and other recordings in Daychi. The assistant's earlier four-domain
proposal described the existing repositories too superficially and did not account
for Cabinet's implemented schedule, user, and reminder capabilities. The decision
is recorded in [architecture](../architecture.md); migration is tracked separately.
