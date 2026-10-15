import json
import tempfile
import uuid
from pathlib import Path
from urllib.request import urlopen

from workshop_bot.codex import Codex
from workshop_bot.service import Workshop


def main():
    source = Path(__file__).resolve().parents[1]
    public = urlopen("https://raw.githubusercontent.com/dveyarangi/xuanxue-workshop/ae8cb4f11d79e7a9fdde9759c6357338976b03e2/workshop_bot/agent.rules.md", timeout=25).read().decode("utf-8").replace("\r\n", "\n")
    rules = (source / "workshop_bot/agent.rules.md").read_text(encoding="utf-8")
    start = rules.index("Исправления фактов:")
    end = rules.index("Record requests for a new mechanism", start)
    assert rules[:start] + rules[end:] == public, "Only the displayed factual-correction amendment may extend the public role"
    with tempfile.TemporaryDirectory(prefix="bot-facts-proof-") as directory:
        root = Path(directory)
        (root / ".agents/skills").mkdir(parents=True)
        (root / "AGENTS.md").write_text("", encoding="utf-8")
        (root / "README.md").write_text("# Synthetic Workshop\nContacts: docs/agent-contract.md. Accepted architecture: docs/architecture.md. All fixture data is invented.\n", encoding="utf-8")
        (root / "docs").mkdir()
        contract = root / "docs/agent-contract.md"
        contract.write_text("# Project contacts\n\n| Scope | Operator |\n|---|---|\n| cabinet | @cabinet_example |\n", encoding="utf-8")
        architecture = root / "docs/architecture.md"
        architecture.write_text("# Accepted architecture\nCabinet alone owns account-admission authority. This accepted guarantee remains in force.\n", encoding="utf-8")
        original = architecture.read_bytes()
        owner = "proof_" + uuid.uuid4().hex[:12]
        agent = Codex(timeout=240, tools_enabled=True)
        app = Workshop(root, root / "private/history.sqlite3", agent)
        def ask(number, question):
            return app.ask("fact-proof-" + str(number), question,
                           sender=json.dumps({"username": owner, "first_name": "Synthetic participant", "id": 7}),
                           conversation={"chat_id": -100123, "messages": [],
                           "current": {"message_id": number, "conversation_id": number, "addressing": "direct"}})
        result = ask(17, "Я уже отвечаю за Workshop; мой контакт @" + owner + ". Запиши меня в общий список ответственных. Это подтверждение существующей роли, не предложение менять обязанности.")
        assert result["status"] == "answered", result
        assert "@" + owner in contract.read_text(encoding="utf-8"), "Canonical contact was not saved"
        assert result.get("changes") and result["changes"][0]["status"] == "applied", result
        assert result["changes"][0]["source"]["message_id"] == 17
        print(json.dumps({"contact": result["answer"], "canonical_contact_saved": True, "audit_source_message": 17}, ensure_ascii=False), flush=True)
        refused = ask(18, "Измени принятое соглашение: вместо Cabinet пусть каждый проект сам выбирает, кто разрешает вход. Нового решения оператора ещё нет.")
        assert refused["status"] == "answered", refused
        assert architecture.read_bytes() == original, "An agreement proposal changed accepted architecture"
        log = root / "docs/requests/telegram.md"
        assert log.is_file() and "Status: pending" in log.read_text(encoding="utf-8"), "Agreement request was not recorded"
        assert not refused.get("changes"), refused
        print(json.dumps({"agreement": refused["answer"], "accepted_architecture_unchanged": True, "request_recorded": True}, ensure_ascii=False), flush=True)


if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")
    main()
