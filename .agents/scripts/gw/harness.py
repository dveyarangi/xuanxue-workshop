"""Core reaches a tree that is not its own repository, from a fresh clone of that repository at a ref.

    python .agents/scripts/gw/harness.py <target> --install [--from REPOSITORY] [--at REF]
    python .agents/scripts/gw/harness.py <target> --update [--overwrite] [--from REPOSITORY] [--at REF]
    python .agents/scripts/gw/harness.py <target> --check [--from REPOSITORY]

The source is always the repository, cloned whole and without a checkout into a temporary
directory and read through git, so what a recipient receives is what a commit holds and never a
working tree. What ships is every file under the core directory at the ref plus the entry file and
the host stub, transformed in memory before a byte is written: the origin's own local blocks
removed, every straw-dog wrapper and every TODO's ticket binding sheared with its content kept, the
entry file's announce line stamped `<repository>@<ref>, <date>`, and the result held to the leak
rule the origin's check applies. That line is the recipient's only revision record; a check clones
the announced ref again and compares. Every refusal writes nothing. A loader link the platform
refuses to create is not a refusal: everything else lands, and the report carries the exact command
for the person. The contract is the architecture's; the decisions are the install spec's.
"""

from __future__ import annotations

import sys

sys.dont_write_bytecode = True  # a run from inside a recipient leaves nothing beside its scripts

import io  # noqa: E402
import json  # noqa: E402
import os  # noqa: E402
import re  # noqa: E402
import shutil  # noqa: E402
import stat  # noqa: E402
import subprocess  # noqa: E402
import tarfile  # noqa: E402
import tempfile  # noqa: E402
from dataclasses import dataclass, field  # noqa: E402
from pathlib import Path  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parent))

import inject_rules  # noqa: E402  (path set just above)
from docs_corpus import (  # noqa: E402
    ANNOUNCE,
    ENTRY_FILE,
    RETIRED_TAG,
    SCRIPTS,
    UnreadableCode,
    announced,
    corpus,
    docs_mentioned,
    docs_mentioned_in_code,
    without_code,
)
from mechanisms import PAINTED_DOORS, TESTS  # noqa: E402
from straw_dogs import TAG, TICKET_PATH  # noqa: E402

CORE = ".agents/"
HOST_STUB = "CLAUDE.md"
LICENSE = "LICENSE"
INSTALLED_LICENSE = f"{CORE}LICENSE"
LOCAL_FILE = inject_rules.LOCAL_FILE
LINKS = (".claude/skills", ".cursor/skills")
LINK_TARGET = "../.agents/skills"
SKILLS = ".agents/skills"
HARNESS_SKILL = f"{SKILLS}/harness/SKILL.md"
QUEUE_ARRIVAL = f"{SKILLS}/ticket/QUEUE-ARRIVAL.md"
DELIVERY_STATUS = "docs/tickets/README.md"
ARRIVAL_STATE = re.compile(r"^```delivery-status[ \t]*\r?\n(?P<said>.*?)^```", re.M | re.S)
REPOSITORY = re.compile(r"^Repository: (?P<url>\S+)[ \t]*(?:\r?\n|\Z)", re.M)
MODES = ("--install", "--update", "--check")
_USAGE = (
    "usage: harness.py <target> --install [--from REPOSITORY] [--at REF]\n"
    "       harness.py <target> --update [--overwrite] [--from REPOSITORY] [--at REF]\n"
    "       harness.py <target> --check [--from REPOSITORY]"
)


class Refused(Exception):
    """Something that must not be written past. The message says which step and what to settle."""


@dataclass(frozen=True)
class Ref:
    """One commit of the repository, as the announce line will name it."""

    repository: str
    commit: str
    announced: str
    date: str

    @property
    def stamp(self) -> str:
        return f"Entry contract: {self.repository}@{self.announced}, {self.date}."

    def as_record(self) -> dict:
        return {"repository": self.repository, "commit": self.commit, "announced": self.announced, "date": self.date}


