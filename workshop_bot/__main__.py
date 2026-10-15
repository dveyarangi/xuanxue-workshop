import argparse
import json
import sqlite3
import sys
import uuid
from pathlib import Path

from .codex import Codex
from .service import Workshop
from .telegram_runtime import configured_group, group_history, serve, setup


def main():
    parser = argparse.ArgumentParser(description="Local Workshop conversation proof")
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--state", type=Path)
    subcommands = parser.add_subparsers(dest="command", required=True)
    ask = subcommands.add_parser("ask")
    ask.add_argument("question")
    ask.add_argument("--target")
    ask.add_argument("--sender", default="operator")
    ask.add_argument("--request-id")
    subcommands.add_parser("history")
    telegram_setup = subcommands.add_parser("telegram-setup")
    telegram_setup.add_argument("--group", type=int)
    telegram = subcommands.add_parser("telegram")
    telegram.add_argument("--once", action="store_true")
    subcommands.add_parser("telegram-history")
    subcommands.add_parser("memory")
    subcommands.add_parser("telegram-outbox")
    send = subcommands.add_parser("telegram-send")
    send.add_argument("--to", required=True, dest="recipient")
    send.add_argument("--message-file", required=True, type=Path)
    send.add_argument("--request-id", required=True)
    args = parser.parse_args()
    state = args.state or args.root / ".local/workshop-bot/history.sqlite3"
    if args.command == "telegram-setup":
        setup(state.parent, args.group)
        return 0
    app = Workshop(args.root, state, Codex(timeout=360, tools_enabled=args.command == "telegram"))
    if args.command == "memory":
        print(app.memory.read_text(encoding="utf-8"))
        return 0
    if args.command in {"telegram-send", "telegram-outbox"}:
        group = configured_group(app, state.parent)
        if args.command == "telegram-outbox":
            result = group.outbox.history()
        else:
            body = args.message_file.read_text(encoding="utf-8-sig")
            group.check_group()
            result = group.outbox.send(args.request_id, args.recipient, body)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 1 if isinstance(result, dict) and result.get("status") in {"rejected", "uncertain"} else 0
    if args.command == "telegram":
        group = configured_group(app, state.parent)
        print("Запускается приём обращений Telegram. Ctrl+C останавливает процесс; история сохраняется.")
        serve(group, once=args.once)
        return 0
    if args.command == "telegram-history":
        print(json.dumps(group_history(app), ensure_ascii=False, indent=2))
        return 0
    if args.command == "history":
        print(json.dumps(app.history(), ensure_ascii=False, indent=2))
        return 0
    request_id = args.request_id or str(uuid.uuid4())
    result = app.ask(request_id, args.question, sender=args.sender, target=args.target)
    print(json.dumps({"request_id": request_id, **result}, ensure_ascii=False, indent=2))
    return 1 if result["status"] in {"failed", "conflict", "uncertain", "not_applied"} else 0


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    try:
        raise SystemExit(main())
    except KeyboardInterrupt:
        print("Остановлено. Состояние сохранено; неподтверждённая отправка будет видна в истории.")
        raise SystemExit(130)
    except (ValueError, RuntimeError, OSError, sqlite3.Error) as error:
        print(str(error) if isinstance(error, (ValueError, RuntimeError)) else
              "Не удалось открыть локальный файл или запустить процесс. Проверьте настройки.", file=sys.stderr)
        raise SystemExit(1)
