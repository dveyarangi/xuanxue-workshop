import json
import os
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from workshop_bot.quick import decide


class QuickModelTests(unittest.TestCase):
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
