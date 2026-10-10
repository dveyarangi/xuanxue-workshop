"""Placing a ref of the repository into a tree that is not its own, updating it, and checking it."""

from __future__ import annotations

import contextlib
import datetime
import hashlib
import io
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from repository import SCRIPTS, RepositoryCase, folder_listing, proves_a_process

import harness
import inject_rules
import mechanisms

KEEPER = ".agents/skills/keeper/SKILL.md"
HARNESS_SKILL = ".agents/skills/harness/SKILL.md"
TICKET_SKILL = ".agents/skills/ticket/SKILL.md"
QUEUE_ARRIVAL = ".agents/skills/ticket/QUEUE-ARRIVAL.md"
DELIVERY_STATUS = "docs/tickets/README.md"
TICKET_SKILL_TEXT = (
    "---\nname: ticket\ndescription: mints tickets\n---\n\n"
    "Mechanism: unowned by design — this fixture's core declares only sample\n\n"
    "Mint them.\n"
)
QUEUE_ARRIVAL_TEXT = (
    "# What the queue says before anything has happened in it\n\n"
    "Machine input for the install, read by nobody at session time.\n\n"
    "```delivery-status\n# Delivery status\n\nCore arrived at `{ref}` and nothing is in flight.\n```\n"
)
HARNESS_SKILL_TEXT = (
    "---\nname: harness\ndescription: places core\n---\n\n"
    "Mechanism: unowned by design — this fixture's core declares only sample\n\n"
    "Repository: https://github.com/example/placed-by-the-fixture.git\n\n"
    "The claim line comes first because the shape check reads the body's first line; the\n"
    "repository line sits below it, which is what core's own harness skill does.\n"
)
DOC = ".agents/mechanisms/sample/sample.md"
TICKET = "docs/tickets/01-0002-sweep.md"
WRAPPED_RULE = "Run the sweep first in every session."
ENTRY = (
    "# Entry contract\n\n"
    "Entry contract: v3, 2026-09-01.\n\n"
    "Open your first reply with the line above.\n\n"
    '<straw-dog question="q-0002">\n'
    f"{WRAPPED_RULE}\n"
    "</straw-dog>\n\n"
    "## Project-local\n\n"
    '<installed by="local">\n'
    "**L1** The origin's own answer, which must not travel.\n"
    "</installed>\n\n"
    "- Doing it is sample work: use /keeper.\n"
)
SAMPLE_DOC = (
    "# sample — one line saying what it is\n\n"
    f"- **instruction** `{KEEPER}` — the act\n"
    "- **state** installed\n"
    "- **kind** what must always hold\n\n"
    "## How it works\n\nProse nothing parses.\n\n"
    "## Moments\n\n"
    "| moment | instructed by | kind, and why |\n|---|---|---|\n"
    f"| keeping | `{KEEPER}` | |\n"
    '| sweeping | — | <straw-dog question="q-0002">not yet</straw-dog> |\n\n'
    "## Install adds, uninstall removes\n\n"
    f"| part | where |\n|---|---|\n| instruction file | `{KEEPER}` |\n\n"
    "## Relies on, and does not own\n\n"
    "| part | where | owner |\n|---|---|---|\n| corpus reader | `.agents/scripts/gw/docs_corpus.py` | nobody removable |\n\n"
    "## What it produces, and who reads it\n\nThe declaration, read by whoever amends this.\n\n"
    "## Not yet at the shape\n\nThe honest gaps.\n\n"
    "## What retires this\n\nA better shape.\n\n"
    "## What would show it working, graded by someone who did not build it\n\n"
    "The next mechanism declared passes unedited.\n"
)
ARRIVAL_TEST = (
    "import unittest\n\n\n"
    "class Arrival(unittest.TestCase):\n"
    "    def test_the_scripts_arrived(self):\n"
    "        self.assertTrue(True)\n"
)
LICENSE_TEXT = "MIT License\n\nCopyright (c) 2026 the fixture's contributors\n"
INSTALLED_LICENSE = ".agents/LICENSE"


def platform_makes_symlinks() -> bool:
    """Whether this machine lets a process create a directory symlink; the platform's answer is
    read from a run, never assumed, so the case proves whichever path the machine takes."""
    with tempfile.TemporaryDirectory() as workspace:
        real = Path(workspace) / "real"
        real.mkdir()
        try:
            os.symlink("real", Path(workspace) / "link", target_is_directory=True)
        except OSError:
            return False
        return True


class History:
    """The source's commits and tags when no repository holds them: each commit a snapshot of the
    source folder, named as Git would name one."""

    def __init__(self) -> None:
        self.commits: dict[str, dict[str, bytes]] = {}
        self.tags: dict[str, str] = {}
        self.head: str | None = None
        self.date = datetime.date.today().isoformat()

    def commit(self, files: dict[str, bytes]) -> None:
        named = hashlib.sha1(repr((len(self.commits), sorted(files.items()))).encode()).hexdigest()
        self.commits[named] = files
        self.head = named

    def tag(self, name: str) -> None:
        self.tags[name] = self.head

    def commit_of(self, ref: str) -> str | None:
        if ref == "HEAD":
            return self.head
        if ref in self.tags:
            return self.tags[ref]
        matching = [named for named in self.commits if named.startswith(ref)]
        return matching[0] if len(matching) == 1 and len(ref) >= 4 else None

    def tag_of(self, commit: str) -> str | None:
        return next((name for name, tagged in self.tags.items() if tagged == commit), None)


class HeldSource(harness.Source):
    """The source read from a `History` instead of a clone: it answers the reads `Source` makes
    of Git, and inherits every choice `Source` makes on what they return."""

    def __init__(self, repository: str, history: History) -> None:
        super().__init__(repository)
        self.history = history

    def __enter__(self) -> HeldSource:
        return self

    def __exit__(self, *_: object) -> None:
        pass

    def _commit(self, ref: str) -> str | None:
        return self.history.commit_of(ref)

    def _tag(self, commit: str) -> str | None:
        return self.history.tag_of(commit)

    def _short(self, commit: str) -> str:
        return commit[:7]

    def _date(self, commit: str) -> str:
        return self.history.date

    def _archived(self, ref: harness.Ref, paths: tuple[str, ...]) -> dict[str, bytes]:
        at = self.history.commits[ref.commit]
        return {name: data for name, data in at.items() if any(name == path or name.startswith(path + "/") for path in paths)}

    def _blob(self, ref: harness.Ref, path: str) -> bytes | None:
        return self.history.commits[ref.commit].get(path)


def plain_target_git(target: Path, *arguments: str) -> subprocess.CompletedProcess:
    """What Git says of a plain folder that is the top of its own work tree, with no origin and
    no setting of its own."""
    if arguments == ("rev-parse", "--show-toplevel"):
        return subprocess.CompletedProcess(arguments, 0, str(target), "")
    return subprocess.CompletedProcess(arguments, 1, "", "")


