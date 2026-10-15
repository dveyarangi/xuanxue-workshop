"""Scoped host capabilities for the Telegram worker; stdio MCP transport."""

import base64
import hashlib
import importlib.util
import ipaddress
import json
import os
import re
import socket
import sqlite3
import subprocess
import sys
import time
from contextlib import closing, contextmanager
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError
from urllib.parse import urlparse
from urllib.request import HTTPRedirectHandler, Request, build_opener

from .records import exclusive_record
from .service import redact


class TurnTools:
    def __init__(self, context):
        self.context = context
        self.root = Path(context["root"])
        self.state = Path(context["state"])
        self.request_id = context["request_id"]
        self.board_state = self.root / ".local/board-review/history.sqlite3"
        spec = importlib.util.spec_from_file_location("workshop_board", Path(__file__).resolve().parents[1] /
                                                     ".agents/scripts/gw/board.py")
        self.board = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.board)
        with self.connect() as db:
            db.executescript("""
                CREATE TABLE IF NOT EXISTS bot_tool_events
                    (request_id TEXT, name TEXT, value TEXT, PRIMARY KEY(request_id,name));
                CREATE TABLE IF NOT EXISTS bot_board_reads
                    (request_id TEXT, number INTEGER, version TEXT, monitor_version TEXT, PRIMARY KEY(request_id,number));
                CREATE TABLE IF NOT EXISTS bot_board_seen
                    (conversation TEXT, number INTEGER, version TEXT, monitor_version TEXT, PRIMARY KEY(conversation,number));
            """)

    @contextmanager
    def connect(self):
        with closing(sqlite3.connect(self.state, timeout=10)) as db:
            with db:
                yield db

    def repo(self):
        value = subprocess.run(["git", "remote", "get-url", "origin"], cwd=self.root,
                               capture_output=True, text=True, check=True).stdout.strip()
        match = re.fullmatch(r"(?:https://github.com/|git@github.com:)([\w.-]+/[\w.-]+?)(?:\.git)?", value)
        if not match:
            raise ValueError("Workshop GitHub origin is not configured")
        return match[1]

    def identity(self):
        if self.board_state.is_file():
            with closing(sqlite3.connect(self.board_state.as_uri() + "?mode=ro", uri=True)) as db:
                return json.loads(db.execute("SELECT value FROM meta WHERE name='identity'").fetchone()[0])
        return {"repo": self.repo(), "labels": ["project:cabinet", "project:daychi", "project:knowledge", "project:workshop"]}

    def local_board(self):
        value = object.__new__(self.board.Board)
        value.state = self.board_state
        return value

    def rows(self):
        if not self.board_state.is_file():
            return []
        with closing(sqlite3.connect(self.board_state.as_uri() + "?mode=ro", uri=True)) as db:
            db.row_factory = sqlite3.Row
            return [dict(row) for row in db.execute("SELECT * FROM cases ORDER BY number")]

    def board_updates(self):
        rows = self.rows()
        # Use the board script's status interface without taking a reviewer lease.
        status = self.local_board().status() if self.board_state.is_file() else None
        with self.connect() as db:
            seen = dict(db.execute("SELECT number,monitor_version FROM bot_board_seen WHERE conversation=?",
                                   (self.context["conversation"],)))
        cases = []
        for row in rows:
            issue = json.loads(row["snapshot"])["issue"]
            cases.append({"number": row["number"], "title": issue["title"], "url": issue["html_url"],
                          "version": row["observed"], "review_version": self.review_version(row),
                          "new_to_conversation": seen.get(row["number"]) != self.review_version(row),
                          "review_current": row["reviewed"] == row["observed"] and
                              not (row["due"] and row["due"] <= time.time()),
                          "review_note": row["note"], "busy": bool(row["token"] and row["expires"] > time.time())})
        report = self.root / "docs/board-review.md"
        text = report.read_text(encoding="utf-8") if report.is_file() else None
        return {"checked_at": datetime.now(timezone.utc).isoformat(), "monitor_available": bool(rows),
                "source": "retained monitor output; not a new GitHub scan", "cases": cases,
                "review_report": text[:40000] if text else None,
                "report_truncated": bool(text and len(text) > 40000),
                "publication_status": status["publications"] if status else []}

    def review_version(self, row):
        return self.board.digest([row["observed"], row["reviewed"], row["outcome"], row["note"]])

    def tracker(self):
        identity = self.identity()
        return self.board.GitHub(identity["repo"], identity["labels"])

    def scan_board(self):
        result = self.board.Board(self.board_state, self.tracker()).scan()
        return {"scan": result, "board": self.board_updates()}

    def read_issue(self, number, section="issue", offset=0, fresh=False):
        if type(number) is not int or number <= 0 or section not in {"issue", "comments", "timeline", "evidence"}:
            raise ValueError("Select an issue number and a supported section")
        if type(offset) is not int or offset < 0:
            raise ValueError("Offset must be nonnegative")
        row = next((r for r in self.rows() if r["number"] == number), None)
        snapshot = self.tracker().snapshot(number) if fresh or row is None else json.loads(row["snapshot"])
        version = self.local_board().fingerprint(snapshot) if self.board_state.is_file() else self.board.digest(snapshot)
        with self.connect() as db:
            db.execute("INSERT OR REPLACE INTO bot_board_reads VALUES (?,?,?,?)",
                       (self.request_id, number, version, self.review_version(row) if row else None))
        text = json.dumps(redact(snapshot[section]), ensure_ascii=False, indent=2)
        return {"number": number, "version": version, "source": "GitHub" if fresh or row is None else "monitor",
                "section": section, "text": text[offset:offset + 24000],
                "next_offset": offset + 24000 if len(text) > offset + 24000 else None}

    def review_notice(self, numbers, text):
        if not isinstance(text, str) or not 1 <= len(text.strip()) <= 320 or redact(text) != text:
            raise ValueError("Supply a brief notice without credentials (1–320 characters)")
        text = text.strip()
        cases = self.board_updates()["cases"]
        new = {case["number"] for case in cases if case["new_to_conversation"]}
        if not numbers or any(type(number) is not int for number in numbers):
            raise ValueError("Name the relevant issue numbers")
        with self.connect() as db:
            reads = dict(db.execute("SELECT number,version FROM bot_board_reads WHERE request_id=?", (self.request_id,)))
            seen = dict(db.execute("SELECT number,version FROM bot_board_seen WHERE conversation=?",
                                   (self.context["conversation"],)))
            new.update(number for number, version in reads.items() if seen.get(number) != version)
            if not new.intersection(numbers):
                return {"status": "unchanged"}
            for case in cases:
                if case["number"] in numbers:
                    db.execute("INSERT OR IGNORE INTO bot_board_reads VALUES (?,?,?,?)",
                               (self.request_id, case["number"], case["version"], case["review_version"]))
            db.execute("INSERT OR IGNORE INTO bot_tool_events VALUES (?, 'notice', ?)",
                       (self.request_id, json.dumps(text, ensure_ascii=False)))
        return {"status": "queued"}

    def notice(self):
        with self.connect() as db:
            row = db.execute("SELECT value FROM bot_tool_events WHERE request_id=? AND name='notice'",
                             (self.request_id,)).fetchone()
        return json.loads(row[0]) if row else None

    def finish(self):
        with self.connect() as db:
            db.execute("INSERT OR REPLACE INTO bot_board_seen SELECT ?,number,version,monitor_version FROM bot_board_reads WHERE request_id=?",
                       (self.context["conversation"], self.request_id))

    def request_operator(self, title, detail, kind="mechanism"):
        if kind not in {"mechanism", "access", "agreement"} or not title.strip() or not detail.strip():
            raise ValueError("A request needs a kind, title and concrete outcome")
        if (len(title) > 200 or len(detail) > 12000 or redact(title + detail) != title + detail
                or "<!-- telegram-request:" in title + detail):
            raise ValueError("Request is too large or contains a credential")
        identifier = hashlib.sha256((self.request_id + kind + title).encode()).hexdigest()[:24]
        marker = f"<!-- telegram-request:{identifier} -->"
        content_marker = "<!-- content:" + hashlib.sha256((title + detail).encode()).hexdigest() + " -->"
        path = self.root / "docs/requests/telegram.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        if not path.exists():
            try:
                with path.open("x", encoding="utf-8") as record:
                    record.write("# Requests from Telegram\n\n")
            except FileExistsError:
                pass
        if path.resolve() != path.absolute() or path.is_symlink():
            raise ValueError("Request log cannot be redirected")
        source = self.context.get("source", {})
        sender = source.get("sender", "unknown")
        if isinstance(sender, dict):
            sender = " ".join(str(sender[key]) for key in ("first_name", "last_name", "username", "id") if key in sender)
        entry = (f"\n{marker}\n## {title.replace(chr(10), ' ')}\n\n"
                 f"- Status: pending\n- Kind: {kind}\n- Date: {datetime.now(timezone.utc).isoformat()}\n"
                 f"- Author: {sender}\n- Message: {source.get('message_url') or source.get('message_id')}\n"
                 f"{content_marker}\n\n" + "\n".join("> " + line for line in detail.splitlines()) + "\n")
        with exclusive_record(path) as record:
            if os.fstat(record.fileno()).st_nlink != 1:
                raise ValueError("Request log cannot be hard-linked")
            existing = record.read().decode("utf-8")
            if marker in existing and content_marker not in existing.split(marker, 1)[1].split("<!-- telegram-request:", 1)[0]:
                raise ValueError("This request already recorded different content; retained for operator review")
            if marker not in existing:
                record.seek(0, 2)
                record.write(entry.encode("utf-8"))
                record.flush()
                os.fsync(record.fileno())
        return {"status": "recorded", "request": identifier, "approval": "pending operator wake"}

    def published_link(self, path):
        name = Path(path)
        if name.is_absolute() or ".." in name.parts or name.suffix != ".md" or name.parts[0] not in {"docs", "README.md", "PRODUCT.md"}:
            raise ValueError("Select a Workshop documentation file")
        repo = self.repo()
        ref = subprocess.run(["git", "rev-parse", "origin/master"], cwd=self.root,
                             capture_output=True, text=True, check=True).stdout.strip()
        value = self.board.Gh()("GET", f"repos/{repo}/contents/{name.as_posix()}?ref={ref}")
        published = base64.b64decode(value.get("content", "")).replace(b"\r\n", b"\n")
        if published != (self.root / name).read_bytes().replace(b"\r\n", b"\n"):
            return {"url": None, "reason": "Local content differs from the published file; omit the reference"}
        return {"url": value["html_url"]}

    def check_site(self, url):
        parsed = urlparse(url)
        homes = ("README.md", "docs/current-system.md", "docs/boundaries.md")
        known = "\n".join((self.root / name).read_text(encoding="utf-8") for name in homes
                          if (self.root / name).is_file())
        hosts = {urlparse(value.rstrip(".,;)" )).hostname for value in re.findall(r"https://[^\s<>\]\"'`]+", known)}
        hosts.update(re.findall(r"`([a-z0-9][a-z0-9.-]*\.[a-z]{2,})`", known, re.IGNORECASE))
        if parsed.scheme != "https" or parsed.hostname not in hosts or parsed.username or parsed.password or parsed.query or parsed.port not in {None, 443}:
            raise ValueError("Use a documented public HTTPS endpoint without credentials or query parameters")
        try:
            addresses = socket.getaddrinfo(parsed.hostname, 443, type=socket.SOCK_STREAM)
        except socket.gaierror:
            return {"url": url, "reachable": False, "error": "DNS resolution failed", "authenticated": False}
        if not addresses or any(not ipaddress.ip_address(item[4][0]).is_global for item in addresses):
            raise ValueError("Endpoint does not resolve to public addresses")

        class NoRedirect(HTTPRedirectHandler):
            def redirect_request(self, *args, **kwargs):
                return None

        try:
            response = build_opener(NoRedirect).open(Request(url, method="GET"), timeout=20)
        except HTTPError as error:
            response = error
        with response:
            return {"url": url, "status": response.code, "location": response.headers.get("Location"),
                    "body": redact(response.read(32000).decode("utf-8", errors="replace")),
                    "authenticated": False}

    def follow_up(self, number, version, body):
        if type(number) is not int or not body.strip() or redact(body) != body:
            raise ValueError("A follow-up needs an issue and credential-free text")
        with self.connect() as db:
            studied = db.execute("SELECT version FROM bot_board_reads WHERE request_id=? AND number=?",
                                 (self.request_id, number)).fetchone()
        if not studied or studied[0] != version:
            raise ValueError("Read the current issue before adding work")
        review = self.board.Board(self.board_state, self.tracker())
        identifier = "telegram-" + hashlib.sha256(f"{self.request_id}:{number}".encode()).hexdigest()[:40]
        try:
            existing = review.publication(identifier)
        except ValueError:
            existing = None
        if existing:
            if existing["body"].split("\n", 1)[1] != body:
                raise ValueError("This request already prepared a different follow-up")
        else:
            claim = review.claim(number)
            try:
                if claim["fingerprint"] != version:
                    raise ValueError("Issue changed; read and reassess the current evidence")
                review.prepare(claim["token"], body, request_id=identifier)
            except Exception:
                with review.connect() as db:
                    db.execute("UPDATE cases SET token=NULL,expires=NULL WHERE token=?", (claim["token"],))
                raise
        result = review.publish(identifier)
        answer = {key: result[key] for key in ("status", "url", "number")}
        if result["status"] == "sent" and not (existing and existing["status"] == "sent"):
            try:
                answer["review"] = review.finish(result["token"], "waiting", "Telegram follow-up published; await recipient evidence")["status"]
            except ValueError:
                answer["review"] = "pending; publication is confirmed"
        return answer


