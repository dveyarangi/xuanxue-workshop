"""Read retained group history and original images within the host-selected group."""

import hashlib
import json
import sqlite3
import os
import tempfile
from contextlib import closing
from pathlib import Path, PurePosixPath
from urllib.parse import unquote


IMAGE_LIMIT = 10 * 1024 * 1024


class Archive:
    def __init__(self, state):
        self.state = Path(state).resolve()
        self.directory = self.state.parent / "archive"
        self.state.parent.mkdir(parents=True, exist_ok=True)
        with closing(sqlite3.connect(self.state)) as db, db:
            db.executescript("""
                CREATE TABLE IF NOT EXISTS group_archive (
                    chat_id INTEGER, message_id INTEGER, record TEXT,
                    PRIMARY KEY(chat_id,message_id));
            """)

    def retain(self, db, chat_id, message):
        previous = db.execute("SELECT record FROM group_archive WHERE chat_id=? AND message_id=?",
                              (chat_id, message["message_id"])).fetchone()
        cached = {a["file_id"]: a for a in json.loads(previous[0]).get("attachments", [])
                  if a.get("file_id") and a.get("blob")} if previous else {}
        attachments = [{**cached.get(a.get("file_id"), {}), **a} for a in message.get("attachments", [])]
        record = {"message_id": message["message_id"], "text": message["body"],
                  "sender": message["sender"], "created": message["created"],
                  "reply_to": message.get("reply_to"), "thread_id": message.get("thread_id"),
                  "attachments": attachments, "source": "telegram"}
        db.execute("INSERT INTO group_archive VALUES (?,?,?) ON CONFLICT(chat_id,message_id) "
                   "DO UPDATE SET record=excluded.record", (chat_id, record["message_id"], json.dumps(record, ensure_ascii=False)))

    def messages(self, chat_id):
        with closing(sqlite3.connect(self.state)) as db, db:
            records = {row[0]: json.loads(row[1]) for row in db.execute(
                "SELECT message_id,record FROM group_archive WHERE chat_id=?", (chat_id,))}
            tables = {row[0] for row in db.execute("SELECT name FROM sqlite_master WHERE type='table'")}
            binding = db.execute("SELECT value FROM telegram_meta WHERE key='binding'").fetchone() if "telegram_meta" in tables else None
            # A receiver database belongs to one group; an export must not expose its other records.
            if binding and json.loads(binding[0])[1] == chat_id and "telegram_requests" in tables:
                db.row_factory = sqlite3.Row
                for row in db.execute("SELECT * FROM telegram_requests"):
                    previous = records.get(row["message_id"], {})
                    records[row["message_id"]] = {**previous, "message_id": row["message_id"],
                        "text": row["body"], "sender": json.loads(row["sender"]), "created": row["created"],
                        "reply_to": row["reply_to"], "thread_id": row["thread_id"], "source": "telegram"}
                    for number, text in zip(json.loads(row["sent_ids"]), json.loads(row["parts"])):
                        records[number] = {"message_id": number, "text": text, "role": "assistant",
                                           "reply_to": row["message_id"], "thread_id": row["thread_id"],
                                           "source": "confirmed_bot_reply", "attachments": []}
                for row in db.execute("SELECT message_id,text,recipient,created FROM telegram_outbox WHERE status='sent'"):
                    records[row["message_id"]] = {**dict(row), "role": "assistant", "source": "confirmed_bot_reply", "attachments": []}
                for row in db.execute("SELECT n.message_id,n.text,r.message_id AS reply_to,r.thread_id FROM telegram_notices n "
                                      "JOIN telegram_requests r ON r.update_id=n.update_id WHERE n.status='sent'"):
                    records[row["message_id"]] = {**dict(row), "role": "assistant", "source": "confirmed_bot_reply", "attachments": []}
        return [records[key] for key in sorted(records)]

    def search(self, chat_id, query="", before=None, limit=20):
        if not isinstance(query, str) or len(query) > 1000 or type(limit) is not int or not 1 <= limit <= 50:
            raise ValueError("Supply a short query and a limit from 1 to 50")
        if before is not None and (type(before) is not int or before <= 0):
            raise ValueError("before must be a positive message identifier")
        words = query.casefold().split()
        matches = [m for m in self.messages(chat_id) if (before is None or m["message_id"] < before)
                   and all(word in (m["text"] + " " + json.dumps(m.get("sender", {}), ensure_ascii=False)).casefold() for word in words)]
        chosen = list(reversed(matches[-limit:]))
        return {"messages": [public_message(m, excerpt=True) for m in chosen], "matches": len(matches),
                "next_before": chosen[-1]["message_id"] if len(matches) > limit else None,
                "scope": "Retained messages of this group only; image content is not a text transcription"}

    def read(self, chat_id, message_id, radius=2):
        if type(message_id) is not int or message_id <= 0 or type(radius) is not int or not 0 <= radius <= 5:
            raise ValueError("Select a message and a radius from 0 to 5")
        records = self.messages(chat_id)
        position = next((i for i, m in enumerate(records) if m["message_id"] == message_id), None)
        if position is None:
            raise ValueError("Message is not retained in this group")
        return {"message": public_message(records[position]), "context": [public_message(m)
                for m in records[max(0, position-radius):position+radius+1] if m["message_id"] != message_id]}

    def image(self, chat_id, message_id, index=0, api=None):
        self.read(chat_id, message_id, radius=0)
        message = next(m for m in self.messages(chat_id) if m["message_id"] == message_id)
        images = [m for m in message.get("attachments", []) if m["kind"] == "image"]
        if type(index) is not int or not 0 <= index < len(images):
            raise ValueError("Select an image index from read_message")
        image = images[index]
        if image.get("blob"):
            data = checked_file(self.directory / "images", image["blob"]).read_bytes()
            if hashlib.sha256(data).hexdigest() != image["blob"]:
                raise ValueError("Retained image changed; source inspection is required")
        elif image.get("file_id") and api:
            data = api.download(image["file_id"], limit=IMAGE_LIMIT)
        else:
            raise ValueError(image.get("unavailable", "Image content is unavailable"))
        mime = image_type(data)
        if image.get("file_id") and not image.get("blob"):
            blob = hashlib.sha256(data).hexdigest()
            save_content(self.directory / "images", blob, data)
            with closing(sqlite3.connect(self.state)) as db, db:
                current = db.execute("SELECT record FROM group_archive WHERE chat_id=? AND message_id=?",
                                     (chat_id, message_id)).fetchone()
                if current:
                    record = json.loads(current[0])
                    for item in record.get("attachments", []):
                        if item.get("file_id") == image["file_id"]:
                            item.update(blob=blob, mime=mime)
                    db.execute("UPDATE group_archive SET record=? WHERE chat_id=? AND message_id=?",
                               (json.dumps(record, ensure_ascii=False), chat_id, message_id))
        return data, mime


