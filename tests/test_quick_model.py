import json
import os
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from workshop_bot.quick import decide


class QuickModelTests(unittest.TestCase):
    def test_continuation_schema_and_context_keep_the_confirmed_answer(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            def invoke(command, **kwargs):
                schema = json.loads(Path(command[command.index("--output-schema") + 1]).read_text())
                self.assertEqual(schema["properties"]["continue_with"]["enum"], [None, 101])
                self.assertIn("work", schema["properties"]["route"]["enum"])
                data = json.loads(kwargs["input"])
                self.assertIn(101, [m["message_id"] for m in data["messages"]])
                Path(command[command.index("--output-last-message") + 1]).write_text(json.dumps({
                    "route": "work", "answer": "", "reason": "accepted offer", "continue_with": 101}))
                return subprocess.CompletedProcess(command, 0, '{"type":"turn.completed"}\n', '')
            with patch("workshop_bot.quick.subprocess.run", side_effect=invoke):
                decision = decide("codex.exe", root, root / "memory.md", "рассказывай", {
                    "current": {"addressing": "ambient"},
                    "continuations": [{"message_id": 101, "conversation_id": 11}],
                    "messages": [{"message_id": 101, "text": "Рассказать о задачах?"}]})
            self.assertEqual(decision["continue_with"], 101)

    def test_implicit_greeting_schema_can_only_acknowledge_or_ignore(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            def invoke(command, **kwargs):
                schema = json.loads(Path(command[command.index("--output-schema") + 1]).read_text())
                self.assertEqual(schema["properties"]["route"]["enum"], ["offer", "ignore"])
                self.assertEqual(schema["properties"]["answer"]["maxLength"], 320)
                Path(command[command.index("--output-last-message") + 1]).write_text(
                    json.dumps({"route": "offer", "answer": "Да, я здесь.", "reason": "addressed greeting"}),
                    encoding="utf-8")
                return subprocess.CompletedProcess(command, 0, '{"type":"turn.completed"}\n', '')
            with patch("workshop_bot.quick.subprocess.run", side_effect=invoke):
                result = decide("codex.exe", root, root / "memory.md", "дух воркшопа, ты здесь?",
                                {"current": {"addressing": "ambient"}})
            self.assertEqual(result["route"], "offer")
            self.assertEqual(result["answer"], "Да, я здесь.")

    def test_bounded_input_is_separate_from_tool_enabled_executor_and_environment(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            memory = root / "memory.md"
            memory.write_text("known memory", encoding="utf-8")
            messages = [{"message_id": i, "text": "x" * 1000, "thread_id": 9} for i in range(100)]

            def invoke(command, **kwargs):
                self.assertNotEqual(Path(kwargs["cwd"]), root)
                self.assertNotIn("TELEGRAM_BOT_TOKEN", kwargs["env"])
                self.assertIn("gpt-6-luna", command)
                self.assertIn('model_reasoning_effort="low"', command)
                self.assertIn("--ephemeral", command)
                self.assertNotIn("--enable", command)
                schema = json.loads(Path(command[command.index("--output-schema") + 1]).read_text())
                self.assertEqual(schema["properties"]["route"]["enum"], ["answer", "work"])
                self.assertEqual(schema["properties"]["answer"]["maxLength"], 2000)
                data = json.loads(kwargs["input"])
                self.assertEqual(data["current"]["addressing"], "direct")
                self.assertIn(0, [m["message_id"] for m in data["messages"]])
                self.assertGreater(data["omitted_messages"], 0)
                self.assertLess(len(kwargs["input"]), 20000)
                output = Path(command[command.index("--output-last-message") + 1])
                output.write_text(json.dumps({"route": "answer", "answer": "Да", "reason": "available"}))
                return subprocess.CompletedProcess(command, 0, '{"type":"turn.completed","usage":{}}\n', '')

            with patch.dict(os.environ, {"TELEGRAM_BOT_TOKEN": "must-not-reach-model"}), \
                    patch("workshop_bot.quick.subprocess.run", side_effect=invoke):
                result = decide("codex.exe", root, memory, "Помнишь?", {
                    "messages": messages, "current": {"reply_to": 0, "thread_id": 9}})
            self.assertEqual(result["route"], "answer")
            self.assertEqual(result["runtime"]["sources"][0]["path"], "memory.md")
