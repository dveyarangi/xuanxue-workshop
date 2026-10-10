from pathlib import Path
import json
import re
import subprocess
import sys

tag = '01a1114c-a3d8-7b71-be77-b242d14ca5cb'
script = '.agents/scripts/gw/questions.py'
leans = [
    ('q-0002', 'Public pilot amendment 4aec5f8 and original provider/consumer issue updates are published and read back. Cabinet installation is accepted; amended provider conformance, Daychi installation/native proof and broader application contracts remain open. Native account-session scope is minted locally for alignment; unrelated readiness/source-rollout work remains separate.'),
    ('q-0002.0002', 'The installed coordinator rule already permits preparing further authorized work during recipient waits; this session exercised that route through native-session scope and approved minting. The redundant rule reminder was not adopted. Public pilot amendment/paired issue readback passed independent recipient reading; broader readiness, coordinator grading and recipient source rollout remain separate.'),
    ('q-0002.0002.0002', 'Public pilot contract 4aec5f8 and paired assignment updates are published. Approved native Cabinet account-session outcome is minted as 01-0008, Ready for alignment; preparation is independent of pilot proof and existing queue/checkpoints remain. Amended provider handling, Daychi installation/native proof and native credential decisions remain outstanding.'),
    ('q-0002.0007', 'Public pilot valid-only best-effort rows and omission error logs are accepted and published at 4aec5f8; original Cabinet/Daychi assignments and superseded 500 review are updated and read back. No version or completeness metadata is added. Actual amended provider/client evidence, native proof, account synchronization and broader cutover remain open.'),
    ('q-0002.0008.0001.0002', 'Approved native account-session outcome is minted locally as 01-0008, Ready for alignment; no authentication implementation assignment is published. Cabinet authority and provisional browser/code-and-PKCE handoff remain fixed. Acquisition/lifecycle/account-read/sign-out wire choices need agreement, preserving Daychi content access and ordinary schedule/reminders.'),
]

for identity, lean in leans:
    subprocess.run([sys.executable, script, 'lean', identity, lean, '--session', tag], check=True)

record = Path('docs/sessions/0008-20261008-public-pilot-amendment-and-native-session-ticket.md')
missing = []
for target in re.findall(r'\]\(([^)]+)\)', record.read_text(encoding='utf-8')):
    if not target.startswith(('https://', 'http://')):
        if not (record.parent / target.split('#')[0]).resolve().exists():
            missing.append(target)
if missing:
    raise SystemExit(f'Missing local links: {missing}')
print('Session record: all local link targets exist.')

for mechanism in ('questions', 'tickets'):
    result = subprocess.run([sys.executable, f'.agents/scripts/gw/{mechanism}.py', '--check'], check=True, capture_output=True, text=True)
    parsed = json.loads(result.stdout)
    if parsed.get('diagnostics'):
        raise SystemExit(json.dumps(parsed['diagnostics']))
    print(f'{mechanism}: no structural diagnostics; {len(parsed.get("findings", []))} existing question similarity findings.')

subprocess.run(['git', 'diff', '--check', '--', 'docs/sessions/0008-20261008-public-pilot-amendment-and-native-session-ticket.md', *[str(p) for p in Path('docs/questions').glob('q-*.md')]], check=True)
print('Conclude checks passed; ending session as the last act.')
subprocess.run([sys.executable, script, '--end', '--session', tag], check=True)
