import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
REV = "__CONTRACT_REVISION__"
BASE = f"https://github.com/dveyarangi/xuanxue-workshop/blob/{REV}/"
contract = ROOT / "docs/contracts/native-account-session.md"
snapshot = OUT / "contract.review.md.snapshot"
snapshot.write_bytes(contract.read_bytes())

for project, number, other in [("cabinet", 7, 8), ("daychi", 8, 7)]:
    source = ROOT / f"docs/assignments/native-session-{project}.draft.md"
    body = source.read_text(encoding="utf-8").split("## Recipient and outcome", 1)[1]
    body = "## Recipient and outcome" + body

    def absolute_link(match):
        target = match.group(2)
        if target.startswith(("https://", "http://", "#")):
            return match.group(0)
        path, separator, anchor = target.partition("#")
        resolved = (source.parent / path).resolve().relative_to(ROOT).as_posix()
        return f"[{match.group(1)}]({BASE}{resolved}{separator}{anchor})"

    body = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", absolute_link, body)
    counterpart = "Consumer" if project == "cabinet" else "Provider"
    header = (
        "Accepted native account-session implementation assignment, including the "
        "2026-10-10 security and browser-continuation amendment.\n\n"
        f"Prepared within [01-0008-native-cabinet-account-session]({BASE}docs/tickets/01-0008-native-cabinet-account-session.md).\n"
        f"Shared contract revision: `{REV}`.\n\n"
        f"{counterpart} contribution: [native account-session #{other}]"
        f"(https://github.com/dveyarangi/xuanxue-workshop/issues/{other}).\n\n"
    )
    (OUT / f"issue-{number}.body.md").write_text(header + body, encoding="utf-8")

files = [snapshot, OUT / "issue-7.body.md", OUT / "issue-8.body.md"]
manifest = {
    "stage": "prepared, not published",
    "authority": str(snapshot.relative_to(ROOT)).replace("\\", "/"),
    "revision_placeholder": REV,
    "publication_condition": "one full committed, accessible Workshop revision in both bodies",
    "files": {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in files},
}
(OUT / "review-manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
print(json.dumps(manifest, indent=2))
