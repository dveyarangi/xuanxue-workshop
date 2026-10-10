import base64
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
PATHS = [
    "docs/agent-contract.md", "docs/contracts/native-account-session.md",
    "docs/assignments/native-session-cabinet.draft.md",
    "docs/assignments/native-session-daychi.draft.md", "docs/current-system.md",
    "docs/mechanisms/coordinate.evidence.md", "docs/rule-failures.md",
    "docs/tickets/01-0008-native-cabinet-account-session.md", "docs/tickets/README.md",
    "docs/questions/q-0002.0008.0001.0002-how-will-native-daychi-maintain-a-cabinet-account-session-without-replacing-its-content-access.md",
]
errors = []
link_count = 0

def check_link(origin, href):
    global link_count
    parsed = urlsplit(href.strip("<>"))
    candidate = "https://github.com/dveyarangi/xuanxue-workshop/blob/__CONTRACT_REVISION__/"
    if href.startswith(candidate):
        target = ROOT / unquote(parsed.path.split("/__CONTRACT_REVISION__/", 1)[1])
    elif parsed.scheme or href.startswith("//"):
        return
    else:
        target = (origin.parent / unquote(parsed.path)).resolve() if parsed.path else origin
    link_count += 1
    if not target.is_file():
        errors.append(f"{origin.relative_to(ROOT)}: missing {href}")
        return
    if parsed.fragment:
        content = target.read_text(encoding="utf-8")
        anchors = set()
        for heading in re.findall(r"^#{1,6}\s+(.+?)\s*#*$", content, re.M):
            heading = re.sub(r"<[^>]+>", "", heading).lower()
            anchors.add(re.sub(r"[^\w\- ]", "", heading).replace(" ", "-"))
        anchors.update(re.findall(r'''id=["']([^"']+)''', content))
        if unquote(parsed.fragment) not in anchors:
            errors.append(f"{origin.relative_to(ROOT)}: missing anchor {href}")

for path in [ROOT / p for p in PATHS] + [OUT / "issue-7.body.md", OUT / "issue-8.body.md"]:
    for href in re.findall(r"\[[^\]]*\]\(([^\s)]+)\)", path.read_text(encoding="utf-8")):
        check_link(path, href)

contract = (ROOT / "docs/contracts/native-account-session.md").read_text(encoding="utf-8")
examples = [json.loads(x) for x in re.findall(r"```json\s*\n(.*?)\n```", contract, re.S)]
assert len(examples) == 2
token = examples[0]["access_token"]
assert re.fullmatch(r"[A-Za-z0-9_-]{43}", token)
assert len(base64.urlsafe_b64decode(token + "=")) == 32
assert examples[0]["expires_in"] == 90 * 24 * 3600
assert examples[0]["renew_after"] == 7 * 24 * 3600 + 1
fields = set(re.findall(r"^\| `([^`]+)` \|", contract.split("| Account field |", 1)[1].split("All fields except", 1)[0], re.M))
assert set(examples[1]["account"]) == fields and len(fields) == 15
cases = set(re.findall(r"^\| (N\d{2}) \|", contract, re.M))
assert cases == {f"N{i:02}" for i in range(1, 18)}
verifier = "dBjftJeZ4CVP-mB92K27uhbUJU1p1r_wW1gFWFOEjXk"
challenge = base64.urlsafe_b64encode(hashlib.sha256(verifier.encode("ascii")).digest()).decode().rstrip("=")
assert challenge == "E9Melhoa2OwvFrEMTJguCHaoeK1t8URWbuGJSstw-cM" and challenge in contract

manifest = json.loads((OUT / "review-manifest.json").read_text(encoding="utf-8"))
for name, digest in manifest["files"].items():
    assert hashlib.sha256((OUT / name).read_bytes()).hexdigest() == digest
assert (OUT / "contract.review.md.snapshot").read_bytes() == (ROOT / "docs/contracts/native-account-session.md").read_bytes()
for number, counterpart in [(7, 8), (8, 7)]:
    body = (OUT / f"issue-{number}.body.md").read_text(encoding="utf-8")
    assert "__CONTRACT_REVISION__" in body and "/blob/HEAD/" not in body
    assert f"https://github.com/dveyarangi/xuanxue-workshop/issues/{counterpart}" in body
    assert "homeHiddenTiles" in body and "/login/native" in body
    assert "Shared contract revision: `__CONTRACT_REVISION__`" in body
    assert "b8ab296e2713580eb4b91155b0c333ea758a74ce" not in body

result = {"documents": len(PATHS), "issue_bodies": 2, "resolving_package_links": link_count,
          "json_examples": len(examples), "account_fields": len(fields), "common_cases": len(cases),
          "pkce_vector": "passed", "review_snapshot": "matches current contract", "errors": errors}
(OUT / "package-check.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(bool(errors))
