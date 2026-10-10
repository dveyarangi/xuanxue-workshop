import json
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError
from urllib.parse import urlencode, urlsplit, parse_qs
from urllib.request import Request, build_opener, HTTPRedirectHandler


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


opener = build_opener(NoRedirect)
origin = "https://staging.xuanxue.su"
state = "S" * 43
params = {
    "response_type": "code", "client_id": "daychi-native",
    "redirect_uri": "su.xuanxue.daychi:/oauth/cabinet",
    "scope": "unsupported", "state": state,
    "code_challenge": "C" * 43, "code_challenge_method": "S256",
}
cases = [
    ("health", "/api/health", None),
    ("missing_native_bearer", "/api/auth/native/me", None),
    ("authorization_invalid_scope", "/auth/native/authorize?" + urlencode(params), None),
    ("unregistered_callback", "/auth/native/authorize?" + urlencode({**params, "redirect_uri": "https://invalid.example/callback"}), None),
    ("unknown_code", "/api/auth/native/token", urlencode({
        "grant_type": "authorization_code", "client_id": "daychi-native",
        "redirect_uri": "su.xuanxue.daychi:/oauth/cabinet",
        "code": "X" * 43, "code_verifier": "V" * 43,
    }).encode()),
]
results = []
for name, path, body in cases:
    request = Request(origin + path, data=body, headers={"User-Agent": "Workshop-contract-review"})
    if body is not None:
        request.add_header("Content-Type", "application/x-www-form-urlencoded; charset=utf-8")
    try:
        response = opener.open(request, timeout=25)
    except HTTPError as error:
        response = error
    with response:
        payload = response.read(65536).decode("utf-8", errors="replace")
        row = {
            "case": name, "status": response.status,
            "cache_control": response.headers.get("Cache-Control"),
            "pragma": response.headers.get("Pragma"),
            "www_authenticate": response.headers.get("WWW-Authenticate"),
            "sets_cookie": response.headers.get("Set-Cookie") is not None,
        }
        if name == "health":
            data = json.loads(payload)
            row["health"] = {key: data.get(key) for key in ("status", "commit", "mongo")}
        elif payload.startswith("{"):
            row["body"] = json.loads(payload)
        location = response.headers.get("Location")
        if location:
            target = urlsplit(location)
            query = parse_qs(target.query)
            row["callback"] = {
                "base": location.split("?")[0], "keys": sorted(query),
                "error": query.get("error"), "issuer": query.get("iss"),
                "synthetic_state_matches": query.get("state") == [state],
            }
        results.append(row)
result = {"observed_at_utc": datetime.now(timezone.utc).isoformat(), "origin": origin,
          "scope": "Anonymous health and refusal probes only; no accounts, issued codes, pending authorizations or fixtures created", "results": results}
Path(__file__).with_name("runtime-result.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
