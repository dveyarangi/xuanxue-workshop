from pathlib import Path
import json
import sys
import re
from collections import defaultdict
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / '.agents/scripts/gw'))
from docs_corpus import citations, target_of, cited_record, corpus

files = [p for p in corpus(ROOT) if p.endswith('.md') and not p.startswith('.local/')]
missing = []
local_count = 0
portable = []
anchors = []
remote = defaultdict(set)
def headings(body):
    found = set()
    repeated = defaultdict(int)
    in_fence = False
    for line in body.splitlines():
        if re.match(r'^\s*(```|~~~)', line):
            in_fence = not in_fence
        if in_fence or not re.match(r'^#{1,6} ', line):
            continue
        title = re.sub(r'^#+\s+', '', line).strip().lower()
        title = re.sub(r'[^\w\- ]', '', title).replace(' ', '-')
        slug = title if not repeated[title] else f'{title}-{repeated[title]}'
        repeated[title] += 1
        found.add(slug)
    return found
for name in files:
    body = (ROOT / name).read_text(encoding='utf-8')
    for written in citations(body):
        target = target_of(written)
        if written == 'COLLABORATE_SKILL_PATH':
            continue  # Explicit installation template, replaced by the recipient.
        dest = cited_record(ROOT, name, target)
        if dest:
            local_count += 1
            if not (ROOT / dest).exists():
                missing.append({'file': name, 'link': written, 'target': dest})
            elif target.fragment and (ROOT / dest).suffix == '.md':
                if unquote(target.fragment[1:]) not in headings((ROOT / dest).read_text(encoding='utf-8')):
                    anchors.append({'file': name, 'link': written, 'target': dest})
        match = re.match(r'https://github.com/([^/]+/[^/]+)/blob/([^/]+)/([^#]+)', written)
        if match:
            repo, ref, path = match.groups()
            remote[f'{repo}@{ref}'].add(unquote(path))
        if name.startswith('skills/collaborate/') and not target.elsewhere and target.path:
            if Path(target.path).name not in {'SKILL.md', 'workshop-issue-format.md'}:
                portable.append({'file': name, 'link': written})
print(json.dumps({'files': len(files), 'local_links': local_count, 'missing': missing,
                  'anchor_candidates': anchors, 'non_companion_install_links': portable,
                  'remote_source_groups': {k: sorted(v) for k, v in remote.items()}}, indent=2))
published = (ROOT / '.local/maintenance-20261006/published-public-lessons.md').read_text(encoding='utf-8')
current = (ROOT / 'docs/contracts/public-lessons.md').read_text(encoding='utf-8')
assert current.rstrip('\n') == published.rstrip('\n'), 'Published contract differs'
assert not missing and not anchors and not portable, 'Unresolved local/installation reference'
