from pathlib import Path, PurePosixPath
import posixpath
import re
import sys
from urllib.parse import urlsplit

root = Path(__file__).resolve().parents[2]
out = root / '.local/continuation-20261010'
sha = 'b8ab296e2713580eb4b91155b0c333ea758a74ce'
base = 'https://github.com/dveyarangi/xuanxue-workshop/blob/' + sha + '/'
provider_url = sys.argv[1] if len(sys.argv) > 1 else None
for kind in ('cabinet', 'daychi'):
    path = 'docs/assignments/native-session-' + kind + '.draft.md'
    draft = (root / path).read_text(encoding='utf-8')
    body = draft[draft.index('## Recipient and outcome'):]
    body = ('Accepted native account-session implementation assignment.\n\n'
            'Prepared within [01-0008-native-cabinet-account-session](' + base +
            'docs/tickets/01-0008-native-cabinet-account-session.md).\n'
            'Shared contract revision: `' + sha + '`.\n\n') + body
    def pinned(match):
        href = match.group(2)
        parsed = urlsplit(href)
        if parsed.scheme or href.startswith('//'):
            return match.group(0)
        target = posixpath.normpath(posixpath.join(str(PurePosixPath(path).parent), parsed.path))
        return '[' + match.group(1) + '](' + base + target + ('#' + parsed.fragment if parsed.fragment else '') + ')'
    body = re.sub(r'\[([^\]]+)\]\(([^\s)]+)\)', pinned, body)
    if kind == 'daychi':
        old = ("Cabinet's original provider assignment supplies provider/fixture evidence; replace\n"
               'this descriptive reference with its direct issue link when the pair is published.')
        if not provider_url:
            continue
        assert old in body
        body = body.replace(old, '[Cabinet\'s provider assignment](' + provider_url + ') supplies provider/fixture evidence.')
    assert '../' not in body
    assert '**Draft' not in body
    assert 'Before publication' not in body
    assert 'homeHiddenTiles' in body
    (out / ('native-' + kind + '-issue.md')).write_text(body.rstrip() + '\n', encoding='utf-8', newline='\n')
