import json
import os
import re
import tempfile
from pathlib import Path

from .records import exclusive_record


class Memory:
    def __init__(self, path):
        self.path = Path(path).absolute()

    def read(self):
        if self.path.is_symlink() or self.path.is_junction():
            raise ValueError("Файл памяти не может быть ссылкой.")
        if not self.path.exists():
            return []
        raw = self.path.read_bytes()
        if len(raw) > 250_000:
            raise ValueError("Файл памяти превышает поддерживаемый размер.")
        data = json.loads(raw)
        if not isinstance(data, dict) or data.get("version") != 1 or not isinstance(data.get("entries"), list):
            raise ValueError("Неизвестный формат памяти бота.")
        for entry in data["entries"]:
            self.validate(entry)
        return data["entries"]

    def contact(self, alias):
        return next((entry["value"] for entry in self.read()
                     if entry["kind"] == "contact" and entry["key"] == alias), None)

    def append(self, entries):
        for entry in entries:
            self.validate(entry)
        lock = self.path.with_suffix(".lock")
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with lock.open("ab"):
            pass
        with exclusive_record(lock):
            existing = self.read()
            added = []
            for entry in entries:
                previous = next((item for item in existing + added
                                 if (item["kind"], item["key"]) == (entry["kind"], entry["key"])), None)
                if previous and previous["value"] != entry["value"]:
                    return {"added": [], "conflict": {"previous": previous, "proposed": entry}}
                if not previous:
                    added.append(entry)
            if added:
                raw = json.dumps({"version": 1, "entries": existing + added}, ensure_ascii=False, indent=2).encode("utf-8")
                if len(raw) > 250_000:
                    raise ValueError("Файл памяти заполнен; новые сведения не записаны.")
                temporary = None
                try:
                    with tempfile.NamedTemporaryFile(dir=self.path.parent, delete=False) as stream:
                        temporary = Path(stream.name)
                        stream.write(raw)
                        stream.flush()
                        os.fsync(stream.fileno())
                    temporary.replace(self.path)
                finally:
                    if temporary and temporary.exists():
                        temporary.unlink()
            return {"added": added, "conflict": None}

    @staticmethod
    def validate(entry):
        if not isinstance(entry, dict) or set(entry) != {"kind", "key", "value", "source"}:
            raise ValueError("Некорректная запись памяти.")
        if entry["kind"] not in {"contact", "fact"} or not isinstance(entry["source"], dict):
            raise ValueError("Некорректный вид или источник записи памяти.")
        if not all(isinstance(entry[key], str) and entry[key].strip() for key in ("key", "value")):
            raise ValueError("Запись памяти не может быть пустой.")
        if len(entry["key"]) > 100 or len(entry["value"]) > 2000:
            raise ValueError("Запись памяти слишком длинная.")
        if entry["kind"] == "contact" and (not re.fullmatch(r"[a-z][a-z0-9_-]{0,63}", entry["key"]) or
                                           not re.fullmatch(r"@[A-Za-z][A-Za-z0-9_]{4,31}", entry["value"])):
            raise ValueError("Для контакта нужны короткое имя роли и точное Telegram @username.")