DUBIOUS_OWNERSHIP = (
    "fatal: detected dubious ownership in repository at '{target}'\n"
    "'{target}/.git' is owned by:\n\t'S-1-5-21-1008'\nbut the current user is:\n\t'S-1-5-21-1001'\n"
    "To add an exception for this directory, call:\n\n"
    "\tgit config --global --add safe.directory {target}\n"
)


def git_refusing_ownership(target: Path, *arguments: str) -> subprocess.CompletedProcess:
    """Git's refusal as issue 1 recorded it, word for word: the suite's Git predates the
    ownership check, so the refusal is proved against the message Git prints where it has one."""
    return subprocess.CompletedProcess(arguments, 128, "", DUBIOUS_OWNERSHIP.format(target=target.as_posix()))


def git_checks_ownership() -> bool:
    """Whether this machine's Git refuses a repository owned by another identity, asked by Git's
    own test knob; a Git older than 2.35.2 has no such check and the knob does nothing."""
    with tempfile.TemporaryDirectory() as workspace:
        subprocess.run(["git", "init", "--quiet", workspace], capture_output=True)
        asked = subprocess.run(
            ["git", "-C", workspace, "rev-parse", "--show-toplevel"],
            capture_output=True, encoding="utf-8", env={**os.environ, "GIT_TEST_ASSUME_DIFFERENT_OWNER": "1"},
        )
        return asked.returncode != 0 and "dubious ownership" in asked.stderr


def checks_in_process(target: Path, arguments: list[str]) -> subprocess.CompletedProcess:
    """The gate's child, run as its `main`: the fixture's target holds copies of the live scripts,
    so the module already loaded is the one the child would have run, rooted where the child
    would have rooted itself."""
    script = Path(arguments[0])
    module = {"inject_rules.py": inject_rules, "mechanisms.py": mechanisms}[script.name]
    said, complained = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(said), contextlib.redirect_stderr(complained):
        status = module.main(arguments[1:], root=script.parents[3])
    return subprocess.CompletedProcess(arguments, status, said.getvalue(), complained.getvalue())


class TwoTrees(RepositoryCase):
    """A source holding a small core with the live scripts, and a target beside it. The source's
    history is held in memory and the gate's checks run in-process, unless the case proves a
    process — then both trees are real repositories and the gate starts its children."""

    def setUp(self) -> None:
        super().setUp()
        self.source = self.root
        if not self._proves_a_process():
            self.history = History()
            self._patch(harness, "Source", lambda repository: HeldSource(repository, self.history))
            self._patch(harness, "_git_said", plain_target_git)
            self._patch(harness, "_python", checks_in_process)
        self.seed_source()
        self.target = self.another_repository()

    def commit(self, message: str = "records") -> None:
        if self._proves_a_process():
            super().commit(message)
        else:
            self.history.commit({name: (self.source / name).read_bytes() for name in folder_listing(self.source)})

    def tag(self, name: str) -> None:
        if self._proves_a_process():
            self.git("tag", name)
        else:
            self.history.tag(name)

    def remove(self, *names: str) -> None:
        """Takes files or whole directories out of the source; the next commit records it."""
        for name in names:
            path = self.source / name
            if path.is_dir():
                shutil.rmtree(path)
            else:
                path.unlink()

    def seed_source(self) -> None:
        self.write(KEEPER, "---\nname: keeper\ndescription: keeps\n---\n\n# Keeper\n\nKeep things.\n")
        self.write(HARNESS_SKILL, HARNESS_SKILL_TEXT)
        self.write(TICKET_SKILL, TICKET_SKILL_TEXT)
        self.write(QUEUE_ARRIVAL, QUEUE_ARRIVAL_TEXT)
        self.write(DOC, SAMPLE_DOC)
        self.write("AGENTS.md", ENTRY)
        self.write("CLAUDE.md", "@AGENTS.md\n")
        self.write(".agents/README.md", "# Installed harness\n\nSkills live under `skills/`.\n")
        self.write(".agents/glossary.md", "# The development method\n\n**Recipient**: a tree that received core.\n")
        for script in SCRIPTS.glob("*.py"):
            # A real gate runs these copies as its children; an in-memory one runs the loaded
            # modules, so a line naming the script stands in and nothing tokenizes the live code.
            if self._proves_a_process():
                text = script.read_text(encoding="utf-8")
            else:
                text = f"# {script.name}: the gate runs the loaded module in its place\n"
            self.write(f".agents/scripts/gw/{script.name}", text)
        self.write(".agents/scripts/gw/test/test_arrival.py", ARRIVAL_TEST)
        self.write(TICKET, "# Sweep\n")
        self.write("README.md", "# The repository's front page, never shipped\n")
        self.write("LICENSE", LICENSE_TEXT)
        self.write("local.rules.md", "# local — never shipped\n")
        self.commit("core")

    def run_harness(self, *operands: str) -> tuple[int, dict]:
        said = io.StringIO()
        with contextlib.redirect_stdout(said):
            status = harness.main([str(self.target), *operands, "--from", str(self.source)])
        return status, json.loads(said.getvalue())

    def target_text(self, name: str) -> str:
        with (self.target / name).open(encoding="utf-8", newline="") as handle:
            return handle.read()

    def target_snapshot(self) -> dict[str, bytes]:
        """Every byte of the target, and its index where the case may start a process."""
        files = {name: (self.target / name).read_bytes() for name in folder_listing(self.target)}
        if not self._proves_a_process():
            return files
        index = subprocess.run(
            ["git", "ls-files", "--stage"], cwd=self.target, capture_output=True, encoding="utf-8", check=True
        ).stdout
        return {**files, "<index>": index.encode()}

    def short_head(self) -> str:
        if self._proves_a_process():
            return self.git("rev-parse", "--short", "HEAD").strip()
        return self.history.head[:7]


# --- the pure parts -----------------------------------------------------------------------------


class TheShear(unittest.TestCase):
    def test_a_block_wrapper_leaves_with_its_lines_and_the_rule_stays(self) -> None:
        text = "# A\n\n<straw-dog question=\"q-0001\">\nThe rule.\n</straw-dog>\n\n## B\n"

        self.assertEqual("# A\n\nThe rule.\n\n## B\n", harness.sheared("a.md", text))

    def test_an_inline_wrapper_in_a_table_cell_leaves_the_row_a_row(self) -> None:
        text = '| sweeping | — | <straw-dog question="q-0001">not yet</straw-dog> |\n'

        self.assertEqual("| sweeping | — | not yet |\n", harness.sheared("a.md", text))

    def test_nested_wrappers_all_leave_and_the_content_is_joined_as_written(self) -> None:
        text = (
            '<straw-dog question="q-0001">\n'
            'Outer says <straw-dog question="q-0001.0001">inner</straw-dog> too.\n'
            "</straw-dog>\n"
        )

        self.assertEqual("Outer says inner too.\n", harness.sheared("a.md", text))

    def test_a_wrapper_drawn_in_a_fence_or_a_code_span_is_left_alone(self) -> None:
        text = (
            "Write `<straw-dog question=\"q-N\">` around it.\n\n"
            "```md\n<straw-dog question=\"q-0001\">rule</straw-dog>\n```\n"
        )

        self.assertEqual(text, harness.sheared("a.md", text))

    def test_an_unbalanced_wrapper_refuses_naming_the_file(self) -> None:
        with self.assertRaises(harness.Refused) as refused:
            harness.sheared("a.md", '<straw-dog question="q-0001">\nRule.\n')

        self.assertIn("a.md", str(refused.exception))
        self.assertIn("never closes", str(refused.exception))

    def test_a_todo_loses_its_binding_and_keeps_its_words(self) -> None:
        code = "x = 1\n# TODO q-0002: the shear strips\n# this on install.\n"

        self.assertEqual("x = 1\n# TODO: the shear strips\n# this on install.\n", harness.todo_bindings_sheared(code))


