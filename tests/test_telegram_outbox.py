import tempfile
import unittest
import threading
from pathlib import Path

from workshop_bot.service import Workshop
from workshop_bot.telegram import Group
from workshop_bot.telegram_api import TelegramError
from tests.test_telegram import TelegramPeer, message


class OutboxTests(unittest.TestCase):
    def test_lost_confirmation_and_process_interruption_never_resend(self):
        for error in (TimeoutError("lost"), SystemExit("crashed"), TelegramError(403)):
            with self.subTest(error=type(error).__name__), tempfile.TemporaryDirectory() as temporary:
                root = Path(temporary)

                class Faulty(TelegramPeer):
                    def call(self, method, **parameters):
                        if method == "sendMessage":
                            self.sent.append(parameters)
                            raise error
                        return super().call(method, **parameters)

                peer = Faulty()
                group = Group(Workshop(root, root / "state.sqlite3", None), peer, -100123)
                group.check_group()
                group.outbox.register("dns", "@kotlarewski")
                try:
                    group.outbox.send("dns-1", "dns", "Нужен адрес")
                except SystemExit:
                    pass
                restarted = Group(group.workshop, peer, -100123)
                restarted.check_group()
                result = restarted.outbox.send("dns-1", "dns", "Нужен адрес")
                self.assertEqual(result["status"], "rejected" if isinstance(error, TelegramError) else "uncertain")
                self.assertEqual(len(peer.sent), 1)
                self.assertIsNone(result["message_url"])

    def test_concurrent_duplicate_cannot_send_again(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            entered, release = threading.Event(), threading.Event()

            class Waiting(TelegramPeer):
                def call(self, method, **parameters):
                    if method == "sendMessage":
                        entered.set()
                        if not release.wait(5):
                            raise TimeoutError()
                    return super().call(method, **parameters)

            group = Group(Workshop(root, root / "state.sqlite3", None), Waiting(), -100123)
            group.check_group()
            group.outbox.register("daychi", "@stnleo")
            results = []
            worker = threading.Thread(target=lambda: results.append(group.outbox.send("one", "daychi", "Вопрос")))
            worker.start()
            try:
                self.assertTrue(entered.wait(5))
                other = Group(group.workshop, group.api, -100123)
                other.check_group()
                self.assertEqual(other.outbox.send("one", "daychi", "Вопрос")["status"], "uncertain")
            finally:
                release.set()
                worker.join(6)
            self.assertEqual(results[0]["status"], "sent")
            self.assertEqual(len(group.api.sent), 1)

    def test_sender_startup_does_not_reset_an_active_group_request(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            entered, release = threading.Event(), threading.Event()

            def agent(context):
                entered.set()
                release.wait(5)
                return {"disposition": "answer", "answer": "Ответ", "reason": "", "sources": [], "edit": None}

            group = Group(Workshop(root, root / "state.sqlite3", agent), TelegramPeer([message()]), -100123)
            group.start()
            group.poll_once(0)
            worker = threading.Thread(target=group.work_once)
            worker.start()
            try:
                self.assertTrue(entered.wait(5))
                sender = Group(group.workshop, group.api, -100123)
                sender.check_group()
                self.assertEqual(sender.history()[0]["status"], "processing")
            finally:
                release.set()
                worker.join(6)
            self.assertFalse(worker.is_alive())
            self.assertEqual(group.history()[0]["status"], "sent")

    def test_unknown_recipient_secret_and_oversized_message_never_send(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            group = Group(Workshop(root, root / "state.sqlite3", None), TelegramPeer(), -100123)
            group.check_group()
            group.outbox.register("daychi", "@stnleo")
            for recipient, body in (("unknown", "Hello"), ("daychi", "😀" * 2000),
                                    ("daychi", "sk-" + "x" * 30)):
                with self.subTest(recipient=recipient), self.assertRaises(ValueError):
                    group.outbox.send("one", recipient, body)
            self.assertEqual(group.api.sent, [])
            self.assertEqual(group.outbox.history(), [])

    def test_reply_to_operator_message_retains_its_context(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            contexts = []

            def agent(context):
                contexts.append(context)
                return {"disposition": "answer", "answer": "Спасибо за ответ.", "reason": "", "sources": [], "edit": None}

            group = Group(Workshop(root, root / "state.sqlite3", agent), TelegramPeer(), -100123)
            group.start()
            group.outbox.register("daychi", "@stnleo")
            sent = group.outbox.send("question-1", "daychi", "Когда можно проверить вход?")
            reply = message(200, "Завтра утром")
            reply["message"]["entities"] = []
            reply["message"]["reply_to_message"] = {"message_id": sent["message_id"]}
            group.api.updates = [reply]
            group.poll_once(0)
            self.assertTrue(group.work_once())
            self.assertEqual(contexts[0]["conversation"]["current"]["conversation_id"], sent["message_id"])
            self.assertTrue(any("Когда можно проверить вход?" in item["text"]
                                for item in contexts[0]["conversation"]["messages"]))

    def test_registered_operator_gets_one_mention_and_duplicate_survives_restart(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            app = Workshop(root, root / "state.sqlite3", None)
            peer = TelegramPeer()
            group = Group(app, peer, -100123)
            group.check_group()
            group.outbox.register("cabinet", "@kotlarewski")
            result = group.outbox.send("cabinet-question-1", "cabinet", "Нужен ответ по входу <текст> 😀")
            self.assertEqual(result["status"], "sent")
            self.assertEqual(result["message_url"], "https://t.me/c/123/101")
            sent = peer.sent[0]
            self.assertEqual(sent["chat_id"], -100123)
            self.assertTrue(sent["text"].startswith("@kotlarewski"))
            self.assertIn("<текст> 😀", sent["text"])
            self.assertNotIn("parse_mode", sent)
            self.assertEqual(sent["entities"], [{"type": "mention", "offset": 0, "length": 12}])
            resumed = Group(Workshop(root, root / "state.sqlite3", None), peer, -100123)
            resumed.check_group()
            self.assertEqual(resumed.outbox.send("cabinet-question-1", "cabinet",
                                                 "Нужен ответ по входу <текст> 😀"), result)
            self.assertEqual(len(peer.sent), 1)
            self.assertEqual(resumed.outbox.history()[0]["body"], "Нужен ответ по входу <текст> 😀")
            with self.assertRaises(ValueError):
                resumed.outbox.send("cabinet-question-1", "cabinet", "Иной текст")


if __name__ == "__main__":
    unittest.main()