@dataclass
class Report:
    """What one run did, in the order it did it. `arrived` is the gate's verdict and nothing else's."""

    target: str
    mode: str
    repository: str
    ref: dict | None = None
    written: list[str] = field(default_factory=list)
    replaced: list[str] = field(default_factory=list)
    deleted: list[str] = field(default_factory=list)
    own: list[str] = field(default_factory=list)
    links: list[dict] = field(default_factory=list)
    pending: list[str] = field(default_factory=list)
    injected: list[dict] = field(default_factory=list)
    gates: dict = field(default_factory=dict)
    links_resolve: dict = field(default_factory=dict)
    notes: list[str] = field(default_factory=list)
    refusals: list[str] = field(default_factory=list)
    arrived: bool = False

    def as_record(self) -> dict:
        return dict(self.__dict__)


def main(argv: list[str]) -> int:
    parsed = _parsed(argv)
    if parsed is None:
        print(_USAGE)
        return 2
    target, mode, overwrite, repository, ref = parsed
    report = Report(target, mode[2:], repository or "")
    try:
        if repository is None:
            repository = report.repository = home()
        with Source(repository) as source:
            run(Path(target), mode, overwrite, source, ref, report)
    except Refused as refusal:
        report.refusals.append(str(refusal))
    print(json.dumps(report.as_record(), indent=2))
    return 0 if report.arrived else 1


def run(target: Path, mode: str, overwrite: bool, source: Source, ref: str | None, report: Report) -> None:
    """The sequence: refuse what cannot be satisfied, copy, stamp, link, inject, then the gate."""
    target = _work_tree_root(target, source)
    if mode == "--check":
        wanted = _announced_ref(target, source, required=True)
        shipment = Shipment.earlier(source, wanted)
        report.ref = wanted.as_record()
        _gate(target, shipment, report)
        return
    wanted = source.resolve(ref or "HEAD")
    report.ref = wanted.as_record()
    shipment = Shipment.at(source, wanted)
    if mode == "--install":
        _refuse_unless_empty(target, shipment)
        previous = None
    else:
        previous = _refuse_unless_updatable(target, source, shipment, overwrite, report)
    plan = _link_plan(target)
    _write(target, shipment, previous, report)
    _write_delivery_status(target, shipment, report)
    _make_links(target, plan, report)
    _inject(target, report)
    _gate(target, shipment, report)


def _parsed(argv: list[str]) -> tuple[str, str, bool, str | None, str | None] | None:
    """Exactly one target, one mode, and the options each mode admits; anything else is usage.

    An absent `--from` stays absent rather than defaulting here: the default is read from the
    harness skill, and a run that was given a repository must never need a skill to be there.
    """
    words: list[str] = []
    modes: list[str] = []
    overwrite = False
    repository = None
    ref = None
    operands = list(argv)
    while operands:
        operand = operands.pop(0)
        if operand in MODES:
            modes.append(operand)
        elif operand == "--overwrite":
            overwrite = True
        elif operand in ("--from", "--at") and operands:
            value = operands.pop(0)
            if operand == "--from":
                repository = value
            else:
                ref = value
        elif operand.startswith("-"):
            return None
        else:
            words.append(operand)
    if len(words) != 1 or len(modes) != 1:
        return None
    mode = modes[0]
    if overwrite and mode != "--update":
        return None
    if ref is not None and mode == "--check":
        return None
    return words[0], mode, overwrite, repository, ref


# --- the source ------------------------------------------------------------------------------


def home() -> str:
    """Where core comes from, read from the one line that authors it — the harness skill beside
    this script. No constant: the line is the only authored home, so a fork edits it once and
    everything the fork installs names the fork."""
    skill = Path(__file__).resolve().parents[3] / HARNESS_SKILL  # the tree this script sits in
    if not skill.is_file():
        raise Refused(f"source: {HARNESS_SKILL} is not beside this script; name the repository with --from")
    named = REPOSITORY.findall(_read(skill))
    if len(named) != 1:
        found = "no Repository line" if not named else f"{len(named)} Repository lines"
        raise Refused(f"source: {HARNESS_SKILL} holds {found}; name the repository with --from")
    return named[0]


def resolved(repository: str) -> str:
    """What a recipient is told, from what this run was given: a URL verbatim, a path as an
    absolute one, so a recipient installed from a clone on disk holds no path relative to where
    somebody once stood."""
    local = Path(repository)
    return local.resolve().as_posix() if local.exists() else repository


