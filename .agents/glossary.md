# The development method

The vocabulary the harness itself is written in — the terms its skills, rules, records and checks
use. It travels with `.agents/`. A project's own domain vocabulary belongs in `docs/glossary.md`,
which the project owns outright; when a term here and a term there collide, the project's wins
inside its own domain and this one wins about the method.

These definitions are a working vocabulary for alignment; a proposed distinction does not by
itself authorize new process machinery.

## Language

**Harness**:
The development instructions and supporting mechanisms through which projects define, implement, verify and maintain software, including the harness itself.

**Mechanism**:
A part of how the work gets done — the development method and its machinery — on which other work relies, together with its instructions, producers, consumers, checks and records. It has exactly one instruction file and may span many other files. What the project produces is not one.

**Skill**:
A mechanism's own instruction file, invocable and identified by its purpose and conditions of use. A skill may also host rules installed into it by mechanisms that do not own it.

**Straw dog**:
Text or code a live ticket will change, wrapped in a `<straw-dog>` bound to that ticket at the moment it is written. Unwrapped, it is drift the enumerator cannot see. What no ticket would change is a claim.
_Avoid_: temporary statement, temporary, placeholder, stub, interim, hack.

**Rules file**:
The one authored home of the rules a mechanism installs into skills, its own included: `<slug>.rules.md` in its own directory, machine input for the installer, read by nobody at session time.

**Installed block**:
A mechanism's rules as they reach a skill: one `<installed>` block per mechanism per target, written by the installer from the rules file and compared against it, never edited where it sits.
_Avoid_: injected pointer, copy.

**Part**:
A file or asset a mechanism owns: installing the mechanism adds it, uninstalling removes it. What a mechanism leans on but would not take with it is relied-on, named with its owner, and not one of its parts.
_Avoid_: component, piece, asset.

**Moment**:
An occasion at which a person acts on a mechanism. Each is either instructed, or carries a stated kind of absence. If nobody acts, it is not a moment.

**Doc**:
The record of why a mechanism's instruction is what it is — the documentation of a mechanism. Never the same file as the instruction.
_Avoid_: manual, reference, spec as a name for this.

**Documentation**:
The role a doc plays for an implementation: what it must do and why. A mechanism's doc for its skill and scripts; a project's architecture for its code.
_Avoid_: spec, manual.

**Implementation**:
What a documentation describes and must agree with: a mechanism's instruction file and scripts; a project's code.
_Avoid_: source; product as a synonym.

**Record**:
What a mechanism writes and keeps under a declared format, live until archived: a ticket, an RFC, a session record, the marks. An entry is one row of a record that holds many.
_Avoid_: log.

**Mark**:
The row a maintenance writes when it has re-checked a mechanism at a level: the fingerprint of what it checked against, the date, and the outcome. Only the maintenance that finished the re-check writes one; no edit to a doc is a mark.
_Avoid_: timestamp, last-checked, checkpoint.

**Due**:
Said of a mechanism at a level when what governs it has moved since its mark, or it has none — *never maintained*. Derived at every look, never stored.
_Avoid_: stale, dirty, pending.

**Evidence**:
The record of why a doc is what it is: what was tried, what was refuted, what it cost, what it used to be. One per mechanism. Evolution belongs here; provenance does not.
_Avoid_: sidecar, notes, history, appendix. *Sidecar* describes a file's position, never its contents.

**Provenance**:
Who decided a rule and when, carried inline on the rule itself. It is not evidence and does not move to the evidence file: attribution at the moment of reading is what makes a rule challengeable.

**Authority**:
Who may establish, amend or waive a rule. Stated on the rule, inline, as its provenance; the repair policy says what a maintainer may do with the rest. Separate from delivery tier and from evidence of effectiveness.
_Avoid_: strict rule, working rule, rule strength.

**Tier**:
How a thing reaches a session — forced into context, asked for, or reachable only by someone who already knows it exists. Reachability, never importance or read-frequency.

**Index**:
A compact list of a register's records, derived from them on request rather than kept beside them. Enough per record to decide whether to open it, and never a second home for what the record already says.
_Avoid_: digest, summary, table of contents.

**Core**:
The accepted shared method and supporting assets governed at their canonical source.

**Project-local**:
A project's own answers and overrides, authored once in its local rules file beside the entry file and reaching core files only as the local block the installer writes there, after every mechanism's. An override names the rule it overrides and is what the reader follows.

**Install** *(of core)*:
Placing a ref of core into a tree that is not core's own repository, from a fresh clone of that repository and never from a working tree; an update is the same over a tree that already holds one, and a check compares a copy against the ref its entry file announces. The mechanism that does all three is `harness`.
_Avoid_: deploy, sync, distribute, port.

**Installation edge**:
Everything about the core–instance interaction an instance must know to integrate core, customise it and stay coherent across core changes: a rule id, a target and its anchor, a script's path and command, a skill's name, the announce form, and a behaviour a recipient's files rely on. What a recipient never meets — a skill's body, a declaration's prose, a script's internals — is not on it.
_Avoid_: API, surface, interface as names for this.

**Release**:
One publish of core to its own repository, carrying a note written for an instance: what moved on the installation edge, from where to where, and what an instance amends. The note is derived at the publish from the edge's engineering record, which every edge change writes its line in as it is made. A recipient reads the notes standing between its ref and the latest before deciding to take them.
_Avoid_: version, cut, ship, distribution.

**Recipient**:
A tree that received core by install. Its entry file's announce line names the repository and the ref it came from, `<repository>@<ref>`; the one tree whose line carries no `@` is core's own repository, the origin, and is never installed into.
_Avoid_: instance as a name for the tree, consumer.

