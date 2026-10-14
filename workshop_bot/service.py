import hashlib
import importlib.util
import json
import os
import re
import shutil
import sqlite3
import subprocess
import sys
import tempfile
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath
from .records import exclusive_record


def redact(value):
    if isinstance(value, str):
        return re.sub(r"(?:sk-[A-Za-z0-9_-]{16,}|\d{6,}:[A-Za-z0-9_-]{20,})", "[credential]", value)
    if isinstance(value, dict):
        return {key: redact(item) for key, item in value.items()}
    if isinstance(value, list):
        return [redact(item) for item in value]
    return value


class Workshop:
    def __init__(self, root, state, agent):
        self.root = Path(root).resolve()
        self.state = Path(state).resolve()
        self.agent = agent
        self.state.parent.mkdir(parents=True, exist_ok=True)
        self.memory = self.path(".local/workshop-bot-memory.md")
        self.memory.parent.mkdir(parents=True, exist_ok=True)
        if not self.memory.exists():
            self.memory.write_text("# Память Workshop Spirit\n", encoding="utf-8")
        with self.connect() as db:
            db.execute("CREATE TABLE IF NOT EXISTS requests "
                       "(id TEXT PRIMARY KEY, sender TEXT, created TEXT, question TEXT, target TEXT, result TEXT)")

    @contextmanager
    def connect(self):
        db = sqlite3.connect(self.state)
        db.row_factory = sqlite3.Row
        try:
            with db:
                yield db
        finally:
            db.close()

    def ask(self, request_id, question, *, sender="operator", target=None, conversation=None):
        request_id, question, sender, target = (redact(value) for value in (request_id, question, sender, target))
        with self.connect() as db:
            added = db.execute("INSERT OR IGNORE INTO requests VALUES (?, ?, ?, ?, ?, NULL)",
                               (request_id, sender, datetime.now(timezone.utc).isoformat(), question, target)).rowcount
            previous = db.execute("SELECT * FROM requests WHERE id=?", (request_id,)).fetchone()
        if not added:
            if previous["question"] != question or previous["sender"] != sender or previous["target"] != target:
                raise ValueError("Request identifier already belongs to another request")
            result = json.loads(previous["result"]) if previous["result"] else {
                "status": "uncertain", "answer": "Предыдущая обработка прервалась; нужна проверка."}
            if result["status"] == "applying":
                result = self.recover(result)
                self.save(request_id, result)
            return result
        try:
            if target is None and hasattr(self.agent, "chat"):
                result = self.agent.chat(self.root, self.memory, self.state.parent,
                                         question, redact(conversation))
                result = redact(result)
                self.save(request_id, result)
                return result
            context = self.context(question, target)
            if conversation is not None:
                context["conversation"] = redact(conversation)
            if len(json.dumps(context, ensure_ascii=False).encode("utf-8")) > 750_000:
                raise ValueError("Source and conversation context exceed the supported size")
            decision = self.agent(redact(context))
            disposition = decision["disposition"]
            if disposition not in {"answer", "change", "clarify", "refuse"}:
                raise ValueError("Invalid decision")
            if (disposition == "change") != (decision["edit"] is not None):
                raise ValueError("Decision and edit disagree")
            if not decision["answer"].strip():
                raise ValueError("Codex returned an empty answer")
            unknown_sources = [p for p in decision["sources"] if p not in context["documents"]]
            if unknown_sources:
                raise ValueError("Sources not supplied to Codex: " + ", ".join(unknown_sources))
            result = {"status": {"answer": "answered", "change": "applying", "clarify": "clarification",
                                 "refuse": "refused"}[disposition], "answer": decision["answer"],
                      "reason": decision["reason"], "sources": decision["sources"],
                      "source_versions": context["versions"]}
            if "runtime" in decision:
                result["runtime"] = decision["runtime"]
            if disposition == "change":
                result = self.apply(request_id, context, decision, result)
        except Exception as error:
            with self.connect() as db:
                saved = db.execute("SELECT result FROM requests WHERE id=?", (request_id,)).fetchone()[0]
            prepared = json.loads(saved) if saved else None
            result = {**prepared, "status": "uncertain",
                      "answer": "Запись прервалась; результат правки требует проверки."} if prepared and prepared["status"] == "applying" else {
                          "status": "failed", "answer": "Не удалось подготовить ответ. Попробуйте задать вопрос ещё раз."}
            result["error"] = type(error).__name__
            if target is None and hasattr(self.agent, "chat"):
                result.update(status="uncertain", answer="Не удалось завершить ответ. Если запрос менял память, её содержимое нужно проверить.")
            if isinstance(error, (ValueError, RuntimeError)):
                result["detail"] = str(error)
        result = redact(result)
        self.save(request_id, result)
        return result

    def save(self, request_id, result):
        with self.connect() as db:
            db.execute("UPDATE requests SET result=? WHERE id=?",
                       (json.dumps(result, ensure_ascii=False), request_id))

    def apply(self, request_id, context, decision, result):
        edit = decision["edit"]
        name = edit["path"]
        if name != context["target"] or not re.fullmatch(r"docs/tickets/\d{2}-[\d.]+-[a-z0-9-]+\.md", name):
            raise ValueError("Only the selected live ticket can change")
        path = self.path(name)
        original = path.read_bytes()
        text = original.decode("utf-8")
        if not edit["before"] or text.count(edit["before"]) != 1:
            raise ValueError("Replacement must identify one exact passage")
        after = text.replace(edit["before"], edit["after"], 1)
        self.validate_ticket(name, text, after)
        if os.name != "nt":
            raise OSError("Exclusive Windows write proof is required on this host")
        with exclusive_record(path) as record:
            if os.fstat(record.fileno()).st_nlink != 1:
                raise ValueError("Hard-linked records are not writable")
            before = record.read()
            changed = before != original or hashlib.sha256(before).hexdigest() != context["versions"][name]
            changed |= any(hashlib.sha256(self.path(p).read_bytes()).hexdigest() != version
                           for p, version in context["versions"].items() if p != name)
            if changed:
                return {**result, "status": "conflict", "answer": "Запись уже изменена. Правка не применена."}
            result["change"] = {"path": name, "before": text, "after": after}
            self.save(request_id, result)
            record.seek(0)
            record.write(after.encode("utf-8"))
            record.truncate()
            record.flush()
            os.fsync(record.fileno())
            return {**result, "status": "applied", "answer": "Задача обновлена.\n" + decision["reason"]}

    def recover(self, result):
        change = result["change"]
        try:
            actual = self.path(change["path"]).read_bytes()
            if actual == change["after"].encode("utf-8"):
                return {**result, "status": "applied", "answer": "Изменение сохранено; повторно не применялось."}
            if actual == change["before"].encode("utf-8"):
                return {**result, "status": "not_applied", "answer": "Правка не была применена."}
        except OSError:
            pass
        return {**result, "status": "uncertain", "answer": "Результат правки требует проверки; повтор не выполнен."}

    def validate_ticket(self, name, before, after):
        if redact(before) != before or redact(after) != after:
            raise ValueError("A credential-bearing record cannot enter the change journal")
        # TODO q-0002.0012: add evidence-aware structural and completion operations.
        protected = lambda text: [line.strip() for line in text.splitlines()
                                  if line.strip().startswith(("#", "- **", "- ["))]
        header = lambda text: re.split(r"(?m)^## ", text, maxsplit=1)[0]
        if protected(before) != protected(after) or header(before) != header(after):
            raise ValueError("Structural and completion changes require their dedicated operation")
        script = self.root / ".agents/scripts/gw/tickets.py"
        if not script.exists():
            raise ValueError("The Workshop ticket validator is required")
        spec = importlib.util.spec_from_file_location("workshop_ticket_validator", script)
        module = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = module
        spec.loader.exec_module(module)
        with tempfile.TemporaryDirectory(prefix="workshop-check-") as temporary:
            preview = Path(temporary)
            shutil.copytree(self.root / "docs", preview / "docs", symlinks=True)
            subprocess.run(["git", "init", "--quiet", str(preview)], check=True, capture_output=True)
            baseline = {(d.record, d.problem) for d in module.check(preview).diagnostics}
            (preview / name).write_bytes(after.encode("utf-8"))
            checked = module.check(preview)
            if checked.skipped or {(d.record, d.problem) for d in checked.diagnostics} - baseline:
                raise ValueError("Ticket validation rejected the change")

    def context(self, question, target):
        if target is not None and not re.fullmatch(r"docs/tickets/\d{2}-[\d.]+-[a-z0-9-]+\.md", target):
            raise ValueError("Only a live ticket can be selected")
        names = ["AGENTS.md", "local.rules.md", "README.md", "PRODUCT.md",
                 "docs/architecture.md", "docs/agent-contract.md", "docs/boundaries.md",
                 "docs/contracts/telegram-workshop.md"]
        if target:
            names.append(target)
        documents = {}
        versions = {}
        for name in dict.fromkeys(names):
            path = self.path(name)
            if not path.is_file():
                if name == target:
                    raise ValueError("Requested record does not exist")
                continue
            data = path.read_bytes()
            if len(data) > 250_000 or sum(len(v) for v in documents.values()) + len(data) > 500_000:
                raise ValueError("Source context exceeds the supported size")
            documents[name] = data.decode("utf-8-sig")
            versions[name] = hashlib.sha256(data).hexdigest()
        instruction_paths = [".agents/skills/recall/SKILL.md", ".agents/skills/ticket/SKILL.md",
                             ".agents/skills/questions/SKILL.md", ".agents/skills/ticket/TICKET-FORMAT.md"]
        instructions = {p: self.path(p).read_text(encoding="utf-8-sig")
                        for p in instruction_paths if self.path(p).is_file()}
        for source in sorted((self.root / "docs/questions").glob("q-*.md")):
            name = source.relative_to(self.root).as_posix()
            data = self.path(name).read_bytes()
            documents[name] = data.decode("utf-8-sig")
            versions[name] = hashlib.sha256(data).hexdigest()
        for name in instructions:
            versions[name] = hashlib.sha256(self.path(name).read_bytes()).hexdigest()
        context = {"question": question, "target": target, "documents": documents, "versions": versions,
                   "instructions": instructions, "memory": self.memory.read_text(encoding="utf-8"),
                   "evidence_scope": "Selected local documents and question records in docs/questions only; "
                   "no live GitHub reads, complete question-store window or store operations in this stage."}
        if len(json.dumps(context, ensure_ascii=False).encode("utf-8")) > 750_000:
            raise ValueError("Source context exceeds the supported size")
        return context

    def path(self, name):
        if not isinstance(name, str) or "\\" in name or ":" in name:
            raise ValueError("Expected a repository-relative path")
        relative = PurePosixPath(name)
        if relative.is_absolute() or ".." in relative.parts:
            raise ValueError("Path leaves the repository")
        path = self.root
        for part in relative.parts:
            path = path / part
            if path.is_symlink() or path.is_junction():
                raise ValueError("Linked paths are not accepted")
        if not path.resolve().is_relative_to(self.root):
            raise ValueError("Path leaves the repository")
        return path

    def history(self):
        with self.connect() as db:
            return [{**dict(row), "result": json.loads(row["result"]) if row["result"] else None}
                    for row in db.execute("SELECT * FROM requests ORDER BY rowid")]
