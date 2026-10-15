import base64
import hashlib
import io
import json
import os
import sqlite3
import tempfile
import unittest
from contextlib import closing
from pathlib import Path
from unittest.mock import patch

from workshop_bot.archive import Archive, IMAGE_LIMIT, checked_file, image_type, save_content
from workshop_bot.service import Workshop
from workshop_bot.telegram import Group
from workshop_bot.tools import TurnTools, serve
from tests.test_telegram import TelegramPeer, message


PNG = base64.b64decode('iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAwMCAO+aD1sAAAAASUVORK5CYII=')


def retained_fixture(archive, chat_id=-100123, text='СХЕМА расписания', pixels=PNG):
    blob = hashlib.sha256(pixels).hexdigest()
    save_content(archive.directory / 'images', blob, pixels)
    records = [
        {'message_id': 2, 'text': text + '\nвторая строка',
         'sender': {'display_name': 'Мария'}, 'created': '2026-10-01T10:00:00+02:00',
         'reply_to': None, 'source': 'export',
         'attachments': [{'kind': 'image', 'name': 'original.png', 'blob': blob}]},
        {'message_id': 3, 'text': '@workshop_bot старое обращение',
         'sender': {'display_name': 'Мария'}, 'source': 'export', 'attachments': []},
        {'message_id': 4, 'text': 'Ответ на схему', 'sender': {'display_name': 'Boris'},
         'reply_to': 2, 'source': 'export', 'attachments': []},
    ]
    with closing(sqlite3.connect(archive.state)) as db, db:
        db.executemany('INSERT INTO group_archive VALUES (?,?,?)',
                       [(chat_id, r['message_id'], json.dumps(r, ensure_ascii=False)) for r in records])


class ArchiveTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.state = self.root / 'private/history.sqlite3'
        self.app = Workshop(self.root, self.state, lambda context: {
            'disposition': 'answer', 'answer': 'new answer', 'reason': '', 'sources': [], 'edit': None})
        self.group = Group(self.app, TelegramPeer(), -100123)
        self.group.start()
        self.archive = Archive(self.state)

    def tools(self, chat_id=-100123):
        return TurnTools({'root': str(self.root), 'state': str(self.state), 'request_id': 'archive-check',
                          'chat_id': chat_id, 'conversation': f'group:{chat_id}', 'source': {}})

    def test_preexisting_history_metadata_images_and_no_request_replay(self):
        retained_fixture(self.archive)
        self.archive = Archive(self.state)
        records = self.archive.messages(-100123)
        self.assertEqual(records[1]['sender']['display_name'], 'Мария')
        self.assertEqual(records[2]['reply_to'], 2)
        self.assertIn('СХЕМА расписания\nвторая строка', records[0]['text'])
        self.assertEqual(records[0]['created'], '2026-10-01T10:00:00+02:00')
        self.assertEqual(self.archive.image(-100123, 2), (PNG, 'image/png'))
        self.assertFalse(self.group.work_once(), 'Old mentions must not be queued')
        with self.app.connect() as db:
            self.assertEqual(db.execute('SELECT count(*) FROM requests').fetchone()[0], 0)
            self.assertEqual(db.execute('SELECT count(*) FROM telegram_requests').fetchone()[0], 0)

    def test_unicode_search_paging_and_scope_do_not_leak_another_group(self):
        retained_fixture(self.archive)
        retained_fixture(self.archive, -100999, text='OTHER GROUP DATA')
        result = self.tools().search_history('схема')
        self.assertEqual([m['message_id'] for m in result['messages']], [2])
        self.assertNotIn('OTHER GROUP DATA', json.dumps(result))
        page = self.tools().search_history(limit=1)
        self.assertEqual(page['messages'][0]['message_id'], 4)
        self.assertEqual(self.tools().search_history(before=page['next_before'], limit=1)['messages'][0]['message_id'], 3)
        with self.assertRaisesRegex(ValueError, 'different or unverified'):
            self.tools(-100999).read_message(2)

    def test_actual_mcp_response_contains_pixels_without_private_path_or_file_selector(self):
        retained_fixture(self.archive)
        tools = self.tools()
        incoming = io.StringIO(json.dumps({'jsonrpc': '2.0', 'id': 1, 'method': 'tools/call',
                              'params': {'name': 'read_image', 'arguments': {'message_id': 2}}}) + '\n')
        outgoing = io.StringIO()
        serve(tools.context, incoming, outgoing)
        content = json.loads(outgoing.getvalue())['result']['content']
        self.assertEqual(content[1]['type'], 'image')
        self.assertEqual(base64.b64decode(content[1]['data']), PNG)
        self.assertEqual(content[1]['mimeType'], 'image/png')
        self.assertNotIn(str(self.root), content[0]['text'])
        self.assertNotIn('blob', content[0]['text'])
        with self.assertRaisesRegex(ValueError, 'image index'):
            tools.read_image(2, index=8)

    def test_later_received_message_has_priority_and_images_are_retained_without_captions(self):
        retained_fixture(self.archive)
        update = message(1, 'Later server text')
        update['message']['message_id'] = 2
        update['message']['entities'] = []
        self.group.api.updates = [update]
        self.group.poll_once(0)
        self.assertEqual(self.tools().read_message(2)['message']['text'], 'Later server text')
        update = message(2)
        update['message'].pop('text')
        update['message'].pop('entities')
        update['message']['photo'] = [{'file_id': 'small', 'width': 2, 'height': 2},
                                     {'file_id': 'original', 'width': 100, 'height': 100}]
        self.group.api.updates = [update]
        self.group.poll_once(0)
        number = update['message']['message_id']
        record = self.tools().read_message(number)['message']
        self.assertTrue(record['images'][0]['available'])
        self.assertIn('Изображение', record['text'])
        peer = type('Download', (), {'download': lambda _, file_id, limit: PNG if file_id == 'original' else b'wrong'})()
        self.assertEqual(self.archive.image(-100123, number, api=peer), (PNG, 'image/png'))
        self.group.api.updates = [update]
        self.group.poll_once(0)
        self.assertEqual(self.archive.image(-100123, number), (PNG, 'image/png'), 'Read pixels survive without Telegram')

    def test_archive_is_available_beyond_the_recent_snapshot_and_old_mentions_do_not_execute(self):
        retained_fixture(self.archive)
        for i in range(20, 60):
            item = message(i, 'Ж' * 4000)
            item['message']['entities'] = []
            self.group.api.updates.append(item)
        current = message(90, '@workshop_bot расскажи о схеме')
        self.group.api.updates.append(current)
        self.group.poll_once(0)
        with self.app.connect() as db:
            row = db.execute('SELECT * FROM telegram_requests WHERE update_id=90').fetchone()
        context = self.group.conversation(row)
        self.assertGreater(context['omitted_messages'], 0)
        self.assertEqual(self.tools().search_history('схема')['messages'][0]['message_id'], 2)

    def test_missing_hardlinked_and_changed_cache_are_not_read(self):
        retained_fixture(self.archive)
        blob = self.archive.messages(-100123)[0]['attachments'][0]['blob']
        path = self.archive.directory / 'images' / blob
        path.write_bytes(b'changed')
        with self.assertRaisesRegex(ValueError, 'changed'):
            self.archive.image(-100123, 2)
        path.unlink()
        with self.assertRaisesRegex(ValueError, 'missing'):
            self.archive.image(-100123, 2)
        outside = self.root / 'outside.png'
        outside.write_bytes(PNG)
        os.link(outside, path)
        with self.assertRaisesRegex(ValueError, 'hard-linked'):
            self.archive.image(-100123, 2)
        with self.assertRaisesRegex(ValueError, 'leaves its directory'):
            checked_file(path.parent, '../outside.png')

    def test_unsupported_and_oversized_image_have_explicit_outcomes(self):
        with self.assertRaisesRegex(ValueError, '10 MiB'):
            image_type(b'\x89PNG\r\n\x1a\n' + bytes(IMAGE_LIMIT))
        with self.assertRaisesRegex(ValueError, 'Only PNG'):
            image_type(b'not an image')


if __name__ == '__main__':
    unittest.main()
