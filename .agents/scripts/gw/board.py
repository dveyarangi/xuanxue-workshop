"""Mechanical discovery and delivery; judgment belongs to assignment review."""

import argparse
import copy
import hashlib
import json
import os
import re
import sqlite3
import subprocess
import sys
import time
import uuid
from contextlib import contextmanager
from pathlib import Path
from types import SimpleNamespace
from urllib.parse import quote, urlparse


FOLLOW_UP_SECONDS = 6 * 60 * 60


def encoded(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def digest(value):
    return hashlib.sha256(encoded(value).encode("utf-8")).hexdigest()


def pull_reference(value):
    if not isinstance(value, dict):
        return value
    result = {key: value[key] for key in ('ref', 'sha') if key in value}
    if 'repo' in value:
        repo = value['repo']
        result['repo'] = {'full_name': repo.get('full_name')} if isinstance(repo, dict) else repo
    return result


def relevant_material(value):
    if isinstance(value, dict):
        return {key: {'full_name': item['full_name']}
                if key in {'repo', 'repository'} and isinstance(item, dict) and 'full_name' in item
                else relevant_material(item) for key, item in value.items()}
    if isinstance(value, list):
        return [relevant_material(item) for item in value]
    return value


class Board:
    def __init__(self, state, tracker=None, *, clock=time.time, lease_seconds=3600):
        self.state, self.tracker, self.clock = Path(state), tracker, clock
        self.lease_seconds = lease_seconds
        if tracker is None:
            if not self.state.is_file():
                raise ValueError("No board progress exists")
            with self.connect() as db:
                identity = db.execute("SELECT value FROM meta WHERE name='identity'").fetchone()
                if identity is None:
                    raise ValueError("Board progress identity is absent")
                tracker = self.tracker = SimpleNamespace(**json.loads(identity[0]))
        self.state.parent.mkdir(parents=True, exist_ok=True)
        with self.connect() as db:
            if db.execute("PRAGMA user_version").fetchone()[0] not in {0, 1}:
                raise ValueError("Unsupported board progress version")
            db.executescript("""
                CREATE TABLE IF NOT EXISTS meta (name TEXT PRIMARY KEY, value TEXT NOT NULL);
                CREATE TABLE IF NOT EXISTS cases (
                    number INTEGER PRIMARY KEY, observed TEXT NOT NULL, reviewed TEXT,
                    snapshot TEXT NOT NULL, due REAL NOT NULL DEFAULT 0, token TEXT UNIQUE,
                    expires REAL, basis TEXT, outcome TEXT, note TEXT);
                CREATE TABLE IF NOT EXISTS publications (
                    id TEXT PRIMARY KEY, number INTEGER NOT NULL, token TEXT NOT NULL,
                    basis TEXT NOT NULL, body TEXT NOT NULL, author TEXT NOT NULL,
                    status TEXT NOT NULL CHECK(status IN ('prepared','sending','sent','conflict','uncertain')),
                    comment_id INTEGER, url TEXT);
            """)
            identity = encoded({"repo": tracker.repo, "labels": sorted(tracker.labels), "author": tracker.author})
            previous = db.execute("SELECT value FROM meta WHERE name='identity'").fetchone()
            if previous and previous[0] != identity:
                raise ValueError("State belongs to another board or recipient selection")
            db.execute("INSERT OR IGNORE INTO meta VALUES ('identity', ?)", (identity,))
            db.execute("PRAGMA user_version=1")

    @contextmanager
    def connect(self):
        db = sqlite3.connect(self.state, timeout=10)
        db.row_factory = sqlite3.Row
        try:
            with db:
                yield db
        finally:
            db.close()

    def snapshot(self, number, *, fresh=True):
        with self.connect() as db:
            own_bodies = [row[0] for row in db.execute("SELECT body FROM publications WHERE number=?", (number,))]
        return self.tracker.snapshot(number, own_bodies=own_bodies, fresh=fresh)

    def fingerprint(self, snapshot):
        return self._fingerprint(snapshot, relevant=True)

    def _fingerprint(self, snapshot, *, relevant):
        with self.connect() as db:
            publications = list(db.execute("SELECT * FROM publications WHERE number=?", (snapshot["issue"]["number"],)))

        def own(comment, publication):
            return (comment.get("body") == publication["body"]
                    and comment.get("user", {}).get("login") == publication["author"]
                    and (publication["comment_id"] is None or comment.get("id") == publication["comment_id"]))

        value = copy.deepcopy(snapshot)
        if relevant:
            for evidence in value.get('evidence', []):
                pull = evidence.get('data', {}).get('pull', {})
                for side in ('head', 'base'):
                    if side in pull:
                        pull[side] = pull_reference(pull[side])
        value["comments"] = [c for c in snapshot["comments"] if not any(own(c, p) for p in publications)]
        value["timeline"] = [event for event in snapshot["timeline"] if not (
            event.get("event") == "commented" and any(own(event, p) for p in publications))]
        value["missing_publications"] = [p["id"] for p in publications if p["status"] == "sent"
                                         and not any(own(c, p) for c in snapshot["comments"])]
        return digest(relevant_material(value) if relevant else value)

    def scan(self):
        numbers = set(self.tracker.discover())
        with self.connect() as db:
            numbers.update(row[0] for row in db.execute("SELECT number FROM cases"))
        candidates, errors = [], []
        for number in sorted(numbers):
            try:
                snapshot = self.snapshot(number, fresh=False)
                version = self.fingerprint(snapshot)
                with self.connect() as db:
                    row = db.execute("SELECT * FROM cases WHERE number=?", (number,)).fetchone()
                    pending = db.execute("SELECT 1 FROM publications WHERE number=? AND status IN ('prepared','sending','uncertain')",
                                         (number,)).fetchone()
                    db.execute("""INSERT INTO cases (number, observed, snapshot) VALUES (?, ?, ?)
                                  ON CONFLICT(number) DO UPDATE SET observed=excluded.observed,
                                  snapshot=excluded.snapshot""", (number, version, encoded(snapshot)))
                reason = "publication" if pending else "new" if row is None or row["reviewed"] is None else (
                    "changed" if version != row["reviewed"] else (
                        "follow_up" if row["due"] and row["due"] <= self.clock() else None))
                if reason:
                    candidates.append({"number": number, "title": snapshot["issue"]["title"],
                                       "url": snapshot["issue"]["html_url"], "reason": reason,
                                       "busy": bool(row and row["token"] and row["expires"] > self.clock())})
            except (RuntimeError, ValueError, OSError) as error:
                errors.append({"number": number, "error": str(error)})
        return {"complete": not errors, "candidates": candidates, "errors": errors}

    def claim(self, number):
        snapshot = self.snapshot(number)
        version, token = self.fingerprint(snapshot), uuid.uuid4().hex
        with self.connect() as db:
            db.execute("BEGIN IMMEDIATE")
            row = db.execute("SELECT * FROM cases WHERE number=?", (number,)).fetchone()
            if row and row["token"] and row["expires"] > self.clock():
                raise ValueError("Case is already claimed")
            db.execute("""INSERT INTO cases (number, observed, snapshot, token, expires, basis)
                          VALUES (?, ?, ?, ?, ?, ?) ON CONFLICT(number) DO UPDATE SET
                          observed=excluded.observed, snapshot=excluded.snapshot, token=excluded.token,
                          expires=excluded.expires, basis=excluded.basis""",
                       (number, version, encoded(snapshot), token, self.clock() + self.lease_seconds, version))
        return {"token": token, "fingerprint": version, "snapshot": snapshot}

    def held(self, db, token):
        row = db.execute("SELECT * FROM cases WHERE token=?", (token,)).fetchone()
        if row is None or row["expires"] <= self.clock():
            raise ValueError("Review lease is absent or expired")
        return row

    def renew(self, token):
        with self.connect() as db:
            db.execute("BEGIN IMMEDIATE")
            self.held(db, token)
            expiry = self.clock() + self.lease_seconds
            db.execute("UPDATE cases SET expires=? WHERE token=?", (expiry, token))
        return {"token": token, "expires": expiry}

    def prepare(self, token, body, *, request_id=None):
        if not body.strip() or len(body) > 60000 or "<!-- workshop-board:" in body:
            raise ValueError("A nonempty comment of at most 60000 characters without reserved markers is required")
        with self.connect() as db:
            case = dict(self.held(db, token))
        snapshot = self.snapshot(case["number"])
        if self.fingerprint(snapshot) != case["basis"]:
            raise ValueError("Case changed during review; reclaim current material")
        if not set(snapshot["issue"]["labels"]).intersection(self.tracker.labels):
            raise ValueError("Case is no longer addressed to this review")
        identifier = request_id or digest([self.tracker.repo, case["number"], case["basis"], body])
        if not re.fullmatch(r"[A-Za-z0-9_-]{1,80}", identifier):
            raise ValueError("Invalid publication identifier")
        comment = f"<!-- workshop-board:{identifier} -->\n{body}"
        with self.connect() as db:
            db.execute("BEGIN IMMEDIATE")
            self.held(db, token)
            old = db.execute("SELECT * FROM publications WHERE id=?", (identifier,)).fetchone()
            if old:
                if (old["number"], old["basis"], old["body"]) != (case["number"], case["basis"], comment):
                    raise ValueError("Publication identifier already belongs to another response")
                if old["status"] in {"prepared", "conflict"}:
                    db.execute("UPDATE publications SET token=?, status='prepared' WHERE id=?", (token, identifier))
                return dict(db.execute("SELECT * FROM publications WHERE id=?", (identifier,)).fetchone())
            if db.execute("SELECT 1 FROM publications WHERE number=? AND status IN ('prepared','sending','uncertain')",
                          (case["number"],)).fetchone():
                raise ValueError("Case has another pending publication")
            db.execute("INSERT INTO publications VALUES (?, ?, ?, ?, ?, ?, 'prepared', NULL, NULL)",
                       (identifier, case["number"], token, case["basis"], comment, self.tracker.author))
        return self.publication(identifier)

    def cancel(self, identifier):
        with self.connect() as db:
            db.execute("BEGIN IMMEDIATE")
            row = db.execute("SELECT * FROM publications WHERE id=?", (identifier,)).fetchone()
            if row is None or row["status"] not in {"prepared", "conflict"}:
                raise ValueError("Only a definitely unsent preparation can be cancelled")
            db.execute("UPDATE publications SET status='conflict' WHERE id=?", (identifier,))
        return self.publication(identifier)

    def publication(self, identifier):
        with self.connect() as db:
            row = db.execute("SELECT * FROM publications WHERE id=?", (identifier,)).fetchone()
            if row is None:
                raise ValueError("Unknown publication identifier")
            return dict(row)

    def publication_status(self, identifier, status, comment=None):
        with self.connect() as db:
            db.execute("UPDATE publications SET status=?, comment_id=?, url=? WHERE id=?",
                       (status, comment.get("id") if comment else None,
                        comment.get("html_url") if comment else None, identifier))
        return self.publication(identifier)

    def publish(self, identifier):
        operation = self.publication(identifier)
        snapshot = self.snapshot(operation["number"])
        matches = [c for c in snapshot["comments"] if c.get("body") == operation["body"]
                   and c.get("user", {}).get("login") == operation["author"]]
        if len(matches) == 1:
            return self.publication_status(identifier, "sent", matches[0])
        if matches or operation["status"] in {"sending", "uncertain", "sent"}:
            # Absence after an ambiguous write is not evidence that retrying is safe.
            return self.publication_status(identifier, "uncertain")
        if operation["status"] != "prepared":
            return operation
        with self.connect() as db:
            db.execute("BEGIN IMMEDIATE")
            case = self.held(db, operation["token"])
            if case["basis"] != operation["basis"] or self.fingerprint(snapshot) != operation["basis"]:
                db.execute("UPDATE publications SET status='conflict' WHERE id=?", (identifier,))
                return {**operation, "status": "conflict"}
            updated = db.execute("UPDATE publications SET status='sending' WHERE id=? AND status='prepared'",
                                 (identifier,)).rowcount
            if not updated:
                return {**operation, "status": "uncertain"}
        try:
            self.tracker.post(operation["number"], operation["body"])
            readback = self.snapshot(operation["number"])
            matches = [c for c in readback["comments"] if c.get("body") == operation["body"]
                       and c.get("user", {}).get("login") == operation["author"]]
            return self.publication_status(identifier, "sent", matches[0]) if len(matches) == 1 else (
                self.publication_status(identifier, "uncertain"))
        except (OSError, RuntimeError, ValueError):
            return self.publication_status(identifier, "uncertain")

    def finish(self, token, outcome, note, *, follow_up=FOLLOW_UP_SECONDS):
        if outcome not in {"reviewed", "waiting", "operator"} or not note.strip() or follow_up <= 0:
            raise ValueError("A review outcome and its resumption note are required")
        with self.connect() as db:
            row = dict(self.held(db, token))
            if db.execute("SELECT 1 FROM publications WHERE number=? AND status IN ('prepared','sending','uncertain')",
                          (row["number"],)).fetchone():
                raise ValueError("Unconfirmed publication prevents review completion")
        snapshot = self.snapshot(row["number"])
        version = self.fingerprint(snapshot)
        with self.connect() as db:
            db.execute("BEGIN IMMEDIATE")
            self.held(db, token)
            if version != row["basis"]:
                db.execute("UPDATE cases SET token=NULL, expires=NULL WHERE token=?", (token,))
                return {"status": "conflict", "number": row["number"]}
            due = self.clock() + max(follow_up, FOLLOW_UP_SECONDS) if outcome != "reviewed" else 0
            db.execute("""UPDATE cases SET reviewed=?, observed=?, snapshot=?, due=?, token=NULL,
                          expires=NULL, outcome=?, note=? WHERE token=?""",
                       (version, version, encoded(snapshot), due, outcome, note, token))
        return {"status": "reviewed", "number": row["number"], "outcome": outcome, "due": due}

    def status(self):
        with self.connect() as db:
            return {"cases": [dict(row) for row in db.execute(
                "SELECT number, observed, reviewed, due, expires, outcome, note FROM cases ORDER BY number")],
                    "publications": [dict(row) for row in db.execute(
                        "SELECT id, number, status, comment_id, url FROM publications ORDER BY rowid")]}

    def upgrade(self, *, previous_follow_up):
        if previous_follow_up <= 0:
            raise ValueError('The known previous follow-up interval is required')
        with self.connect() as db:
            db.execute('BEGIN IMMEDIATE')
            if db.execute("SELECT 1 FROM meta WHERE name='material_version' AND value='2'").fetchone():
                return {'upgraded': 0}
            if db.execute('SELECT 1 FROM cases WHERE token IS NOT NULL AND expires>?', (self.clock(),)).fetchone():
                raise ValueError('Wait for active review leases before upgrading progress')
            rows = list(db.execute('SELECT * FROM cases'))
            for row in rows:
                snapshot = json.loads(row['snapshot'])
                old = self._fingerprint(snapshot, relevant=False)
                current = self.fingerprint(snapshot)
                # Rebase only a digest proved by its stored snapshot; retain unreviewed changes.
                reviewed = current if row['reviewed'] == old else row['reviewed']
                basis = current if row['basis'] == old else row['basis']
                due = row['due']
                if due and row['outcome'] in {'waiting', 'operator'}:
                    due += max(0, FOLLOW_UP_SECONDS - previous_follow_up)
                db.execute('UPDATE cases SET observed=?,reviewed=?,basis=?,due=? WHERE number=?',
                           (current, reviewed, basis, due, row['number']))
                db.execute('UPDATE publications SET basis=? WHERE number=? AND basis=?',
                           (current, row['number'], old))
            db.execute("INSERT OR REPLACE INTO meta VALUES ('material_version','2')")
        return {'upgraded': len(rows)}

    def check(self):
        with self.connect() as db:
            if db.execute("PRAGMA integrity_check").fetchone()[0] != "ok":
                raise ValueError("Board progress database failed integrity checking")
            for row in db.execute("SELECT * FROM cases"):
                snapshot = json.loads(row["snapshot"])
                if snapshot["issue"]["number"] != row["number"] or not re.fullmatch(r"[a-f0-9]{64}", row["observed"]):
                    raise ValueError("Invalid case progress")
            count = db.execute("SELECT COUNT(*) FROM cases").fetchone()[0]
        return {"valid": True, "cases": count}


class Gh:
    def __init__(self, run=subprocess.run):
        self.run = run

    def __call__(self, method, path, payload=None, *, collection=None):
        command = ["gh", "api", "--method", method, "-H", "Accept: application/vnd.github+json",
                   "-H", "X-GitHub-Api-Version: 2022-11-28", path]
        if collection is not None:
            command += ["--paginate", "--slurp"]
        if payload is not None:
            command += ["--input", "-"]
        try:
            response = self.run(command, input=None if payload is None else encoded(payload).encode("utf-8"),
                                capture_output=True, timeout=90, check=True,
                                creationflags=subprocess.CREATE_NO_WINDOW if os.name == "nt" else 0)
            value = json.loads(response.stdout)
        except (subprocess.SubprocessError, OSError, ValueError) as error:
            raise RuntimeError(f"GitHub {method} failed: {path}") from error
        if collection is None:
            return value
        result = []
        for page in value:
            items = page[collection] if collection else page
            if not isinstance(items, list):
                raise RuntimeError("GitHub pagination returned an unexpected shape")
            result.extend(items)
        return result


class GitHub:
    def __init__(self, repo, labels, api=None):
        if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", repo) or not labels:
            raise ValueError("An explicit owner/repository and recipient labels are required")
        self.repo, self.labels, self.api = repo, tuple(labels), api or Gh()
        self.author = self.api("GET", "user")["login"]
        self.cache = {}

    def discover(self):
        self.cache.clear()
        values = self.api("GET", f"repos/{self.repo}/issues?state=all&per_page=100", collection="")
        return [item["number"] for item in values if "pull_request" not in item
                and set(self.labels).intersection(label["name"] for label in item["labels"])]

    @staticmethod
    def issue(value):
        result = {key: value.get(key) for key in
                  ("number", "title", "body", "state", "state_reason", "locked", "html_url")}
        result["labels"] = sorted(label["name"] for label in value["labels"])
        return result

    def snapshot(self, number, own_bodies=(), *, fresh=True):
        if fresh:
            self.cache.clear()
        prefix = f"repos/{self.repo}/issues/{int(number)}"
        issue = self.api("GET", prefix)
        comments = self.api("GET", prefix + "/comments?per_page=100", collection="")
        timeline = self.api("GET", prefix + "/timeline?per_page=100", collection="")
        after = self.api("GET", prefix)
        if issue.get("updated_at") != after.get("updated_at") or self.issue(issue) != self.issue(after):
            raise RuntimeError("Issue changed while being read; retry discovery")
        bodies = [issue.get("body") or ""]
        bodies.extend(c.get("body") or "" for c in comments if not (
            c.get("body") in own_bodies and c.get("user", {}).get("login") == self.author))
        bodies.extend(e.get("body") or "" for e in timeline if e.get("event") != "commented")
        bodies.extend(e.get("source", {}).get("issue", {}).get("html_url") or "" for e in timeline)
        text = "\n".join(bodies)
        links = set(re.findall(r'https://github\.com/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+/(?:issues|pull|commit|blob|actions/runs)/[^\s<>"\)\]\x27\\]+', text))
        for referenced_repo, referenced_number in re.findall(r"\b([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)#([1-9][0-9]*)\b", text):
            links.add(f"https://github.com/{referenced_repo}/issues/{referenced_number}")
        for referenced_number in re.findall(r"(?<![A-Za-z0-9_/#])#([1-9][0-9]*)\b", text):
            links.add(f"https://github.com/{self.repo}/issues/{referenced_number}")
        for event in timeline:
            commit_url = event.get("commit_url") or ""
            match = re.fullmatch(r"https://api\.github\.com/repos/([^/]+/[^/]+)/commits/([A-Za-z0-9]+)", commit_url)
            if match:
                links.add(f"https://github.com/{match[1]}/commit/{match[2]}")
        evidence = []
        for link in sorted(links):
            link = urlparse(link.rstrip(".,;"))._replace(fragment="").geturl()
            if urlparse(link).path.rstrip("/") == f"/{self.repo}/issues/{number}":
                continue
            if link not in self.cache:
                try:
                    self.cache[link] = {"url": link, "data": self.reference(link)}
                except (RuntimeError, ValueError, KeyError) as error:
                    self.cache[link] = {"url": link, "unavailable": True, "reason": str(error)}
            evidence.append(self.cache[link])
        return relevant_material({"issue": self.issue(issue), "comments": comments,
                                  "timeline": timeline, "evidence": evidence})

    def reference(self, url):
        parts = urlparse(url).path.strip("/").split("/")
        repo, kind, identifier = "/".join(parts[:2]), parts[2], parts[3]
        prefix = f"repos/{repo}"
        identifier = quote(identifier, safe="")
        if kind == "pull":
            pull = self.api("GET", f"{prefix}/pulls/{identifier}")
            sha = pull["head"]["sha"]
            for side in ('head', 'base'):
                if side in pull:
                    pull[side] = pull_reference(pull[side])
            return {"pull": {key: pull.get(key) for key in ("number", "title", "body", "state", "merged", "merged_at", "head", "base")},
                    "comments": self.api("GET", f"{prefix}/issues/{identifier}/comments?per_page=100", collection=""),
                    "reviews": self.api("GET", f"{prefix}/pulls/{identifier}/reviews?per_page=100", collection=""),
                    "review_comments": self.api("GET", f"{prefix}/pulls/{identifier}/comments?per_page=100", collection=""),
                    "checks": self.api("GET", f"{prefix}/commits/{sha}/check-runs?per_page=100", collection="check_runs"),
                    "status": self.api("GET", f"{prefix}/commits/{sha}/status")}
        if kind == "issues":
            issue = self.api("GET", f"{prefix}/issues/{identifier}")
            if "pull_request" in issue:
                return self.reference(f"https://github.com/{repo}/pull/{identifier}")
            return {"issue": self.issue(issue),
                    "comments": self.api("GET", f"{prefix}/issues/{identifier}/comments?per_page=100", collection=""),
                    "timeline": self.api("GET", f"{prefix}/issues/{identifier}/timeline?per_page=100", collection="")}
        if kind == "commit":
            commit = self.api("GET", f"{prefix}/commits/{identifier}")
            return {"sha": commit["sha"],
                    "checks": self.api("GET", f"{prefix}/commits/{identifier}/check-runs?per_page=100", collection="check_runs"),
                    "status": self.api("GET", f"{prefix}/commits/{identifier}/status")}
        if kind == "blob":
            path = "/".join(quote(part, safe="") for part in parts[4:])
            content = self.api("GET", f"{prefix}/contents/{path}?ref={identifier}")
            if not isinstance(content, dict):
                raise ValueError("Source reference did not identify a file")
            return {key: content.get(key) for key in ("sha", "path", "type", "html_url")}
        if kind == "actions" and identifier == "runs" and len(parts) > 4:
            run = self.api("GET", f"{prefix}/actions/runs/{int(parts[4])}")
            return {key: run.get(key) for key in ("id", "head_sha", "status", "conclusion", "run_attempt", "updated_at")}
        raise ValueError("Unsupported GitHub evidence URL")

    def post(self, number, body):
        return self.api("POST", f"repos/{self.repo}/issues/{int(number)}/comments", {"body": body})


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", required=True)
    parser.add_argument("--label", action="append", required=True)
    parser.add_argument("--state", type=Path, default=Path(".local/board-review/history.sqlite3"))
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("scan")
    sub.add_parser("status")
    sub.add_parser("check")
    upgrade = sub.add_parser('upgrade')
    upgrade.add_argument('--previous-follow-up', type=int, required=True)
    claim = sub.add_parser("claim")
    claim.add_argument("number", type=int)
    claim.add_argument("--output", type=Path, required=True)
    renew = sub.add_parser("renew")
    renew.add_argument("token")
    prepare = sub.add_parser("prepare")
    prepare.add_argument("token")
    prepare.add_argument("--message-file", type=Path, required=True)
    prepare.add_argument("--request-id")
    publish = sub.add_parser("publish")
    publish.add_argument("request_id")
    cancel = sub.add_parser("cancel")
    cancel.add_argument("request_id")
    finish = sub.add_parser("finish")
    finish.add_argument("token")
    finish.add_argument("--outcome", required=True, choices=("reviewed", "waiting", "operator"))
    finish.add_argument("--note", required=True)
    finish.add_argument("--follow-up", type=int, default=FOLLOW_UP_SECONDS)
    args = parser.parse_args()
    if args.command in {"status", "check", "cancel", "upgrade"}:
        review = Board(args.state)
        if review.tracker.repo != args.repo or sorted(review.tracker.labels) != sorted(args.label):
            raise ValueError("State belongs to another board or recipient selection")
    else:
        review = Board(args.state, GitHub(args.repo, args.label))
    if args.command == "claim":
        result = review.claim(args.number)
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(encoded(result), encoding="utf-8")
        result = {"token": result["token"], "fingerprint": result["fingerprint"], "snapshot_file": str(args.output)}
    elif args.command == "renew":
        result = review.renew(args.token)
    elif args.command == "prepare":
        operation = review.prepare(args.token, args.message_file.read_text(encoding="utf-8-sig"), request_id=args.request_id)
        result = {key: operation[key] for key in ("id", "number", "status")}
    elif args.command in {"publish", "cancel"}:
        operation = getattr(review, args.command)(args.request_id)
        result = {key: operation[key] for key in ("id", "number", "status", "comment_id", "url")}
    elif args.command == "finish":
        result = review.finish(args.token, args.outcome, args.note, follow_up=args.follow_up)
    elif args.command == 'upgrade':
        result = review.upgrade(previous_follow_up=args.previous_follow_up)
    else:
        result = getattr(review, args.command)()
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return int(result.get("complete") is False or (
        args.command != "cancel" and result.get("status") in {"uncertain", "conflict"}))


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    try:
        raise SystemExit(main())
    except (RuntimeError, ValueError, OSError, sqlite3.Error) as error:
        print(encoded({"error": str(error), "review_complete": False}), file=sys.stderr)
        raise SystemExit(1)
