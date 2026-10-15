import json
import logging
import threading
import time
from contextlib import contextmanager, nullcontext
from datetime import datetime, timezone
from urllib.parse import parse_qs, urlsplit

from .service import redact
from .telegram_api import TelegramError
from .telegram_outbox import Outbox

TYPING_INTERVAL = 2
logger = logging.getLogger(__name__)


class Group:
    """Retain group discussion while answering only messages addressed to the bot."""

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
            for name in ("reply_to", "conversation_id", "addressed_message_id"):
                if name not in columns:
                    db.execute(f"ALTER TABLE telegram_requests ADD COLUMN {name} INTEGER")
            if "context" not in columns:
                db.execute("ALTER TABLE telegram_requests ADD COLUMN context TEXT")
            if "addressing" not in columns:
                db.execute("ALTER TABLE telegram_requests ADD COLUMN addressing TEXT DEFAULT 'direct'")
            if "reply_context" not in columns:
                db.execute("ALTER TABLE telegram_requests ADD COLUMN reply_context TEXT")
            for name in ("received_at", "started_at", "completed_at", "sent_at"):
                if name not in columns:
                    db.execute(f"ALTER TABLE telegram_requests ADD COLUMN {name} REAL")
            db.execute("UPDATE telegram_requests SET conversation_id=message_id "
                       "WHERE conversation_id IS NULL AND status != 'observed'")
        self.outbox = Outbox(self)
        with self.workshop.connect() as db:
            db.execute("CREATE TABLE IF NOT EXISTS telegram_notices "
                       "(update_id INTEGER PRIMARY KEY, message_id INTEGER, text TEXT, status TEXT, error TEXT)")

    def start(self):
        self.check_group()
        with self.workshop.connect() as db:
            db.execute("UPDATE telegram_notices SET status='uncertain' WHERE status='sending'")
            db.execute("UPDATE telegram_requests SET status='uncertain', error='Подтверждение отправки потеряно.' "
                       "WHERE status='sending'")
            db.execute("UPDATE telegram_requests SET status=CASE WHEN addressing='ambient' THEN 'candidate' "
                       "ELSE 'queued' END WHERE status='processing'")

    def check_group(self):
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
                               "(update_id,message_id,sender,created,body,thread_id,status,reply_to,conversation_id,addressed_message_id,addressing,reply_context,received_at) "
                               "VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",
                               (update["update_id"], selected["message_id"],
                                json.dumps(redact(selected["sender"]), ensure_ascii=False), selected["created"],
                                redact(selected["body"]), selected["thread_id"],
                                "queued" if selected["addressed"] else "candidate" if
                                getattr(self.workshop.agent, "quick_enabled", False) and
                                not selected["body"].startswith("[Сообщение без текста:") else "observed",
                                selected["reply_to"], selected["conversation_id"], selected["addressed_message_id"],
                                "direct" if selected["addressed"] else "ambient",
                                json.dumps(redact(selected["reply_context"]), ensure_ascii=False), time.time()))
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
        if not text:
            kind = next((key for key in ("photo", "video", "voice", "audio", "document", "sticker", "animation",
                                        "video_note", "poll", "contact", "location", "venue") if key in message), "service")
            text = f"[Сообщение без текста: {kind}; содержимое недоступно]"
        entities = message.get("entities", message.get("caption_entities", []))
        references = self.references(text, entities)
        reply = message.get("reply_to_message", {})
        reply_to = reply.get("message_id")
        parent = None
        if reply_to is not None:
            with self.workshop.connect() as db:
                parent = db.execute("SELECT * FROM telegram_requests WHERE EXISTS "
                                    "(SELECT 1 FROM json_each(sent_ids) WHERE value=?)", (reply_to,)).fetchone()
                if parent is None:
                    parent = db.execute("SELECT r.* FROM telegram_requests r JOIN telegram_notices n "
                                        "ON n.update_id=r.update_id WHERE n.status='sent' AND n.message_id=?",
                                        (reply_to,)).fetchone()
                if parent is None:
                    parent = db.execute("SELECT message_id AS conversation_id FROM telegram_outbox "
                                        "WHERE status='sent' AND message_id=?", (reply_to,)).fetchone()
        reply_to_bot = reply.get("from", {}).get("id") == self.identity["id"] and reply.get("from", {}).get("is_bot")
        addressed = bool(references) or parent is not None or bool(reply_to_bot)
        remaining = text
        for reference in references:
            remaining = remaining.replace(reference, "", 1)
        selected = {"message_id": message["message_id"], "body": text,
                "addressed": addressed, "reply_to": reply_to,
                "conversation_id": (parent["conversation_id"] or reply_to) if parent else reply_to if reply_to_bot else message["message_id"],
                "reply_context": {"message_id": reply_to, "role": "assistant" if reply_to_bot else "user",
                                  "sender": {"id": reply.get("from", {}).get("id")},
                                  "text": reply.get("text", reply.get("caption", ""))[:20000]} if reply_to else None,
                "bare": bool(references) and not remaining.strip(" \t\r\n,.;:!?—-"),
                "sender": {k: v for k, v in message.get("sender_chat", message.get("from", {})).items()
                           if k in {"id", "first_name", "last_name", "username", "title", "type"}},
                "created": datetime.fromtimestamp(message["date"], timezone.utc).isoformat(),
                "thread_id": message.get("message_thread_id"), "addressed_message_id": None}
        if selected["bare"] and reply_to is None:
            previous = self.previous_message(selected)
            if previous:
                selected["conversation_id"] = previous["conversation_id"] or previous["message_id"]
                if previous["status"] in {"observed", "candidate"}:
                    selected["addressed_message_id"] = previous["message_id"]
        return selected

    def previous_message(self, selected):
        sender = selected["sender"]
        if sender.get("id") is None:
            return None
        with self.workshop.connect() as db:
            rows = db.execute(
                "SELECT * FROM telegram_requests WHERE message_id < ? AND thread_id IS ? "
                "AND json_extract(sender,'$.id')=? AND COALESCE(json_extract(sender,'$.type'),'')=? "
                "ORDER BY message_id DESC",
                (selected["message_id"], selected["thread_id"], sender["id"], sender.get("type", "")))
            for previous in rows:
                # Older receivers stored this canned invitation as an answered request.
                legacy = {"status": "answered", "answer": "Задайте вопрос о проектах Workshop — помогу разобраться.",
                          "sources": []}
                if previous["addressed_message_id"] is None and previous["result"] and json.loads(previous["result"]) == legacy:
                    continue
                if previous["body"].startswith("[Сообщение без текста:"):
                    return None
                return previous
        return None

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
            row = db.execute("SELECT * FROM telegram_requests WHERE status IN ('queued','ready','candidate') "
                             "ORDER BY CASE WHEN status='candidate' THEN 1 ELSE 0 END, update_id LIMIT 1").fetchone()
            if row is None:
                return False
            if row["retry_at"] > time.time():
                return False
            if row["status"] == "candidate" and db.execute(
                    "SELECT 1 FROM telegram_requests WHERE addressed_message_id=? OR "
                    "(reply_to=? AND addressing='direct') LIMIT 1", (row["message_id"], row["message_id"])).fetchone():
                db.execute("UPDATE telegram_requests SET status='observed' WHERE update_id=?", (row["update_id"],))
                return True
            if row["status"] in {"queued", "candidate"}:
                context = json.loads(row["context"]) if row["context"] else self.conversation(row)
                db.execute("UPDATE telegram_requests SET status='processing', context=?,started_at=? WHERE update_id=?",
                           (json.dumps(context, ensure_ascii=False), time.time(), row["update_id"]))
        if row["status"] in {"queued", "candidate"}:
            question = context.get("addressed_message", {}).get("text", row["body"])
            with self.typing(row) if row["addressing"] == "direct" else nullcontext():
                result = self.workshop.ask(f"telegram:{self.identity['id']}:{self.group_id}:{row['message_id']}",
                                           question, sender=row["sender"], conversation=context,
                                           on_progress=lambda text: self.notice(row, text))
            if result["status"] == "ignored" or (row["addressing"] == "ambient" and result["status"] != "offered"):
                with self.workshop.connect() as db:
                    db.execute("UPDATE telegram_requests SET status='observed',result=?,completed_at=? WHERE update_id=?",
                               (json.dumps(result, ensure_ascii=False), time.time(), row["update_id"]))
                return True
            text = result["answer"]
            parts = split_reply(text)
            with self.workshop.connect() as db:
                db.execute("UPDATE telegram_requests SET status='ready', result=?, parts=?,completed_at=? WHERE update_id=?",
                           (json.dumps(result, ensure_ascii=False), json.dumps(parts, ensure_ascii=False), time.time(), row["update_id"]))
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
                db.execute("UPDATE telegram_requests SET status=?, sent_ids=?, error=NULL,sent_at=? WHERE update_id=?",
                           ("sent" if len(sent_ids) == len(parts) else "ready", json.dumps(sent_ids),
                            time.time() if len(sent_ids) == len(parts) else None, row["update_id"]))
        return True

    @contextmanager
    def typing(self, row):
        parameters = {"chat_id": self.group_id, "action": "typing"}
        if row["thread_id"] is not None:
            parameters["message_thread_id"] = row["thread_id"]
        stop = threading.Event()

        def indicate():
            started = time.monotonic()
            try:
                self.api.call("sendChatAction", **parameters)
            except TelegramError as error:
                logger.warning("typing message=%s result=failed code=%s retry_after=%s",
                               row["message_id"], error.code, error.retry_after)
                if error.retry_after:
                    return max(TYPING_INTERVAL, error.retry_after)
            except Exception:
                logger.warning("typing message=%s result=failed code=unknown", row["message_id"])
            else:
                logger.info("typing message=%s result=accepted duration_ms=%d", row["message_id"],
                            round((time.monotonic() - started) * 1000))
            return max(0, TYPING_INTERVAL - (time.monotonic() - started))

        delay = indicate()

        def renew():
            interval = delay
            while not stop.wait(interval):
                interval = indicate()

        worker = threading.Thread(target=renew, name="telegram-typing", daemon=True)
        worker.start()
        try:
            yield
        finally:
            stop.set()
            worker.join()

    def notice(self, row, text):
        with self.workshop.connect() as db:
            inserted = db.execute("INSERT OR IGNORE INTO telegram_notices VALUES (?,NULL,?,'sending',NULL)",
                                  (row["update_id"], text)).rowcount
        if not inserted:
            return
        parameters = {"chat_id": self.group_id, "text": text,
                      "reply_parameters": {"message_id": row["message_id"]},
                      "link_preview_options": {"is_disabled": True}}
        if row["thread_id"] is not None:
            parameters["message_thread_id"] = row["thread_id"]
        try:
            sent = self.api.call("sendMessage", **parameters)
            if type(sent.get("message_id")) is not int or sent.get("chat", {}).get("id") != self.group_id:
                raise TelegramError()
            with self.workshop.connect() as db:
                db.execute("UPDATE telegram_notices SET message_id=?,status='sent' WHERE update_id=?",
                           (sent["message_id"], row["update_id"]))
        except Exception as error:
            with self.workshop.connect() as db:
                db.execute("UPDATE telegram_notices SET status=?,error=? WHERE update_id=?",
                           ("rejected" if isinstance(error, TelegramError) and not error.uncertain else "uncertain",
                            str(error) if isinstance(error, TelegramError) else "Notice delivery unconfirmed", row["update_id"]))

    def conversation(self, request):
        with self.workshop.connect() as db:
            rows = db.execute("SELECT * FROM telegram_requests WHERE message_id < ? ORDER BY message_id",
                              (request["message_id"],)).fetchall()
            outgoing = db.execute("SELECT * FROM telegram_outbox WHERE status='sent' AND message_id < ?",
                                  (request["message_id"],)).fetchall()
            notices = db.execute("SELECT n.*,r.message_id AS reply_to,r.conversation_id,r.thread_id "
                                 "FROM telegram_notices n JOIN telegram_requests r ON r.update_id=n.update_id "
                                 "WHERE n.status='sent' AND n.message_id < ?", (request["message_id"],)).fetchall()
        messages = [{"message_id": row["message_id"], "role": "assistant", "text": row["text"],
                     "created": row["created"], "conversation_id": row["message_id"],
                     "recipient": row["recipient"]} for row in outgoing]
        messages.extend({"message_id": n["message_id"], "role": "assistant", "text": n["text"],
                         "reply_to": n["reply_to"], "conversation_id": n["conversation_id"],
                         "thread_id": n["thread_id"]} for n in notices)
        for row in rows:
            messages.append({"message_id": row["message_id"], "role": "user", "text": row["body"],
                             "sender": json.loads(row["sender"]), "created": row["created"],
                             "thread_id": row["thread_id"], "reply_to": row["reply_to"],
                             "conversation_id": row["conversation_id"], "request_status": row["status"]})
            for message_id, part in zip(json.loads(row["sent_ids"]), json.loads(row["parts"])):
                if message_id < request["message_id"]:
                    messages.append({"message_id": message_id, "role": "assistant", "text": part,
                                     "reply_to": row["message_id"], "thread_id": row["thread_id"],
                                     "conversation_id": row["conversation_id"]})
        messages.sort(key=lambda message: message["message_id"])
        quoted = json.loads(request["reply_context"]) if request["reply_context"] else None
        if quoted and not any(m["message_id"] == quoted["message_id"] for m in messages):
            messages.append(quoted)
            messages.sort(key=lambda message: message["message_id"])
        anchors = {request["reply_to"], request["conversation_id"]}
        priority = [m for m in messages if m["message_id"] in anchors]
        recent = [m for m in reversed(messages) if m["message_id"] not in anchors]
        selected, size = [], 2
        for message in priority + recent:
            length = len(json.dumps(message, ensure_ascii=False).encode("utf-8")) + 2
            if size + length > 120_000:
                continue
            selected.append(message)
            size += length
        selected.sort(key=lambda message: message["message_id"])
        result = {"chat_id": self.group_id, "messages": selected, "omitted_messages": len(messages) - len(selected),
                "scope": "Received group text/captions and confirmed bot replies; no pre-collection archive, "
                         "attachment contents or messages Telegram did not deliver.",
                "current": {"message_id": request["message_id"], "sender": json.loads(request["sender"]),
                            "created": request["created"], "thread_id": request["thread_id"],
                            "reply_to": request["reply_to"], "conversation_id": request["conversation_id"],
                            "addressing": request["addressing"]}}
        if request["addressed_message_id"] is not None:
            result["addressed_message"] = next(m for m in messages if m["message_id"] == request["addressed_message_id"])
        return result

    def history(self):
        with self.workshop.connect() as db:
            rows = db.execute("SELECT * FROM telegram_requests ORDER BY update_id").fetchall()
            notices = {row["update_id"]: dict(row) for row in db.execute("SELECT * FROM telegram_notices")}
        records = []
        for row in rows:
            record = dict(row)
            record["notice"] = notices.get(row["update_id"])
            record.update(sender=json.loads(row["sender"]), result=json.loads(row["result"]) if row["result"] else None,
                          sent_ids=json.loads(row["sent_ids"]), parts=json.loads(row["parts"]), chat_id=self.group_id,
                          context=json.loads(row["context"]) if row["context"] else None)
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