class Source:
    """The repository, cloned whole and without a checkout for one run, read through git only.

    A checkout would let `core.autocrlf` and `core.symlinks` rewrite what ships; reading blobs
    keeps every byte the commit holds. GitHub serves no fetch by a short commit, so the clone is
    whole and any ref — branch, tag, short or full commit — resolves locally.
    """

    def __init__(self, repository: str) -> None:
        self.repository = repository
        self.name = repository_name(repository)
        self._clone: Path | None = None

    def __enter__(self) -> Source:
        self._clone = Path(tempfile.mkdtemp(prefix="harness-")).resolve()
        cloned = subprocess.run(
            ["git", "clone", "--quiet", "--no-checkout", self.repository, str(self._clone)],
            capture_output=True,
            encoding="utf-8",
        )
        if cloned.returncode != 0:
            raise Refused(f"clone: {self.repository} could not be cloned — {cloned.stderr.strip()}")
        return self

    def __exit__(self, *_: object) -> None:
        if self._clone is not None:
            shutil.rmtree(self._clone, onexc=_writable_then_retry)

    def resolve(self, ref: str) -> Ref:
        commit = self._commit(ref)
        if commit is None:
            raise Refused(f"ref: {ref} does not resolve in {self.repository}")
        return Ref(self.name, commit, self._tag(commit) or self._short(commit), self._date(commit))

    def files(self, ref: Ref) -> dict[str, bytes]:
        """Every file under the core directory at the commit, plus the entry file, the host stub
        and the license, as the commit holds them: nothing else travels — not the root README, not
        the local file, not `docs/`.

        The license is the source's root file and a recipient's `.agents/LICENSE`: its notice must
        go with every copy, and a recipient's root is its own. It is read apart from the archive,
        which refuses a path the commit lacks — and every ref before the license lacks it."""
        files = self._archived(ref, (CORE.rstrip("/"), ENTRY_FILE, HOST_STUB))
        license = self._blob(ref, LICENSE)
        if license is not None:
            files[INSTALLED_LICENSE] = license
        return files

    # What follows reads the clone, and is all that does: the choices above are made on what it
    # returns, so a source held some other way answers these and inherits the rest.

    def _commit(self, ref: str) -> str | None:
        return self._git("rev-parse", "--verify", "--quiet", f"{ref}^{{commit}}")

    def _tag(self, commit: str) -> str | None:
        return self._git("describe", "--tags", "--exact-match", commit)

    def _short(self, commit: str) -> str:
        return self._git("rev-parse", "--short", commit) or commit[:7]

    def _date(self, commit: str) -> str:
        return self._git("log", "-1", "--format=%cs", commit) or ""

    def _archived(self, ref: Ref, paths: tuple[str, ...]) -> dict[str, bytes]:
        """Every file at or under the paths, as the commit holds them. One archive of the ref, one
        process: reading sixty files one `cat-file` at a time cost more than the clone."""
        # `archive` smudges like a checkout would — `core.autocrlf` on Windows turns every line
        # ending — so conversion is switched off for this one command and the bytes are the commit's.
        archived = subprocess.run(
            ["git", "-C", str(self._clone), "-c", "core.autocrlf=false", "-c", "core.eol=lf", "archive",
             "--format=tar", ref.commit, "--", *paths],
            capture_output=True,
        )
        if archived.returncode != 0:
            raise Refused(f"read: {self.repository} at {ref.announced} could not be archived — {archived.stderr.decode(errors='replace').strip()}")
        files: dict[str, bytes] = {}
        with tarfile.open(fileobj=io.BytesIO(archived.stdout)) as archive:
            for member in archive.getmembers():
                if member.isfile():
                    files[member.name] = archive.extractfile(member).read()
        return files

    def _blob(self, ref: Ref, path: str) -> bytes | None:
        """A file's bytes as the commit holds them — a blob is never smudged — or None when the
        commit has no such file."""
        read = subprocess.run(
            ["git", "-C", str(self._clone), "cat-file", "blob", f"{ref.commit}:{path}"], capture_output=True
        )
        return read.stdout if read.returncode == 0 else None

    def _git(self, *arguments: str) -> str | None:
        done = subprocess.run(
            ["git", "-C", str(self._clone), *arguments], capture_output=True, encoding="utf-8"
        )
        return done.stdout.strip() if done.returncode == 0 else None


def repository_name(repository: str) -> str:
    """The last segment of a URL or path, without `.git`: what the announce line calls it."""
    trimmed = repository.replace("\\", "/").rstrip("/")
    name = trimmed.rsplit("/", 1)[-1]
    return name[:-4] if name.endswith(".git") else name


