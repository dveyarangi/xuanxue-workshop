# Workshop coordination ready — implementation plan

**Authored:** 2026-10-05

Implements [workshop-coordination-ready](../tickets/01-0005-workshop-coordination-ready.md).

## Governing decisions

The [agent contract](../agent-contract.md#workshop-rules) owns Workshop's review,
verification, record-reconciliation and original-issue acknowledgement obligations.
The [exchange contract](../agent-contract.md#exchange-through-github-issues) owns
the accepted conversation history and evidence standard. The user accepted
session entry after recall and the reconciliation connection on 2026-10-05.
The [entry contract](../../AGENTS.md#the-loop) retains decision, publication and
next-cycle checkpoints. Project setup and releases belong to recipient operators.

## Implementation

One `review-assignments` skill discovers issued and incoming cross-project work
and inspects current discussions and closure history. Its description covers
session entry and handling project reports. The mechanism declaration accounts
for its instruction, invocation, maintenance and operator grading.

Project pointers reach the skill through the installed local context. Local rule
L14 holds the review/action/continuation instruction in assignment review.
L15 invokes review after recall. Reconciliation uses the existing review findings.
No acknowledgement
ledger, periodic runner or project-local installation is introduced.

The review distinguishes outgoing assignments from incoming Workshop requests
using the contract and recipient labels. Both open and closed issues are read;
pull requests are excluded. The issue conversation establishes what has already
been answered or accepted. Identity and closure are assessed in context rather
than treating a last author or closed state as proof of verified completion.

Handling follows L14. Publication of revised Workshop records retains commit and
push approvals; acceptance references the resulting record revision or confirms
that no boundary changed. An acceptance response cannot precede the record change
it claims. Relevant evidence re-enters the existing reconciliation pass without
restarting collection or recursively starting another review of the same issue.

Before a reply or closure, a fresh read checks for intervening messages or changed
evidence. Successful writes are read back. Inaccessible tracker evidence remains
explicitly unverified; it cannot justify acceptance, closure or claiming that no
reply needs attention. Independently authorized local work can continue.

## Implementation stages and validation

1. Exercise the existing declaration and binding checks before installation.
   A declaration with its instruction absent must fail; adding the instruction
   must remove that failure. Missing or altered installed context must fail the
   rule checker. These are structure checks, not tests of model judgment.
2. Install the skill, declaration, maintenance binding and shared local rules.
   Run the reference, mechanism and binding gates. Confirm the existing host
   entry and loader links still resolve and recall remains first.
3. Invoke review in this session against all Workshop issues. Record actual
   pending work without sending invented reports or creating demonstration issues.
4. Prepare operator-review scenarios for an obstacle, incomplete result, complete
   installation result, already-closed result, unchanged Workshop answer and an
   inaccessible tracker. Expected outcomes follow the canonical contract and L14.
   The operator grades them; assistant self-assessment is not independent grading.
5. A fresh ordinary Workshop session must demonstrate entry-file loading, recall,
   review invocation and actual tracker discovery. Installation and explicit
   invocation alone cannot establish fresh-entry invocation.
6. Publish only after the existing commit and push approvals. Read back the entry
   and review evidence. Recipient installations and their acceptance remain separate
   outcomes; this coordinator verification does not gate recipient execution.

The 2026-10-08 dependency correction extends L14 to assess necessity as well as
fulfillment against source, checks, runtime and operator evidence. Readiness and
installation acknowledgements do not hold implementation against a settled shared
contract. Actual integration still requires its provider, fixtures and runtime.

Current implementation and verification results are recorded in the
[review evidence](../mechanisms/review-assignments.evidence.md#remaining-readiness-evidence).
The readiness ticket retains independent grading and publication criteria;
structural success alone does not satisfy its whole outcome.

## Impact

Changes Workshop's session-entry instruction, one review skill and declaration,
installed local context, maintenance binding and readiness records. Reconciliation
and session review share L14. The original GitHub issue remains the communication
channel. No sibling implementation, credentials or release process changes.

## Hidden edges

Closed issues may contain unreviewed reports. A later report may follow a Workshop
answer, and messages or evidence can change during inspection. Multiple roles may
use the same connected account, so author identity alone is insufficient. A failed
tracker read cannot establish an empty inbox. Published source does not establish
actual startup invocation or recipient adoption.

## Leave alone

Recipient installations, application contracts and source, gateway/consolidation
deferrals, existing queue order, host question hooks and publication checkpoints.
No automatic background polling or separate review-history file.

## Recommendation

Proceed within the existing readiness ticket. Reuse the installer, declaration
checker and live GitHub tracker; add only the missing instruction and entry
binding. Keep structural installation, explicit review, independent grading,
fresh-entry proof and publication evidence distinct.
