"""Read-only native proof of the bot's scoped MCP connection."""
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from workshop_bot.codex import Codex
from workshop_bot.service import Workshop


def main():
    root = Path(__file__).resolve().parents[1]
    evidence = root / '.local' / datetime.now(timezone.utc).strftime('harness-proof-tools-%Y%m%d-%H%M%S')
    private = evidence / 'private'
    private.mkdir(parents=True)
    agent = Codex(timeout=360, tools_enabled=True)
    native = agent.run_stream
    events = []
    notices = []

    def observed(command, prompt, environment, directory, observe):
        def event(value):
            events.append(value)
            observe(value)
        result = native(command, prompt, environment, directory, event)
        (private / 'events.json').write_text(json.dumps(events, ensure_ascii=False, indent=2), encoding='utf-8')
        return result

    agent.run_stream = observed
    app = Workshop(root, private / 'history.sqlite3', agent)
    result = app.ask('native-board-tools', 'Что сейчас известно по Workshop issue 14? '
                     'Проверь текущую запись GitHub. Ничего не публикуй и не меняй.',
                     conversation={'chat_id': -100123, 'messages': [],
                                   'current': {'message_id': 11, 'conversation_id': 11}},
                     on_progress=lambda text: notices.append(text) if text not in notices else None)
    (private / 'result.json').write_text(json.dumps({'result': result, 'notices': notices}, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps({'result': result, 'notices': notices, 'evidence': str(evidence)}, ensure_ascii=False), flush=True)
    assert result['status'] == 'answered', result
    assert any(e.get('item', {}).get('type') == 'mcp_tool_call' for e in events), 'No native MCP tool use'
    assert any(e.get('item', {}).get('tool') == 'read_issue' and
               e['item'].get('status') == 'completed' and not e['item'].get('error') and
               not (e['item'].get('result') or {}).get('isError') for e in events), 'No successful board issue evidence read'
    assert 'docs/' not in result['answer'], 'Bare local reference'


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    main()
