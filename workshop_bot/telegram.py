import json
import time
from datetime import datetime, timezone
from urllib.parse import parse_qs, urlsplit

from .service import redact
from .telegram_api import TelegramError


class Group:
    """First group exchange; continuation context is pending under q-0002.0012."""

    def __init__(self, workshop, api, group_id):
        self.workshop = workshop
        self.api = api
        self.group_id = group_id
        self.identity = None
        with workshop.connect() as db:
            db.execute("CREATE TABLE IF NOT EXISTS telegram_meta (key TEXT PRIMARY KEY, value TEXT)")
            db.execute("CREATE TABLE IF NOT EXISTS telegram_requests ("
                       "update_id INTEGER PRIMARY KEY, message_id INTEGER UNIQUE, sender TEXT, "
                       "created TEXT, body TEXT, thread_id INTEGER, status TEXT, result TEXT, "
                       "sent_ids TEXT DEFAULT '[]', error TEXT, parts TEXT DEFAULT '[]', "
                       "attempts INTEGER DEFAULT 0, retry_at REAL DEFAULT 0)")
            columns = {row[1] for row in db.execute("PRAGMA table_info(telegram_requests)")}
            if not {"parts", "retry_at", "attempts"}.issubset(columns):
                raise ValueError("Версия истории Telegram не поддерживается; исходная история сохранена.")

    def start(self):
        identity = self.api.call("getMe")
        if not identity.get("is_bot") or not identity.get("username"):
            raise ValueError("Telegram не подтвердил аккаунт бота.")
        if self.api.call("getWebhookInfo").get("url"):
            raise ValueError("У бота настроен другой получатель сообщений (webhook).")
        chat = self.api.call("getChat", chat_id=self.group_id)
        if chat.get("id") != self.group_id or chat.get("type") not in {"group", "supergroup"}:
            raise ValueError("Нужен числовой идентификатор выбранной группы.")
        member = self.api.call("getChatMember", chat_id=self.group_id, user_id=identity["id"])
        if member.get("status") not in {"member", "administrator", "creator"}:
            raise ValueError("Бот не является участником группы с правом отправки сообщений.")
        if member["status"] == "member" and chat.get("permissions", {}).get("can_send_messages") is False:
            raise ValueError("В группе запрещена отправка сообщений участникам.")
        if not identity.get("can_read_all_group_messages") and member["status"] not in {"administrator", "creator"}:
            raise ValueError("Отключите privacy mode у BotFather и заново добавьте бота в группу.")
        binding = json.dumps([identity["id"], self.group_id])
        with self.workshop.connect() as db:
            old = db.execute("SELECT value FROM telegram_meta WHERE key='binding'").fetchone()
            if old and old[0] != binding:
                raise ValueError("Эта история принадлежит другому боту или группе.")
            db.execute("INSERT OR IGNORE INTO telegram_meta VALUES ('binding', ?)", (binding,))
            db.execute("UPDATE telegram_requests SET status='uncertain', error='Подтверждение отправки потеряно.' "
                       "WHERE status='sending'")
            db.execute("UPDATE telegram_requests SET status='queued' WHERE status='processing'")
        self.identity = identity

    def poll_once(self, timeout=25):
        with self.workshop.connect() as db:
            offset = db.execute("SELECT value FROM telegram_meta WHERE key='offset'").fetchone()
        updates = self.api.call("getUpdates", offset=int(offset[0]) if offset else 0,
                                timeout=timeout, allowed_updates=["message"])
        for update in sorted(updates, key=lambda item: item["update_id"]):
            selected = self.select(update)
            with self.workshop.connect() as db:
                if selected:
                    db.execute("INSERT OR IGNORE INTO telegram_requests "
                               "(update_id,message_id,sender,created,body,thread_id,status) VALUES (?,?,?,?,?,?,'queued')",
                               (update["update_id"], selected["message_id"],
                                json.dumps(redact(selected["sender"]), ensure_ascii=False), selected["created"],
                                redact(selected["body"]), selected["thread_id"]))
                    if selected["bare"]:
                        invitation = "Задайте вопрос о проектах Workshop — помогу разобраться."
                        db.execute("UPDATE telegram_requests SET status='ready', result=?, parts=? "
                                   "WHERE update_id=? AND status='queued'",
                                   (json.dumps({"status": "answered", "answer": invitation, "sources": []}, ensure_ascii=False),
                                    json.dumps([invitation], ensure_ascii=False), update["update_id"]))
                db.execute("INSERT INTO telegram_meta VALUES ('offset', ?) "
                           "ON CONFLICT(key) DO UPDATE SET value=CAST(MAX(CAST(value AS INTEGER), "
                           "CAST(excluded.value AS INTEGER)) AS TEXT)",
                           (str(update["update_id"] + 1),))
        return len(updates)

    def select(self, update):
        message = update.get("message", {})
        if message.get("chat", {}).get("id") != self.group_id:
            return None
        if message.get("from", {}).get("is_bot") and not message.get("sender_chat"):
            return None
        text = message.get("text", message.get("caption", ""))
        entities = message.get("entities", message.get("caption_entities", []))
        references = self.references(text, entities)
        if not references:
            return None
        remaining = text
        for reference in references:
            remaining = remaining.replace(reference, "", 1)
        return {"message_id": message["message_id"], "body": text,
                "bare": not remaining.strip(" \t\r\n,.;:!?—-"),
                "sender": {k: v for k, v in message.get("sender_chat", message.get("from", {})).items()
                           if k in {"id", "first_name", "last_name", "username", "title", "type"}},
                "created": datetime.fromtimestamp(message["date"], timezone.utc).isoformat(),
                "thread_id": message.get("message_thread_id")}

    def references(self, text, entities):
        references = []
        username = self.identity["username"].lower()
        for entity in entities:
            try:
                start, end = entity["offset"] * 2, (entity["offset"] + entity["length"]) * 2
                encoded = text.encode("utf-16-le")
                if not 0 <= start < end <= len(encoded):
                    continue
                visible = encoded[start:end].decode("utf-16-le")
                kind = entity.get("type")
                matched = kind == "mention" and visible.lower() == "@" + username
                if kind == "text_mention":
                    matched = entity.get("user", {}).get("id") == self.identity["id"]
                if kind in {"url", "text_link"}:
                    raw = entity.get("url", visible)
                    url = urlsplit(raw if "://" in raw else "https://" + raw)
                    matched = (url.scheme in {"http", "https"} and
                               url.netloc.lower() in {"t.me", "telegram.me", "telegram.dog"} and
                               url.path.rstrip("/").lower() == "/" + username)
                    if url.scheme == "tg" and url.netloc == "resolve":
                        matched = parse_qs(url.query).get("domain", [""])[0].lower() == username
                    if url.scheme == "tg" and url.netloc == "user":
                        matched = parse_qs(url.query).get("id", [""])[0] == str(self.identity["id"])
                if matched:
                    references.append(visible)
            except (KeyError, TypeError, ValueError, UnicodeError):
                continue
        return references

    def work_once(self):
        with self.workshop.connect() as db:
            row = db.execute("SELECT * FROM telegram_requests WHERE status IN ('queued','ready') "
                             "ORDER BY update_id LIMIT 1").fetchone()
            if row is None:
                return False
            if row["retry_at"] > time.time():
                return False
            if row["status"] == "queued":
                db.execute("UPDATE telegram_requests SET status='processing' WHERE update_id=?", (row["update_id"],))
        if row["status"] == "queued":
            result = self.workshop.ask(f"telegram:{self.identity['id']}:{self.group_id}:{row['message_id']}",
                                       row["body"], sender=row["sender"])
            text = result["answer"]
            if result.get("sources"):
                text += "\n\nИсточники — локальные записи Workshop:\n" + "\n".join(result["sources"])
            parts = split_reply(text)
            with self.workshop.connect() as db:
                db.execute("UPDATE telegram_requests SET status='ready', result=?, parts=? WHERE update_id=?",
                           (json.dumps(result, ensure_ascii=False), json.dumps(parts, ensure_ascii=False), row["update_id"]))
        else:
            parts = json.loads(row["parts"])
        sent_ids = json.loads(row["sent_ids"])
        for part in parts[len(sent_ids):]:
            with self.workshop.connect() as db:
                db.execute("UPDATE telegram_requests SET status='sending' WHERE update_id=?", (row["update_id"],))
            parameters = {"chat_id": self.group_id, "text": part,
                          "reply_parameters": {"message_id": row["message_id"]},
                          "link_preview_options": {"is_disabled": True}}
            if row["thread_id"] is not None:
                parameters["message_thread_id"] = row["thread_id"]
            try:
                sent = self.api.call("sendMessage", **parameters)
                if not isinstance(sent.get("message_id"), int) or sent.get("chat", {}).get("id") != self.group_id:
                    raise TelegramError()
            except Exception as error:
                known = isinstance(error, TelegramError)
                retry = known and error.code == 429 and row["attempts"] < 3
                status = "ready" if retry else "rejected" if known and not error.uncertain else "uncertain"
                detail = str(error) if known else "Доставка не подтверждена; повтор не выполнен."
                with self.workshop.connect() as db:
                    db.execute("UPDATE telegram_requests SET status=?, error=?, attempts=attempts+1, retry_at=? "
                               "WHERE update_id=?", (status, detail,
                                                     time.time() + error.retry_after if retry else 0, row["update_id"]))
                return True
            sent_ids.append(sent["message_id"])
            with self.workshop.connect() as db:
                db.execute("UPDATE telegram_requests SET status=?, sent_ids=?, error=NULL WHERE update_id=?",
                           ("sent" if len(sent_ids) == len(parts) else "ready", json.dumps(sent_ids), row["update_id"]))
        return True

    def history(self):
        with self.workshop.connect() as db:
            rows = db.execute("SELECT * FROM telegram_requests ORDER BY update_id").fetchall()
        records = []
        for row in rows:
            record = dict(row)
            record.update(sender=json.loads(row["sender"]), result=json.loads(row["result"]) if row["result"] else None,
                          sent_ids=json.loads(row["sent_ids"]), parts=json.loads(row["parts"]), chat_id=self.group_id)
            record["message_url"] = (f"https://t.me/c/{str(self.group_id)[4:]}/{row['message_id']}"
                                     if str(self.group_id).startswith("-100") else None)
            records.append(record)
        return records


def split_reply(text):
    parts, current, size = [], [], 0
    for character in text:
        width = len(character.encode("utf-16-le")) // 2
        if size + width > 4000:
            parts.append("".join(current))
            current, size = [], 0
        current.append(character)
        size += width
    if current:
        parts.append("".join(current))
    return parts
