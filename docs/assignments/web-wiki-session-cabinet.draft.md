# xuanxue-cabinet: Cabinet session for web-wiki reading

**Published final acceptance, 2026-11-05:** [original 12](https://github.com/dveyarangi/xuanxue-workshop/issues/12), closed as completed.
This file retains the exactly read-back final issue body; its authority owns the
accepted behavior and explicit evidence exclusions.

**Status: completed — final operator acceptance, 2026-11-05.**

## Accepted outcome and authority

Cabinet browser-session provider is accepted under the [accepted final browser contract](https://github.com/dveyarangi/xuanxue-workshop/blob/8149678f4542a9d87cb916cdb57137394f32b2a2/docs/contracts/web-wiki-session.md#final-operator-acceptance--2026-11-05), immutable Workshop revision `8149678f4542a9d87cb916cdb57137394f32b2a2`. The operator requested closing the six reviewed issues in sequence after the necessity review and browser observations. The final section explicitly governs sufficient evidence and exclusions; it supersedes earlier live-proof and paired-closure gates while preserving shared behavior and recipient ownership.

## Credited evidence

Browser provider source/HTTP/environment/entry/logout checks and staging deployment are credited. The operator reports functioning Cabinet-mediated sign-in/out, original-page return, material reading and refusal after sign-out.

Evidence home: [provider HTTP/entry review](https://github.com/dveyarangi/xuanxue-workshop/issues/12#issuecomment-6171246714). Existing source, executed CI, synthetic and operator-observation provenance remains unchanged; no suite or live scenario was rerun for this closure.

## Disclosed limits and exclusions

Separate live recording delivery and new deployment/exposure/environment reports are excluded from closure. The operator supplied no hostname/revision. This is not a new independently instrumented browser run.

No deployment, configuration, account/data mutation, release or activation is claimed or authorized by closing this issue. The [set-wide final scope](https://github.com/dveyarangi/xuanxue-workshop/blob/8149678f4542a9d87cb916cdb57137394f32b2a2/docs/boundaries.md#final-operator-acceptance--2026-11-05) and [observed-state distinction](https://github.com/dveyarangi/xuanxue-workshop/blob/8149678f4542a9d87cb916cdb57137394f32b2a2/docs/current-system.md#final-chain-acceptance--2026-11-05) preserve those limits. Shared interface/access/preservation behavior remains binding. No further recipient action remains in this accepted assignment; a later concrete defect can be handled in its original without repeating accepted work wholesale.

## BOUNDARY_SUMMARY

```markdown
Existing boundary: Cabinet backend ↔ Cabinet frontend, with local entry points
`api/`, `web/` and `shared/`. Cabinet owns accounts and current account restrictions.
Daychi retains its content backend; Knowledge supplies Daychi's editorial/import
inputs. Current scope/evidence: [Workshop current system](https://github.com/dveyarangi/xuanxue-workshop/blob/3c6ff8a7136483b3d266786fa8267eab4f2d2828/docs/current-system.md).

Accepted target boundaries, joint integration not established: Cabinet backend ↔
Daychi clients for schedule/account capabilities; Daychi backend ↔ Cabinet backend
for authoritative access checks. [Target contracts](https://github.com/dveyarangi/xuanxue-workshop/blob/3c6ff8a7136483b3d266786fa8267eab4f2d2828/docs/boundaries.md#target-connections)
and [native account-session profile](https://github.com/dveyarangi/xuanxue-workshop/blob/3c98d4a5201710f8f777183dd7b61caefe47e2d5/docs/contracts/native-account-session.md) own
their respective scopes; web-wiki work does not change native bearer/private access.

Accepted web-wiki target: Cabinet and wiki share Cabinet's browser session.
Cabinet owns issuance/current-account validation, browser entry/return and logout;
Daychi owns protected web delivery and per-request validation through Cabinet.
All and only valid Cabinet-authenticated web readers receive the same content,
without additional wiki eligibility or persisted wiki reader credentials/accounts.
[Web-wiki session contract](https://github.com/dveyarangi/xuanxue-workshop/blob/3c6ff8a7136483b3d266786fa8267eab4f2d2828/docs/contracts/web-wiki-session.md) owns this boundary.
Daychi's homepage may expose only the contract's separate limited public graph
overview without a Cabinet session. Existing reader APIs remain protected;
entering the reader reuses a valid session or signs in with original-page return.
Daychi owns preview data/projection and exposure controls. This exception changes
no Cabinet wire, account authority, native/private or editorial/import scope.
The contract's environment profiles fix matching production/staging origins and
independent cookie/authority/lifecycle behavior.
Implementation, coordinated anonymous-access cutover and deployed joint proof
remain separate evidence from accepting the target.
```
