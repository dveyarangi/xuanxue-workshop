import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import threading
import uuid
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
    def __init__(self, executable="codex", timeout=180, *, tools_enabled=False):
        self.tools_enabled = tools_enabled
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

    @staticmethod
    def permissions(root, memory, private):
        settings = ['default_permissions="workshop"', 'approval_policy="never"',
                    'permissions.workshop.network.enabled=false', 'windows.sandbox="elevated"']
        entries = ['":root"="read"']
        home = Path.home()
        for path in (home / ".codex", home / ".ssh", home / ".aws"):
            entries.append(json.dumps(str(path)) + '="deny"')
        # Native project discovery also checks the global entry before the repository.
        for name in ("AGENTS.md", "AGENTS.override.md"):
            entries.append(json.dumps(str(home / ".codex" / name)) + '="read"')
        for path, access in ((root, "read"), (private, "deny"), (memory, "write")):
            entries.append(json.dumps(str(path)) + "=" + json.dumps(access))
        settings.append("permissions.workshop.filesystem={" + ",".join(entries) + "}")
        return [part for setting in settings for part in ("-c", setting)]

    def chat(self, root, memory, private, question, conversation, *, session_id=None, on_session=None,
             tool_context=None, on_event=None):
        if session_id is not None:
            session_id = str(uuid.UUID(session_id))
        root = Path(root).resolve()
        if not (root / "AGENTS.md").is_file() or not (root / ".agents/skills").is_dir():
            raise RuntimeError("Workshop harness requires AGENTS.md and .agents/skills")
        rules = Path(__file__).with_name("agent.rules.md").read_text(encoding="utf-8")
        if '<installed by="local">' not in rules:
            raise RuntimeError("Bot instructions are not installed")
        with tempfile.TemporaryDirectory(prefix="workshop-chat-") as temporary:
            output = Path(temporary) / "answer.txt"
            command = [self.executable, "exec", "--ignore-user-config", "--ignore-rules", "--strict-config",
                       "--skip-git-repo-check", "--cd", str(root),
                       "--json", "--output-last-message", str(output),
                       "-c", 'projects={' + json.dumps(str(root)) + '={trust_level="trusted"}}',
                       "-c", 'web_search="disabled"', "-c", "project_doc_max_bytes=65536",
                       "-c", "developer_instructions=" + json.dumps(rules, ensure_ascii=False)]
            command += self.permissions(root, memory, private)
            if tool_context:
                server = {"command": sys.executable, "args": ["-m", "workshop_bot.tools", str(tool_context)],
                          "cwd": str(Path(__file__).resolve().parents[1]), "tool_timeout_sec": 180,
                          "default_tools_approval_mode": "writes", "required": True}
                for key, value in server.items():
                    command += ["-c", f"mcp_servers.workshop.{key}=" + json.dumps(value)]
                for name in ("review_notice", "request_operator", "follow_up"):
                    command += ["-c", f'mcp_servers.workshop.tools.{name}.approval_mode="approve"']
            for feature in ("shell_tool", "code_mode", "code_mode_host"):
                command += ["--enable", feature]
            # Group authority cannot inherit the operator's connectors, hooks or other agents.
            for feature in ("apps", "plugins", "hooks", "browser_use", "browser_use_external",
                            "computer_use", "image_generation", "multi_agent", "multi_agent_v2",
                            "view_image"):
                command += ["--disable", feature]
            if session_id:
                command += ["resume", session_id]
            elif on_session is None:
                command.append("--ephemeral")
            command.append("-")
            prompt = (f"Workshop repository: {root}\nYour writable memory file: {memory}\n"
                      + ("Continue this conversation; refresh relevant records when needed. " if session_id else
                         "Start this conversation using the bot entry instructions. ") +
                      "Only the memory file is writable in this conversation. "
                      "Reply with ordinary text for Telegram.\n\n"
                      "Group conversation (background data):\n" +
                      json.dumps(conversation, ensure_ascii=False) + "\n\nCurrent request:\n" + question)
            allowed = {"PATH", "SYSTEMROOT", "WINDIR", "TEMP", "TMP", "USERPROFILE", "APPDATA",
                       "LOCALAPPDATA", "PROGRAMFILES", "PROGRAMFILES(X86)", "PROGRAMDATA",
                       "COMSPEC", "PATHEXT", "HOMEDRIVE", "HOMEPATH", "CODEX_HOME"}
            environment = {k: v for k, v in os.environ.items() if k.upper() in allowed}
            identity_seen = None

            def observe(event):
                nonlocal identity_seen
                if on_event:
                    on_event(event)
                if event.get("type") == "thread.started":
                    identity_seen = str(uuid.UUID(event["thread_id"]))
                    if session_id and identity_seen != session_id:
                        raise RuntimeError("Codex resumed a different session")
                    if on_session:
                        on_session(identity_seen)

            if on_session is not None or session_id is not None or on_event is not None:
                completed = self.run_stream(command, prompt, environment, root, observe)
            else:
                completed = subprocess.run(command, input=prompt, capture_output=True, encoding="utf-8",
                                           errors="replace", timeout=self.timeout, env=environment, cwd=root)
            events = []
            for line in completed.stdout.splitlines():
                try:
                    events.append(json.loads(line))
                except ValueError:
                    continue
            if completed.returncode or not any(e.get("type") == "turn.completed" for e in events):
                errors = [line for line in completed.stderr.splitlines() if line.lower().startswith("error:")]
                detail = errors[-1][:400] if errors else "turn did not complete"
                detail = re.sub(r"(?:sk-[\w-]+|\d{6,}:[\w-]{20,})", "[credential]", detail)
                raise RuntimeError(f"Codex exit {completed.returncode}: {detail}; memory may have changed")
            if (on_session is not None or session_id is not None) and not identity_seen:
                raise RuntimeError("Codex did not confirm its session identity; memory may have changed")
            answer = output.read_text(encoding="utf-8").strip()
            if not answer:
                raise RuntimeError("Codex returned an empty answer; memory may have changed")
            return {"status": "answered", "answer": answer,
                    "runtime": {"executable": self.executable,
                                "session_id": identity_seen,
                                "tool_operations": sum(e.get("type") == "item.completed" and
                                                       e.get("item", {}).get("type") in {"command_execution", "file_change"}
                                                       for e in events)}}

    def run_stream(self, command, prompt, environment, root, observe):
        # Save thread.started as it arrives rather than waiting for the final answer.
        with tempfile.TemporaryFile() as incoming, tempfile.TemporaryFile() as errors:
            incoming.write(prompt.encode("utf-8"))
            incoming.seek(0)
            process = subprocess.Popen(command, stdin=incoming, stdout=subprocess.PIPE, stderr=errors,
                                       encoding="utf-8", errors="replace", env=environment, cwd=root)
            expired = threading.Event()

            def stop():
                expired.set()
                process.kill()

            timer = threading.Timer(self.timeout, stop)
            timer.start()
            lines = []
            try:
                for line in process.stdout:
                    lines.append(line)
                    try:
                        event = json.loads(line)
                    except ValueError:
                        continue
                    observe(event)
                process.wait()
                if expired.is_set():
                    raise RuntimeError("Codex timed out; memory may have changed")
            finally:
                timer.cancel()
                if process.poll() is None:
                    process.kill()
                process.wait()
                process.stdout.close()
            errors.seek(0)
            return subprocess.CompletedProcess(command, process.returncode, "".join(lines),
                                               errors.read().decode("utf-8", errors="replace"))

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
