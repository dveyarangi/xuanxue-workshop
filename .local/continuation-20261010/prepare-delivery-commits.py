from pathlib import Path, PurePosixPath
import hashlib
import json
import posixpath
import re
import subprocess
import sys
from urllib.parse import unquote, urlsplit

root = Path(__file__).resolve().parents[2]
out = root / '.local/continuation-20261010/delivery-commits'
out.mkdir(exist_ok=True)

def git(*args, data=None):
    return subprocess.run(['git', *args], cwd=root, input=data, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE, check=True).stdout

def head(path):
    return git('show', 'HEAD:' + path).decode('utf-8')

def work(path):
    return (root / path).read_text(encoding='utf-8')

def saved(group, path):
    return out / group / (hashlib.sha256(path.encode()).hexdigest()[:16] + '.txt')

def rule(name):
    return re.search(r'^## ' + name + r' .*?(?=^## |\Z)', work('local.rules.md'), re.M | re.S).group(0)

def installed(name):
    section = rule(name)
    return '**' + name + '** ' + re.search(r'<rule>\n(.*?)\n</rule>', section, re.S).group(1)

def with_local(path, extra):
    source = head(path)
    match = re.search(r'<installed by="local">\n(.*?)\n</installed>', source, re.S)
    if match:
        return source[:match.end(1)] + '\n\n' + extra + source[match.end(1):]
    return source.rstrip() + '\n\n<installed by="local">\n' + extra + '\n</installed>\n'

mode = sys.argv[1]
if mode == 'prepare':
    assert git('rev-parse', 'HEAD').decode().strip() == 'b8ab296e2713580eb4b91155b0c333ea758a74ce'
    assert not git('diff', '--cached', '--name-only').strip(), 'Existing index is not empty'
    p = 'local.rules.md'
    source = head(p)
    anchor = '| `AGENTS.md` | `## Project-local` |\n'
    assert source.count(anchor) == 1
    source = source.replace(anchor, anchor + '| `.agents/skills/conclude/SKILL.md` | `## Installed from other mechanisms` |\n')
    implementation = {
        p: source.rstrip() + '\n\n' + rule('L17').rstrip() + '\n\n' + rule('L18').rstrip() + '\n',
        'AGENTS.md': with_local('AGENTS.md', installed('L17')),
        '.agents/skills/conclude/SKILL.md': with_local('.agents/skills/conclude/SKILL.md', installed('L17')),
        '.agents/skills/coordinate/SKILL.md': with_local('.agents/skills/coordinate/SKILL.md', installed('L18')),
    }
    full = [
        'docs/contracts/native-account-session.md',
        'docs/assignments/native-session-cabinet.draft.md',
        'docs/assignments/native-session-daychi.draft.md',
        'docs/tickets/01-0008-native-cabinet-account-session.md',
        'docs/questions/q-0002.0008.0001.0002-how-will-native-daychi-maintain-a-cabinet-account-session-without-replacing-its-content-access.md',
        'docs/questions/done/q-0002.0002.0005-how-should-the-delivery-pipeline-make-its-current-stage-and-next-action-clear-without-reopening-settled-decisions.md',
    ]
    documentation = {p: work(p) for p in full}
    p = 'docs/tickets/README.md'
    source = head(p)
    old = next(s for s in source.splitlines() if s.startswith('| [native-cabinet-account-session]'))
    new = next(s for s in work(p).splitlines() if s.startswith('| [native-cabinet-account-session]'))
    documentation[p] = source.replace(old, new)
    p = 'docs/rule-failures.md'
    heading = '## 2026-10-04 — Alignment stopped after answering a clarification\n\n'
    status = 'Status: amendment refused as redundant; execution corrected by resuming alignment.\n\n'
    marker = heading + status
    source = work(p)
    start = source.index(marker) + len(marker)
    end = source.index('Struck again, 2026-10-06, session', start)
    addition = source[start:end]
    assert addition.startswith('Struck again, 2026-10-10:')
    assert head(p).count(marker) == 1
    documentation[p] = head(p).replace(marker, marker + addition)
    p = 'docs/questions/sessions'
    tag = '01a122c9-5910-7ce3-aa61-1ceb56838ad8'
    row = next(s for s in work(p).splitlines() if s.startswith(tag + ' '))
    assert tag not in head(p)
    documentation[p] = head(p).rstrip() + '\n' + row + '\n'
    for group, contents in [('implementation', implementation), ('documentation', documentation)]:
        for p, content in contents.items():
            dest = saved(group, p)
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text(content, encoding='utf-8', newline='\n')
        (out / (group + '.json')).write_text(json.dumps(list(contents), indent=2), encoding='utf-8')
    paths = git('ls-files', '-z').decode().split('\0')
    snapshot = {p: hashlib.sha256((root / p).read_bytes()).hexdigest()
                for p in paths if p and (root / p).is_file()}
    snapshot[full[-1]] = hashlib.sha256((root / full[-1]).read_bytes()).hexdigest()
    (out / 'worktree.json').write_text(json.dumps(snapshot, indent=2), encoding='utf-8')
    print(json.dumps({'prepared': True, 'implementation_files': len(implementation), 'documentation_files': len(documentation), 'worktree_files': len(snapshot)}))

