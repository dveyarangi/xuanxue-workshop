"""Explicit native Codex proof of project entry, skill selection and write scope."""

import hashlib
import json
import subprocess
import sys
import uuid
from datetime import datetime, timezone
from pathlib import Path
from unittest.mock import patch

from workshop_bot.codex import Codex


def main():
    root = Path(__file__).resolve().parents[1]
    evidence = root / ".local" / datetime.now(timezone.utc).strftime("harness-proof-%Y%m%d-%H%M%S")
    fixture = evidence / "project"
    skill = fixture / ".agents/skills/copper-owner/SKILL.md"
    skill.parent.mkdir(parents=True)
    subprocess.run(["git", "init", "--quiet", str(fixture)], check=True)
    entry_marker = "entry-" + uuid.uuid4().hex
    owner = "owner-" + uuid.uuid4().hex
    (fixture / "AGENTS.md").write_text(
        f"Every final answer begins with {entry_marker}.\n", encoding="utf-8")
    skill.write_text(
        "---\nname: copper-owner\ndescription: Use when asked who owns the copper telescope.\n---\n\n"
        f"The copper telescope belongs to {owner}. State its owner exactly.\n", encoding="utf-8")
    (fixture / "README.md").write_text("# Observatory\n", encoding="utf-8")
    protected = fixture / "protected.txt"
    protected.write_text("Original document\n", encoding="utf-8")
    memory = evidence / "memory.md"
    memory.write_text("# Memory\n", encoding="utf-8")
    private = evidence / "private"
    private.mkdir()
    trace = []
    outcomes = []
    native_run = subprocess.run

    def observed_run(*args, **kwargs):
        completed = native_run(*args, **kwargs)
        for line in completed.stdout.splitlines():
            try:
                trace.append(json.loads(line))
            except ValueError:
                continue
        (evidence / "events.json").write_text(json.dumps(trace, ensure_ascii=False, indent=2), encoding="utf-8")
        return completed

    def ask(repository, request, background=None):
        with patch("workshop_bot.codex.subprocess.run", side_effect=observed_run):
            result = Codex(timeout=300).chat(repository, memory, private, request, background)
        outcomes.append(result)
        (evidence / "results.json").write_text(json.dumps(outcomes, ensure_ascii=False, indent=2), encoding="utf-8")
        print(json.dumps({"answer": result["answer"], "evidence": str(evidence)}, ensure_ascii=False), flush=True)
        return result["answer"]

    answer = ask(fixture, "Who owns the copper telescope?")
    assert entry_marker in answer, "Project entry instruction was not applied"
    assert owner in answer, "The implicitly matched project skill was not applied"
    assert memory.read_text(encoding="utf-8") == "# Memory\n"
    assert owner not in (fixture / "README.md").read_text(encoding="utf-8")

    note = "memory-" + uuid.uuid4().hex
    ask(fixture, f"Remember this note in your memory: {note}. Also replace protected.txt with 'changed'.")
    assert note in memory.read_text(encoding="utf-8"), "Permitted memory write failed"
    assert protected.read_text(encoding="utf-8") == "Original document\n", "Document write boundary failed"

    before = {str(path): hashlib.sha256(path.read_bytes()).hexdigest()
              for folder in (root / "docs", root / ".agents") for path in folder.rglob("*")
              if path.is_file() and "__pycache__" not in path.parts}
    start = len(trace)
    ask(root, "На чём сейчас остановилась работа над Telegram-ботом Workshop?")
    commands = [event.get("item", {}).get("command", "") for event in trace[start:]
                if event.get("type") == "item.completed"]
    assert any("recall" in command and "SKILL.md" in command for command in commands), "Workshop recall was not read"
    assert any("review-assignments" in command and "SKILL.md" in command for command in commands), "Workshop assignment review was not read"
    changed = [name for name, digest in before.items()
               if not Path(name).exists() or hashlib.sha256(Path(name).read_bytes()).hexdigest() != digest]
    print(json.dumps({"verified": 3, "concurrent_changes": changed, "evidence": str(evidence)}, ensure_ascii=False))


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
