import getpass
import json
import threading
from contextlib import contextmanager
from pathlib import Path

from .records import exclusive_record
from .telegram import Group
from .telegram_api import TelegramAPI, TelegramError


@contextmanager
def receiver_lease(state):
    path = Path(str(state) + ".telegram.lock").resolve()
    path.parent.mkdir(parents=True, exist_ok=True)
    try:
        with path.open("ab"):
            pass
    except OSError:
        raise RuntimeError("Приёмник для этой истории уже работает или каталог недоступен.") from None
    with exclusive_record(path):
        yield


def serve(group, *, once=False, stop=None):
    stop = stop or threading.Event()
    with receiver_lease(group.workshop.state):
        group.start()
        if once:
            group.poll_once(timeout=0)
            while group.work_once():
                pass
            return
        failures = []

        def receive():
            consecutive_errors = 0
            while not stop.is_set():
                try:
                    received = group.poll_once()
                    consecutive_errors = 0
                    if not received:
                        stop.wait(0.25)
                except TelegramError as error:
                    consecutive_errors += 1
                    if error.code in {401, 403, 409} or consecutive_errors >= 3:
                        failures.append(error)
                        stop.set()
                        return
                    stop.wait(max(error.retry_after, min(2 ** consecutive_errors, 30)))
                except Exception:
                    failures.append(RuntimeError("Приём сообщений остановлен; сохранённая очередь остаётся в истории."))
                    stop.set()

        receiver = threading.Thread(target=receive, name="telegram-receiver")
        receiver.start()
        try:
            while not stop.is_set():
                if not group.work_once():
                    stop.wait(0.25)
        finally:
            stop.set()
            receiver.join()
        if failures:
            raise failures[0]


def setup(directory, group_id=None):
    directory = Path(directory).resolve()
    directory.mkdir(parents=True, exist_ok=True)
    token_file = directory / "telegram.token"
    if token_file.exists():
        token = token_file.read_text(encoding="utf-8").strip()
    else:
        token = getpass.getpass("Токен BotFather (ввод скрыт): ").strip()
    api = TelegramAPI(token)
    identity = api.call("getMe")
    if api.call("getWebhookInfo").get("url"):
        raise ValueError("У бота уже настроен webhook; настройка остановлена без изменения получателя.")
    print(f"Бот: @{identity['username']}")
    if group_id is None:
        chats = {}
        for update in api.call("getUpdates", timeout=0, allowed_updates=["message"]):
            chat = update.get("message", {}).get("chat", {})
            if chat.get("type") in {"group", "supergroup"}:
                chats[chat["id"]] = chat.get("title", "Группа")
        if not chats:
            raise ValueError("Группа не найдена. Добавьте бота, напишите в группе /start@имя_бота и повторите настройку.")
        for chat_id, title in chats.items():
            print(f"{chat_id}: {title}")
        group_id = int(input("Идентификатор нужной группы из списка: "))
        if group_id not in chats:
            raise ValueError("Выбрана группа не из списка.")
    chat = api.call("getChat", chat_id=group_id)
    if chat.get("id") != group_id or chat.get("type") not in {"group", "supergroup"}:
        raise ValueError("Выбранный чат не является группой.")
    token_file.write_text(token, encoding="utf-8")
    (directory / "telegram.json").write_text(json.dumps({"group_id": group_id}, indent=2), encoding="utf-8")
    print("Локальные настройки сохранены. Токен не выводится и не передаётся Codex.")


def configured_group(workshop, directory):
    directory = Path(directory)
    try:
        config = json.loads((directory / "telegram.json").read_text(encoding="utf-8"))
        token = (directory / "telegram.token").read_text(encoding="utf-8").strip()
        group_id = config["group_id"]
    except (OSError, ValueError, KeyError):
        raise ValueError("Нет локальных настроек Telegram. Сначала выполните telegram-setup.") from None
    if not isinstance(group_id, int) or group_id >= 0:
        raise ValueError("В настройках нужен отрицательный числовой идентификатор группы.")
    return Group(workshop, TelegramAPI(token), group_id)


def group_history(workshop):
    with workshop.connect() as db:
        exists = db.execute("SELECT name FROM sqlite_master WHERE name='telegram_meta'").fetchone()
        binding = db.execute("SELECT value FROM telegram_meta WHERE key='binding'").fetchone() if exists else None
    if not binding:
        return []
    return Group(workshop, None, json.loads(binding[0])[1]).history()