def definition(name, description, properties, required=()):
    return {"name": name, "description": description,
            "annotations": {"readOnlyHint": name in {"board_updates", "scan_board", "read_issue", "published_link", "check_site"},
                            "destructiveHint": False}, "inputSchema": {
        "type": "object", "properties": properties, "required": list(required), "additionalProperties": False}}


STRING = {"type": "string"}
INTEGER = {"type": "integer"}
TOOLS = [
    definition("board_updates", "Read the board script's retained update/review status. Cached evidence is dated, not a fresh scan.", {}),
    definition("scan_board", "Run existing board discovery when monitor output is absent or a fresh scan is needed. Never publishes or claims a review.", {}),
    definition("read_issue", "Read a Workshop issue section with pagination. fresh=true retrieves GitHub evidence.",
               {"number": INTEGER, "section": STRING, "offset": INTEGER, "fresh": {"type": "boolean"}}, ("number",)),
    definition("review_notice", "Queue your brief, source-grounded description of what you are about to check in new relevant evidence.",
               {"numbers": {"type": "array", "items": INTEGER},
                "text": {"type": "string", "minLength": 1, "maxLength": 320}}, ("numbers", "text")),
    definition("request_operator", "Append a pending mechanism, access or agreement request for the next operator wake. Never grants approval.",
               {"title": STRING, "detail": STRING, "kind": STRING}, ("title", "detail")),
    definition("published_link", "Verify a local Markdown document matches an actually published repository file and return its URL.",
               {"path": STRING}, ("path",)),
    definition("check_site", "Check a documented public HTTPS endpoint without credentials; no redirects or authenticated-session proof.",
               {"url": STRING}, ("url",)),
    definition("follow_up", "Add compatible recipient work to an existing Workshop issue after review; recover publication instead of duplicating it.",
               {"number": INTEGER, "version": STRING, "body": STRING}, ("number", "version", "body")),
]


