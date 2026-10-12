import json
import os
import re
import shutil
import subprocess
import tempfile
from pathlib import Path


SCHEMA = {
    "type": "object", "additionalProperties": False,
    "required": ["disposition", "answer", "reason", "sources", "edit"],
    "properties": {
        "disposition": {"type": "string", "enum": ["answer", "change", "clarify", "refuse"]},
        "answer": {"type": "string"}, "reason": {"type": "string"},
        "sources": {"type": "array", "items": {"type": "string"}},
        "edit": {"anyOf": [{"type": "null"}, {"type": "object", "additionalProperties": False,
                   "required": ["path", "before", "after"],
                   "properties": {k: {"type": "string"} for k in ("path", "before", "after")}}]},
    },
}


class Codex:
    def __init__(self, executable="codex", timeout=180):
        if os.name == "nt" and executable == "codex":
            native = shutil.which("codex.exe")
            candidates = list((Path(os.environ.get("LOCALAPPDATA", "")) / "OpenAI/Codex/bin").glob("*/codex.exe"))
            if native:
                executable = native
            elif candidates:
                executable = str(max(candidates, key=lambda path: path.stat().st_mtime))
            else:
                executable = "codex.exe"
        self.executable = shutil.which(executable) or executable
        if os.name == "nt" and Path(self.executable).suffix.lower() != ".exe":
            raise ValueError("A native codex.exe is required; shell wrappers are not supported")
        self.timeout = timeout

    def __call__(self, context):
        rules = Path(__file__).with_name("agent.rules.md").read_text(encoding="utf-8")
        if '<installed by="local">' not in rules:
            raise RuntimeError("Local decision instructions are not installed")
        with tempfile.TemporaryDirectory(prefix="workshop-codex-") as temporary:
            directory = Path(temporary)
            schema = directory / "response.schema.json"
            output = directory / "response.json"
            schema.write_text(json.dumps(SCHEMA), encoding="utf-8")
            command = [self.executable, "exec", "--ignore-user-config", "--strict-config",
                       "--ephemeral", "--skip-git-repo-check", "--sandbox", "read-only",
                       "--cd", str(directory), "--json", "--output-schema", str(schema),
                       "--output-last-message", str(output), "-c", 'approval_policy="never"',
                       "-c", 'web_search="disabled"',
                       "-c", "developer_instructions=" + json.dumps(rules, ensure_ascii=False)]
            # The worker only makes a decision; capabilities belong to the caller.
            for feature in ("shell_tool", "apps", "plugins", "hooks", "browser_use", "browser_use_external",
                            "computer_use", "image_generation", "multi_agent", "multi_agent_v2",
                            "code_mode", "code_mode_host", "skill_search", "view_image"):
                command += ["--disable", feature]
            command.append("-")
            allowed = {"PATH", "SYSTEMROOT", "WINDIR", "TEMP", "TMP", "USERPROFILE", "APPDATA",
                       "LOCALAPPDATA", "PROGRAMFILES", "PROGRAMFILES(X86)", "PROGRAMDATA",
                       "COMSPEC", "PATHEXT", "HOMEDRIVE", "HOMEPATH", "CODEX_HOME"}
            environment = {k: v for k, v in os.environ.items() if k.upper() in allowed}
            completed = subprocess.run(command, input=json.dumps(context, ensure_ascii=False),
                                       capture_output=True, encoding="utf-8", errors="replace",
                                       timeout=self.timeout, env=environment, cwd=directory)
            if completed.returncode:
                errors = [line for line in completed.stderr.splitlines() if line.lower().startswith("error:")]
                for line in completed.stdout.splitlines():
                    try:
                        event = json.loads(line)
                    except ValueError:
                        continue
                    if event.get("type") == "error" and isinstance(event.get("message"), str):
                        errors.append(event["message"])
                    if event.get("type") == "turn.failed" and isinstance(event.get("error"), dict):
                        errors.append(str(event["error"].get("message", "Turn failed")))
                detail = errors[-1][:400] if errors else "no final response"
                detail = re.sub(r"(?:sk-[\w-]+|\d{6,}:[\w-]{20,})", "[credential]", detail)
                raise RuntimeError(f"Codex exit {completed.returncode}: {detail}")
            events = [json.loads(line) for line in completed.stdout.splitlines() if line.strip()]
            if not any(event.get("type") == "turn.completed" for event in events):
                raise RuntimeError("Codex did not complete its turn")
            for event in events:
                item = event.get("item", {})
                if item.get("type") == "error" and item.get("message", "").startswith(
                        "Code Mode is unavailable because code-mode host is disabled."):
                    continue
                if item and item.get("type") not in {"agent_message", "reasoning"}:
                    raise RuntimeError("Decision worker attempted a tool operation")
            decision = json.loads(output.read_text(encoding="utf-8"))
            decision["runtime"] = {"executable": self.executable, "tool_operations": 0,
                                   "usage": next(e.get("usage") for e in events if e.get("type") == "turn.completed")}
            return decision