elif mode == 'stage':
    group = sys.argv[2]
    assert not git('diff', '--cached', '--name-only').strip(), 'Existing index is not empty'
    paths = json.loads((out / (group + '.json')).read_text(encoding='utf-8'))
    for p in paths:
        data = saved(group, p).read_bytes()
        blob = git('hash-object', '-w', '--stdin', data=data).decode().strip()
        git('update-index', '--add', '--cacheinfo', '100644,' + blob + ',' + p)
    print(json.dumps({'staged': group, 'files': len(paths), 'paths': paths}))

elif mode == 'check':
    group = sys.argv[2]
    paths = json.loads((out / (group + '.json')).read_text(encoding='utf-8'))
    assert set(git('diff', '--cached', '--name-only').decode().splitlines()) == set(paths)
    for p in paths:
        assert git('show', ':' + p) == saved(group, p).read_bytes(), p
    if group == 'implementation':
        rules_source = git('show', ':local.rules.md').decode('utf-8')
        sections = re.findall(r'^## (L\d+) .*?\n(.*?)(?=^## |\Z)', rules_source, re.M | re.S)
        for p in paths:
            if p == 'local.rules.md':
                continue
            rules = []
            for name, section in sections:
                if p in re.findall(r'^- \*\*target\*\* `([^`]+)`', section, re.M):
                    body = re.search(r'<rule>\n(.*?)\n</rule>', section, re.S).group(1)
                    rules.append('**' + name + '** ' + body)
            expected = '<installed by="local">\n' + '\n\n'.join(rules) + '\n</installed>'
            actual = re.search(r'<installed by="local">.*?</installed>', git('show', ':' + p).decode('utf-8'), re.S).group(0)
            assert actual == expected, 'Indexed local installation differs: ' + p
    git('diff', '--cached', '--check')
    errors = []
    count = 0
    for p in paths:
        source = git('show', ':' + p).decode('utf-8')
        prose = re.sub(r'```.*?```', '', source, flags=re.S)
        prose = re.sub(r'`[^`]*`', '', prose)
        for href in re.findall(r'\[[^\]]*\]\(([^\s)]+)\)', prose):
            href = href.strip('<>')
            parsed = urlsplit(href)
            if parsed.scheme or href.startswith('//'):
                continue
            target = posixpath.normpath(posixpath.join(str(PurePosixPath(p).parent), unquote(parsed.path))) if parsed.path else p
            count += 1
            try:
                content = git('show', ':' + target).decode('utf-8')
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
    for p, digest in json.loads((out / 'worktree.json').read_text(encoding='utf-8')).items():
        assert hashlib.sha256((root / p).read_bytes()).hexdigest() == digest, 'Working file changed: ' + p
    print(json.dumps({'checked': group, 'files': len(paths), 'links': count, 'worktree_preserved': True, 'errors': errors}))
    assert not errors

elif mode == 'postcommit':
    group = sys.argv[2]
    paths = json.loads((out / (group + '.json')).read_text(encoding='utf-8'))
    assert set(git('diff-tree', '--no-commit-id', '--name-only', '-r', 'HEAD').decode().splitlines()) == set(paths)
    for p in paths:
        assert git('show', 'HEAD:' + p) == saved(group, p).read_bytes(), p
    for p, digest in json.loads((out / 'worktree.json').read_text(encoding='utf-8')).items():
        assert hashlib.sha256((root / p).read_bytes()).hexdigest() == digest, p
    assert not git('diff', '--cached', '--name-only').strip()
    print(json.dumps({'committed': group, 'head': git('rev-parse', 'HEAD').decode().strip(), 'exact_package': True, 'worktree_preserved': True}))
else:
    raise SystemExit('Unknown operation')
