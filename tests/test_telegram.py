import json
import tempfile
import unittest
import threading
import sqlite3
from pathlib import Path

from workshop_bot.service import Workshop
from workshop_bot.telegram import Group
from workshop_bot.telegram_api import TelegramError
from workshop_bot.telegram_runtime import serve, receiver_lease


class TelegramPeer:
    def __init__(self, updates=()):
        self.updates = list(updates)
        self.sent = []

    def call(self, method, **parameters):
        if method == "getMe":
            return {"id": 42, "is_bot": True, "username": "workshop_bot", "can_read_all_group_messages": True}
        if method == "getWebhookInfo":
            return {"url": ""}
        if method == "getChat":
            return {"id": -100123, "type": "supergroup"}
        if method == "getChatMember":
            return {"status": "member"}
        if method == "getUpdates":
            result, self.updates = self.updates, []
            return result
        if method == "sendMessage":
            self.sent.append(parameters)
            return {"message_id": 100 + len(self.sent), "chat": {"id": parameters["chat_id"]}}
        raise AssertionError(method)


def message(update=1, text="@workshop_bot Кто владеет проектами?", chat=-100123):
    return {"update_id": update, "message": {
        "message_id": update + 10, "date": 1791780000,
        "chat": {"id": chat, "type": "supergroup"},
        "from": {"id": 7, "first_name": "Anna", "username": "anna"},
        "message_thread_id": 9, "text": text,
        "entities": [{"type": "mention", "offset": 0, "length": 13}]}}


