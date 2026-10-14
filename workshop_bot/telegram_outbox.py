from datetime import datetime, timezone

from .service import redact
from .telegram_api import TelegramError


class Outbox:
    def __init__(self, group):
        self.group = group
        self.workshop = group.workshop
        with self.workshop.connect() as db:
            db.execute("CREATE TABLE IF NOT EXISTS telegram_outbox ("
                       "id TEXT PRIMARY KEY, recipient TEXT, username TEXT, body TEXT, text TEXT, "
                       "created TEXT, status TEXT, message_id INTEGER, error TEXT)")

    def register(self, alias, username):
        entry = {"kind": "contact", "key": alias, "value": username,
                 "source": {"channel": "codex", "created": datetime.now(timezone.utc).isoformat()}}
        result = self.workshop.memory.append([entry])
        if result["conflict"]:
            raise ValueError("Для этой роли уже записан другой контакт; сначала разрешите противоречие.")
        return entry

    def send(self, request_id, recipient, body):
        if self.group.identity is None:
            raise ValueError("Сначала требуется проверка выбранной группы.")
        if not request_id.strip() or len(request_id) > 200 or not body.strip():
            raise ValueError("Нужны идентификатор поручения и непустой текст.")
        if redact(body) != body:
            raise ValueError("Сообщение похоже на содержащее ключ или токен; отправка остановлена.")
        with self.workshop.connect() as db:
            # Reserve before sending: a concurrent caller or a crash must not repeat delivery.
            db.execute("BEGIN IMMEDIATE")
            previous = db.execute("SELECT * FROM telegram_outbox WHERE id=?", (request_id,)).fetchone()
            if previous:
                if previous["recipient"] != recipient or previous["body"] != body:
                    raise ValueError("Этот идентификатор уже принадлежит другому сообщению.")
                return self.record(previous)
            username = self.workshop.memory.contact(recipient)
            if not username:
                raise ValueError("Ответственный не указан в памяти бота; отправка остановлена.")
            text = f"{username} · {recipient}\nСообщение от Workshop:\n\n{body}"
            if len(text.encode("utf-16-le")) // 2 > 4000:
                raise ValueError("Сообщение слишком длинное; сократите его перед отправкой.")
            db.execute("INSERT INTO telegram_outbox VALUES (?,?,?,?,?,?,'sending',NULL,NULL)",
                       (request_id, recipient, username, body, text, datetime.now(timezone.utc).isoformat()))
        try:
            sent = self.group.api.call("sendMessage", chat_id=self.group.group_id, text=text,
                                       entities=[{"type": "mention", "offset": 0, "length": len(username)}],
                                       link_preview_options={"is_disabled": True})
            if type(sent.get("message_id")) is not int or sent["message_id"] <= 0 or sent.get("chat", {}).get("id") != self.group.group_id:
                raise TelegramError()
            with self.workshop.connect() as db:
                db.execute("UPDATE telegram_outbox SET status='sent',message_id=? WHERE id=?",
                           (sent["message_id"], request_id))
        except Exception as error:
            definite = isinstance(error, TelegramError) and not error.uncertain
            with self.workshop.connect() as db:
                db.execute("UPDATE telegram_outbox SET status=?,error=? WHERE id=?",
                           ("rejected" if definite else "uncertain", str(error) if isinstance(error, TelegramError)
                            else "Доставка не подтверждена; автоматического повтора нет.", request_id))
        with self.workshop.connect() as db:
            return self.record(db.execute("SELECT * FROM telegram_outbox WHERE id=?", (request_id,)).fetchone())

    def record(self, row):
        result = dict(row)
        if result["status"] == "sending":
            result["status"] = "uncertain"
            result["error"] = "Отправка начата, но подтверждение ещё не сохранено; повтор не выполнен."
        group_id = str(self.group.group_id)
        result["message_url"] = (f"https://t.me/c/{group_id[4:]}/{row['message_id']}"
                                 if row["message_id"] and group_id.startswith("-100") else None)
        return result

    def history(self):
        with self.workshop.connect() as db:
            return [self.record(row) for row in db.execute("SELECT * FROM telegram_outbox ORDER BY rowid")]
