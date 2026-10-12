import argparse
import json
import sys
import uuid
from pathlib import Path

from .codex import Codex
from .service import Workshop


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
    args = parser.parse_args()
    state = args.state or args.root / ".local/workshop-bot/history.sqlite3"
    app = Workshop(args.root, state, Codex())
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
    raise SystemExit(main())
