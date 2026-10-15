import tempfile
import threading
import unittest
from pathlib import Path
from unittest.mock import patch

from tests.test_telegram import TelegramPeer, message
from workshop_bot.service import Workshop
from workshop_bot.telegram import Group
from workshop_bot.telegram_api import TelegramError


class TypingTests(unittest.TestCase):
    def test_typing_renews_during_answer_in_the_same_topic_and_stops_afterwards(self):
        renewed = threading.Event()
        actions = []

        class Peer(TelegramPeer):
            def call(self, method, **parameters):
                if method == 'sendChatAction':
                    actions.append(parameters)
                    if len(actions) >= 2:
                        renewed.set()
                    return True
                return super().call(method, **parameters)

        class Agent:
            def chat(self, *args, **kwargs):
                if not renewed.wait(2):
                    raise RuntimeError('No renewed typing indicator while preparing the answer')
                return {'status': 'answered', 'answer': 'Done'}

        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            peer = Peer([message()])
            group = Group(Workshop(root, root / 'history.sqlite3', Agent()), peer, -100123)
            group.start()
            group.poll_once(0)
            with patch('workshop_bot.telegram.TYPING_INTERVAL', 0.01, create=True):
                group.work_once()
            self.assertEqual(peer.sent[0]['text'], 'Done')
            self.assertGreaterEqual(len(actions), 2)
            self.assertTrue(all(a == {'chat_id': -100123, 'message_thread_id': 9, 'action': 'typing'} for a in actions))
            self.assertFalse(any(t.name == 'telegram-typing' for t in threading.enumerate()))

    def test_typing_failure_does_not_prevent_answer_and_background_messages_do_not_type(self):
        actions = []

        class Peer(TelegramPeer):
            def call(self, method, **parameters):
                if method == 'sendChatAction':
                    actions.append(parameters)
                    raise TelegramError(429, retry_after=30)
                return super().call(method, **parameters)

        class Agent:
            def chat(self, *args, **kwargs):
                return {'status': 'answered', 'answer': 'Done'}

        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            peer = Peer([message(text='Обычное сообщение')])
            group = Group(Workshop(root, root / 'history.sqlite3', Agent()), peer, -100123)
            group.start()
            group.poll_once(0)
            self.assertFalse(group.work_once())
            self.assertEqual(actions, [])
            peer.updates.append(message(update=2))
            group.poll_once(0)
            group.work_once()
            self.assertEqual(peer.sent[0]['text'], 'Done')
            self.assertEqual(len(actions), 1)