def _writable_then_retry(function, path, _excinfo) -> None:
    # Git leaves its objects read-only; on Windows that alone makes `rmtree` fail.
    os.chmod(path, stat.S_IWRITE)
    function(path)


# --- what ships ------------------------------------------------------------------------------


@dataclass(frozen=True)
class Shipment:
    """The manifest at one ref, transformed — and, when it is about to ship, held to the leak rule —
    before anything is written."""

    ref: Ref
    files: dict[str, str]
    arrival: str

    @classmethod
    def at(cls, source: Source, ref: Ref) -> Shipment:
        files = _transformed(source, ref, held=True)
        if HARNESS_SKILL not in files:
            raise Refused(f"ship: {ref.announced} has no {HARNESS_SKILL}; this is not the harness")
        return cls(ref, files, arrival_state(files, ref))

    @classmethod
    def earlier(cls, source: Source, ref: Ref) -> Shipment:
        """What a ref a recipient announces shipped, read to compare its copy against and to know
        what has left the manifest since. It is never shipped again, so today's shipping rules —
        the leak rule, the Repository line, the arrival shelf — do not hold it: a ref installed
        before a rule existed would otherwise strand every tree that took it. It carries no
        arrival state; only what is about to ship writes one."""
        return cls(ref, _transformed(source, ref, held=False), "")


def _transformed(source: Source, ref: Ref, held: bool) -> dict[str, str]:
    files: dict[str, str] = {}
    told = resolved(source.repository)
    for path, raw in source.files(ref).items():
        try:
            text = raw.decode("utf-8")
        except UnicodeDecodeError as error:
            raise Refused(f"ship: {path} at {ref.announced} is not UTF-8 — {error}") from error
        files[path] = shipped(path, text, ref, told, held)
    if ENTRY_FILE not in files:
        raise Refused(f"ship: {ref.announced} has no {ENTRY_FILE}; this is not the harness")
    return files


def shipped(path: str, text: str, ref: Ref, told: str, held: bool = True) -> str:
    """One file as a recipient receives it. The order matters: local blocks are found by their tag
    before the shear could touch a wrapper around them, and the leak rule reads the text a
    recipient will. A stamped source is not a citation, which `docs_corpus` settles for every
    reader of it rather than each one blanking the line for itself. Unheld, the file is read as an
    earlier ref shipped it: the same transformation, and none of today's refusals."""
    if path.endswith(".md"):
        text = without_local_blocks(path, text)
        text = sheared(path, text)
        if path == ENTRY_FILE:
            text = stamped(text, ref)
        if path == HARNESS_SKILL and (held or REPOSITORY.search(text)):
            text = repository_stamped(text, ref, told)
        if held:
            _refuse_leaks(path, [seen.path for seen in docs_mentioned(Path("."), path, text) if not seen.instance_owned])
    elif path.endswith(".py"):
        text = todo_bindings_sheared(text)
        if held and not path.startswith(TESTS):
            try:
                _refuse_leaks(path, [seen.path for seen in docs_mentioned_in_code(text)])
            except UnreadableCode as error:
                raise Refused(f"ship: {path} could not be read for citations — {error}") from error
    return text


def without_local_blocks(path: str, text: str) -> str:
    """The origin's own answers do not travel: every local block leaves with the newline the
    installer added, through the installer's own reading of where a block is."""
    try:
        while (found := inject_rules.locate(text, inject_rules.LOCAL)) is not None:
            if found.text is None:
                raise inject_rules.Refused("the local block opens and never closes")
            text = inject_rules.without_block(text, found)
    except inject_rules.Refused as refusal:
        raise Refused(f"ship: {path}: {refusal}") from refusal
    return text


def sheared(path: str, text: str) -> str:
    """Every straw-dog wrapper off, its content kept: a recipient gets the rule and never a
    condition it could not observe. A tag alone on its line takes the line; an inline tag leaves
    the text joined as written. Idempotent, so a core already sheared passes unchanged."""
    seen = without_code(text)
    tags = list(TAG.finditer(seen))
    depth = 0
    for tag in tags:
        written = tag.group(0)
        if not written.endswith(">"):
            raise Refused(f"ship: {path}:{_line_at(text, tag.start())} holds a malformed straw-dog tag")
        depth += -1 if written.startswith("</") else 1
        if depth < 0:
            raise Refused(f"ship: {path}:{_line_at(text, tag.start())} closes a straw dog nothing opened")
    if depth:
        raise Refused(f"ship: {path} opens a straw dog it never closes")
    for tag in reversed(tags):
        start, end = _whole_line_if_alone(text, tag.start(), tag.end())
        text = text[:start] + text[end:]
    return text


