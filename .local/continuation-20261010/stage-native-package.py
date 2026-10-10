from pathlib import Path
import difflib
import hashlib
import json
import subprocess

root = Path(__file__).resolve().parents[2]
out = root / '.local/continuation-20261010/commit-package'
out.mkdir(exist_ok=True)

def git(*args, data=None):
    return subprocess.run(['git', *args], cwd=root, input=data,
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                          check=True).stdout

def head(path):
    return git('show', 'HEAD:' + path).decode('utf-8')

def work(path):
    return (root / path).read_text(encoding='utf-8')

if git('diff', '--cached', '--name-only').strip():
    raise SystemExit('Refusing to modify a nonempty existing index')

full = [
    'docs/contracts/native-account-session.md',
    'docs/assignments/native-session-cabinet.draft.md',
    'docs/assignments/native-session-daychi.draft.md',
    'docs/tickets/01-0008-native-cabinet-account-session.md',
    'docs/questions/q-0002.0008.0001.0002-how-will-native-daychi-maintain-a-cabinet-account-session-without-replacing-its-content-access.md',
    'docs/boundaries.md',
    'docs/migration-changes.md',
    'docs/questions/q-0002.0008.0001-how-will-daychi-clients-obtain-and-present-cabinet-credentials.md',
    'docs/questions/q-0002.0008.0001.0001-which-authentication-standard-should-cabinet-and-daychi-adopt.md',
    'docs/questions/q-0002.0010-should-clients-reach-cabinet-and-daychi-through-a-shared-gateway.md',
    'docs/questions/q-0002.0002.0002-which-workshop-outcomes-should-the-remaining-reconciliation-pass-deliver.md',
]
contents = {p: work(p) for p in full}

p = 'docs/architecture.md'
before = head(p)
old = next(line for line in before.splitlines() if line.startswith('- [Gateway]'))
new = next(line for line in work(p).splitlines() if line.startswith('- [Gateway]'))
contents[p] = before.replace(old, new)

p = 'docs/tickets/README.md'
before = head(p)
before = before.replace('**Last updated:** 2026-10-06', '**Last updated:** 2026-10-10')
native_row = next(line for line in work(p).splitlines() if line.startswith('| [native-cabinet-account-session]'))
anchor = '| [daychi-backend-capabilities-in-cabinet]'
assert before.count(anchor) == 1
contents[p] = before.replace(anchor, native_row + '\n' + anchor)

p = 'docs/current-system.md'
anchor = '## Cabinet public-schedule environments — checked 2026-10-06'
start = '## Assignment and native-profile recheck — 2026-10-10'
fresh = 'Fresh remote heads are Cabinet'
source = work(p)
added = source[source.index(start):source.index(anchor)]
intro_end = added.index(fresh)
added = start + '\n\n' + added[intro_end:]
before = head(p)
assert before.count(anchor) == 1
contents[p] = before.replace(anchor, added + anchor)

tracked = git('ls-files', '-z').decode('utf-8').split('\0')
untouched = {p: hashlib.sha256((root / p).read_bytes()).hexdigest()
             for p in tracked if p and p not in contents and (root / p).is_file()}
(out / 'untouched-worktree.json').write_text(json.dumps(untouched, indent=2), encoding='utf-8')
patch = []
for p, text in contents.items():
    try:
        old = head(p)
    except subprocess.CalledProcessError:
        old = ''
    patch.extend(difflib.unified_diff(old.splitlines(keepends=True), text.splitlines(keepends=True),
                                    fromfile='a/' + p, tofile='b/' + p))
    saved = out / p
    saved.parent.mkdir(parents=True, exist_ok=True)
    saved.write_text(text, encoding='utf-8', newline='\n')
(out / 'native-package.patch').write_text(''.join(patch), encoding='utf-8', newline='\n')
(out / 'paths.json').write_text(json.dumps(list(contents), indent=2), encoding='utf-8')
for p, text in contents.items():
    blob = git('hash-object', '-w', '--stdin', data=text.encode('utf-8')).decode().strip()
    git('update-index', '--add', '--cacheinfo', '100644,' + blob + ',' + p)
print(json.dumps({'staged_files': len(contents), 'paths': list(contents)}, indent=2))
