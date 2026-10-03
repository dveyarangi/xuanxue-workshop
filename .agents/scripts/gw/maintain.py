"""Which mechanisms are due for a re-check, from marks only a maintenance writes.

    uv run --offline --no-project python .agents/scripts/gw/maintain.py --check
    uv run --offline --no-project python .agents/scripts/gw/maintain.py --mark <mechanism> <level> <outcome>

A mechanism is checked at two levels. At `rules` its doc is due when the meta-rules moved since
its mark; at `output` its records are due when its own doc, rules file or skill moved since its
mark. A mark is the fingerprint of what a maintenance checked, written by `--mark` when the
maintenance finishes and by nothing else: no edit to a doc counts as a re-check. Dueness is
derived at every look and never stored. The marks' format is `/maintain`'s, in the format shelf
beside its skill, `MARKS-FORMAT.md`.

`--check` never fails on a due mechanism — being due is the news, not a defect — only on marks it
cannot read or a surface it cannot fingerprint. In a recipient the built-in mechanisms are
maintained where core is made, so the clock covers the recipient's own mechanisms alone.
"""

from __future__ import annotations

import hashlib
import json
import re
import sys
from dataclasses import dataclass
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import inject_rules  # noqa: E402  (path set just above)
from docs_corpus import ENTRY_FILE, INSTALLED_OPENING, announced, without_code  # noqa: E402
from mechanisms import Declaration, declarations  # noqa: E402

MARKS = "docs/mechanisms/maintenance.md"
# The mechanism whose rules every mechanism's doc is written to.
SHAPE = "mechanism-shape"
EVIDENCE = "EVIDENCE.md"
# TODO: a third trigger — a mechanism's records changed
# enough since its mark — waits for each mechanism to declare where its records live.
LEVELS = ("rules", "output")
NEVER = "never maintained"
DUE = "due"
CURRENT = "current"
WHY_MOVED = {
    "rules": "the meta-rules moved since its mark",
    "output": "its doc, rules file or skill moved since its mark",
}
WHY_BUILT_IN = "a recipient's built-in mechanisms came with core, maintained where core is made"
OUTCOMES = ("amended", "nothing to change")
COLUMNS = ("mechanism", "level", "fingerprint", "date", "outcome")
_FINGERPRINT = re.compile(r"^[0-9a-f]{64}$")
_USAGE = "usage: maintain.py --check | --mark <mechanism> <level> <outcome>"


class Refused(Exception):
    """A mark that must not be written. The message says what to settle first."""


class Unreadable(Exception):
    """A surface that cannot be fingerprinted. Guessed around, it would read as current."""


@dataclass(frozen=True)
class Mark:
    """One row of the marks: what a maintenance checked one mechanism's level against, and when."""

    mechanism: str
    level: str
    fingerprint: str
    date: str
    outcome: str

    @property
    def row(self) -> str:
        return f"| {self.mechanism} | {self.level} | {self.fingerprint} | {self.date} | {self.outcome} |"

    def as_record(self) -> dict:
        return dict(zip(COLUMNS, (self.mechanism, self.level, self.fingerprint, self.date, self.outcome)))


@dataclass(frozen=True)
class Standing:
    """Where one mechanism stands at one level: due, current, or never maintained, and why."""

    mechanism: str
    level: str
    state: str
    why: str | None

    def as_record(self) -> dict:
        return {"mechanism": self.mechanism, "level": self.level, "state": self.state, "why": self.why}


@dataclass(frozen=True)
class Checked:
    """What one reading of the marks against the declarations found."""

    standings: list[Standing]
    built_in: list[str]
    """In a recipient, the mechanisms it received with core and does not maintain."""
    undeclared: list[Mark]
    """Rows whose mechanism is no longer declared: dropped at the next mark, so reported, never failed."""
    diagnostics: list[str]

    def as_record(self) -> dict:
        return {
            "mechanisms": [standing.as_record() for standing in self.standings],
            "built in": {"why": WHY_BUILT_IN, "mechanisms": self.built_in},
            "undeclared": [held.as_record() for held in self.undeclared],
            "diagnostics": self.diagnostics,
        }


def main(argv: list[str], root: Path | None = None, today: date | None = None) -> int:
    root = root or Path(__file__).resolve().parents[3]
    if argv == ["--check"]:
        checked = check(root)
        print(json.dumps(checked.as_record(), indent=2))
        return 1 if checked.diagnostics else 0
    if len(argv) == 4 and argv[0] == "--mark":
        report = mark(root, *argv[1:], today or date.today())
        print(json.dumps(report, indent=2))
        return 1 if report.get("refusals") else 0
    print(_USAGE)
    return 2


