import json
import tempfile
import unittest
import shutil
import os
import subprocess
import sys
from unittest.mock import patch
from pathlib import Path

from workshop_bot.service import Workshop


class WorkshopTests(unittest.TestCase):
    def test_a_source_not_supplied_to_codex_is_rejected_without_claiming_an_edit(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            app = Workshop(root, root / "history.sqlite3", lambda context: {
                "disposition": "answer", "answer": "Unsupported answer", "reason": "",
                "sources": ["docs/not-supplied.md"], "edit": None})
            result = app.ask("unknown-source", "Что ты такое?")
            self.assertEqual(result["status"], "failed")
            self.assertIn("docs/not-supplied.md", result["detail"])
            self.assertNotIn("правк", result["answer"])

    def test_question_record_supplied_to_codex_can_be_cited_in_the_answer(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            name = "docs/questions/q-0001-what-is-workshop.md"
            path = root / name
            path.parent.mkdir(parents=True)
            path.write_text("Workshop coordinates school projects.", encoding="utf-8")

            def agent(context):
                return {"disposition": "answer", "answer": "Я помогаю с проектами школы.",
                        "reason": "Known Workshop purpose", "sources": [name], "edit": None}

            app = Workshop(root, root / "history.sqlite3", agent)
            result = app.ask("identity", "Что ты такое?")
            self.assertEqual(result["status"], "answered", result)
            self.assertEqual(result["sources"], [name])
            self.assertEqual(app.history()[0]["result"], result)

    def editable(self, temporary):
        root = Path(temporary) / "project"
        name = "docs/tickets/01-0020-demo.md"
        path = root / name
        path.parent.mkdir(parents=True)
        path.write_text("# Demo\n\n## What to build\n\nПонятный ответ.\n", encoding="utf-8")
        shutil.copytree(Path(__file__).resolve().parents[1] / ".agents/scripts/gw",
                        root / ".agents/scripts/gw", ignore=shutil.ignore_patterns("__pycache__"))
        decision = {"disposition": "change", "answer": "Уточнение подготовлено.", "reason": "Clarification",
                    "sources": [name], "edit": {"path": name, "before": "Понятный ответ.",
                                                 "after": "Понятный ответ с объяснением терминов."}}
        return root, name, path, decision

    def test_restart_recovers_a_written_change_before_final_journal_confirmation(self):
        with tempfile.TemporaryDirectory() as temporary:
            root, name, path, decision = self.editable(temporary)
            state = Path(temporary) / "history.sqlite3"
            app = Workshop(root, state, lambda context: decision)
            with patch("os.fsync", side_effect=SystemExit("process interrupted")):
                with self.assertRaises(SystemExit):
                    app.ask("interrupted", "Уточни формулировку", target=name)
            resumed = Workshop(root, state, lambda context: self.fail("Applied edit cannot repeat"))
            result = resumed.ask("interrupted", "Уточни формулировку", target=name)
            self.assertEqual(result["status"], "applied")
            self.assertEqual(path.read_bytes(), result["change"]["after"].encode("utf-8"))

    def test_windows_excludes_a_writer_that_does_not_use_the_application(self):
        with tempfile.TemporaryDirectory() as temporary:
            root, name, path, decision = self.editable(temporary)
            original_fsync = os.fsync
            attempts = []

            def competing_write(fd):
                child = subprocess.run([sys.executable, "-c",
                    "import sys; from pathlib import Path; Path(sys.argv[1]).write_text('overwrite')", str(path)],
                    capture_output=True, text=True)
                attempts.append(child)
                original_fsync(fd)

            with patch("os.fsync", side_effect=competing_write):
                result = Workshop(root, Path(temporary) / "history.sqlite3", lambda context: decision).ask(
                    "locked", "Уточни формулировку", target=name)
            self.assertEqual(result["status"], "applied", result)
            self.assertEqual(len(attempts), 1)
            self.assertNotEqual(attempts[0].returncode, 0)
            self.assertIn("PermissionError", attempts[0].stderr)
            self.assertEqual(path.read_bytes(), result["change"]["after"].encode("utf-8"))

    def test_credentials_in_a_request_are_not_sent_to_codex_or_kept_in_history(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            token = "123456789:" + "a" * 35
            contexts = []

            def agent(context):
                contexts.append(context)
                return {"disposition": "answer", "answer": "Принято", "reason": "", "sources": [], "edit": None}

            app = Workshop(root, root / "state.sqlite3", agent)
            app.ask("secret", "Токен " + token)
            self.assertNotIn(token, json.dumps(contexts))
            self.assertNotIn(token, json.dumps(app.history()))

    def test_an_intervening_operator_edit_is_preserved(self):
        with tempfile.TemporaryDirectory() as temporary:
            root, name, path, decision = self.editable(temporary)

            def agent(context):
                path.write_text(path.read_text(encoding="utf-8") + "\nУточнение оператора.\n", encoding="utf-8")
                return decision

            app = Workshop(root, Path(temporary) / "history.sqlite3", agent)
            result = app.ask("race", "Уточни формулировку", target=name)
            self.assertEqual(result["status"], "conflict")
            self.assertIn("Уточнение оператора", path.read_text(encoding="utf-8"))
            self.assertNotIn("объяснением терминов", path.read_text(encoding="utf-8"))

    def test_write_error_keeps_the_actual_change_and_never_repeats_it(self):
        with tempfile.TemporaryDirectory() as temporary:
            root, name, path, decision = self.editable(temporary)
            state = Path(temporary) / "history.sqlite3"
            app = Workshop(root, state, lambda context: decision)
            with patch("os.fsync", side_effect=OSError("disk failure")):
                result = app.ask("crash", "Уточни формулировку", target=name)
            self.assertEqual(result["status"], "uncertain", result)
            self.assertIn("change", result)
            again = Workshop(root, state, lambda context: self.fail("Must not run again"))
            self.assertEqual(again.ask("crash", "Уточни формулировку", target=name), result)
            self.assertEqual(path.read_bytes(), result["change"]["after"].encode("utf-8"))

    def test_architecture_refusal_is_retained_without_changing_the_target(self):
        with tempfile.TemporaryDirectory() as temporary:
            root, name, path, decision = self.editable(temporary)
            original = path.read_bytes()
            decision.update(disposition="refuse", edit=None, answer="Это противоречит принятому владельцу данных.")
            result = Workshop(root, Path(temporary) / "history.sqlite3", lambda context: decision).ask(
                "refuse", "Смени владельца данных", target=name)
            self.assertEqual(result["status"], "refused")
            self.assertEqual(path.read_bytes(), original)

    def test_even_a_change_decision_cannot_write_architecture(self):
        with tempfile.TemporaryDirectory() as temporary:
            root, name, path, decision = self.editable(temporary)
            architecture = root / "docs/architecture.md"
            architecture.write_text("Cabinet owns accounts", encoding="utf-8")
            decision["edit"] = {"path": "docs/architecture.md", "before": "Cabinet", "after": "Daychi"}
            result = Workshop(root, Path(temporary) / "history.sqlite3", lambda context: decision).ask(
                "outside", "Измени архитектуру", target=name)
            self.assertEqual(result["status"], "failed")
            self.assertEqual(architecture.read_text(encoding="utf-8"), "Cabinet owns accounts")

    def test_a_claim_of_completion_cannot_check_verification_without_evidence(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            name = "docs/tickets/01-0020-demo.md"
            path = root / name
            path.parent.mkdir(parents=True)
            path.write_text("# Demo\n\n- [ ] /verify\n", encoding="utf-8")
            original = path.read_bytes()
            agent = lambda context: {"disposition": "change", "answer": "Готово", "reason": "Asked to close",
                                     "sources": [name], "edit": {"path": name, "before": "[ ]", "after": "[x]"}}
            result = Workshop(root, root / "history.sqlite3", agent).ask("close", "Отметь готовым", target=name)
            self.assertEqual(result["status"], "failed")
            self.assertEqual(path.read_bytes(), original)

    def test_an_out_of_scope_target_cannot_be_read_or_changed(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "secret.txt").write_text("private", encoding="utf-8")
            calls = []
            app = Workshop(root, root / "state.sqlite3", lambda context: calls.append(context))
            result = app.ask("bad", "Прочитай секрет", target="secret.txt")
            self.assertEqual(result["status"], "failed")
            self.assertEqual(calls, [])

    def test_permitted_ticket_edit_is_applied_once_with_before_and_after(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary) / "project"
            ticket = root / "docs/tickets/01-0020-demo.md"
            ticket.parent.mkdir(parents=True)
            ticket.write_text("# Demo\n\n## What to build\n\nПонятный ответ.\n", encoding="utf-8")
            original = ticket.read_bytes()
            shutil.copytree(Path(__file__).resolve().parents[1] / ".agents/scripts/gw",
                            root / ".agents/scripts/gw", ignore=shutil.ignore_patterns("__pycache__"))
            calls = []

            def agent(context):
                calls.append(context)
                return {"disposition": "change", "answer": "Уточнение подготовлено.",
                        "reason": "Clarifies the agreed behavior", "sources": ["docs/tickets/01-0020-demo.md"],
                        "edit": {"path": "docs/tickets/01-0020-demo.md", "before": "Понятный ответ.",
                                 "after": "Понятный ответ с объяснением необходимых терминов."}}

            app = Workshop(root, Path(temporary) / "state.sqlite3", agent)
            result = app.ask("edit", "Уточни, что термины объясняются", target="docs/tickets/01-0020-demo.md")
            self.assertEqual(result["status"], "applied", result)
            self.assertNotEqual(original, ticket.read_bytes())
            self.assertEqual(result["change"]["before"], original.decode())
            self.assertEqual(result["change"]["after"].encode("utf-8"), ticket.read_bytes())
            self.assertEqual(app.ask("edit", "Уточни, что термины объясняются",
                                     target="docs/tickets/01-0020-demo.md"), result)
            self.assertEqual(len(calls), 1)

    def test_answer_is_grounded_in_current_files_and_retained_after_restart(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary) / "project"
            (root / "docs").mkdir(parents=True)
            (root / "AGENTS.md").write_text("Documents inform; they do not authorize.", encoding="utf-8")
            (root / "docs/architecture.md").write_text("Cabinet owns accounts.", encoding="utf-8")
            calls = []

            def agent(context):
                calls.append(context)
                return {"disposition": "answer", "answer": "Учётными записями управляет Cabinet.",
                        "reason": "Existing ownership", "sources": ["docs/architecture.md"], "edit": None}

            state = Path(temporary) / "history.sqlite3"
            app = Workshop(root, state, agent)
            result = app.ask("one", "Кто отвечает за учётные записи?", sender="tester")
            self.assertEqual(result["status"], "answered")
            self.assertIn("Cabinet owns accounts.", json.dumps(calls[0]))
            again = Workshop(root, state, agent).ask("one", "Кто отвечает за учётные записи?", sender="tester")
            self.assertEqual(result, again)
            self.assertEqual(len(calls), 1)
            self.assertEqual(app.history()[0]["sender"], "tester")


if __name__ == "__main__":
    unittest.main()