class TheLocalBlockStrip(unittest.TestCase):
    def test_the_block_and_the_newline_the_installer_added_leave_and_the_rest_is_byte_identical(self) -> None:
        around = "## Project-local\n\n<installed by=\"shape\">\n**R7** Core's.\n</installed>\n"
        text = around + '\n<installed by="local">\n**L1** Ours.\n</installed>\n' + "\n## Straw dogs\n"

        self.assertEqual(around + "\n## Straw dogs\n", harness.without_local_blocks("AGENTS.md", text))


class TheStamp(unittest.TestCase):
    def test_the_announce_line_names_the_repository_and_the_ref_and_keeps_the_lines_ending(self) -> None:
        ref = harness.Ref("goodwolf-harness", "abc" * 13 + "d", "abc1234", "2026-09-20")
        text = "# Entry contract\r\n\r\nEntry contract: v13, 2026-09-20.\r\n\r\nOpen with it.\r\n"

        self.assertEqual(
            "# Entry contract\r\n\r\nEntry contract: goodwolf-harness@abc1234, 2026-09-20.\r\n\r\nOpen with it.\r\n",
            harness.stamped(text, ref),
        )

    def test_an_entry_file_with_no_announce_line_refuses(self) -> None:
        ref = harness.Ref("goodwolf-harness", "a" * 40, "aaaaaaa", "2026-09-20")

        with self.assertRaises(harness.Refused) as refused:
            harness.stamped("# Something else\n", ref)

        self.assertIn("not the harness", str(refused.exception))


class TheLinks(unittest.TestCase):
    """The link step against a platform that refuses a symlink, which is refused here by hand so
    the case proves the same thing on a machine that would have made one."""

    def setUp(self) -> None:
        workspace = tempfile.TemporaryDirectory()
        self.addCleanup(workspace.cleanup)
        self.target = Path(workspace.name).resolve()
        (self.target / harness.SKILLS).mkdir(parents=True)
        self.link = self.target / ".claude/skills"
        self.report = harness.Report(target=".", mode="update", repository="")

        def refuse(*arguments: object, **options: object) -> None:
            raise OSError("a required privilege is not held")

        self.symlink = os.symlink
        os.symlink = refuse
        self.addCleanup(setattr, os, "symlink", self.symlink)

    def test_a_link_the_platform_will_not_replace_is_left_standing(self) -> None:
        # A directory stands in for the link: what is proved is that nothing is removed.
        self.link.mkdir(parents=True)

        harness._make_links(self.target, {".claude/skills": "repoint"}, self.report)

        self.assertTrue(os.path.lexists(self.link))
        self.assertEqual("pending", self.report.links[0]["state"])
        self.assertTrue(self.report.links[0]["stands"])
        self.assertFalse(os.path.lexists(self.link.with_name("skills.gw-new")))

    def test_a_refused_repoint_hands_over_a_command_that_removes_before_it_makes(self) -> None:
        self.link.mkdir(parents=True)

        harness._make_links(self.target, {".claude/skills": "repoint"}, self.report)

        command = self.report.pending[0]
        self.assertLess(command.index("rmdir" if os.name == "nt" else "rm "), command.index("mklink" if os.name == "nt" else "ln -s"))

    def test_a_link_written_to_the_skills_is_kept_by_a_process_that_cannot_see_through_it(self) -> None:
        os.symlink = self.symlink
        if not platform_makes_symlinks():
            self.skipTest("this platform refuses to create a symlink; a link to keep cannot be made")
        for link in harness.LINKS:
            (self.target / link).parent.mkdir(parents=True, exist_ok=True)
            self.symlink(harness.LINK_TARGET.replace("/", os.sep), self.target / link, target_is_directory=True)
        resolves = harness._resolves_to
        harness._resolves_to = lambda link, skills: False
        self.addCleanup(setattr, harness, "_resolves_to", resolves)

        self.assertEqual({link: "keep" for link in harness.LINKS}, harness._link_plan(self.target))


class TheRepositoryLine(unittest.TestCase):
    """The line naming where core comes from: stamped, and set aside."""

    def test_the_stamp_replaces_the_url_and_keeps_the_lines_ending(self) -> None:
        ref = harness.Ref("goodwolf-harness", "a" * 40, "aaaaaaa", "2026-09-20")
        text = "---\nname: harness\n---\r\n\r\nRepository: https://example.invalid/old.git\r\n\r\nProse.\r\n"

        self.assertEqual(
            "---\nname: harness\n---\r\n\r\nRepository: https://example.invalid/new.git\r\n\r\nProse.\r\n",
            harness.repository_stamped(text, ref, "https://example.invalid/new.git"),
        )

    def test_the_line_leaves_with_its_newline_and_only_from_the_harness_skill(self) -> None:
        text = "A\n\nRepository: https://example.invalid/x.git\n\nB\n"

        self.assertEqual("A\n\n\nB\n", harness.without_repository_line(HARNESS_SKILL, text))
        self.assertEqual(text, harness.without_repository_line(KEEPER, text))

    def test_a_line_with_anything_after_the_url_is_not_the_line(self) -> None:
        self.assertIsNone(harness.REPOSITORY.search("Repository: https://example.invalid/x.git and more\n"))


