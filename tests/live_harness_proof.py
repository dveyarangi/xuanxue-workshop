"""Native proof of bot entry, skill discovery and continuation across worker processes."""

import json
import subprocess
import sys
import uuid
from datetime import datetime, timezone
from pathlib import Path

from workshop_bot.codex import Codex
from workshop_bot.service import Workshop


def worker():
    data = json.load(sys.stdin)
    agent = Codex(timeout=300)
    trace = []
    native = agent.run_stream

    def observed(command, prompt, environment, root, observe):
        def event(value):
            trace.append(value)
            observe(value)
        return native(command, prompt, environment, root, event)

    agent.run_stream = observed
    app = Workshop(data["root"], data["state"], agent)
    if data.get("memory"):
        app.memory = Path(data["memory"])
    result = app.ask(data["request_id"], data["request"], conversation=data["conversation"])
    Path(data["evidence"]).write_text(json.dumps({"result": result, "events": trace},
                                               ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False), flush=True)


def main():
    root = Path(__file__).resolve().parents[1]
    evidence = root / ".local" / datetime.now(timezone.utc).strftime("harness-proof-%Y%m%d-%H%M%S")
    fixture = evidence / "project"
    skill = fixture / ".agents/skills/copper-owner/SKILL.md"
    skill.parent.mkdir(parents=True)
    subprocess.run(["git", "init", "--quiet", str(fixture)], check=True)
    owner = "owner-" + uuid.uuid4().hex
    (fixture / "AGENTS.md").write_text(
        "Run /recall first in every conversation.\n"
        "A bot entry may override the operator lifecycle.\n", encoding="utf-8")
    skill.write_text(
        "---\nname: copper-owner\ndescription: Use when asked who owns the copper telescope.\n---\n\n"
        f"The copper telescope belongs to {owner}. State its owner exactly.\n", encoding="utf-8")
    (fixture / "README.md").write_text("# Observatory\n", encoding="utf-8")
    protected = fixture / "protected.txt"
    protected.write_text("Original document\n", encoding="utf-8")
    private = evidence / "private"
    private.mkdir()
    memory = fixture / ".local/workshop-bot-memory.md"
    memory.parent.mkdir()
    memory.write_text("# Memory\n", encoding="utf-8")

    def ask(number, request, conversation=10, repository=fixture):
        data = {"root": str(repository), "state": str(private / "history.sqlite3"),
                "memory": str(memory), "evidence": str(private / f"turn-{number}.json"),
                "request_id": str(number), "request": request,
                "conversation": {"chat_id": -100, "messages": [],
                                 "current": {"conversation_id": conversation}}}
        completed = subprocess.run([sys.executable, "-m", "tests.live_harness_proof", "--worker"],
                                   input=json.dumps(data), capture_output=True, encoding="utf-8",
                                   errors="replace", timeout=330, cwd=root)
        if completed.returncode:
            raise RuntimeError(completed.stderr)
        result = json.loads(completed.stdout)
        print(json.dumps({"turn": number, "result": result, "evidence": str(evidence)},
                         ensure_ascii=False), flush=True)
        assert result["status"] == "answered", result
        events = json.loads(Path(data["evidence"]).read_text(encoding="utf-8"))["events"]
        return result

    token = "conversation-" + uuid.uuid4().hex
    first = ask(1, f"Who owns the copper telescope? Keep {token} only in this conversation, not in a file.")
    assert owner in first["answer"], "Implicit skill selection failed"
    assert token not in memory.read_text(encoding="utf-8")
    second = ask(2, "What exact conversation token did I give you earlier? Also remember 'Meeting on Thursday' "
                 "in your memory file and replace protected.txt with 'changed'.")
    assert token in second["answer"], "Context did not survive worker restart"
    assert first["runtime"]["session_id"] == second["runtime"]["session_id"]
    assert memory.read_text(encoding="utf-8") != "# Memory\n", "Memory write failed on resume"
    assert protected.read_text(encoding="utf-8") == "Original document\n", "Write boundary failed on resume"
    third = ask(3, "What exact conversation token did I give you earlier?", conversation=20)
    assert token not in third["answer"], "Independent conversation leaked context"
    assert first["runtime"]["session_id"] != third["runtime"]["session_id"]
    ask(4, "Кто отвечает за Cabinet и Knowledge в Telegram?", conversation=30, repository=root)
    print(json.dumps({"verified": 4, "evidence": str(evidence)}), flush=True)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    worker() if "--worker" in sys.argv else main()
