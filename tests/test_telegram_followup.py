import json
import tempfile
import unittest
from pathlib import Path

from tests.test_telegram import TelegramPeer, message
from workshop_bot.service import Workshop
from workshop_bot.telegram import Group


class FollowupTests(unittest.TestCase):
    def test_separate_mention_answers_previous_message_after_restart_once(self):
        received = []

        class Agent:
            def chat(self, root, memory, private, question, conversation, **kwargs):
                received.append((question, conversation))
                return {'status': 'answered', 'answer': 'Конкретные шаги'}

        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            app = Workshop(root, root / 'history.sqlite3', Agent())
            original = message(text='покажи же новое "что нужно сделать"?')
            original['message']['entities'] = []
            peer = TelegramPeer([original])
            group = Group(app, peer, -100123)
            group.start()
            group.poll_once(0)
            self.assertFalse(group.work_once())
            mention = message(update=2, text='@workshop_bot')
            mention['message']['date'] += 120
            peer.updates = [mention, mention]
            group = Group(app, peer, -100123)
            group.start()
            group.poll_once(0)
            group.work_once()
            self.assertEqual([x[0] for x in received], [original['message']['text']])
            self.assertEqual(received[0][1]['current']['conversation_id'], 11)
            self.assertEqual(peer.sent[0]['text'], 'Конкретные шаги')
            self.assertEqual(len(peer.sent), 1)
            self.assertEqual(group.history()[0]['status'], 'observed')
            self.assertEqual(group.history()[1]['body'], '@workshop_bot')
            self.assertEqual(group.history()[1]['addressed_message_id'], 11)

    def test_legacy_invitations_do_not_hide_unanswered_question(self):
        received = []

        class Agent:
            def chat(self, root, memory, private, question, conversation, **kwargs):
                received.append((question, conversation))
                return {'status': 'answered', 'answer': 'Конкретные шаги'}

        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            app = Workshop(root, root / 'history.sqlite3', Agent())
            peer = TelegramPeer()
            group = Group(app, peer, -100123)
            group.start()
            # Persist the old receiver's output, rather than generating it with the new receiver.
            invitation = 'Задайте вопрос о проектах Workshop — помогу разобраться.'
            question = 'покажи же новое "что нужно сделать"?'
            with app.connect() as db:
                for mid, created in ((50, '10:34:48'), (51, '10:36:38'), (53, '10:44:02'), (55, '10:44:09')):
                    db.execute(
                        'INSERT INTO telegram_requests '
                        '(update_id,message_id,sender,created,body,thread_id,status,result,parts,sent_ids,conversation_id) '
                        'VALUES (?,?,?,?,?,?,?,?,?,?,?)',
                        (mid, mid, json.dumps({'id': 7, 'first_name': 'Anna'}),
                         f'2026-10-15T{created}+00:00', question if mid == 50 else '@workshop_bot', 9,
                         'observed' if mid == 50 else 'sent',
                         None if mid == 50 else json.dumps({'status': 'answered', 'answer': invitation, 'sources': []}),
                         '[]' if mid == 50 else json.dumps([invitation]),
                         '[]' if mid == 50 else json.dumps([mid + 1]), None if mid == 50 else mid))
            mention = message(update=60, text='@workshop_bot')
            mention['message']['date'] = 1792061400  # 2026-10-15 10:50 UTC
            peer.updates = [mention, mention]
            group = Group(app, peer, -100123)
            group.start()
            group.poll_once(0)
            group.work_once()
            self.assertFalse(group.work_once())
            self.assertEqual([item[0] for item in received], [question])
            self.assertEqual(received[0][1]['current']['conversation_id'], 50)
            self.assertEqual(received[0][1]['addressed_message']['message_id'], 50)
            self.assertEqual(peer.sent[0]['text'], 'Конкретные шаги')

    def test_linked_request_in_any_state_is_not_executed_again(self):
        for status in ('queued', 'processing', 'ready', 'sent', 'uncertain', 'rejected'):
            with self.subTest(status=status), tempfile.TemporaryDirectory() as temporary:
                root = Path(temporary)
                app = Workshop(root, root / 'history.sqlite3', None)
                original = message(text='измени задачу')
                original['message']['entities'] = []
                peer = TelegramPeer([original, message(update=2, text='@workshop_bot')])
                group = Group(app, peer, -100123)
                group.start()
                group.poll_once(0)
                with app.connect() as db:
                    db.execute('UPDATE telegram_requests SET status=? WHERE message_id=12', (status,))
                selected = group.select(message(update=3, text='@workshop_bot'))
                self.assertIsNone(selected['addressed_message_id'])
                self.assertEqual(selected['conversation_id'], 11)

    def test_bare_mention_does_not_reuse_other_sender_topic_or_addressed_text(self):
        received = []

        class Agent:
            def chat(self, root, memory, private, question, conversation, **kwargs):
                received.append(question)
                kwargs['on_session']('00000000-0000-4000-8000-000000000001')
                return {'status': 'answered', 'answer': 'Уточнение по истории'}

        for variant in ('other_sender', 'other_topic', 'already_addressed', 'explicit_reply', 'unavailable'):
            with self.subTest(variant=variant), tempfile.TemporaryDirectory() as temporary:
                root = Path(temporary)
                original = message(text='покажи шаги')
                original['message']['entities'] = []
                if variant == 'other_sender':
                    original['message']['from']['id'] = 99
                if variant == 'other_topic':
                    original['message']['message_thread_id'] = 100
                if variant == 'already_addressed':
                    original = message(text='@workshop_bot исходный вопрос')
                if variant == 'unavailable':
                    original['message'].pop('text')
                    original['message']['photo'] = []
                mention = message(update=2, text='@workshop_bot')
                mention['message']['date'] += 120
                if variant == 'explicit_reply':
                    mention['message']['reply_to_message'] = {'message_id': 999}
                peer = TelegramPeer([original, mention])
                group = Group(Workshop(root, root / 'history.sqlite3', Agent()), peer, -100123)
                group.start()
                group.poll_once(0)
                while group.work_once():
                    pass
                self.assertEqual(received[-1], '@workshop_bot')
                self.assertIsNone(group.history()[-1]['addressed_message_id'])
                self.assertTrue(all(item['text'] == 'Уточнение по истории' for item in peer.sent))
                self.assertEqual(group.history()[-1]['result']['status'], 'answered')