def check(root: Path) -> Checked:
    """Every clocked mechanism at every level, with why it stands where it does."""
    declared = declarations(root)
    clocked = _clocked(root, declared)
    held_marks, unreadable_marks = _read_marks(root)
    standings, unreadable_surfaces = _standings(root, declared, clocked, held_marks)
    return Checked(
        standings,
        built_in=[one.slug for one in _built_in(root, declared)],
        undeclared=[held for held in held_marks if held.mechanism not in _slugs(clocked)],
        diagnostics=unreadable_marks + unreadable_surfaces,
    )


def mark(root: Path, mechanism: str, level: str, outcome: str, today: date) -> dict:
    """Write the one row saying `mechanism` was maintained at `level` against what it reads now.
    Anything it cannot stand behind is refused before a byte is written."""
    declared = declarations(root)
    held_marks, unreadable = _read_marks(root)
    try:
        if unreadable:
            raise Refused(f"the marks do not read — {unreadable[0]}; repair them before marking over them")
        marked = _markable(root, declared, mechanism, level, outcome)
        fingerprint = _fingerprint(root, _surface(root, declared, marked, level))
    except (Refused, Unreadable) as refusal:
        return {"refusals": [str(refusal)]}
    written = Mark(mechanism, level, fingerprint, today.isoformat(), outcome)
    _write_marks(root, _kept(held_marks, _clocked(root, declared), written) + [written])
    return {"marked": written.row}


def _kept(held_marks: list[Mark], clocked: list[Declaration], written: Mark) -> list[Mark]:
    """Every row a new mark leaves standing: not the one it replaces, and none for a mechanism no
    longer declared, which is how such a row leaves."""
    return [
        held for held in held_marks
        if held.mechanism in _slugs(clocked) and (held.mechanism, held.level) != (written.mechanism, written.level)
    ]


def _standings(
    root: Path, declared: list[Declaration], clocked: list[Declaration], held_marks: list[Mark]
) -> tuple[list[Standing], list[str]]:
    """Where each clocked mechanism stands at each level, and each surface that could not be read
    — said once, though every mechanism's `rules` shares one."""
    marks = {(held.mechanism, held.level): held for held in held_marks}
    standings: list[Standing] = []
    unreadable: list[str] = []
    for mechanism in clocked:
        for level in LEVELS:
            try:
                fingerprint = _fingerprint(root, _surface(root, declared, mechanism, level))
            except Unreadable as reason:
                unreadable.append(str(reason))
                continue
            standings.append(_standing(mechanism.slug, level, marks.get((mechanism.slug, level)), fingerprint))
    return standings, list(dict.fromkeys(unreadable))


def _slugs(mechanisms: list[Declaration]) -> set[str]:
    return {one.slug for one in mechanisms}


def _markable(root: Path, declared: list[Declaration], mechanism: str, level: str, outcome: str) -> Declaration:
    if level not in LEVELS:
        raise Refused(f"{level} is not a level; a mark is at {' or '.join(LEVELS)}")
    if outcome not in OUTCOMES:
        raise Refused(f"{outcome} is not an outcome; a maintenance ends {' or '.join(OUTCOMES)}")
    if mechanism in _slugs(_built_in(root, declared)):
        raise Refused(f"{mechanism} came with core and is maintained where core is made")
    clocked = {one.slug: one for one in _clocked(root, declared)}
    if mechanism not in clocked:
        raise Refused(f"{mechanism} is not a declared mechanism")
    return clocked[mechanism]


def _standing(mechanism: str, level: str, held: Mark | None, fingerprint: str) -> Standing:
    if held is None:
        return Standing(mechanism, level, NEVER, "no mark")
    if held.fingerprint != fingerprint:
        return Standing(mechanism, level, DUE, WHY_MOVED[level])
    return Standing(mechanism, level, CURRENT, None)


def _clocked(root: Path, declared: list[Declaration]) -> list[Declaration]:
    """The mechanisms this tree maintains: all of them where core is made, and in a recipient
    none of those under `.agents/`, which came with core."""
    return [] if _received_core(root) else declared


def _built_in(root: Path, declared: list[Declaration]) -> list[Declaration]:
    return declared if _received_core(root) else []


def _received_core(root: Path) -> bool:
    # TODO: recipient-own-mechanisms, unminted,
    # settles where a recipient's own mechanisms live; until then every one a recipient holds is core's.
    return announced(root) is not None


# --- what a level is checked against ----------------------------------------------------------


def _surface(root: Path, declared: list[Declaration], mechanism: Declaration, level: str) -> list[str]:
    """The files a level is checked against: the meta-rules at `rules`, the same for every
    mechanism; the mechanism's own doc, rules file and skill at `output`."""
    if level == "rules":
        shape = next((one for one in declared if one.slug == SHAPE), None)
        if shape is None or shape.rules is None:
            raise Unreadable(f"no {SHAPE} is declared with a rules file, so the meta-rules have no home to read")
        return sorted([ENTRY_FILE, shape.rules, *_skill_files(root, shape)])
    rules = [mechanism.rules] if mechanism.rules else []
    return sorted([mechanism.doc, *rules, *_skill_files(root, mechanism)])


