import io
import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from workshop_bot.service import Workshop

from workshop_bot.tools import TurnTools, serve


class FactCorrectionTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        self.path = self.root / "docs/agent-contract.md"
        self.path.parent.mkdir()
        self.before = "| cabinet | @cabinet_example |\n"
        self.after = self.before + "| workshop | @owner_example |\n"
        self.path.write_text("# Operators\n\n" + self.before, encoding="utf-8")
        state = self.root / "private/history.sqlite3"
        state.parent.mkdir()
        self.context = {"root": str(self.root), "state": str(state), "request_id": "confirmed-contact",
                        "conversation": "group:10", "source": {"sender": {"username": "owner_example"},
                        "message_id": 17}}
        self.tools = TurnTools(self.context)

    def test_requested_contact_is_saved_once_with_source_and_change_history(self):
        document = self.tools.read_document("docs/agent-contract.md")
        arguments = {"path": "docs/agent-contract.md", "version": document["version"],
                     "before": self.before, "after": self.after,
                     "evidence": "The participant confirmed their existing Workshop responsibility."}
        incoming = io.StringIO(json.dumps({"jsonrpc": "2.0", "id": 1, "method": "tools/call",
                                          "params": {"name": "correct_fact", "arguments": arguments}}) + "\n")
        outgoing = io.StringIO()
        serve(self.context, incoming, outgoing)
        reply = json.loads(outgoing.getvalue())["result"]
        self.assertFalse(reply.get("isError"), reply)
        applied = json.loads(reply["content"][0]["text"])
        self.assertEqual(applied["status"], "applied")
        self.assertEqual(self.path.read_text(encoding="utf-8").count("| workshop |"), 1)
        self.path.write_text(self.path.read_text(encoding="utf-8") + "Unrelated later note\n", encoding="utf-8")
        self.assertEqual(self.tools.correct_fact(**arguments), applied)
        self.assertIn("Unrelated later note", self.path.read_text(encoding="utf-8"))
        changes = self.tools.fact_changes()
        self.assertEqual(len(changes), 1)
        self.assertEqual(changes[0]["source"]["message_id"], 17)
        self.assertEqual(changes[0]["before"], self.before)
        self.assertEqual(changes[0]["after"], self.after)

    def correction(self):
        return {"path": "docs/agent-contract.md",
                "version": self.tools.read_document("docs/agent-contract.md")["version"],
                "before": self.before, "after": self.after, "evidence": "Confirmed by the participant."}

    def test_changed_document_requires_rereading_without_overwriting_other_work(self):
        arguments = self.correction()
        self.path.write_text(self.path.read_text(encoding="utf-8") + "New decision\n", encoding="utf-8")
        unchanged = self.path.read_bytes()
        with self.assertRaisesRegex(ValueError, "changed"):
            self.tools.correct_fact(**arguments)
        self.assertEqual(self.path.read_bytes(), unchanged)
        self.assertEqual(self.tools.fact_changes(), [])

    def test_instructions_managed_records_and_redirected_files_are_outside_the_tool(self):
        for path in ("local.rules.md", "../docs/agent-contract.md", "docs/tickets/example.md",
                     "docs/requests/telegram.md", "docs/board-review.md", "docs/contracts/example.md"):
            with self.subTest(path=path), self.assertRaises(ValueError):
                self.tools.read_document(path)
        linked = self.root / "linked.md"
        os.link(self.path, linked)
        with self.assertRaisesRegex(ValueError, "hard-linked"):
            self.tools.correct_fact(**self.correction())

    def test_applied_write_recovers_after_lost_completion_receipt(self):
        arguments = self.correction()
        with patch("workshop_bot.tools.os.fsync", side_effect=OSError("completion interrupted")):
            with self.assertRaises(OSError):
                self.tools.correct_fact(**arguments)
        restarted = TurnTools(self.context)
        self.assertEqual(restarted.correct_fact(**arguments)["status"], "applied")
        self.assertEqual(self.path.read_text(encoding="utf-8").count("| workshop |"), 1)
        self.assertEqual(restarted.fact_changes()[0]["status"], "applied")

    def test_uncertain_recovery_preserves_a_later_edit(self):
        arguments = self.correction()
        with patch("workshop_bot.tools.os.fsync", side_effect=OSError("completion interrupted")):
            with self.assertRaises(OSError):
                self.tools.correct_fact(**arguments)
        self.path.write_text("An intervening operator edit\n", encoding="utf-8")
        restarted = TurnTools(self.context)
        self.assertEqual(restarted.correct_fact(**arguments)["status"], "uncertain")
        self.assertEqual(self.path.read_text(encoding="utf-8"), "An intervening operator edit\n")

    def test_operator_history_contains_the_applied_passage_and_its_source(self):
        class Agent:
            tools_enabled = True
            def chat(agent, *args, **kwargs):
                context = json.loads(Path(kwargs["tool_context"]).read_text(encoding="utf-8"))
                tools = TurnTools(context)
                arguments = self.correction()
                tools.correct_fact(**arguments)
                return {"status": "answered", "answer": "Contact corrected."}
        app = Workshop(self.root, Path(self.context["state"]), Agent())
        result = app.ask("history-proof", "Record my existing responsibility", sender='{"username":"owner_example"}',
                         conversation={"current": {"message_id": 17, "addressing": "direct"}})
        self.assertEqual(result["status"], "answered")
        self.assertEqual(result["changes"][0]["source"]["sender"]["username"], "owner_example")
        self.assertEqual(app.history()[-1]["result"]["changes"][0]["after"], self.after)