def serve(context, incoming=sys.stdin, outgoing=sys.stdout):
    tools = TurnTools(context)
    for line in incoming:
        request = json.loads(line)
        if "id" not in request:
            continue
        try:
            method = request["method"]
            if method == "initialize":
                result = {"protocolVersion": request["params"]["protocolVersion"], "capabilities": {"tools": {}},
                          "serverInfo": {"name": "workshop", "version": "1.0"}}
            elif method == "tools/list":
                result = {"tools": TOOLS}
            elif method == "tools/call":
                params = request["params"]
                if params["name"] not in {item["name"] for item in TOOLS}:
                    raise ValueError("Unknown tool")
                value = getattr(tools, params["name"])(**params.get("arguments", {}))
                result = {"content": [{"type": "text", "text": json.dumps(redact(value), ensure_ascii=False)}]}
            elif method == "ping":
                result = {}
            else:
                raise ValueError("Unsupported method")
        except Exception as error:
            result = {"isError": True, "content": [{"type": "text", "text": redact(str(error))[:1000]}]}
        outgoing.write(json.dumps({"jsonrpc": "2.0", "id": request["id"], "result": result}, ensure_ascii=False) + "\n")
        outgoing.flush()


if __name__ == "__main__":
    sys.stdin.reconfigure(encoding="utf-8")
    sys.stdout.reconfigure(encoding="utf-8")
    serve(json.loads(Path(sys.argv[1]).read_text(encoding="utf-8")))
