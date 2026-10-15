import tempfile
import unittest
import uuid
import json
import subprocess
import sys
from pathlib import Path
from unittest.mock import patch

from workshop_bot.codex import Codex
from workshop_bot.service import Workshop
from tests.test_telegram import TelegramPeer, message
from workshop_bot.telegram import Group


class SessionTests(unittest.TestCase):
    def test_telegram_reply_from_another_member_resumes_after_restart(self):
        calls = []
        identity = str(uuid.uuid4())

        class Agent:
            def chat(self, *args, session_id=None, on_session=None):
                calls.append(session_id)
                on_session(session_id or identity)
                return {"status": "answered", "answer": "Friday"}

        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            state = root / "private/history.sqlite3"
            peer = TelegramPeer([message()])
            group = Group(Workshop(root, state, Agent()), peer, -100123)
            group.start()
            group.poll_once(0)
            group.work_once()
            reply = message(200, "What time?")
            reply["message"]["entities"] = []
            reply["message"]["from"] = {"id": 8, "first_name": "Boris"}
            reply["message"]["reply_to_message"] = {"message_id": 101}
            peer.updates = [reply]
            group = Group(Workshop(root, state, Agent()), peer, -100123)
            group.start()
            group.poll_once(0)
            group.work_once()
            self.assertEqual(calls, [None, identity])
            self.assertEqual(peer.sent[-1]["reply_parameters"]["message_id"], 210)

    def test_stream_persists_identity_before_child_finishes(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            marker = root / "ack"
            identity = str(uuid.uuid4())
            code = ("import json,time,pathlib; "
                    f"print(json.dumps({{'type':'thread.started','thread_id':'{identity}'}}),flush=True); "
                    f"p=pathlib.Path({str(marker)!r}); "
                    "\nfor _ in range(100):\n if p.exists(): break\n time.sleep(.02)\n"
                    "assert p.exists(), 'identity was not saved while running'\n")
            observed = []

            def save(event):
                observed.append(event["thread_id"])
                marker.write_text("saved")

            result = Codex(timeout=5).run_stream([sys.executable, "-c", code], "", None, root, save)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(observed, [identity])

    def test_resume_reasserts_permissions_and_never_falls_back(self):
        identity = str(uuid.uuid4())
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "AGENTS.md").write_text("Project")
            (root / ".agents/skills").mkdir(parents=True)
            calls = []

            def run(command, prompt, environment, cwd, observe):
                calls.append(command)
                self.assertEqual(command[-3:], ["resume", identity, "-"])
                self.assertNotIn("--ephemeral", command)
                self.assertNotIn("--last", command)
                self.assertIn('approval_policy="never"', command)
                self.assertIn('permissions.workshop.network.enabled=false', command)
                profile = next(c for c in command if c.startswith("permissions.workshop.filesystem="))
                self.assertEqual(profile.count('="write"'), 1)
                self.assertIn(json.dumps(str(root / "private")) + '="deny"', profile)
                return subprocess.CompletedProcess(command, 1, "", "error: session unavailable")

            with patch.object(Codex, "run_stream", side_effect=run):
                with self.assertRaisesRegex(RuntimeError, "session unavailable"):
                    Codex().chat(root, root / "memory.md", root / "private", "Continue", None,
                                 session_id=identity, on_session=lambda value: None)
            self.assertEqual(len(calls), 1)

    def test_restart_resumes_exact_conversation_and_new_roots_stay_separate(self):
        calls = []

        class Agent:
            def chat(self, *args, session_id=None, on_session=None):
                calls.append(session_id)
                on_session(session_id or str(uuid.uuid4()))
                return {"status": "answered", "answer": "Done"}

        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            state = root / "private/history.sqlite3"
            context = {"chat_id": -100, "current": {"conversation_id": 10}}
            first = Workshop(root, state, Agent()).ask("one", "Hello", conversation=context)
            self.assertEqual(first["status"], "answered")
            app = Workshop(root, state, Agent())
            second = app.ask("two", "Continue", sender="another member", conversation=context)
            self.assertEqual(second["status"], "answered")
            self.assertIsNotNone(calls[1])
            self.assertEqual(app.ask("two", "Continue", sender="another member", conversation=context), second)
            app.ask("three", "New", conversation={"chat_id": -100, "current": {"conversation_id": 11}})
            app.ask("four", "Other group", conversation={"chat_id": -200, "current": {"conversation_id": 10}})
            self.assertEqual(calls, [None, calls[1], None, None])

    def test_session_identity_survives_failed_turn_without_replaying_request(self):
        identity = str(uuid.uuid4())
        calls = []

        class Agent:
            def chat(self, *args, session_id=None, on_session=None):
                calls.append(session_id)
                on_session(session_id or identity)
                if len(calls) == 1:
                    raise RuntimeError("Interrupted after session started")
                return {"status": "answered", "answer": "Continued"}

        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            context = {"chat_id": -100, "current": {"conversation_id": 10}}
            app = Workshop(root, root / "private/history.sqlite3", Agent())
            result = app.ask("one", "Hello", conversation=context)
            self.assertEqual(result["status"], "uncertain")
            self.assertEqual(app.ask("one", "Hello", conversation=context), result)
            app = Workshop(root, app.state, Agent())
            self.assertEqual(app.ask("two", "Continue", conversation=context)["status"], "answered")
            self.assertEqual(calls, [None, identity])

    def test_unknown_session_start_is_not_silently_replaced(self):
        calls = []

        class Agent:
            def chat(self, *args, **kwargs):
                calls.append(True)
                raise RuntimeError("No session identity received")

        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            app = Workshop(root, root / "private/history.sqlite3", Agent())
            context = {"chat_id": -100, "current": {"conversation_id": 10}}
            self.assertEqual(app.ask("one", "Hello", conversation=context)["status"], "uncertain")
            self.assertEqual(app.ask("two", "Continue", conversation=context)["status"], "uncertain")
            self.assertEqual(len(calls), 1)


if __name__ == "__main__":
    unittest.main()