class TheSource(TwoTrees):
    @proves_a_process
    def test_the_manifest_at_a_ref_is_core_the_two_root_files_and_the_license_and_nothing_else(self) -> None:
        with harness.Source(str(self.source)) as source:
            ref = source.resolve("HEAD")
            manifest = source.files(ref)

        self.assertIn("AGENTS.md", manifest)
        self.assertIn("CLAUDE.md", manifest)
        self.assertIn(KEEPER, manifest)
        self.assertIn(".agents/scripts/gw/test/test_arrival.py", manifest)
        self.assertEqual((self.source / "LICENSE").read_bytes(), manifest[INSTALLED_LICENSE])
        self.assertNotIn("LICENSE", manifest)
        self.assertNotIn("README.md", manifest)
        self.assertNotIn("local.rules.md", manifest)
        self.assertNotIn(TICKET, manifest)

        with self.subTest(license="absent at the ref"):
            # Every ref before the license existed lacks it, and the archive refuses a path the ref lacks.
            self.remove("LICENSE")
            self.commit("no license")
            with harness.Source(str(self.source)) as source:
                self.assertNotIn(INSTALLED_LICENSE, source.files(source.resolve("HEAD")))

    @proves_a_process
    def test_a_tagged_commit_is_announced_by_its_tag_and_an_untagged_one_by_its_short_commit(self) -> None:
        with harness.Source(str(self.source)) as source:
            untagged = source.resolve("HEAD")
        self.tag("v1")
        with harness.Source(str(self.source)) as source:
            tagged = source.resolve("HEAD")

        self.assertEqual(self.short_head(), untagged.announced)
        self.assertEqual("v1", tagged.announced)
        self.assertEqual(self.source.name, tagged.repository)
        self.assertEqual("Entry contract: " + self.source.name + "@v1, " + tagged.date + ".", tagged.stamp)

    def test_the_repository_name_is_the_last_segment_without_dot_git(self) -> None:
        self.assertEqual("goodwolf-harness", harness.repository_name("https://github.com/x/goodwolf-harness.git"))
        self.assertEqual("agents", harness.repository_name("D:\\Dev\\AI\\agents\\"))


# --- refusals ------------------------------------------------------------------------------------


class ARefusal(TwoTrees):
    """Each writes nothing, and names its step."""

    def assert_refused(self, operands: tuple[str, ...], *said: str) -> None:
        before = self.target_snapshot()

        status, report = self.run_harness(*operands)

        self.assertEqual(1, status)
        self.assertEqual(1, len(report["refusals"]), report)
        self.last_refusal = report["refusals"][0]
        for word in said:
            self.assertIn(word, self.last_refusal)
        self.assertEqual(before, self.target_snapshot())

    # The two refusals Git decides are asked of the target before anything is read from the
    # source, so a `Source` never entered — never cloned — is all they need of it.

    @proves_a_process
    def test_a_target_that_is_not_a_work_tree_root(self) -> None:
        inside = self.target / "inside"
        inside.mkdir()

        with self.assertRaisesRegex(harness.Refused, f"target:.*top level.*{self.target.name}"):
            harness._work_tree_root(inside, harness.Source(str(self.source)))

    def plain_folder(self, *holding: str) -> Path:
        """A folder inside no repository, holding the named files; the case's own, cleaned up."""
        workspace = tempfile.TemporaryDirectory()
        self.addCleanup(workspace.cleanup)
        folder = Path(workspace.name).resolve()
        for name in holding:
            (folder / name).write_text("theirs\n", encoding="utf-8")
        return folder

    def run_harness_at(self, folder: Path, *operands: str) -> tuple[int, dict]:
        said = io.StringIO()
        with contextlib.redirect_stdout(said):
            status = harness.main([str(folder), *operands, "--from", str(self.source)])
        return status, json.loads(said.getvalue())

    @proves_a_process
    def test_a_folder_with_files_of_its_own_that_is_no_repository_is_refused_with_the_step(self) -> None:
        folder = self.plain_folder("notes.txt")

        status, report = self.run_harness_at(folder, "--install")

        self.assertEqual(1, status)
        self.assertEqual(1, len(report["refusals"]), report)
        self.assertIn("not a git repository", report["refusals"][0])
        self.assertIn("git init", report["refusals"][0])
        self.assertEqual(["notes.txt"], [path.name for path in folder.iterdir()])

    @proves_a_process
    def test_an_empty_folder_is_initialised_and_the_install_arrives(self) -> None:
        folder = self.plain_folder()

        status, report = self.run_harness_at(folder, "--install")

        self.assertEqual([], report["refusals"])
        self.assertTrue((folder / ".git").is_dir())
        self.assertTrue(any("git init" in note for note in report["notes"]), report["notes"])
        for name, gate in report["gates"].items():
            self.assertTrue(gate["passed"], (name, gate))
        self.assertTrue(report["arrived"])

    @proves_a_process
    def test_the_link_step_initialises_nothing_in_an_empty_folder(self) -> None:
        folder = self.plain_folder()
        said = io.StringIO()
        with contextlib.redirect_stdout(said):
            status = harness.main([str(folder), "--links"])
        report = json.loads(said.getvalue())

        self.assertEqual(1, status)
        self.assertIn("not a git repository", report["refusals"][0])
        self.assertFalse((folder / ".git").exists())

    def test_a_target_git_refuses_for_dubious_ownership_is_refused_with_gits_own_command(self) -> None:
        self._patch(harness, "_git_said", git_refusing_ownership)

        self.assert_refused(("--install",), "target:", "dubious ownership", f"safe.directory {self.target.as_posix()}")
        self.assertNotIn("top level", self.last_refusal)

    @proves_a_process
    def test_gits_own_ownership_check_is_what_the_refusal_reads(self) -> None:
        if not git_checks_ownership():
            self.skipTest("this Git predates the ownership check; the refusal is proved against its message")
        self._patch(os, "environ", {**os.environ, "GIT_TEST_ASSUME_DIFFERENT_OWNER": "1"})

        self.assert_refused(("--install",), "target:", "dubious ownership", "safe.directory")

    @proves_a_process
    def test_the_source_itself_by_its_remote(self) -> None:
        subprocess.run(["git", "remote", "add", "origin", str(self.source)], cwd=self.target, check=True)

        with self.assertRaisesRegex(harness.Refused, "target:.*the source itself"):
            harness._work_tree_root(self.target, harness.Source(str(self.source)))

    def test_install_over_a_present_manifest_path(self) -> None:
        for present in ("AGENTS.md", "CLAUDE.md", KEEPER, INSTALLED_LICENSE):
            with self.subTest(present=present):
                shutil.rmtree(self.target / ".agents", ignore_errors=True)
                for stale in ("AGENTS.md", "CLAUDE.md"):
                    (self.target / stale).unlink(missing_ok=True)
                (self.target / present).parent.mkdir(parents=True, exist_ok=True)
                (self.target / present).write_text("theirs\n", encoding="utf-8")

                self.assert_refused(("--install",), "install:", present, "--update")

    def test_update_without_core(self) -> None:
        self.assert_refused(("--update",), "update:", "--install")

    def test_update_over_an_entry_file_holding_a_retired_tag(self) -> None:
        self.run_harness("--install")
        entry = self.target / "AGENTS.md"
        entry.write_text(entry.read_text(encoding="utf-8") + "\n<project-local>\ntheirs\n</project-local>\n", encoding="utf-8")

        self.assert_refused(("--update",), "update:", "<project-local>", "local.rules.md")

    def test_update_over_an_edited_core_file_without_overwrite(self) -> None:
        self.run_harness("--install")
        (self.target / KEEPER).write_text("# Keeper, edited by hand\n", encoding="utf-8")

        self.assert_refused(("--update",), "update:", KEEPER, "--overwrite")

    def test_update_when_the_tree_announces_no_ref_without_overwrite(self) -> None:
        self.run_harness("--install")
        entry = self.target / "AGENTS.md"
        entry.write_text(entry.read_text(encoding="utf-8").replace(f"{self.source.name}@", "v"), encoding="utf-8")

        self.assert_refused(("--update",), "update:", "no ref", "--overwrite")

    def test_a_tree_announcing_another_repository(self) -> None:
        self.run_harness("--install")
        entry = self.target / "AGENTS.md"
        entry.write_text(entry.read_text(encoding="utf-8").replace(f"{self.source.name}@", "other@"), encoding="utf-8")

        self.assert_refused(("--check",), "announces other", self.source.name)

    def test_a_ref_that_does_not_resolve(self) -> None:
        self.assert_refused(("--install", "--at", "nowhere"), "ref:", "nowhere", str(self.source))

    def test_a_docs_link_inside_a_straw_dog_at_the_ref_cannot_ship(self) -> None:
        self.write(
            KEEPER,
            "# Keeper\n\n"
            f'<straw-dog question="q-0002">\nSee [the sweep](../../../{TICKET}).\n</straw-dog>\n',
        )
        self.commit("a leak")

        self.assert_refused(("--install",), "ship:", KEEPER, TICKET)

    def test_a_check_of_a_tree_that_is_not_a_recipient(self) -> None:
        self.assert_refused(("--check",), "check:", "not a recipient")

    @unittest.skipUnless(os.name == "nt", "a junction is a Windows object")
    def test_a_junction_where_a_link_goes(self) -> None:
        (self.target / ".agents" / "skills").mkdir(parents=True)
        (self.target / ".claude").mkdir()
        import _winapi  # a junction without a process, as CPython's own tests make one

        _winapi.CreateJunction(str(self.target / ".agents" / "skills"), str(self.target / ".claude" / "skills"))
        shutil.rmtree(self.target / ".agents")

        self.assert_refused(("--install",), "link:", ".claude/skills", "junction")

    def test_a_directory_of_the_recipients_own_where_a_link_goes(self) -> None:
        (self.target / ".cursor" / "skills").mkdir(parents=True)

        self.assert_refused(("--install",), "link:", ".cursor/skills", "recipient's own")