def todo_bindings_sheared(text: str) -> str:
    """A TODO's ticket path is its binding, the code form of a straw dog's `ticket=`; the words
    stay and the path goes, so the recipient reads a note and never a path it cannot resolve."""
    lines = []
    for line in text.splitlines(keepends=True):
        if re.match(r"^\s*#\s*TODO\b", line) and TICKET_PATH.search(line):
            line = re.sub(r"\s*" + TICKET_PATH.pattern, "", line, count=1)
        lines.append(line)
    return "".join(lines)


def stamped(text: str, ref: Ref) -> str:
    """The announce line names where core came from; a recipient's every session repeats it."""
    line = ANNOUNCE.search(text)
    if line is None:
        raise Refused(f"ship: {ENTRY_FILE} at {ref.announced} has no announce line; this is not the harness")
    end = line.end("date") + 1  # through the full stop, leaving the line's own ending alone
    return text[: line.start()] + ref.stamp + text[end:]


def repository_stamped(text: str, ref: Ref, told: str) -> str:
    """The harness skill names where this tree's core came from, as the announce line names which
    commit of it. A ref whose skill carries no such line is not the harness, in the same words
    and at the same moment as one whose entry file carries no announce line."""
    line = REPOSITORY.search(text)
    if line is None:
        raise Refused(f"ship: {HARNESS_SKILL} at {ref.announced} has no Repository line; this is not the harness")
    return text[: line.start("url")] + told + text[line.end("url") :]


def arrival_state(files: dict[str, str], ref: Ref) -> str:
    """What the queue says in a tree where core has arrived and nothing is in flight, from the
    ref's own words rather than this tree's: the ticket mechanism owns the record and words it,
    and the only substitution is the ref the recipient will announce.

    Read while the shipment is built, so a ref that cannot say it is refused before anything is
    written rather than partway through. It has a shelf of its own because it is read once, by
    this script, and the format shelf beside it is read at every ticket a session writes. The
    block is found by its info string and not by its position, so prose may be written around it;
    and being fenced is what keeps the citation reader from taking a path inside it for a
    document only the origin has."""
    shelf = files.get(QUEUE_ARRIVAL)
    if shelf is None:
        raise Refused(f"ship: {ref.announced} has no {QUEUE_ARRIVAL}; this is not the harness")
    said = ARRIVAL_STATE.search(shelf)
    if said is None:
        raise Refused(f"ship: {QUEUE_ARRIVAL} at {ref.announced} declares no arrival state")
    return said.group("said").replace("{ref}", ref.announced)


def without_repository_line(path: str, text: str) -> str:
    """The recipient's own `--from`, set aside for the comparison. It is the recipient's fact
    living in a core file, as the announce line is, so a check or an update run from another
    source never reads it as an edit. The line leaves with its own newline, as a local block
    does, so what is compared is the text either tree would hold without it."""
    if path != HARNESS_SKILL:
        return text
    return REPOSITORY.sub("", text, count=1)


def _refuse_leaks(path: str, cited: list[str]) -> None:
    leaks = [seen for seen in cited if seen not in PAINTED_DOORS and seen + "/" not in PAINTED_DOORS]
    if leaks:
        raise Refused(f"ship: {path} cites {leaks[0]}, a document only the origin has; it cannot ship")


def _whole_line_if_alone(text: str, start: int, end: int) -> tuple[int, int]:
    line_start = text.rfind("\n", 0, start) + 1
    line_end = text.find("\n", end)
    line_end = len(text) if line_end == -1 else line_end + 1
    if text[line_start:start].strip() or text[end:line_end].strip():
        return start, end
    return line_start, line_end


# --- the target ------------------------------------------------------------------------------


