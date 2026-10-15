"""A bounded conversation pass with no tools or mutation authority."""

import hashlib
import json
import os
import subprocess
import tempfile
import time
from pathlib import Path


SCHEMA = {"type": "object", "additionalProperties": False,
          "required": ["route", "answer", "reason"], "properties": {
              "route": {"type": "string", "enum": ["answer", "work", "offer", "ignore"]},
              "answer": {"type": "string"}, "reason": {"type": "string"}}}


def decide(executable, root, memory, question, conversation):
    root = Path(root)
    rules = Path(__file__).with_name("quick.rules.md").read_text(encoding="utf-8")
    if '<installed by="local">' not in rules:
        raise RuntimeError("Quick conversation instructions are not installed")
    sources, inventory = {}, []
    for label, path, limit in (("product", root / "PRODUCT.md", 3500),
                                ("memory", Path(memory), 4000),
                                ("operator_requests", root / "docs/requests/telegram.md", 6000)):
        if not path.is_file():
            continue
        body = path.read_text(encoding="utf-8")
        sources[label] = {"text": body[:limit], "truncated": len(body) > limit}
        inventory.append({"path": str(path.relative_to(root)), "supplied_characters": min(len(body), limit),
                          "sha256": hashlib.sha256(body.encode()).hexdigest()})
    current = {"addressing": "direct", **conversation.get("current", {})}
    anchors = {current.get("reply_to"), current.get("conversation_id"),
               conversation.get("addressed_message", {}).get("message_id")}
    messages = conversation.get("messages", [])
    priority = [m for m in messages if m.get("message_id") in anchors]
    recent = [m for m in reversed(messages) if m.get("message_id") not in anchors and
              m.get("thread_id") == current.get("thread_id")][:16]
    selected, size = [], 0
    for message in priority + recent:
        length = len(json.dumps(message, ensure_ascii=False).encode())
        if size + length <= 16000:
            selected.append(message)
            size += length
    selected.sort(key=lambda m: m.get("message_id", 0))
    board = conversation.get("board", {})
    board_summary = {key: board.get(key) for key in ("monitor_available", "checked_at", "source", "error")}
    board_summary["cases"] = [{key: case.get(key) for key in
                                ("number", "title", "new_to_conversation", "review_current")}
                               for case in board.get("cases", [])]
    data = {"question": question, "current": current, "messages": selected,
            "omitted_messages": len(messages) - len(selected) + conversation.get("omitted_messages", 0),
            "addressed_message": conversation.get("addressed_message"),
            "sources": sources, "board": board_summary}
    prompt = json.dumps(data, ensure_ascii=False)
    if len(prompt.encode()) > 65000:
        raise ValueError("Quick context exceeds its budget")
    started = time.monotonic()
    with tempfile.TemporaryDirectory(prefix="workshop-quick-") as temporary:
        schema, output = Path(temporary) / "schema.json", Path(temporary) / "answer.json"
        schema.write_text(json.dumps(SCHEMA), encoding="utf-8")
        command = [executable, "exec", "--ignore-user-config", "--ignore-rules", "--strict-config",
                   "--skip-git-repo-check", "--cd", temporary, "--ephemeral", "--json",
                   "--model", "gpt-6-luna", "-c", 'model_reasoning_effort="low"',
                   "-c", "project_doc_max_bytes=0", "-c", 'web_search="disabled"',
                   "-c", "developer_instructions=" + json.dumps(rules, ensure_ascii=False),
                   "--sandbox", "read-only", "-c", 'approval_policy="never"',
                   "--output-schema", str(schema), "--output-last-message", str(output)]
        for feature in ("shell_tool", "code_mode", "code_mode_host", "apps", "plugins", "hooks", "browser_use",
                        "browser_use_external", "computer_use", "image_generation", "multi_agent",
                        "multi_agent_v2", "view_image"):
            command += ["--disable", feature]
        allowed = {"PATH", "SYSTEMROOT", "WINDIR", "TEMP", "TMP", "USERPROFILE", "APPDATA",
                   "LOCALAPPDATA", "PROGRAMFILES", "PROGRAMFILES(X86)", "PROGRAMDATA",
                   "COMSPEC", "PATHEXT", "HOMEDRIVE", "HOMEPATH", "CODEX_HOME"}
        completed = subprocess.run(command + ["-"], input=prompt, capture_output=True, encoding="utf-8",
                                   errors="replace", timeout=25, cwd=temporary,
                                   env={k: v for k, v in os.environ.items() if k.upper() in allowed})
        events = []
        for line in completed.stdout.splitlines():
            try:
                events.append(json.loads(line))
            except ValueError:
                pass
        turns = [e for e in events if e.get("type") == "turn.completed"]
        if any(e.get("type") == "item.completed" and e.get("item", {}).get("type") not in
               {"agent_message", "reasoning", "error"} for e in events):
            raise RuntimeError("Quick conversation unexpectedly used a tool")
        if completed.returncode or not turns or not output.is_file():
            raise RuntimeError("Quick conversation did not complete")
        decision = json.loads(output.read_text(encoding="utf-8"))
    if set(decision) != {"route", "answer", "reason"} or not all(isinstance(v, str) for v in decision.values()):
        raise ValueError("Invalid quick decision")
    if decision["route"] not in SCHEMA["properties"]["route"]["enum"] or len(decision["answer"]) > 2000:
        raise ValueError("Invalid quick route or answer length")
    if decision["route"] == "offer" and len(decision["answer"]) > 320:
        raise ValueError("Offer exceeds one short message")
    decision["runtime"] = {"model": "gpt-6-luna", "effort": "low",
                           "seconds": round(time.monotonic() - started, 3),
                           "usage": turns[-1].get("usage"), "sources": inventory,
                           "prompt_bytes": len(prompt.encode()), "history_messages": len(selected)}
    return decision
