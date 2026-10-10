from pathlib import Path
import subprocess

root = Path(__file__).resolve().parents[2]
path = 'docs/agent-contract.md'
def git(*args, data=None):
    return subprocess.run(['git', *args], cwd=root, input=data,
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                          check=True).stdout

text = git('show', ':' + path).decode('utf-8')
old = ('recipient project under its operator. The\n'
       '[onboarding agreement](onboarding.md#collaboration-installation) defines that\n'
       'installation and its evidence. Installation is a separately reviewable outcome;')
new = 'recipient project under its operator. Installation is a separately reviewable outcome;'
assert text.count(old) == 1
text = text.replace(old, new)
blob = git('hash-object', '-w', '--stdin', data=text.encode('utf-8')).decode().strip()
git('update-index', '--cacheinfo', '100644,' + blob + ',' + path)
(root / '.local/continuation-20261010/commit-package' / path).write_text(text, encoding='utf-8', newline='\n')
