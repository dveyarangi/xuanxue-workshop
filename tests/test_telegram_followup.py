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

    def test_bare_mention_does_not_reuse_other_sender_topic_old_or_already_addressed_text(self):
        for variant in ('other_sender', 'other_topic', 'old', 'already_addressed', 'explicit_reply'):
            with self.subTest(variant=variant), tempfile.TemporaryDirectory() as temporary:
                root = Path(temporary)
                original = message(text='покажи шаги')
                original['message']['entities'] = []
                if variant == 'other_sender':
                    original['message']['from']['id'] = 99
                if variant == 'other_topic':
                    original['message']['message_thread_id'] = 100
                if variant == 'already_addressed':
                    original = message(text='@workshop_bot')
                mention = message(update=2, text='@workshop_bot')
                mention['message']['date'] += 301 if variant == 'old' else 120
                if variant == 'explicit_reply':
                    mention['message']['reply_to_message'] = {'message_id': 999}
                peer = TelegramPeer([original, mention])
                group = Group(Workshop(root, root / 'history.sqlite3', None), peer, -100123)
                group.start()
                group.poll_once(0)
                while group.work_once():
                    pass
                self.assertTrue(all('Задайте' in item['text'] for item in peer.sent))
                self.assertEqual(group.history()[-1]['result']['status'], 'answered')
