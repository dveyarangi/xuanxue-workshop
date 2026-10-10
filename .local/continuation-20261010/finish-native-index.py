from pathlib import Path
import json
import subprocess

root = Path(__file__).resolve().parents[2]
out = root / '.local/continuation-20261010/commit-package'

def git(*args, data=None):
    return subprocess.run(['git', *args], cwd=root, input=data,
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                          check=True).stdout

def stage(path, text):
    blob = git('hash-object', '-w', '--stdin', data=text.encode('utf-8')).decode().strip()
    git('update-index', '--add', '--cacheinfo', '100644,' + blob + ',' + path)
    saved = out / path
    saved.parent.mkdir(parents=True, exist_ok=True)
    saved.write_text(text, encoding='utf-8', newline='\n')

for p in ('docs/assignments/native-session-cabinet.draft.md',
          'docs/assignments/native-session-daychi.draft.md'):
    text = (root / p).read_text(encoding='utf-8').rstrip() + '\n'
    (root / p).write_text(text, encoding='utf-8', newline='\n')
    stage(p, text)

for p in ('docs/questions/q-0002.0010-should-clients-reach-cabinet-and-daychi-through-a-shared-gateway.md',
          'docs/questions/q-0002.0002.0002-which-workshop-outcomes-should-the-remaining-reconciliation-pass-deliver.md'):
    stage(p, (root / p).read_text(encoding='utf-8'))

p = 'docs/agent-contract.md'
old = git('show', 'HEAD:' + p).decode('utf-8')
current = (root / p).read_text(encoding='utf-8')
old_header = ('Accepted by the user, 2026-10-04, including the role separation, startup review,\n'
              'reporting channels and installation-first order below.')
new_header = ('Accepted by the user on 2026-10-04, with clarifications through 2026-10-08 incorporated.')
assert old.count(old_header) == 1
old = old.replace(old_header, new_header)
start = 'The first assignment requests installation'
new_start = 'The first assignment\'s outcome is collaboration installed'
end = '### Boundary summary in project instructions'
old = old[:old.index(start)] + current[current.index(new_start):current.index(end)] + old[old.index(end):]
old_part = ('acceptance acknowledgement. Initial recipient assignments concern verified local\n'
            'collaboration installation. Subsequent execution depends on confirmed onboarding;\n'
            'Planned posting may precede it.')
new_part = ('acceptance acknowledgement. Initial recipient assignments concern verified local\n'
            'collaboration installation. That installation and Workshop readiness do not gate\n'
            'application implementation under the recipient operator against an accessible\n'
            'settled shared contract.')
assert old.count(old_part) == 1
old = old.replace(old_part, new_part)
old_part = ('Cabinet installation issue 1 is accepted/closed; Daychi installation retains its\n'
            'readiness dependency.')
new_part = ('Cabinet installation issue 1 and Daychi installation issue 2 are accepted/closed;\n'
            'their evidence does not introduce an additional native implementation gate.')
assert old.count(old_part) == 1
old = old.replace(old_part, new_part)
stage(p, old)
paths = json.loads((out / 'paths.json').read_text(encoding='utf-8'))
paths.append(p)
(out / 'paths.json').write_text(json.dumps(paths, indent=2), encoding='utf-8')
manifest = json.loads((out / 'untouched-worktree.json').read_text(encoding='utf-8'))
manifest.pop(p, None)
(out / 'untouched-worktree.json').write_text(json.dumps(manifest, indent=2), encoding='utf-8')
print('Final staged set: ' + str(len(paths)) + ' documentation files')
