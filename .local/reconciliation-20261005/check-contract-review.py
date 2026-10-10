"""Check literal examples and links in the local contract review; no app proof."""

import json
import re
from datetime import datetime
from pathlib import Path

root = Path(__file__).resolve().parents[2]
review = root / "docs/contracts/public-lessons.md"
text = review.read_text(encoding="utf-8")

def instant(value):
    return datetime.fromisoformat(value.replace("Z", "+00:00"))

start = instant("2026-10-05T00:00:00+03:00")
end = instant("2026-10-19T00:00:00+03:00")
assert start == instant("2026-10-04T21:00:00Z")
assert end == instant("2026-10-18T21:00:00Z")
rows = re.findall(r"\| `(00[1-6])` \| `([^`]+)` \| (Included|Excluded)", text)
assert len(rows) == 6
assert [key for key, value, expected in rows if start <= instant(value) < end] == ["002", "003", "004", "005"]
for key, value, expected in rows:
    assert (start <= instant(value) < end) == (expected == "Included"), key

sample = json.loads(re.search(r"```json\s*(.*?)\s*```", text, re.S).group(1))
assert set(sample) == {"id", "classId", "startsAt", "durationMin", "classTitle", "groupLabel", "format", "topic", "status", "tags"}
assert len(sample["id"]) == len(sample["classId"]) == 24
assert start <= instant(sample["startsAt"]) < end
assert sample["startsAt"].endswith("Z")
assert sample["format"] in {"online", "offline", "both"}
assert sample["status"] in {"scheduled", "cancelled"}
assert isinstance(sample["tags"], list)
assert not any("zoom" in key.lower() or "password" in key.lower() for key in sample)
assert [key for key, _, expected in rows if expected == "Included"] == ["002", "003", "004", "005"]

move_within = instant("2026-10-07T15:00:00Z")
move_outside = instant("2026-10-20T15:00:00Z")
assert start <= move_within < end
assert instant("2026-10-06T16:00:00Z") < move_within < instant("2026-10-18T20:59:59Z")
assert not start <= move_outside < end

dst_start = instant("2024-10-20T00:00:00+03:00")
dst_end = instant("2024-11-03T00:00:00+02:00")
assert dst_start == instant("2024-10-19T21:00:00Z")
assert dst_end == instant("2024-11-02T22:00:00Z")
assert (dst_end.date() - dst_start.date()).days == 14
assert (dst_end - dst_start).total_seconds() == 337 * 3600

questions = list((root / "docs/questions").rglob("q-0002.0007.0005-what-is-the-exact-public-schedule-contract-for-the-cabinet-daychi-pilot.md"))
assert len(questions) == 1
files = [review, root / "docs/boundaries.md", questions[0], Path(__file__).with_name("participant-reconciliation-plan.md"), Path(__file__).with_name("public-lessons-contract-review.md")]
links = 0
for file in files:
    content = file.read_text(encoding="utf-8")
    for target in re.findall(r"\]\(([^)]+)\)", content):
        if "://" in target or target.startswith("#"):
            continue
        path = target.split("#", 1)[0]
        assert (file.parent / path).resolve().exists(), (file, target)
        links += 1
print(f"PASS: literal interval/move/response/DST examples; {links} local links across {len(files)} files. No application checks run.")
