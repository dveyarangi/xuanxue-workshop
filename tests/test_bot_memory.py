import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from workshop_bot.service import Workshop
from workshop_bot.telegram import Group
from tests.test_telegram import TelegramPeer, message


class MemoryTests(unittest.TestCase):
    def test_memory_conflict_and_invented_source_leave_existing_memory_unchanged(self):
        for source_id in (11, 999):
            with self.subTest(source_id=source_id), tempfile.TemporaryDirectory() as temporary:
                root = Path(temporary)
                app = Workshop(root, root / "state.sqlite3", lambda context: {
                    "disposition": "answer", "answer": "Новые сведения.", "reason": "", "sources": [], "edit": None,
                    "memory_updates": [{"kind": "fact", "key": "new-fact", "value": "Другое сведение", "source_message_id": source_id},
                                       {"kind": "contact", "key": "daychi", "value": "@someone", "source_message_id": source_id}]})
                group = Group(app, TelegramPeer([message()]), -100123)
                group.outbox.register("daychi", "@stnleo")
                before = app.memory.path.read_bytes()
                group.start()
                group.poll_once(0)
                group.work_once()
                self.assertEqual(app.memory.path.read_bytes(), before)
                self.assertEqual(group.history()[0]["result"]["status"], "clarification" if source_id == 11 else "failed")

    def test_failed_memory_replacement_preserves_the_existing_file(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            app = Workshop(root, root / "state.sqlite3", None)
            old = {"kind": "fact", "key": "one", "value": "Первый факт", "source": {"channel": "codex"}}
            app.memory.append([old])
            before = app.memory.path.read_bytes()
            with patch("workshop_bot.memory.os.replace", side_effect=OSError("write failed")):
                with self.assertRaises(OSError):
                    app.memory.append([{**old, "key": "two", "value": "Второй факт"}])
            self.assertEqual(app.memory.path.read_bytes(), before)

    def test_group_fact_is_saved_with_source_and_reaches_the_next_answer(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            contexts = []

            def agent(context):
                contexts.append(context)
                return {"disposition": "answer", "answer": "За расписание отвечает Анна.",
                        "reason": "", "sources": [], "edit": None,
                        "memory_updates": [{"kind": "fact", "key": "schedule-owner",
                                            "value": "За расписание отвечает Анна.", "source_message_id": 11}]
                                          if len(contexts) == 1 else []}

            app = Workshop(root, root / "state.sqlite3", agent)
            ordinary = message(1, "За расписание отвечает Анна.")
            ordinary["message"]["entities"] = []
            peer = TelegramPeer([ordinary, message(2, "@workshop_bot Запомни, кто отвечает за расписание")])
            group = Group(app, peer, -100123)
            group.start()
            group.poll_once(0)
            group.work_once()
            self.assertTrue((root / "memory.json").is_file())
            remembered = app.memory.read()[0]
            self.assertEqual(remembered["source"]["message_id"], 11)
            self.assertEqual(remembered["source"]["sender"]["id"], 7)
            self.assertIn("Запомнил", peer.sent[0]["text"])
            app.ask("next-question", "Кто отвечает за расписание?")
            self.assertEqual(contexts[1]["memory"], [remembered])


if __name__ == "__main__":
    unittest.main()
