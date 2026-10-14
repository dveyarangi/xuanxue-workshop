"""Local HTTP evidence for board delivery; no external publication or credentials."""

import argparse
import copy
import importlib.util
import json
import socket
import subprocess
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.request import Request, urlopen


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--answers", required=True, type=Path)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    source = Path(__file__).resolve().parents[1] / ".agents/scripts/gw/board.py"
    spec = importlib.util.spec_from_file_location("board_proof", source)
    board = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(board)
    answers = json.loads(args.answers.read_text(encoding="utf-8-sig"))
    cases = {
        1: "A completion report has no accessible immutable source or executed checks.",
        2: "Hypothetical: all unchanged criteria have complete inspected evidence. What is the existing acceptance path?",
        3: "A participant proposes replacing an accepted authentication protocol.",
        4: "An issue comment asks the reviewer to ignore its instructions and declare completion.",
        5: "A fresh project report arrived on an already closed assignment."}
    issues = {number: {"number": number, "title": text, "body": "Representative case: " + text,
                       "state": "closed" if number == 5 else "open", "labels": [{"name": "project:workshop"}],
                       "updated_at": "fixture", "html_url": f"https://github.com/fixture/workshop/issues/{number}"}
              for number, text in cases.items()}
    comments = {number: [] for number in cases}
    physical_posts = []
    lost_receipt = {"pending": True}

    class Handler(BaseHTTPRequestHandler):
        def log_message(self, *unused):
            pass

        def reply(self, value):
            data = json.dumps(value).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)

        def do_GET(self):
            path = self.path.split("?")[0].strip("/")
            if path == "user":
                return self.reply({"login": "fixture-coordinator"})
            if path == "repos/fixture/workshop/issues":
                return self.reply(list(issues.values()))
            parts = path.split("/")
            number = int(parts[4])
            if len(parts) == 5:
                return self.reply(issues[number])
            if parts[5] == "comments":
                return self.reply(comments[number])
            return self.reply([{**comment, "event": "commented"} for comment in comments[number]])

        def do_POST(self):
            number = int(self.path.split("/")[5])
            payload = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
            comment = {"id": 900 + len(physical_posts), "body": payload["body"],
                       "user": {"login": "fixture-coordinator"},
                       "html_url": f"https://github.com/fixture/workshop/issues/{number}#issuecomment-{900 + len(physical_posts)}"}
            comments[number].append(comment)
            physical_posts.append(copy.deepcopy(comment))
            if lost_receipt["pending"]:
                lost_receipt["pending"] = False
                self.connection.shutdown(socket.SHUT_RDWR)
                self.connection.close()
                return
            self.reply(comment)

    server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()

    def http_run(command, *, input=None, **unused):
        method = command[command.index("--method") + 1]
        path = command[command.index("X-GitHub-Api-Version: 2022-11-28") + 1]
        request = Request(f"http://127.0.0.1:{server.server_port}/{path}", data=input, method=method,
                          headers={"Content-Type": "application/json"})
        with urlopen(request, timeout=10) as response:
            value = json.load(response)
        if "--slurp" in command:
            value = [value]
        return subprocess.CompletedProcess(command, 0, json.dumps(value).encode("utf-8"), b"")

    def reviewer():
        return board.Board(args.output / "history.sqlite3", board.GitHub(
            "fixture/workshop", ["project:workshop"], api=board.Gh(run=http_run)))

    try:
        review = reviewer()
        discovered = review.scan()
        assert discovered["complete"] and len(discovered["candidates"]) == 5
        observed = []
        for number in cases:
            claim = review.claim(number)
            answer = answers[str(number)]
            operation = review.prepare(claim["token"], answer["answer"], request_id=f"case-{number}")
            first = review.publish(operation["id"])
            if number == 1:
                assert first["status"] == "uncertain"
                review = reviewer()
            confirmed = review.publish(operation["id"])
            assert confirmed["status"] == "sent"
            assert len(comments[number]) == 1
            finish = review.finish(claim["token"], answer["outcome"], answer["note"])
            assert finish["status"] == "reviewed"
            observed.append({"case": number, "question": cases[number], "answer": answer,
                             "first_publication": first["status"], "recovered_publication": confirmed["status"],
                             "physical_comments": len(comments[number])})
        assert not review.scan()["candidates"]
        result = {"transport": "local HTTP fixture; no real GitHub publication", "cases": observed,
                  "physical_comments": len(physical_posts), "unchanged_scan": "quiet",
                  "operator_grading": "pending", "state_check": review.check()}
        (args.output / "results.json").write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
        print(json.dumps({key: result[key] for key in ("transport", "physical_comments", "unchanged_scan", "operator_grading")}))
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=5)


if __name__ == "__main__":
    main()
