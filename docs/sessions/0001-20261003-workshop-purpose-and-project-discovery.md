# Workshop purpose and project discovery

Session concluded 2026-10-03. This record covers the investigation and product discussion in this chat; it does not authorize an implementation cycle.

## Work completed and agreed direction

- Investigated Daychi and Xuanxue Cabinet: architecture, deployment, API compatibility, and monitoring. The projects were built independently for the same school; the aim is to enable cooperation while retaining clear ownership.
- Created the Workshop folder and drafted [PRODUCT.md](../../PRODUCT.md). The user accepted the shorter purpose-and-goals style after rejecting a premise-heavy draft. Keep future product writing concrete and avoid repeating the origin story.
- The user wants the Workshop to hold authoritative shared responsibilities and agreements, onboard developers and agents, publish versioned updates, track adoption, coordinate work, and eventually support reservations for overlapping work. The product document describes intended capabilities, not implemented mechanisms.
- Scope remains product definition first. No integration, application source change, deployment, or choice of hosting topology was made in this chat.

## Findings to retain

Xuanxue Cabinet builds its React/Vite frontend and NestJS backend together and deploys them as one Railway service. NestJS serves the frontend and `/api/*` on the same domain. MongoDB Atlas is a separate database; browsers call the backend rather than connecting directly to MongoDB. See the sibling repository's [Dockerfile](../../../xuanxue-cabinet/Dockerfile), [Railway configuration](../../../xuanxue-cabinet/railway.json), and [application module](../../../xuanxue-cabinet/api/src/app.module.ts).

Daychi has an Expo client, its own FastAPI backend, and a wiki. Connecting its client to Xuanxue requires an agreed authentication flow and API/data mapping: cookie sessions versus bearer tokens, schedule formats and visibility, stable identifiers, permissions, and coverage for learning materials. The shared backend is a proposed direction, not an accepted ownership boundary. See the [Daychi architecture](../../../daychi/docs/ARCHITECTURE.md).

Xuanxue has structured logs, request IDs, a custom error journal, Telegram alerts, dependency-aware health checks, optional PostHog, and an optional heartbeat. No Sentry integration was found. Its [runbook](../../../xuanxue-cabinet/docs/RUNBOOK.md) records a 2026-10-02 audit: a scheduled uptime check every six hours was active; heartbeat was not configured in production or staging; no external monitor was observed in the sampled HTTP logs. PostHog production enablement was not verified. Daychi's inspected setup had basic health checks and limited monitoring, with no PostHog or Sentry found. Configuration support must not be reported as verified operation.

The same domain can route `/something/` to a separately deployed app through a reverse proxy. Railway's documented [Edge Rules](https://docs.railway.com/networking/edge-rules) do not provide an origin-routing action. A proxy can reach another account's app over public HTTPS; [private networking](https://docs.railway.com/networking/private-networking) is scoped to one project and environment. The app must support its URL prefix. No separate fee applies to the path itself: a proxy consumes ordinary service resources, potentially within existing plan credits. Pricing was checked on 2026-10-03; recheck [Railway pricing](https://docs.railway.com/pricing) before budgeting.

Research discussed Git-versioned agreements, API specifications, a shared issue board, compatibility checks, explicit review ownership, and adoption tracking. These are candidates; no particular board, contract tool, or reservation mechanism was selected. Agent instructions alone cannot guarantee compatibility or current adoption.

## Open questions and continuation

The product document remains the governing draft. The following discussion points have no accepted answer there yet; this section preserves the documentation gaps rather than treating suggestions as decisions.

1. **What belongs in the finished product goals?** Consider decision authority and conflict resolution, shared domain semantics, reproducible integration environments, migrations and rollback, contributor access and handoffs, authoritative versus derived records, completion criteria, and low overhead for routine work. These were suggested after the user asked what was missing; they have not been incorporated or accepted individually.
2. **Who owns each shared capability?** Identify provider, consumers, data owner, accountable person, reviewer, release responsibility, and failure response. Schedules and materials overlap today. Do not infer that Xuanxue owns everything merely because Daychi might consume its API.
3. **How will shared instructions and agreements evolve?** Define bootstrap behavior, reread/rebootstrap triggers, version compatibility, publication, adoption evidence, and exceptions before choosing their storage and tooling. The user proposed a bootstrap entry point; none was implemented by this chat.
4. **How will concurrent cross-repository work coordinate?** Define the protected scope, reservation conflicts, expiry, renewal, takeover, and enforcement. The `/impact` approach in `D:/Dev/AI/agents` was mentioned as a possible starting point, not selected as the solution.
5. **Which operational promises will be required?** Decide health, error reporting, alert ownership, verification frequency, and evidence of enablement. Hosting under one domain does not settle authentication, ownership, or operational responsibility.

Continue from the maintained [delivery status](../tickets/README.md), whose candidate is the first `/align` on PRODUCT.md. Do not turn this handoff into an approved implementation plan.

## Workspace state and unfinished verification

- At conclusion the Workshop is an initialized Git repository on `master` with no commits. PRODUCT.md, README.md, the development harness, local rules, and docs are untracked. The harness appeared in the current tree outside the product-writing work of this chat; preserve it. No commit or push was made here.
- Delivery status records harness installation at `ad971a4`, with installation gates passed. It also records Windows loader symlinks still to create and host hooks not yet observed in a fresh session. Those are existing installation follow-ups, not completed by this conclusion.
- No question store existed when `/conclude` read it; there were no existing question records on which to write lean updates. Open discussion is retained above.
- The user canceled local startup. The temporary Docker container `xuanxue-local-mongo-20261002` was stopped at cancellation; no app server was started. The `mongo:8.0` image and partial npm dependencies/cache under the workspace's `.local/npm-cache` may remain. This conclusion did not recheck Docker state or perform cleanup.
- Investigation found Windows verification issues in Xuanxue: file-URL entry guards in `scripts/check.mjs` and `scripts/check-prod-health.mjs` can skip execution, and `scripts/ci-main-concurrency.test.mjs` failed with CRLF checkout lines. No fixes were authorized or made. Selected Daychi schedule/access-link/wiki tests passed and Xuanxue's environment-example check passed; this was not a full integration verification.