# --- install -------------------------------------------------------------------------------------


class AnInstall(TwoTrees):
    def test_lands_the_manifest_transformed_and_nothing_outside_it(self) -> None:
        status, report = self.run_harness("--install")

        self.assertTrue((self.target / KEEPER).is_file())
        self.assertTrue((self.target / ".agents/scripts/gw/harness.py").is_file())
        self.assertFalse((self.target / "README.md").exists())
        self.assertFalse((self.target / "local.rules.md").exists())
        self.assertFalse((self.target / TICKET).exists())
        entry = self.target_text("AGENTS.md")
        self.assertIn(f"Entry contract: {self.source.name}@{self.short_head()}, ", entry)
        self.assertIn(WRAPPED_RULE, entry)
        self.assertNotIn("<straw-dog", entry)
        self.assertNotIn('<installed by="local">', entry)
        self.assertEqual("| sweeping | — | not yet |", next(
            line for line in self.target_text(DOC).splitlines() if line.startswith("| sweeping")
        ))
        for name in report["written"]:
            if name.endswith(".md"):
                self.assertNotIn("<straw-dog", self.target_text(name), name)
        self.assertEqual("@AGENTS.md\n", self.target_text("CLAUDE.md"))

    def test_arrives_on_three_gates_and_reports_the_links_made_or_pending_with_the_command(self) -> None:
        status, report = self.run_harness("--install")

        self.assertEqual(["ref", "injector", "shape"], list(report["gates"]))
        for name, gate in report["gates"].items():
            self.assertTrue(gate["passed"], (name, gate))
        self.assertTrue(report["arrived"])
        self.assertEqual(0, status)
        if platform_makes_symlinks():
            self.assertEqual(["made", "made"], [link["state"] for link in report["links"]])
            self.assertEqual({".claude/skills": True, ".cursor/skills": True}, report["links_resolve"])
        else:
            self.assertEqual(["pending", "pending"], [link["state"] for link in report["links"]])
            self.assertEqual(2, len(report["pending"]))
            self.assertIn(str(self.target / ".claude" / "skills"), report["pending"][0])
            self.assertIn("mklink /D" if os.name == "nt" else "ln -s", report["pending"][0])
            self.assertEqual({".claude/skills": False, ".cursor/skills": False}, report["links_resolve"])

    def test_a_shape_diagnostic_in_the_recipient_leaves_arrival_false_naming_the_gate(self) -> None:
        self.write(".agents/skills/silent/SKILL.md", "# Silent\n\nNamed by nothing, claiming nothing.\n")
        self.commit("a silent skill")

        status, report = self.run_harness("--install")

        self.assertFalse(report["gates"]["shape"]["passed"])
        self.assertFalse(report["arrived"])
        self.assertEqual(1, status)

    def test_a_file_edited_after_install_is_named_by_the_check(self) -> None:
        self.run_harness("--install")
        (self.target / KEEPER).write_text("# Keeper, edited\n", encoding="utf-8")

        status, report = self.run_harness("--check")

        self.assertEqual([KEEPER], report["gates"]["ref"]["differs"])
        self.assertFalse(report["arrived"])

    def test_a_crlf_copy_of_a_shipped_file_is_not_an_edit(self) -> None:
        self.run_harness("--install")
        copy = self.target / KEEPER
        copy.write_bytes(copy.read_bytes().replace(b"\n", b"\r\n"))

        status, report = self.run_harness("--check")

        self.assertEqual([], report["gates"]["ref"]["differs"])


# --- update --------------------------------------------------------------------------------------


class TheRealPath(TwoTrees):
    """What every other case here holds in memory, done once for real: the source cloned, and the
    gate's checks run as the recipient's own scripts, each in a child of its own."""

    proves_a_process = True

    def test_an_install_arrives_a_check_names_an_edit_and_an_update_replaces_it(self) -> None:
        status, report = self.run_harness("--install")

        self.assertEqual(0, status, report["gates"])
        self.assertFalse(any("__pycache__" in path.parts for path in self.target.rglob("*")))

        (self.target / KEEPER).write_text("# Keeper, edited\n", encoding="utf-8")
        status, report = self.run_harness("--check")

        self.assertEqual(1, status)
        self.assertEqual([KEEPER], report["gates"]["ref"]["differs"])

        self.write(KEEPER, "# Keeper\n\nKeep more things.\n")
        self.commit("core moved")
        status, report = self.run_harness("--update", "--overwrite")

        self.assertEqual(0, status, report["gates"])
        self.assertEqual([KEEPER], report["replaced"])
        self.assertIn("Keep more things.", self.target_text(KEEPER))