class GroupTests(unittest.TestCase):
    def test_existing_history_is_preserved_and_an_old_reply_survives_context_limits(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            state = root / "state.sqlite3"
            with sqlite3.connect(state) as db:
                db.execute("CREATE TABLE telegram_requests (update_id INTEGER PRIMARY KEY, message_id INTEGER UNIQUE, "
                           "sender TEXT, created TEXT, body TEXT, thread_id INTEGER, status TEXT, result TEXT, "
                           "sent_ids TEXT DEFAULT '[]', error TEXT, parts TEXT DEFAULT '[]', "
                           "attempts INTEGER DEFAULT 0, retry_at REAL DEFAULT 0)")
                db.execute("INSERT INTO telegram_requests "
                           "(update_id,message_id,sender,created,body,status,result,sent_ids,parts) "
                           "VALUES (1,11,'{}','2026-10-12','Первый вопрос','sent',?, '[101]', ?)",
                           (json.dumps({"answer": "Первый ответ"}), json.dumps(["Первый ответ"])))
            db.close()
            calls = []

            def agent(context):
                calls.append(context)
                return {"disposition": "answer", "answer": "Ответ", "reason": "", "sources": [], "edit": None}

            updates = [message(i, "Ж" * 4000) for i in range(200, 240)]
            for update in updates:
                update["message"]["entities"] = []
            reply = message(300, "Продолжим первый вопрос")
            reply["message"]["entities"] = []
            reply["message"]["reply_to_message"] = {"message_id": 101}
            group = Group(Workshop(root, state, agent), TelegramPeer([*updates, reply]), -100123)
            group.start()
            group.poll_once(0)
            self.assertTrue(group.work_once())
            context = calls[0]["conversation"]
            self.assertGreater(context["omitted_messages"], 0)
            self.assertTrue(any(m["text"] == "Первый ответ" for m in context["messages"]))
            self.assertTrue(any(m["text"] == "Первый вопрос" for m in context["messages"]))
            self.assertLessEqual(len(json.dumps(context["messages"], ensure_ascii=False).encode("utf-8")), 120_000)
            self.assertEqual(len(group.history()), 42)
            self.assertEqual(group.history()[0]["sent_ids"], [101])

    def test_another_member_can_reply_after_restart_with_group_and_bot_history(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            calls = []

            def agent(context):
                calls.append(context)
                return {"disposition": "answer", "answer": "План: начать в пятницу.",
                        "reason": "", "sources": [], "edit": None}

            app = Workshop(root, root / "state.sqlite3", agent)
            group = Group(app, TelegramPeer([message()]), -100123)
            group.start()
            group.poll_once(0)
            group.work_once()
            reply = message(200, "А во сколько?")
            reply["message"]["entities"] = []
            reply["message"]["from"] = {"id": 8, "first_name": "Boris"}
            reply["message"]["reply_to_message"] = {"message_id": 101, "text": "UNTRUSTED nested quote"}
            future = message(201, "FUTURE discussion")
            future["message"]["entities"] = []
            peer = TelegramPeer([reply, future])
            resumed = Group(Workshop(root, root / "state.sqlite3", agent), peer, -100123)
            resumed.start()
            resumed.poll_once(0)
            self.assertTrue(resumed.work_once())
            self.assertFalse(resumed.work_once())
            self.assertEqual(len(calls), 2)
            history = calls[1]["conversation"]
            self.assertEqual(history["current"]["reply_to"], 101)
            self.assertEqual(history["current"]["conversation_id"], 11)
            self.assertEqual(history["current"]["sender"]["id"], 8)
            self.assertEqual([m["role"] for m in history["messages"]], ["user", "assistant"])
            self.assertIn("План: начать в пятницу.", json.dumps(history, ensure_ascii=False))
            self.assertNotIn("FUTURE", json.dumps(history))
            self.assertNotIn("UNTRUSTED", json.dumps(history))
            self.assertEqual(peer.sent[0]["reply_parameters"]["message_id"], 210)

    def test_process_interruption_during_send_is_visible_after_restart(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)

            class Interrupted(TelegramPeer):
                def call(self, method, **parameters):
                    if method == "sendMessage":
                        raise SystemExit("Interrupted before local acknowledgement")
                    return super().call(method, **parameters)

            app = Workshop(root, root / "state.sqlite3", lambda context: {
                "disposition": "answer", "answer": "Ответ", "reason": "", "sources": [], "edit": None})
            group = Group(app, Interrupted([message()]), -100123)
            group.start()
            group.poll_once(0)
            with self.assertRaises(SystemExit):
                group.work_once()
            peer = TelegramPeer()
            resumed = Group(app, peer, -100123)
            resumed.start()
            self.assertFalse(resumed.work_once())
            self.assertEqual(resumed.history()[0]["status"], "uncertain")
            self.assertEqual(peer.sent, [])

    def test_polling_retains_the_next_request_while_codex_is_busy(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            entered, received, release, stop = (threading.Event() for _ in range(4))
            errors = []

            def agent(context):
                entered.set()
                self.assertTrue(release.wait(5))
                return {"disposition": "answer", "answer": "Ответ", "reason": "", "sources": [], "edit": None}

            class Arrivals(TelegramPeer):
                polls = 0

                def call(self, method, **parameters):
                    if method == "getUpdates":
                        self.polls += 1
                        if self.polls == 1:
                            return [message()]
                        if self.polls == 2:
                            entered.wait(5)
                            return [message(2)]
                        received.set()
                        stop.wait(0.02)
                        return []
                    return super().call(method, **parameters)

            group = Group(Workshop(root, root / "state.sqlite3", agent), Arrivals(), -100123)

            def run():
                try:
                    serve(group, stop=stop)
                except BaseException as error:
                    errors.append(error)

            worker = threading.Thread(target=run)
            worker.start()
            try:
                self.assertTrue(received.wait(5))
                self.assertEqual(len(group.history()), 2)
                self.assertEqual(group.history()[1]["status"], "queued")
                with self.assertRaises((RuntimeError, OSError)):
                    with receiver_lease(group.workshop.state):
                        self.fail("Second receiver acquired the same history")
            finally:
                stop.set()
                release.set()
                worker.join(6)
            self.assertFalse(worker.is_alive())
            self.assertEqual(errors, [])

    def test_existing_webhook_stops_start_without_deleting_it(self):
        with tempfile.TemporaryDirectory() as temporary:
            class ExistingReceiver(TelegramPeer):
                def call(self, method, **parameters):
                    if method == "getWebhookInfo":
                        return {"url": "https://existing.example/webhook"}
                    return super().call(method, **parameters)

            root = Path(temporary)
            group = Group(Workshop(root, root / "state.sqlite3", None), ExistingReceiver(), -100123)
            with self.assertRaisesRegex(ValueError, "webhook"):
                group.start()

    def test_bare_reference_reaches_agent_with_history_and_typing(self):
        received, actions = [], []

        class Agent:
            def chat(self, root, memory, private, question, conversation, **kwargs):
                received.append((question, conversation))
                self_typing = actions[-1]
                assert self_typing == 'sendChatAction'
                return {'status': 'answered', 'answer': 'Что вы хотите узнать?'}

        class Peer(TelegramPeer):
            def call(self, method, **parameters):
                actions.append(method)
                if method == 'sendChatAction':
                    return True
                return super().call(method, **parameters)

        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            app = Workshop(root, root / "state.sqlite3", Agent())
            peer = Peer([message(text="@workshop_bot")])
            group = Group(app, peer, -100123)
            group.start()
            group.poll_once(0)
            group.work_once()
            self.assertEqual(received[0][0], '@workshop_bot')
            self.assertEqual(received[0][1]['messages'], [])
            self.assertEqual(peer.sent[0]['text'], 'Что вы хотите узнать?')

    def test_long_reply_survives_rate_limit_without_repeating_confirmed_parts(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            answer = "😀" * 2400

            class Limited(TelegramPeer):
                limited = False

                def call(self, method, **parameters):
                    if method == "sendMessage" and len(self.sent) == 1 and not self.limited:
                        self.limited = True
                        raise TelegramError(429, retry_after=0)
                    return super().call(method, **parameters)

            app = Workshop(root, root / "state.sqlite3", lambda context: {
                "disposition": "answer", "answer": answer, "reason": "", "sources": [], "edit": None})
            peer = Limited([message()])
            group = Group(app, peer, -100123)
            group.start()
            group.poll_once(0)
            for _ in range(5):
                group.work_once()
            self.assertEqual(group.history()[0]["status"], "sent")
            self.assertTrue(peer.limited)
            self.assertEqual("".join(item["text"] for item in peer.sent), answer)
            self.assertTrue(all(len(item["text"].encode("utf-16-le")) // 2 <= 4096 for item in peer.sent))

    def test_group_discussion_is_context_but_only_real_references_get_answers(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            contexts = []

            def agent(context):
                contexts.append(context)
                return {"disposition": "answer", "answer": "Ответ", "reason": "", "sources": [], "edit": None}

            ordinary = message(1, "Обсуждаем запуск в пятницу")
            ordinary["message"]["entities"] = []
            elsewhere = message(2, "@workshop_bot PRIVATE other group", chat=-100999)
            linked = message(3)
            linked["message"].pop("text")
            linked["message"].pop("entities")
            linked["message"]["caption"] = "😀 бот, что готово?"
            linked["message"]["caption_entities"] = [{"type": "text_link", "offset": 3, "length": 3,
                                                      "url": "https://t.me/workshop_bot"}]
            linked["message"]["reply_to_message"] = {"text": "PRIVATE unrelated quote"}
            spoof = message(4)
            spoof["message"]["entities"] = [{"type": "text_link", "offset": 0, "length": 13,
                                              "url": "https://t.me.evil.example/workshop_bot"}]
            app = Workshop(root, root / "state.sqlite3", agent)
            group = Group(app, TelegramPeer([ordinary, elsewhere, linked, spoof]), -100123)
            group.start()
            group.poll_once(0)
            while group.work_once():
                pass
            self.assertEqual(len(contexts), 1)
            self.assertEqual(len(group.history()), 3)
            self.assertIn("Обсуждаем запуск в пятницу", json.dumps(contexts, ensure_ascii=False))
            self.assertEqual([r["status"] for r in group.history()], ["observed", "sent", "observed"])
            self.assertNotIn("PRIVATE", json.dumps([contexts, group.history(), app.history()]))

    def test_uncertain_send_is_not_repeated_after_restart_and_next_request_runs(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            calls = []

            def agent(context):
                calls.append(context)
                return {"disposition": "answer", "answer": "Ответ", "reason": "", "sources": [], "edit": None}

            class LostAcknowledgement(TelegramPeer):
                def call(self, method, **parameters):
                    if method == "sendMessage":
                        self.sent.append(parameters)
                        raise TimeoutError("Response lost")
                    return super().call(method, **parameters)

            app = Workshop(root, root / "state.sqlite3", agent)
            peer = LostAcknowledgement([message()])
            group = Group(app, peer, -100123)
            group.start()
            group.poll_once(0)
            self.assertTrue(group.work_once())
            self.assertEqual(group.history()[0]["status"], "uncertain")
            resumed_peer = TelegramPeer([message(), message(2)])
            resumed = Group(app, resumed_peer, -100123)
            resumed.start()
            resumed.poll_once(0)
            self.assertTrue(resumed.work_once())
            self.assertFalse(resumed.work_once())
            self.assertEqual(len(calls), 2)
            self.assertEqual(len(resumed_peer.sent), 1)
            self.assertEqual([row["status"] for row in resumed.history()], ["uncertain", "sent"])

    def test_group_request_gets_a_reply_and_inspectable_history(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            calls = []

            def agent(context):
                calls.append(context)
                return {"disposition": "answer", "answer": "Проекты отвечают за свою реализацию.",
                        "reason": "", "sources": [], "edit": None}

            app = Workshop(root, root / "state.sqlite3", agent)
            peer = TelegramPeer([message()])
            group = Group(app, peer, -100123)
            group.start()
            group.poll_once(timeout=0)
            self.assertTrue(group.work_once())
            self.assertEqual(len(calls), 1)
            self.assertEqual(peer.sent[0]["reply_parameters"], {"message_id": 11})
            self.assertEqual(peer.sent[0]["message_thread_id"], 9)
            self.assertEqual(peer.sent[0]["chat_id"], -100123)
            history = group.history()
            self.assertEqual(history[0]["status"], "sent")
            self.assertEqual(history[0]["sender"]["id"], 7)
            self.assertEqual(history[0]["message_url"], "https://t.me/c/123/11")
            self.assertIn("Проекты отвечают", history[0]["result"]["answer"])


if __name__ == "__main__":
    unittest.main()
