"""Native request recording followed by discovery in a fresh operator recall."""
import json
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from workshop_bot.codex import Codex
from workshop_bot.service import Workshop
from tests.test_board import Tracker, board


def main():
    source = Path(__file__).resolve().parents[1]
    evidence = source / '.local' / datetime.now(timezone.utc).strftime('harness-proof-requests-%Y%m%d-%H%M%S')
    root = evidence / 'project'
    private = evidence / 'private'
    private.mkdir(parents=True)
    root.mkdir()
    for skill in ('recall', 'review-assignments'):
        destination = root / '.agents/skills' / skill / 'SKILL.md'
        destination.parent.mkdir(parents=True)
        shutil.copyfile(source / '.agents/skills' / skill / 'SKILL.md', destination)
    (root / 'AGENTS.md').write_text('At entry, read .agents/skills/recall/SKILL.md. This isolated proof permits reading existing records only; do not register sessions or mutate question records.\n', encoding='utf-8')
    (root / 'README.md').write_text('# Proof workshop\nAn isolated example for pending operator requests.\n', encoding='utf-8')
    (root / 'docs/tickets').mkdir(parents=True)
    (root / 'docs/tickets/README.md').write_text('# Queue\nNo implementation authorized.\n', encoding='utf-8')
    subprocess.run(['git', 'init', '--quiet', str(root)], check=True)
    review = board.Board(root / '.local/board-review/history.sqlite3', Tracker())
    review.scan()
    agent = Codex(timeout=360, tools_enabled=True)
    events = []
    original = agent.run_stream
    def observed(command, prompt, environment, directory, observe):
        def event(value):
            events.append(value)
            observe(value)
        return original(command, prompt, environment, directory, event)
    agent.run_stream = observed
    app = Workshop(root, private / 'history.sqlite3', agent)
    result = app.ask('request-proof', 'Нужен новый механизм «Северный маяк» для проверки доступности стенда. Запиши запрос для следующего wake оператора; сейчас ничего не реализуй.',
                     sender='Proof operator', conversation={'chat_id': -100123, 'messages': [],
                     'current': {'message_id': 11, 'conversation_id': 11}})
    (private / 'bot.json').write_text(json.dumps({'result': result, 'events': events}, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps({'bot': result, 'evidence': str(evidence)}, ensure_ascii=False), flush=True)
    assert result['status'] == 'answered', result
    log = root / 'docs/requests/telegram.md'
    assert log.is_file(), 'No operator request recorded'
    assert 'Северный маяк' in log.read_text(encoding='utf-8')
    assert 'Status: pending' in log.read_text(encoding='utf-8')
    assert any(e.get('item',{}).get('tool') == 'request_operator' and
               e['item'].get('status') == 'completed' and not e['item'].get('error') and
               not (e['item'].get('result') or {}).get('isError') for e in events)
    commands = [e.get('item',{}).get('command','') for e in events]
    assert any('recall' in command and 'SKILL.md' in command for command in commands), 'No recall fallback'
    assert any('review-assignments' in command and 'SKILL.md' in command for command in commands), 'No assignment review fallback'
    answer = private / 'operator.txt'
    command = [agent.executable, 'exec', '--ignore-user-config', '--ignore-rules', '--strict-config', '--ephemeral',
               '--skip-git-repo-check', '--cd', str(root), '--json', '--output-last-message', str(answer),
               '-c', 'web_search="disabled"'] + agent.permissions(root, app.memory, private)
    for name in ('shell_tool', 'code_mode', 'code_mode_host'):
        command += ['--enable', name]
    for name in ('hooks', 'apps', 'plugins', 'multi_agent', 'multi_agent_v2', 'browser_use', 'browser_use_external', 'computer_use'):
        command += ['--disable', name]
    command.append('-')
    completed = subprocess.run(command, input='Начни операторскую сессию. Какие запросы ждут моего решения? Ничего не реализуй.',
                               capture_output=True, encoding='utf-8', errors='replace', timeout=360, cwd=root)
    (private / 'operator-events.jsonl').write_text(completed.stdout, encoding='utf-8')
    assert completed.returncode == 0, completed.stderr[-1000:]
    text = answer.read_text(encoding='utf-8')
    assert 'Северный маяк' in text, 'Fresh recall did not discover the pending request'
    print(json.dumps({'operator': text, 'verified': 'request + fallback + fresh recall'}, ensure_ascii=False), flush=True)


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    main()
