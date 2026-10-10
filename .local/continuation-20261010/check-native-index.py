from pathlib import Path, PurePosixPath
import hashlib
import json
import posixpath
import re
import subprocess
from urllib.parse import unquote, urlsplit

root = Path(__file__).resolve().parents[2]
out = root / '.local/continuation-20261010/commit-package'
paths = json.loads((out / 'paths.json').read_text(encoding='utf-8'))

def git(*args):
    return subprocess.run(['git', *args], cwd=root, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE, check=True).stdout

cache = {}
def indexed(path):
    if path not in cache:
        cache[path] = git('show', ':' + path).decode('utf-8')
    return cache[path]

actual = git('diff', '--cached', '--name-only').decode().splitlines()
assert set(actual) == set(paths), 'Index contains unexpected or missing files'
assert all(p.startswith('docs/') for p in actual)
errors = []
links = 0
for p in paths:
    source = indexed(p)
    for href in re.findall(r'\[[^\]]*\]\(([^\s)]+)\)', source):
        href = href.strip('<>')
        parsed = urlsplit(href)
        if parsed.scheme or href.startswith('//'):
            continue
        target = posixpath.normpath(posixpath.join(str(PurePosixPath(p).parent), unquote(parsed.path))) if parsed.path else p
        links += 1
        try:
            content = indexed(target)
        except subprocess.CalledProcessError:
            errors.append(f'{p}: missing indexed target {href}')
            continue
        if parsed.fragment:
            anchors = set()
            for title in re.findall(r'^#{1,6}\s+(.+?)\s*#*$', content, re.M):
                title = re.sub(r'<[^>]+>', '', title).lower()
                anchors.add(re.sub(r'[^\w\- ]', '', title).replace(' ', '-'))
            anchors.update(re.findall(r'id=["\']([^"\']+)', content))
            if unquote(parsed.fragment) not in anchors:
                errors.append(f'{p}: missing indexed anchor {href}')

contract = indexed('docs/contracts/native-account-session.md')
examples = re.findall(r'```json\s*\n(.*?)\n```', contract, re.S)
for example in examples:
    json.loads(example)
assert len(examples) == 2
assert set(re.findall(r'^\| (N\d{2}) \|', contract, re.M)) == {f'N{i:02}' for i in range(1, 18)}
for p in ('docs/assignments/native-session-cabinet.draft.md', 'docs/assignments/native-session-daychi.draft.md'):
    assert 'homeHiddenTiles' in indexed(p)
    assert '**Draft — not issued.**' in indexed(p)
    assert '../contracts/native-account-session.md' in indexed(p)

manifest = json.loads((out / 'untouched-worktree.json').read_text(encoding='utf-8'))
for p, digest in manifest.items():
    if hashlib.sha256((root / p).read_bytes()).hexdigest() != digest:
        errors.append(f'Unrelated worktree changed: {p}')
result = {'files': len(paths), 'local_links': links, 'json_examples': len(examples),
          'common_cases': 17, 'unrelated_files_preserved': len(manifest), 'errors': errors}
(out / 'index-check.json').write_text(json.dumps(result, indent=2), encoding='utf-8')
print(json.dumps(result, indent=2))
if errors:
    raise SystemExit(1)