def _skill_files(root: Path, mechanism: Declaration) -> list[str]:
    """Every file beside the instruction file — its format shelf among them, where a record's
    format is declared. Evidence is story and governs nothing, so an `EVIDENCE.md` a skill still
    carries from before its mechanism was declared is left out, as R2 leaves out evidence."""
    if not mechanism.instruction or not (root / mechanism.instruction).is_file():
        raise Unreadable(f"{mechanism.slug}'s instruction file {mechanism.instruction} does not resolve")
    skill = (root / mechanism.instruction).parent
    return [
        path.relative_to(root).as_posix()
        for path in skill.rglob("*")
        if path.is_file() and path.name != EVIDENCE
    ]


def _fingerprint(root: Path, surface: list[str]) -> str:
    """What a surface says, independent of the line endings a checkout gives it and of the rules
    other mechanisms installed into it."""
    digest = hashlib.sha256()
    for name in surface:
        text = _authored(name, _text(root, name))
        digest.update(name.encode("utf-8") + b"\0" + text.encode("utf-8") + b"\0")
    return digest.hexdigest()


def _text(root: Path, name: str) -> str:
    try:
        return (root / name).read_bytes().decode("utf-8")
    except FileNotFoundError:
        raise Unreadable(f"{name} does not resolve") from None
    except UnicodeDecodeError:
        raise Unreadable(f"{name} is not UTF-8") from None


def _authored(name: str, text: str) -> str:
    """A file as its own author wrote it: LF line endings, and every installed block taken back out
    by the installer's own inverse, so installing or retracting a rule moves nothing. A block is
    policed as injection drift, not as content (R2); one the inverse refuses was edited by hand,
    and `inject_rules.py --check` reports the same block as drift."""
    text = text.replace("\r\n", "\n")
    for slug in dict.fromkeys(INSTALLED_OPENING.findall(without_code(text))):
        try:
            found = inject_rules.locate(text, slug)
            if found.text is None:
                raise Unreadable(f"{name}: the {slug} block never closes")
            text = inject_rules.without_block(text, found)
        except inject_rules.Refused as refusal:
            raise Unreadable(f"{name}: {refusal}") from None
    return text


# --- the marks --------------------------------------------------------------------------------


def _read_marks(root: Path) -> tuple[list[Mark], list[str]]:
    """The rows as the format in `/maintain`'s skill declares them, and every place one does not
    read. A tree with no marks has none and nothing wrong with it."""
    path = root / MARKS
    if not path.is_file():
        return [], []
    lines = path.read_text(encoding="utf-8").splitlines()
    table = [(number, line) for number, line in enumerate(lines, 1) if line.startswith("|")]
    if not table or _cells(table[0][1]) != list(COLUMNS):
        at = table[0][0] if table else 1
        return [], [f"{MARKS}:{at}: the table's header is not | {' | '.join(COLUMNS)} |"]
    marks: list[Mark] = []
    problems: list[str] = []
    for number, line in table[2:]:
        read, problem = _row(_cells(line), {(held.mechanism, held.level) for held in marks})
        if problem:
            problems.append(f"{MARKS}:{number}: {problem}")
        else:
            marks.append(read)
    return marks, problems


def _row(cells: list[str], seen: set[tuple[str, str]]) -> tuple[Mark | None, str | None]:
    if len(cells) != len(COLUMNS):
        return None, f"a row holds {len(cells)} cells, not {len(COLUMNS)}"
    read = Mark(*cells)
    if read.level not in LEVELS:
        return None, f"{read.level} is not a level"
    if not _FINGERPRINT.match(read.fingerprint):
        return None, f"{read.fingerprint} is not a fingerprint — 64 lowercase hex"
    if not _is_date(read.date):
        return None, f"{read.date} is not a date — YYYY-MM-DD"
    if read.outcome not in OUTCOMES:
        return None, f"{read.outcome} is not an outcome"
    if (read.mechanism, read.level) in seen:
        return None, f"a second row for {read.mechanism} at {read.level}"
    return read, None


def _cells(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def _is_date(written: str) -> bool:
    try:
        return date.fromisoformat(written).isoformat() == written
    except ValueError:
        return False


def _write_marks(root: Path, marks: list[Mark]) -> None:
    ordered = sorted(marks, key=lambda held: (held.mechanism, LEVELS.index(held.level)))
    header = "| " + " | ".join(COLUMNS) + " |\n" + "|" + "---|" * len(COLUMNS) + "\n"
    text = (
        "# Maintenance marks\n\n"
        "One row per mechanism per level, written by `maintain.py --mark` when a maintenance\n"
        "finishes; the format is `/maintain`'s, in `.agents/skills/maintain/MARKS-FORMAT.md`.\n\n"
        + header
        + "".join(held.row + "\n" for held in ordered)
    )
    path = root / MARKS
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
