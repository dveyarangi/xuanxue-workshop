import json
import tempfile
import unittest
import uuid
from pathlib import Path

from workshop_bot.service import Workshop
from workshop_bot.telegram import Group
from tests.test_telegram import TelegramPeer, message


class Agent:
    quick_enabled = True

    def __init__(self, route="answer", answer="Да, запрос сохранён."):
        self.route, self.answer = route, answer
        self.quick_calls, self.work_calls = [], []

    def quick(self, root, memory, question, conversation):
        self.quick_calls.append((question, conversation))
        return {"route": self.route, "answer": self.answer, "reason": "test"}

    def chat(self, *args, session_id=None, on_session=None, **kwargs):
        self.work_calls.append(args)
        if on_session:
            on_session(session_id or str(uuid.uuid4()))
        return {"status": "answered", "answer": "Проверенный ответ."}


class QuickTelegramTests(unittest.TestCase):
    def test_implicit_offer_then_reply_is_answered_and_events_are_not_replayed(self):
        with tempfile.TemporaryDirectory() as folder:
            agent = Agent("offer", "Есть информация о входе в Кабинет. Рассказать?")
            app = Workshop(folder, Path(folder) / "private/history.sqlite3", agent)
            initial = message(text="Workshop, что сейчас со входом?")
            peer = TelegramPeer([initial])
            group = Group(app, peer, -100123)
            group.start()
            group.poll_once()
            self.assertTrue(group.work_once())
            self.assertEqual(len(peer.sent), 1)
            self.assertEqual(agent.quick_calls[0][1]["current"]["addressing"], "ambient")
            self.assertFalse(agent.work_calls)
            agent.route, agent.answer = "work", ""
            reply = message(update=2, text="да")
            reply["message"]["reply_to_message"] = {
                "message_id": 101, "from": {"id": 42, "is_bot": True}}
            peer.updates = [initial, reply]
            group.poll_once()
            self.assertTrue(group.work_once())
            self.assertEqual(len(peer.sent), 2)
            self.assertEqual(len(agent.work_calls), 1)
            self.assertEqual(agent.work_calls[0][4]["current"]["conversation_id"], 11)
            self.assertFalse(group.work_once())

    def test_ambient_cannot_start_work_and_failure_stays_silent(self):
        for route in ("ignore", "work", "answer", "invalid"):
            with self.subTest(route=route), tempfile.TemporaryDirectory() as folder:
                agent = Agent(route)
                app = Workshop(folder, Path(folder) / "private/history.sqlite3", agent)
                peer = TelegramPeer([message(text="Anna, как дела?")])
                group = Group(app, peer, -100123)
                group.start()
                group.poll_once()
                group.work_once()
                self.assertFalse(peer.sent)
                self.assertFalse(agent.work_calls)
                self.assertEqual(group.history()[0]["status"], "observed")

    def test_explicit_followup_takes_priority_and_suppresses_late_offer(self):
        with tempfile.TemporaryDirectory() as folder:
            agent = Agent()
            app = Workshop(folder, Path(folder) / "private/history.sqlite3", agent)
            peer = TelegramPeer([message(text="что со входом?"), message(update=2, text="@workshop_bot")])
            group = Group(app, peer, -100123)
            group.start()
            group.poll_once()
            group.work_once()
            self.assertEqual(agent.quick_calls[0][0], "что со входом?")
            group.work_once()
            self.assertEqual(len(peer.sent), 1)
            self.assertEqual(len(agent.quick_calls), 1)

    def test_invalid_quick_reply_falls_back_to_full_worker_only_for_direct_request(self):
        with tempfile.TemporaryDirectory() as folder:
            agent = Agent("ignore", "")
            app = Workshop(folder, Path(folder) / "private/history.sqlite3", agent)
            peer = TelegramPeer([message()])
            group = Group(app, peer, -100123)
            group.start()
            group.poll_once()
            group.work_once()
            self.assertEqual(len(agent.work_calls), 1)
            self.assertEqual(peer.sent[0]["text"], "Проверенный ответ.")

    def test_candidate_survives_restart_and_silent_decision_never_types(self):
        class Peer(TelegramPeer):
            def call(self, method, **parameters):
                if method == "sendChatAction":
                    raise AssertionError("Ambient screening must not display typing")
                return super().call(method, **parameters)

        with tempfile.TemporaryDirectory() as folder:
            agent = Agent("ignore", "")
            app = Workshop(folder, Path(folder) / "private/history.sqlite3", agent)
            peer = Peer([message(text="Спасибо, Анна!")])
            group = Group(app, peer, -100123)
            group.start()
            group.poll_once()
            resumed = Group(app, peer, -100123)
            resumed.start()
            resumed.work_once()
            record = resumed.history()[0]
            self.assertEqual(record["status"], "observed")
            self.assertLessEqual(record["received_at"], record["started_at"])
            self.assertLessEqual(record["started_at"], record["completed_at"])
            self.assertIsNone(record["sent_at"])
            self.assertFalse(peer.sent)

    def test_reply_to_actual_bot_is_direct_even_without_local_sent_id(self):
        with tempfile.TemporaryDirectory() as folder:
            agent = Agent()
            app = Workshop(folder, Path(folder) / "private/history.sqlite3", agent)
            peer = TelegramPeer()
            group = Group(app, peer, -100123)
            group.start()
            update = message(text="да, расскажи")
            update["message"]["reply_to_message"] = {
                "message_id": 6, "from": {"id": 42, "is_bot": True},
                "text": "У меня есть информация о входе в Кабинет."}
            peer.updates = [update]
            group.poll_once()
            self.assertTrue(group.work_once())
            self.assertEqual(len(peer.sent), 1)
            self.assertEqual(agent.quick_calls[0][1]["current"]["addressing"], "direct")
            self.assertIn("информация о входе", agent.quick_calls[0][1]["messages"][0]["text"])
            self.assertFalse(agent.work_calls)
