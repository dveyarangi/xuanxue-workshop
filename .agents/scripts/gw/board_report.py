"""Validate and atomically replace the shared review snapshot."""

import argparse
import errno
import hashlib
import json
import os
import re
import tempfile
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path


SECTIONS = ("Reviewed scope", "Results", "Open matters", "Operations")


def initial_report():
    return ("# Board review\n\n- **record of** what happened\n- **Reviewed:** none\n\n"
            "## Reviewed scope\n\nNo full review is recorded in this snapshot.\n\n"
            "## Results\n\nNo new result recorded.\n\n"
            "## Open matters\n\nConsult the original assignments and question store.\n\n"
            "## Operations\n\nNo controller outcome recorded.\n")


def validate(text):
    if not text.startswith("# Board review\n") or "- **record of** what happened" not in text:
        raise ValueError("Invalid board report header")
    matches = re.findall(r"^- \*\*Reviewed:\*\* (.+)$", text, re.M)
    if len(matches) != 1:
        raise ValueError("Board report requires a reviewed timestamp or none")
    stamp_text = matches[0]
    if stamp_text != "none":
        try:
            stamp = datetime.fromisoformat(stamp_text.replace("Z", "+00:00"))
            if stamp.tzinfo is None:
                raise ValueError()
        except ValueError:
            raise ValueError("Board report timestamp requires an explicit timezone") from None
    headings = re.findall(r"^## (.+)$", text, re.M)
    if tuple(headings) != SECTIONS:
        raise ValueError("Board report sections must be: " + ", ".join(SECTIONS))
    parts = re.split(r"^## .+\n", text, flags=re.M)[1:]
    if any(not part.strip() for part in parts):
        raise ValueError("Board report sections cannot be empty")
    return text


def version(path):
    path = Path(path)
    return hashlib.sha256(path.read_bytes()).hexdigest() if path.exists() else "absent"


@contextmanager
def exclusive(path):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a+b") as handle:
        if not path.stat().st_size:
            handle.write(b"0")
            handle.flush()
        handle.seek(0)
        try:
            if os.name == "nt":
                import msvcrt
                msvcrt.locking(handle.fileno(), msvcrt.LK_NBLCK, 1)
            else:
                import fcntl
                fcntl.flock(handle.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        except OSError as error:
            if error.errno not in {errno.EACCES, errno.EAGAIN} and getattr(error, "winerror", None) != 33:
                raise
            raise BlockingIOError("Another board process holds this scope") from error
        try:
            yield
        finally:
            handle.seek(0)
            if os.name == "nt":
                msvcrt.locking(handle.fileno(), msvcrt.LK_UNLCK, 1)
            else:
                fcntl.flock(handle.fileno(), fcntl.LOCK_UN)


def write_report(path, text, *, expected):
    validate(text)
    path = Path(path)
    key = hashlib.sha256(str(path.resolve()).encode()).hexdigest()
    with exclusive(Path(tempfile.gettempdir()) / f"workshop-report-{key}.lock"):
        if version(path) != expected:
            raise ValueError("Board report changed; reread before replacing it")
        path.parent.mkdir(parents=True, exist_ok=True)
        descriptor, temporary = tempfile.mkstemp(prefix=".board-report-", dir=path.parent)
        try:
            with os.fdopen(descriptor, "w", encoding="utf-8", newline="\n") as output:
                output.write(text)
                output.flush()
                os.fsync(output.fileno())
            os.replace(temporary, path)
        finally:
            Path(temporary).unlink(missing_ok=True)
    return version(path)


def operation(path, message):
    path = Path(path)
    before = version(path)
    text = path.read_text(encoding="utf-8") if path.exists() else initial_report()
    validate(text)
    head, previous = text.rsplit("\n## Operations\n", 1)
    if previous.strip().endswith("\n" + message) or previous.strip() == message:
        return False
    now = datetime.now(timezone.utc).isoformat(timespec="seconds")
    write_report(path, head + f"\n## Operations\n\n{now}\n{message}\n", expected=before)
    return True


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("check", "version", "write"))
    parser.add_argument("path", type=Path)
    parser.add_argument("--source", type=Path)
    parser.add_argument("--expected")
    args = parser.parse_args()
    try:
        if args.command == "check":
            validate(args.path.read_text(encoding="utf-8"))
        elif args.command == "write":
            if args.source is None or args.expected is None:
                raise ValueError("Report write requires --source and --expected")
            write_report(args.path, args.source.read_text(encoding="utf-8"), expected=args.expected)
        print(json.dumps({"valid": True, "version": version(args.path)}))
    except (OSError, ValueError) as error:
        print(json.dumps({"valid": False, "error": str(error)}))
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