**Painted door**:
A path under `docs/` that a mechanism declares as where its records live — the directory, or the one file that is a record — and thereby reserves in every recipient: core may name it, and a record written there makes it. Some arrive with content, where the owning mechanism declares what the record says before anything has happened in it; the rest come into being when the first record is written. A particular record inside one is a document, not a painted door.
_Avoid_: place, path convention.

**Leak**:
A citation from core to a document only the instance has. A painted door is not one; a particular record behind it is.
_Avoid_: reach, dangling link, cross-reference as names for this.

**Open issue**:
An unresolved problem, question or risk that needs a disposition. It is unresolved subject matter, not a synonym for a spec, ticket or RFC; its current owning record holds it.
_Avoid_: issue as a generic name for every development document.

**Spec**:
A change-scoped definition of intended capability, scope and governing behavior from which delivery work can be derived. Its enduring agreements belong in maintained governing documents; its eventual historical status does not itself establish that the change was delivered.

**Architecture**:
The maintained description of system responsibilities, load-bearing seams and governing constraints, with the status of current and agreed target behavior explicit.

**Capture**:
Recording an issue with enough context to preserve its meaning and an identifiable owner. Capture does not by itself authorize investigation, implementation or a new mechanism.

**Routing**:
Selecting the existing record or kind of work that should own an issue, and the next applicable development stage.

**Decomposition**:
Dividing agreed work into independently verifiable parts while preserving its scope, contracts and dependencies.

**Pace**:
Which authorized work proceeds now, pauses, or awaits a decision. Pace is distinct from the scale or document type of the work.

**Execution step**:
The execution of a single skill. It has an input state, an immediate purpose, an expected result and a reassessment boundary at its end, and need not complete its owning ticket.

**Turn**:
One agent reply, from the user's message to the reply's end. A turn holds at most one execution step; a step may span turns.

**Archived record**:
A historical account retained after its active role ends, with its disposition explicit. Current work should be understandable from maintained sources without requiring that record; historical investigation and mechanical maintenance may still reach it.

**Ticket**:
A tracked unit of work with an intended outcome and observable completion criteria. It may own unresolved decisions before implementation is ready.

**Ticket stage**:
What a ticket holds, read from whether it has a plan. Incepted — no plan yet — it hosts chunks: routed inputs, ideas, open questions. Shaped — its plan exists — it keeps only what is actual: the work, its criteria, and what is still open. A resolved decision lives in its durable home and in the session record, not in the ticket.
_Avoid_: dossier, decision log, history as names for a ticket's contents.

**HITL ticket**:
A ticket whose progress requires a human decision or interaction. Its scope may still be undecomposed, but HITL does not itself specify size or maturity; investigation can reveal a need for a spec and multiple delivery tickets.

**RFC**:
An implementation proposal or agreed plan for an owning ticket, grounded in the governing architecture and contracts. Its existence alone does not mean its proposal has been accepted.

**Shape**:
Whatever is currently under consideration, held between an idea and a thing: it has taken enough form to have a context and a structure, and is not yet exhausted by any one realization. A concept, contract, invariant, behavior, rule, method or artifact can each be held as a shape.

- Idea — "historical forecasts should stay comparable." No form yet; `/align` owns it.
- Shape — "historical forecast issues must remain independently addressable by (location, valid_time, issue_time)."
- Thing — "forecasts are stored in the `forecast_hourly` collection." One realization.

Being a shape says nothing about being load-bearing. An implementation method is a shape, and can be a rich one that repays `/impact` and `/discover`, while remaining local to the code it lives in.
_Avoid_: form, construct, entity.

**Seam**:
A boundary across which a producer supplies behavior, information or an artifact that a consumer relies upon.

**Load-bearing seam — proposed definition**:
A seam across distinct responsibilities whose contract determines a promised outcome, authority, data meaning or integrity, compatibility, or recovery beyond either side's implementation-local choices. A change that appears valid at one end can invalidate the other end or their shared guarantee.

**Principle**:
A reason a rule exists, read at tier 1 and applied by judgement. It names no occasion and no outcome, so it never fires and is never a rule failure: a principle that "did not fire" is a rule missing. Its home is the entry file's general section, a mechanism's doc, or this glossary; in an instruction file it appears only as the pointer behind a rule.
_Avoid_: rule, guideline as its name.

**Rule**:
An instruction with a moment — the occasion, in the words a person would use for it — and an outcome that can be checked afterwards. Its home is a rules file, installed at the tier its moment reads, citing the principle behind it. A judge's invocation is a rule; what the judge judges by is a principle.
_Avoid_: principle, for an instruction that has no moment.

**Meta-rule**:
A rule governing how other rules or mechanisms are created, changed, checked or maintained.

**Tier 1**:
Context supplied to the agent at the relevant occasion without a separate retrieval action. Intended Tier 1 placement and observed delivery are distinct facts.

**Tier 2**:
Content retrieved when a Tier 1 trigger or reference makes it relevant. A request to read content does not itself establish retrieval.

**Rule slice**:
The selected portion of governing instructions relevant to a particular task, stage or event, retaining its source and applicability.

**Delivery evidence**:
An observation supporting that selected content reached the agent's context. It is distinct from a file existing, a hook emitting output, or evidence that the instruction was followed.

**Derived work**:
An artifact or behavior produced or maintained under a governing rule or contract, whose validity may need reassessment when that source changes.

**Reconciliation**:
Resolving differences between independently evolved states against their origins and governing agreements, retaining unresolved differences until they have a disposition.

**Entry contract**:
The instructions every host supplies at session start, versioned, and announced verbatim by the session's first reply as evidence of delivery.

**Autonomy switch**:
A named setting a project gives a value to, deciding whether an action proceeds or waits for a human; skills defer to it.