def public_message(message, excerpt=False):
    value = {key: item for key, item in message.items() if key != "attachments"}
    value["images"] = [{"index": index, "name": item.get("name"), "available": bool(item.get("blob") or item.get("file_id")),
                        "unavailable": item.get("unavailable")} for index, item in enumerate(
                        a for a in message.get("attachments", []) if a["kind"] == "image")]
    value["other_attachments"] = [{"name": a.get("name"), "available": False} for a in message.get("attachments", []) if a["kind"] != "image"]
    if excerpt and len(value["text"]) > 1600:
        value["text"] = value["text"][:1600]
        value["truncated"] = True
    return value


def image_type(data):
    if len(data) > IMAGE_LIMIT:
        raise ValueError("Image exceeds the 10 MiB reading limit")
    if data.startswith(b"\x89PNG\r\n\x1a\n"):
        return "image/png"
    if data.startswith(b"\xff\xd8\xff"):
        return "image/jpeg"
    if data.startswith(b"RIFF") and data[8:12] == b"WEBP":
        return "image/webp"
    raise ValueError("Only PNG, JPEG and WebP still images are supported")


def checked_file(root, name):
    relative = PurePosixPath(unquote(name))
    if relative.is_absolute() or ".." in relative.parts or "\\" in name or ":" in name:
        raise ValueError("Export attachment leaves its directory")
    root = Path(root).absolute()
    path = root
    for part in relative.parts:
        path = path / part
        if path.is_symlink() or path.is_junction():
            raise ValueError("Redirected attachments are not accepted")
    if root.resolve() != root or not path.resolve().is_relative_to(root) or not path.is_file() or path.stat().st_nlink != 1:
        raise ValueError("Attachment is missing, redirected or hard-linked")
    return path


def save_content(root, name, data):
    root = Path(root).absolute()
    target = root / name
    if root.resolve() != root or not target.resolve().is_relative_to(root):
        raise ValueError("Archive storage cannot be redirected")
    for parent in [target, *target.parents]:
        if parent.is_symlink() or parent.is_junction():
            raise ValueError("Archive storage cannot be redirected")
        if parent == root:
            break
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists():
        if checked_file(root, name).read_bytes() != data:
            raise ValueError("Retained source was changed")
        return
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(dir=target.parent, delete=False) as stream:
            temporary = Path(stream.name)
            stream.write(data)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, target)
    finally:
        if temporary:
            temporary.unlink(missing_ok=True)