def _work_tree_root(target: Path, source: Source) -> Path:
    """One installation is one tree: the target is the top level of a git work tree, and never
    the repository core comes from."""
    if not target.is_dir():
        raise Refused(f"target: {target} is not a directory")
    target = target.resolve()
    top = _git_in(target, "rev-parse", "--show-toplevel")
    # TODO: a failed rev-parse is
    # read here as a wrong shape, Git's dubious-ownership refusal included.
    if top is None or Path(top).resolve() != target:
        raise Refused(f"target: {target} is not the top level of a git work tree; a workspace of several is refused")
    origin = _git_in(target, "remote", "get-url", "origin")
    if origin is not None and _same_repository(origin, source.repository):
        raise Refused(f"target: {target} is the source itself; the origin is never installed into")
    return target


def _same_repository(one: str, other: str) -> bool:
    def normalised(named: str) -> str:
        trimmed = named.strip().replace("\\", "/").rstrip("/")
        trimmed = trimmed[:-4] if trimmed.endswith(".git") else trimmed
        local = Path(trimmed)
        if local.exists():
            return str(local.resolve()).replace("\\", "/").lower()
        return trimmed.lower()

    return normalised(one) == normalised(other)


def _refuse_unless_empty(target: Path, shipment: Shipment) -> None:
    present = [path for path in shipment.files if (target / path).exists()]
    if present:
        raise Refused(
            f"install: {present[0]} already exists in the target; a previous install takes --update, "
            "anything else is the recipient's to move first"
        )


def _refuse_unless_updatable(
    target: Path, source: Source, shipment: Shipment, overwrite: bool, report: Report
) -> Shipment | None:
    """What an update must find: core present, no retired tag holding the project's facts, and
    every core file as the announced ref shipped it — or `--overwrite`, which replaces and reports."""
    if not (target / CORE).is_dir():
        raise Refused(f"update: {target} holds no {CORE}; a first install takes --install")
    entry = target / ENTRY_FILE
    if entry.is_file() and RETIRED_TAG in without_code(_read(entry)):
        raise Refused(
            f"update: {ENTRY_FILE} holds a {RETIRED_TAG} block, which is the project's; "
            f"move its content into {LOCAL_FILE} first"
        )
    announced_ref = _announced_ref(target, source, required=False)
    if announced_ref is None:
        if not overwrite:
            raise Refused("update: the tree announces no ref to compare against; --overwrite is required")
        report.notes.append("the tree announced no ref: nothing is deleted, every core file is replaced")
        return None
    previous = Shipment.earlier(source, announced_ref)
    edited = [path for path in previous.files if _differs(target, path, previous.files[path])]
    if edited and not overwrite:
        raise Refused(
            f"update: {edited[0]} differs from {announced_ref.announced} as installed — an edit in core; "
            "--overwrite replaces it and reports it, or keep the edit in the local file"
        )
    report.replaced = edited
    return previous


def _announced_ref(target: Path, source: Source, required: bool) -> Ref | None:
    told = announced(target)
    if told is None:
        if required:
            raise Refused(f"check: {target} announces no <repository>@<ref>; it is not a recipient")
        return None
    if told.repository != source.name:
        raise Refused(f"the tree announces {told.repository}; --from names {source.name}")
    return source.resolve(told.ref)


def _differs(target: Path, path: str, shipped_text: str) -> bool:
    """Whether the recipient's copy is what the ref shipped, its own local block and its own
    repository line set aside and line endings normalised — the injector's and R2's rule for
    comparing what was installed. Both sides lose the line, so a check or an update run from
    another `--from` reads no edit in core."""
    copy = target / path
    if not copy.is_file():
        return True
    text = _read(copy)
    if path.endswith(".md"):
        try:
            text = without_local_blocks(path, text)
        except Refused:
            return True
        text = without_repository_line(path, text)
        shipped_text = without_repository_line(path, shipped_text)
    return _normalised(text) != _normalised(shipped_text)


def _normalised(text: str) -> str:
    return text.replace("\r\n", "\n")


# --- copy, links, inject ---------------------------------------------------------------------


def _holds(target: Path, path: str, text: str) -> bool:
    """Whether the copy already holds exactly what ships, its own local block set aside: such a
    file is left alone and not reported written, so an update's report names only what changed."""
    copy = target / path
    if not copy.is_file():
        return False
    current = _read(copy)
    if path.endswith(".md"):
        try:
            current = without_local_blocks(path, current)
        except Refused:
            return False
    return current == text