class AnUpdate(TwoTrees):
    def setUp(self) -> None:
        super().setUp()
        self.run_harness("--install")
        self.write_target(
            "local.rules.md",
            "# local — this project's rules\n\n| target | anchor |\n|---|---|\n| `AGENTS.md` | `## Project-local` |\n\n"
            "## L1 — ours\n\n- **target** `AGENTS.md`\n- **authority** the user, 2026-09-21\n\n<rule>\nOur answer.\n</rule>\n",
        )
        self.local_before = (self.target / "local.rules.md").read_bytes()

    def write_target(self, name: str, text: str) -> None:
        path = self.target / name
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", encoding="utf-8", newline="") as handle:
            handle.write(text)

    def test_leaves_the_local_file_byte_identical_and_restores_its_block_last(self) -> None:
        self.write(KEEPER, "# Keeper\n\nKeep more things.\n")
        self.commit("core moved")

        status, report = self.run_harness("--update")

        self.assertEqual(self.local_before, (self.target / "local.rules.md").read_bytes())
        self.assertIn("Keep more things.", self.target_text(KEEPER))
        entry = self.target_text("AGENTS.md")
        self.assertIn('<installed by="local">\n**L1** Our answer.\n</installed>', entry)
        self.assertGreater(entry.index('<installed by="local">'), entry.index("## Project-local"))
        self.assertIn(f"@{self.short_head()}, ", entry)
        self.assertTrue(report["gates"]["ref"]["passed"], report["gates"]["ref"])
        self.assertTrue(report["gates"]["injector"]["passed"], report["gates"]["injector"])

    def test_reports_written_only_the_files_that_changed(self) -> None:
        self.write(KEEPER, "# Keeper\n\nKeep more things.\n")
        self.commit("core moved")

        status, report = self.run_harness("--update")

        self.assertIn(KEEPER, report["written"])
        self.assertIn("AGENTS.md", report["written"], "the announce line names the new ref")
        self.assertNotIn(".agents/glossary.md", report["written"])

    def test_deletes_what_left_the_manifest_and_the_directories_it_emptied_when_the_line_announces_a_ref(self) -> None:
        self.remove(".agents/glossary.md", ".agents/scripts/gw/test")
        self.commit("the glossary and the shipped tests leave")

        status, report = self.run_harness("--update")

        self.assertEqual(
            [".agents/glossary.md", ".agents/scripts/gw/test/test_arrival.py"], sorted(report["deleted"])
        )
        self.assertFalse((self.target / ".agents/glossary.md").exists())
        self.assertFalse((self.target / ".agents/scripts/gw/test").exists())

    def test_reports_the_recipients_own_files_under_core_and_leaves_them(self) -> None:
        self.write_target(".agents/skills/theirs/SKILL.md", "Mechanism: unowned by design — theirs\n\n# Theirs\n")

        status, report = self.run_harness("--update")

        self.assertEqual([".agents/skills/theirs/SKILL.md"], report["own"])
        self.assertTrue((self.target / ".agents/skills/theirs/SKILL.md").is_file())

    def test_a_block_the_recipients_own_mechanism_installed_is_not_an_edit_in_core(self) -> None:
        self.write_target(
            ".agents/mechanisms/theirs/theirs.rules.md",
            f"# theirs — the recipient's own rules\n\n| target | anchor |\n|---|---|\n| `{KEEPER}` | `# Keeper` |\n\n"
            f"## T1 — theirs\n\n- **target** `{KEEPER}`\n- **authority** the user, 2026-10-05\n\n<rule>\nTheir rule.\n</rule>\n",
        )
        inject_rules.install(self.target, inject_rules.read_rules_file(self.target, "theirs"), overwrite=False)
        self.assertIn('<installed by="theirs">', self.target_text(KEEPER))

        _, checked = self.run_harness("--check")
        self.assertTrue(checked["gates"]["ref"]["passed"], checked["gates"]["ref"])

        _, report = self.run_harness("--update")

        self.assertEqual([], report["replaced"])
        self.assertNotIn(KEEPER, report["written"])
        self.assertIn('<installed by="theirs">', self.target_text(KEEPER))
        self.assertTrue(report["gates"]["ref"]["passed"], report["gates"]["ref"])

    def test_a_block_whose_owner_has_no_rules_file_is_an_edit_in_core(self) -> None:
        self.write_target(KEEPER, self.target_text(KEEPER) + '\n<installed by="nobody">\n**N1** A rule.\n</installed>\n')

        _, checked = self.run_harness("--check")

        self.assertEqual([KEEPER], checked["gates"]["ref"]["differs"])

    def test_with_no_announced_ref_overwrite_replaces_every_core_file_and_deletes_nothing(self) -> None:
        entry = self.target / "AGENTS.md"
        entry.write_text(entry.read_text(encoding="utf-8").replace(f"{self.source.name}@", "v"), encoding="utf-8")
        self.write_target(".agents/stale.md", "left over from a hand install\n")
        self.remove(".agents/glossary.md")
        self.commit("the glossary leaves")

        status, report = self.run_harness("--update", "--overwrite")

        self.assertEqual([], report["deleted"])
        self.assertTrue((self.target / ".agents/glossary.md").exists())
        self.assertIn(".agents/stale.md", report["own"])
        self.assertIn(f"@{self.short_head()}, ", self.target_text("AGENTS.md"))

    def test_overwrite_replaces_an_edited_core_file_and_names_it(self) -> None:
        (self.target / KEEPER).write_text("# Keeper, edited\n", encoding="utf-8")

        status, report = self.run_harness("--update", "--overwrite")

        self.assertEqual([KEEPER], report["replaced"])
        self.assertIn("Keep things.", self.target_text(KEEPER))

    def test_a_link_that_resolves_is_left_alone(self) -> None:
        if not platform_makes_symlinks():
            self.skipTest("this platform refuses to create a symlink; a kept link cannot be made")

        status, report = self.run_harness("--update")

        self.assertEqual(["kept", "kept"], [link["state"] for link in report["links"]])

    def test_an_injector_refusal_is_unfinished_and_names_the_resume(self) -> None:
        self.write_target(
            "local.rules.md",
            "# local\n\n| target | anchor |\n|---|---|\n| `AGENTS.md` | `## Project-local` |\n\n"
            "## L1 — ours\n\n- **target** `AGENTS.md`\n- **overrides** `sample/P9`\n"
            "- **authority** the user, 2026-09-21\n\n<rule>\nOur answer.\n</rule>\n",
        )

        status, report = self.run_harness("--update")

        self.assertEqual(1, status)
        self.assertIn("inject:", report["refusals"][0])
        self.assertIn("L1 overrides sample/P9", report["refusals"][0])
        self.assertIn("harness.py . --check", report["refusals"][0])
        self.assertIn("Keep things.", self.target_text(KEEPER))


