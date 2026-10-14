import json
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from workshop_bot.codex import Codex
from workshop_bot.service import Workshop


class MemoryTests(unittest.TestCase):
    def test_chat_reads_and_writes_plain_memory_without_a_source_bundle(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)

            class Agent:
                def chat(self, repository, memory, private, question, conversation):
                    self.assertions = (repository == root, conversation == {"messages": []})
                    self.before = memory.read_text(encoding="utf-8")
                    memory.write_text("# Память\nВстреча в четверг.\n", encoding="utf-8")
                    return {"status": "answered", "answer": "Запомнил встречу."}

            agent = Agent()
            app = Workshop(root, root / "private/history.sqlite3", agent)
            app.memory.write_text("# Память\nПредыдущая заметка.\n", encoding="utf-8")
            with patch.object(app, "context", side_effect=AssertionError("fixed bundle used")):
                result = app.ask("one", "Запомни встречу", conversation={"messages": []})
            self.assertEqual(result["status"], "answered")
            self.assertTrue(all(agent.assertions))
            self.assertIn("Предыдущая заметка", agent.before)
            self.assertIn("Встреча в четверг", app.memory.read_text(encoding="utf-8"))
            app.memory.write_text("Изменено оператором", encoding="utf-8")
            self.assertEqual(app.ask("one", "Запомни встречу", conversation={"messages": []}), result)
            self.assertEqual(app.memory.read_text(encoding="utf-8"), "Изменено оператором")
            self.assertFalse((root / "private/memory.json").exists())

    def test_codex_uses_plain_final_text_and_only_memory_is_writable(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            memory = root / "MEMORY.md"
            private = root / "private"
            def run(command, **kwargs):
                self.assertNotIn("--output-schema", command)
                self.assertEqual(command[command.index("shell_tool") - 1], "--enable")
                self.assertIn("--ignore-user-config", command)
                self.assertIn("--ignore-rules", command)
                self.assertIn('approval_policy="never"', command)
                profile = next(c for c in command if c.startswith("permissions.workshop.filesystem="))
                self.assertIn(json.dumps(str(memory)) + '="write"', profile)
                self.assertEqual(profile.count('="write"'), 1)
                self.assertIn(json.dumps(str(private)) + '="deny"', profile)
                Path(command[command.index("--output-last-message") + 1]).write_text("Обычный ответ.", encoding="utf-8")
                return subprocess.CompletedProcess(command, 0, '{"type":"turn.completed"}\n', '')
            with patch("workshop_bot.codex.subprocess.run", side_effect=run):
                result = Codex().chat(root, memory, private, "Вопрос", None)
            self.assertEqual(result["answer"], "Обычный ответ.")

    def test_failed_turn_does_not_claim_memory_was_unchanged(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            with patch("workshop_bot.codex.subprocess.run", return_value=subprocess.CompletedProcess([], 1, '', 'error: failed')):
                with self.assertRaisesRegex(RuntimeError, "memory may have changed"):
                    Codex().chat(root, root / "MEMORY.md", root / "private", "Вопрос", None)


if __name__ == "__main__":
    unittest.main()