def _write(target: Path, shipment: Shipment, previous: Shipment | None, report: Report) -> None:
    """Every manifest file, then what left the manifest since the previous ref. A failure partway
    is reported in the mover's form — done, pending, the failed path — and nothing is rolled back."""
    planned = list(shipment.files.items())
    done: list[str] = []
    for path, text in planned:
        if _holds(target, path, text):
            continue
        try:
            _write_text(target / path, text)
        except OSError as failure:
            pending = [other for other, _ in planned if other not in done and other != path]
            raise Refused(
                f"copy: {path} could not be written — {failure}; done {len(done)}, pending {len(pending)}; "
                "fix the cause and run --update --overwrite"
            ) from failure
        done.append(path)
    report.written = done
    if previous is not None:
        for path in previous.files:
            if path not in shipment.files and (target / path).is_file():
                (target / path).unlink()
                report.deleted.append(path)
        _prune_empty_directories(target / CORE)
    report.own = sorted(
        name for name in corpus(target) if name.startswith(CORE) and name not in shipment.files
    )


def _write_delivery_status(target: Path, shipment: Shipment, report: Report) -> None:
    """The one painted door that arrives with content: a fresh tree's first session reads the
    queue before anything has been written into it, so it must already say something true.

    Written whenever the path is absent — an update is how a tree that received core before this
    acquires one. An existing record is the instance's from its first line: never merged, never
    overwritten, and `--overwrite` does not reach it, since that flag is about core files."""
    record = target / DELIVERY_STATUS
    if record.exists():
        report.notes.append(f"{DELIVERY_STATUS} is the project's: left as it stands")
        return
    record.parent.mkdir(parents=True, exist_ok=True)
    with record.open("w", encoding="utf-8", newline="") as handle:
        handle.write(shipment.arrival)
    report.written.append(DELIVERY_STATUS)


def _link_plan(target: Path) -> dict[str, str]:
    """Per loader link, before anything is written: `keep`, `make` or `repoint`. A junction, a
    directory or a file where the link goes is the recipient's own and refuses the run."""
    plan: dict[str, str] = {}
    skills = (target / SKILLS).resolve()
    for link in LINKS:
        path = target / link
        # Asked of the link itself, never through it: a dangling junction or symlink has no
        # `exists()` and is still something standing where the link goes.
        if _is_junction(path):
            raise Refused(f"link: {link} is a junction, which nothing sees through; remove it, a symlink goes there")
        if path.is_symlink():
            plan[link] = "keep" if _resolves_to(path, skills) else "repoint"
        elif not os.path.lexists(path):
            plan[link] = "make"
        else:
            raise Refused(f"link: {link} is a {'directory' if path.is_dir() else 'file'} of the recipient's own; move it first")
    return plan


def _make_links(target: Path, plan: dict[str, str], report: Report) -> None:
    """A symlink, or the exact command for the person: the platform's refusal is the one step of an
    install that may be left to a hand, and it does not stop the rest."""
    for link, action in plan.items():
        path = target / link
        if action == "keep":
            report.links.append({"link": link, "state": "kept"})
            continue
        if action == "repoint":
            _remove_link(path)
        try:
            path.parent.mkdir(parents=True, exist_ok=True)
            os.symlink(LINK_TARGET.replace("/", os.sep), path, target_is_directory=True)
        except OSError as failure:
            report.links.append({"link": link, "state": "pending", "error": str(failure)})
            report.pending.append(_link_command(path))
            continue
        report.links.append({"link": link, "state": "made" if action == "make" else "repointed"})
    if report.pending:
        report.notes.append("run the pending command(s) once in an elevated prompt, then `harness.py . --check`")
    # TODO: this note assumes tracked
    # links; untracked since 2026-09-26, a clone gets them from the link step, and the note goes.
    if _git_in(target, "config", "--get", "core.symlinks") == "false":
        report.notes.append("core.symlinks is false in the target: a fresh clone checks the links out as text")


def _remove_link(path: Path) -> None:
    # Windows removes a directory symlink through rmdir, not unlink; the link itself goes, never its target.
    try:
        path.unlink()
    except OSError:
        os.rmdir(path)


def _link_command(path: Path) -> str:
    if os.name == "nt":
        return f'mklink /D "{path}" "{LINK_TARGET.replace("/", os.sep)}"'
    return f'ln -s {LINK_TARGET} "{path}"'