class ATreeInstalledUnderEarlierRules(TwoTrees):
    """A recipient announcing a ref that today's shipping rules would refuse: no arrival shelf, a
    harness skill with no Repository line, and a test outside `gw/test/` citing a record only the
    origin has. What such a ref shipped is read to compare
    against and to know what left the manifest, and is never shipped again, so none of the three
    may stop a check or an update.

    The tree is made the way the earlier code left it rather than by the code under test: installed
    from today's core, then given each difference by hand."""

    OLD_TEST = ".agents/scripts/test/test_citations.py"
    OLD_TEST_TEXT = 'CITED = "docs/tickets/01-0001-closed.md"\n'

    def setUp(self) -> None:
        super().setUp()
        today = self.short_head()
        self.run_harness("--install")
        self.remove(QUEUE_ARRIVAL, "LICENSE")
        self.write(HARNESS_SKILL, harness.REPOSITORY.sub("", HARNESS_SKILL_TEXT, count=1))
        self.write(self.OLD_TEST, self.OLD_TEST_TEXT)
        self.commit("core as it stood under earlier rules")
        self.earlier = self.short_head()
        (self.target / QUEUE_ARRIVAL).unlink()
        (self.target / DELIVERY_STATUS).unlink()
        (self.target / INSTALLED_LICENSE).unlink(missing_ok=True)
        skill = self.target / HARNESS_SKILL
        skill.write_text(harness.REPOSITORY.sub("", skill.read_text(encoding="utf-8"), count=1), encoding="utf-8")
        (self.target / self.OLD_TEST).parent.mkdir(parents=True, exist_ok=True)
        (self.target / self.OLD_TEST).write_text(self.OLD_TEST_TEXT, encoding="utf-8")
        entry = self.target / "AGENTS.md"
        entry.write_text(entry.read_text(encoding="utf-8").replace(f"@{today},", f"@{self.earlier},"), encoding="utf-8")
        self.remove(self.OLD_TEST)
        self.write(QUEUE_ARRIVAL, QUEUE_ARRIVAL_TEXT)
        self.write(HARNESS_SKILL, HARNESS_SKILL_TEXT)
        self.write("LICENSE", LICENSE_TEXT)
        self.commit("today's rules")

    def test_a_check_compares_against_what_the_earlier_ref_shipped(self) -> None:
        _, report = self.run_harness("--check")

        self.assertEqual([], report["refusals"])
        self.assertTrue(report["gates"]["ref"]["passed"], report["gates"]["ref"])

    def test_an_update_takes_today_and_gives_the_tree_what_it_lacked(self) -> None:
        status, report = self.run_harness("--update")

        self.assertEqual([], report["refusals"])
        self.assertEqual([], report["replaced"], "nothing in the tree was edited in core")
        self.assertIn(self.OLD_TEST, report["deleted"])
        self.assertFalse((self.target / self.OLD_TEST).exists())
        self.assertIn(DELIVERY_STATUS, report["written"])
        self.assertIn(INSTALLED_LICENSE, report["written"])
        self.assertIsNotNone(harness.REPOSITORY.search(self.target_text(HARNESS_SKILL)))
        self.assertIn(f"@{self.short_head()}, ", self.target_text("AGENTS.md"))
        self.assertEqual(0, status, report["gates"])


# --- where core came from -------------------------------------------------------------------------


class TheSourceARecipientHolds(TwoTrees):
    """The stamped line, what it survives, and what a recipient can do with no `--from`."""

    def stamped_line(self) -> str:
        found = harness.REPOSITORY.search(self.target_text(HARNESS_SKILL))
        self.assertIsNotNone(found, "the recipient's harness skill must carry the line")
        return found.group("url")

    def test_a_path_from_is_stamped_resolved_so_it_does_not_depend_on_where_anyone_stood(self) -> None:
        said = io.StringIO()
        with contextlib.chdir(self.source.parent), contextlib.redirect_stdout(said):
            status = harness.main([str(self.target), "--install", "--from", self.source.name])

        self.assertEqual(0, status, said.getvalue())
        self.assertEqual(self.source.resolve().as_posix(), self.stamped_line())

    def test_a_url_from_is_stamped_verbatim(self) -> None:
        # A `file://` URL names the source without being a path that exists, so it is stamped as
        # given rather than resolved.
        url = self.source.resolve().as_uri()

        said = io.StringIO()
        with contextlib.redirect_stdout(said):
            status = harness.main([str(self.target), "--install", "--from", url])

        self.assertEqual(0, status, said.getvalue())
        self.assertEqual(url, self.stamped_line())

    def test_an_update_from_another_source_replaces_nothing_in_core(self) -> None:
        self.run_harness("--install")
        beside = self.another_repository() / self.source.name  # the same history, held elsewhere
        beside.mkdir()

        said = io.StringIO()
        with contextlib.redirect_stdout(said):
            status = harness.main([str(self.target), "--update", "--from", str(beside)])
        report = json.loads(said.getvalue())

        self.assertEqual([], report["refusals"])
        self.assertEqual([], report["replaced"])
        self.assertEqual(0, status, report["gates"])
        self.assertEqual(beside.resolve().as_posix(), self.stamped_line())


    def test_a_ref_whose_harness_skill_has_no_line_is_refused_and_nothing_is_written(self) -> None:
        self.write(HARNESS_SKILL, "---\nname: harness\ndescription: places core\n---\n\nNo line here.\n")
        self.commit("the line goes")
        before = self.target_snapshot()

        status, report = self.run_harness("--install")

        self.assertEqual(1, status)
        self.assertIn("not the harness", report["refusals"][0])
        self.assertEqual(before, self.target_snapshot())

    @proves_a_process
    def test_a_recipients_own_script_checks_with_no_from_and_refuses_once_its_skill_lost_the_line(self) -> None:
        self.run_harness("--install")

        checked = self.recipients_own_check()

        self.assertEqual(self.source.resolve().as_posix(), checked["repository"])
        self.assertTrue(checked["gates"]["ref"]["passed"], checked)
        # The fixture's skill carries the line; the one core authors in this tree must too, or
        # every recipient's script would have nothing to read. `home` refuses naming the file.
        self.assertTrue(harness.home(), "core's own harness skill must author the line")

        skill = self.target / HARNESS_SKILL
        skill.write_text(
            harness.without_repository_line(HARNESS_SKILL, skill.read_text(encoding="utf-8")), encoding="utf-8"
        )
        refusal = self.recipients_own_check()["refusals"][0]

        self.assertIn(HARNESS_SKILL, refusal)
        self.assertIn("--from", refusal)
        self.assertIn("no Repository line", refusal)

    def recipients_own_check(self) -> dict:
        """The recipient's copy of the script, run as its own process with no `--from`."""
        done = subprocess.run(
            [sys.executable, str(self.target / ".agents/scripts/gw/harness.py"), str(self.target), "--check"],
            capture_output=True,
            encoding="utf-8",
        )
        return json.loads(done.stdout)


# --- the one door that arrives with content ---------------------------------------------------


