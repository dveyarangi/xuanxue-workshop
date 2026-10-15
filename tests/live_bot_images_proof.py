"""Native image-tool proof with an invented group and image-only random digits."""

import binascii
import json
import re
import secrets
import struct
import sys
import tempfile
import zlib
from pathlib import Path

from tests.test_bot_archive import retained_fixture
from tests.test_telegram import TelegramPeer
from workshop_bot.archive import Archive
from workshop_bot.codex import Codex
from workshop_bot.service import Workshop
from workshop_bot.telegram import Group


def number_image(number):
    glyphs = [
        ['01110','10001','10011','10101','11001','10001','01110'],
        ['00100','01100','00100','00100','00100','00100','01110'],
        ['01110','10001','00001','00010','00100','01000','11111'],
        ['11110','00001','00001','01110','00001','00001','11110'],
        ['00010','00110','01010','10010','11111','00010','00010'],
        ['11111','10000','10000','11110','00001','00001','11110'],
        ['01110','10000','10000','11110','10001','10001','01110'],
        ['11111','00001','00010','00100','01000','01000','01000'],
        ['01110','10001','10001','01110','10001','10001','01110'],
        ['01110','10001','10001','01111','00001','00001','01110'],
    ]
    width, height, scale = (len(number)*7+4)*10, 110, 10
    rows = bytearray()
    for y in range(height):
        rows.append(0)
        for x in range(width):
            gx, gy = x//scale-2, y//scale-2
            cell, column = divmod(gx, 7)
            black = 0 <= cell < len(number) and 0 <= gy < 7 and column < 5 and glyphs[int(number[cell])][gy][column] == '1'
            rows.extend(b'\0\0\0' if black else b'\xff\xff\xff')
    def chunk(name, data):
        return struct.pack('!I', len(data)) + name + data + struct.pack('!I', binascii.crc32(name+data))
    return b'\x89PNG\r\n\x1a\n' + chunk(b'IHDR', struct.pack('!IIBBBBB', width, height, 8, 2, 0, 0, 0)) + chunk(b'IDAT', zlib.compress(rows)) + chunk(b'IEND', b'')


def main():
    digits = ''.join(str(secrets.randbelow(10)) for _ in range(6))
    with tempfile.TemporaryDirectory(prefix='workshop-visual-proof-') as directory:
        root = Path(directory)
        (root / '.agents/skills').mkdir(parents=True)
        (root / 'AGENTS.md').write_text('', encoding='utf-8')
        (root / 'README.md').write_text('# Synthetic group\nAn invented imported image is retained at message 2. No external project tracker is connected.\n', encoding='utf-8')
        state = root / 'private/history.sqlite3'
        agent = Codex(timeout=360, tools_enabled=True)
        events = []
        native = agent.run_stream
        def observed(command, prompt, environment, directory, observe):
            def event(value):
                events.append(value)
                observe(value)
            return native(command, prompt, environment, directory, event)
        agent.run_stream = observed
        app = Workshop(root, state, agent)
        Group(app, TelegramPeer(), -100123).start()
        retained_fixture(Archive(state), text='Изображение для проверки чтения', pixels=number_image(digits))
        result = app.ask('visual-proof', 'Посмотри изображение 0 у сообщения 2 через read_image. Какие шесть цифр на нём написаны? Ответь только цифрами.',
                         conversation={'chat_id': -100123, 'messages': [],
                                       'current': {'message_id': 10, 'conversation_id': 10, 'addressing': 'direct'}})
        used = any(e.get('item', {}).get('tool') == 'read_image' and e['item'].get('status') == 'completed'
                   and not e['item'].get('error') for e in events)
        assert result['status'] == 'answered', result
        assert used, 'No successful native read_image call'
        assert re.sub(r'\D', '', result['answer']) == digits, 'Image-only digits were not read correctly'
        print(json.dumps({'native_image_read': True, 'image_only_digits_matched': True,
                          'telegram_messages_sent': 0, 'real_group_data_used': False}), flush=True)


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    main()