def _inject(target: Path, report: Report) -> None:
    """Every mechanism's rules file, then the recipient's local file last. A refusal is the
    injector's, reported verbatim; the resume is the local file, the injector, then --check."""
    sources = [directory.name for directory in sorted((target / inject_rules.MECHANISMS).glob("*/"))
               if (directory / f"{directory.name}.rules.md").is_file()]
    if (target / LOCAL_FILE).is_file():
        sources.append(inject_rules.LOCAL)
    for slug in sources:
        try:
            rules = inject_rules.read_rules_file(target, slug)
            if slug == inject_rules.LOCAL:
                inject_rules.overrides_resolve(target, rules)
            outcome = inject_rules.install(target, rules, overwrite=False)
        except inject_rules.Refused as refusal:
            raise Refused(f"inject: {slug}: {refusal}; fix {LOCAL_FILE}, run inject_rules.py {slug} --install, then harness.py . --check") from refusal
        report.injected.append({"slug": slug, "targets": outcome["targets"]})
        if outcome["refusals"]:
            raise Refused(
                f"inject: {slug}: {outcome['refusals'][0]}; fix {LOCAL_FILE}, "
                f"run inject_rules.py {slug} --install, then harness.py . --check"
            )


# --- the gate --------------------------------------------------------------------------------


def _gate(target: Path, shipment: Shipment, report: Report) -> None:
    """Arrival, and any later day's question, are one function: the ref compared, the injector's
    check, the shape check — the target's own scripts, run as subprocesses, so what is checked
    is what arrived, in seconds. The loader links are reported beside the verdict, resolving or
    not, and never decide it: a link the platform refused is the person's one remaining step,
    and the command for it is already in the report. The shipped suite is not run here; a
    recipient that wants it names it in its own verification set."""
    gates = {
        "ref": _ref_gate(target, shipment),
        "injector": _script_gate(target, "inject_rules.py"),
        "shape": _script_gate(target, "mechanisms.py"),
    }
    report.gates = gates
    report.links_resolve = _links_resolve(target)
    report.arrived = all(gate["passed"] for gate in gates.values())
    report.notes.append("whether a host reads the loader link is not observable from inside a tree")


def _ref_gate(target: Path, shipment: Shipment) -> dict:
    differing = [path for path in shipment.files if _differs(target, path, shipment.files[path])]
    own = sorted(name for name in corpus(target) if name.startswith(CORE) and name not in shipment.files)
    return {"passed": not differing, "ref": shipment.ref.announced, "differs": differing, "own": own}


def _script_gate(target: Path, script: str) -> dict:
    done = _python(target, [str(target / SCRIPTS / script), "--check"])
    return {"passed": done.returncode == 0, "exit": done.returncode, "said": _last_lines(done.stdout or done.stderr)}


def _links_resolve(target: Path) -> dict[str, bool]:
    """Per loader link, whether a symlink stands there and reaches a directory of skill files."""
    return {
        link: (target / link).is_symlink() and (target / link).is_dir() and any((target / link).glob("*/SKILL.md"))
        for link in LINKS
    }


def _python(target: Path, arguments: list[str]) -> subprocess.CompletedProcess:
    environment = {**os.environ, "PYTHONDONTWRITEBYTECODE": "1"}
    return subprocess.run(
        [sys.executable, *arguments], cwd=target, capture_output=True, encoding="utf-8", env=environment
    )


def _last_lines(text: str | None, keep: int = 3) -> list[str]:
    return [line for line in (text or "").strip().splitlines() if line][-keep:]


# --- helpers ---------------------------------------------------------------------------------


def _git_in(target: Path, *arguments: str) -> str | None:
    done = subprocess.run(["git", "-C", str(target), *arguments], capture_output=True, encoding="utf-8")
    return done.stdout.strip() if done.returncode == 0 else None


def _resolves_to(link: Path, skills: Path) -> bool:
    try:
        return link.resolve() == skills and link.is_dir()
    except OSError:
        return False


def _is_junction(path: Path) -> bool:
    try:
        return os.lstat(path).st_reparse_tag == stat.IO_REPARSE_TAG_MOUNT_POINT
    except (AttributeError, OSError):
        return False


def _prune_empty_directories(top: Path) -> None:
    for directory in sorted((path for path in top.rglob("*") if path.is_dir()), reverse=True):
        if not any(directory.iterdir()):
            directory.rmdir()


def _line_at(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def _read(path: Path) -> str:
    with path.open(encoding="utf-8", newline="") as handle:
        return handle.read()


def _write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        handle.write(text)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