class TheDeliveryStatus(TwoTrees):
    """A fresh tree's first session reads the queue before anything has been written into it."""

    def test_an_install_writes_it_in_the_refs_own_words(self) -> None:
        self.write(
            QUEUE_ARRIVAL,
            QUEUE_ARRIVAL_TEXT.replace("nothing is in flight", "the queue is empty, reworded"),
        )
        self.commit("the mechanism rewords its own record")

        status, report = self.run_harness("--install")
        written = self.target_text(DELIVERY_STATUS)

        self.assertEqual(0, status, report)
        self.assertIn("the queue is empty, reworded", written)
        self.assertIn(report["ref"]["announced"], written)
        self.assertNotIn("{ref}", written)
        self.assertIn(DELIVERY_STATUS, report["written"])

    def test_an_install_leaves_a_record_the_tree_brought_with_it(self) -> None:
        # An install refuses only over manifest paths, and this is not one — so a tree that
        # already keeps its own docs/ receives core beside them.
        theirs = "# Материалы\n\nThe project's own queue, in its own words.\n"
        record = self.target / DELIVERY_STATUS
        record.parent.mkdir(parents=True, exist_ok=True)
        record.write_text(theirs, encoding="utf-8", newline="")

        status, report = self.run_harness("--install")

        self.assertEqual(0, status, report["refusals"])
        self.assertEqual(theirs, self.target_text(DELIVERY_STATUS))
        self.assertNotIn(DELIVERY_STATUS, report["written"])
        self.assertTrue(any(DELIVERY_STATUS in note for note in report["notes"]), report["notes"])

    def test_a_ref_with_no_shelf_or_no_block_is_refused_and_nothing_is_written(self) -> None:
        for spoil, reason in (
            (lambda: (self.root / QUEUE_ARRIVAL).unlink(), "this is not the harness"),
            (lambda: self.write(QUEUE_ARRIVAL, "# Arrival\n\nNo block.\n"), "declares no arrival state"),
        ):
            with self.subTest(reason=reason):
                self.write(QUEUE_ARRIVAL, QUEUE_ARRIVAL_TEXT)
                spoil()
                self.commit("spoil the shelf")
                before = self.target_snapshot()

                status, report = self.run_harness("--install")

                self.assertEqual(1, status)
                self.assertIn(reason, report["refusals"][0])
                self.assertEqual(before, self.target_snapshot())


class TheCommandLine(unittest.TestCase):
    def run_main(self, *operands: str) -> int:
        with contextlib.redirect_stdout(io.StringIO()):
            return harness.main(list(operands))

    def test_no_mode_two_modes_or_no_target_is_usage(self) -> None:
        self.assertEqual(2, self.run_main("x"))
        self.assertEqual(2, self.run_main("x", "--install", "--check"))
        self.assertEqual(2, self.run_main("--install"))

    def test_overwrite_belongs_to_update_and_at_never_to_check(self) -> None:
        self.assertEqual(2, self.run_main("x", "--install", "--overwrite"))
        self.assertEqual(2, self.run_main("x", "--check", "--at", "v1"))

    def test_links_takes_no_source_no_ref_and_no_overwrite(self) -> None:
        self.assertEqual(2, self.run_main("x", "--links", "--from", "y"))
        self.assertEqual(2, self.run_main("x", "--links", "--at", "v1"))
        self.assertEqual(2, self.run_main("x", "--links", "--overwrite"))


class TheLinkStep(TwoTrees):
    """`--links` in a tree that holds core: the per-clone step, with no source and no network."""

    def run_links(self) -> tuple[int, dict]:
        said = io.StringIO()
        with contextlib.redirect_stdout(said):
            status = harness.main([str(self.target), "--links"])
        return status, json.loads(said.getvalue())

    def test_a_tree_without_core_is_refused_before_anything_is_written(self) -> None:
        before = self.target_snapshot()

        status, report = self.run_links()

        self.assertEqual(1, status)
        self.assertEqual(1, len(report["refusals"]), report)
        self.assertIn("links:", report["refusals"][0])
        self.assertIn("--install first", report["refusals"][0])
        self.assertEqual(before, self.target_snapshot())

    def test_opens_no_source_and_reports_the_links_without_a_verdict(self) -> None:
        self.run_harness("--install")

        def never(repository: str) -> None:
            raise AssertionError(f"--links opened a source: {repository}")

        self._patch(harness, "Source", never)

        status, report = self.run_links()

        self.assertNotIn("arrived", report)
        self.assertNotIn("gates", report)
        self.assertNotIn("ref", report)
        self.assertEqual("links", report["mode"])
        if platform_makes_symlinks():
            self.assertEqual(0, status)
            self.assertEqual(["kept", "kept"], [link["state"] for link in report["links"]])
            self.assertEqual({".claude/skills": True, ".cursor/skills": True}, report["links_resolve"])
        else:
            self.assertEqual(1, status)
            self.assertEqual(["pending", "pending"], [link["state"] for link in report["links"]])
            self.assertEqual(2, len(report["pending"]))
            self.assertIn("mklink /D" if os.name == "nt" else "ln -s", report["pending"][0])

    def test_the_pending_note_sends_the_person_to_the_step_and_nothing_names_core_symlinks(self) -> None:
        _, report = self.run_harness("--install")

        self.assertFalse(any("core.symlinks" in note for note in report["notes"]), report["notes"])
        if not platform_makes_symlinks():
            self.assertTrue(any("--links" in note for note in report["notes"]), report["notes"])
            self.assertFalse(any("--check" in note for note in report["notes"]), report["notes"])

    @proves_a_process
    def test_whatever_plans_a_link_names_it_in_the_clones_exclude_file_once(self) -> None:
        self.run_harness("--install")
        _, report = self.run_links()

        self.assertEqual(list(harness.LINKS), report["excluded"])
        for link in harness.LINKS:
            ignored = subprocess.run(["git", "-C", str(self.target), "check-ignore", "-q", link], capture_output=True)
            self.assertEqual(0, ignored.returncode, link)
        exclude = (self.target / ".git" / "info" / "exclude").read_text(encoding="utf-8")
        for link in harness.LINKS:
            self.assertEqual(1, exclude.splitlines().count(link), exclude)

    @proves_a_process
    def test_a_pending_link_is_excluded_before_it_exists(self) -> None:
        def refuse(*arguments: object, **options: object) -> None:
            raise OSError("a required privilege is not held")

        self._patch(os, "symlink", refuse)

        _, report = self.run_harness("--install")

        self.assertEqual(["pending", "pending"], [link["state"] for link in report["links"]])
        self.assertEqual(list(harness.LINKS), report["excluded"])

    def test_a_fresh_clone_of_a_recipient_gets_its_links_from_the_step(self) -> None:
        self.run_harness("--install")
        for link in harness.LINKS:
            path = self.target / link
            if path.is_symlink():
                harness._remove_link(path)
        self.assertFalse(any((self.target / link).is_symlink() for link in harness.LINKS))

        status, report = self.run_links()

        if platform_makes_symlinks():
            self.assertEqual(["made", "made"], [link["state"] for link in report["links"]])
            self.assertTrue(all(report["links_resolve"].values()))
        else:
            self.assertEqual(["pending", "pending"], [link["state"] for link in report["links"]])


if __name__ == "__main__":
    unittest.main()
