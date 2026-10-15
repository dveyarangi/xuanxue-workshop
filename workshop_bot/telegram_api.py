import json
import re
from urllib.error import HTTPError, URLError
from urllib.request import HTTPRedirectHandler, ProxyHandler, Request, build_opener


class TelegramError(RuntimeError):
    def __init__(self, code=None, retry_after=0):
        self.code = code if type(code) is int else None
        self.retry_after = max(0, retry_after) if type(retry_after) is int else 0
        self.uncertain = self.code is None or self.code >= 500
        messages = {401: "Telegram отклонил токен бота.", 403: "Telegram запретил отправку в эту группу.",
                    409: "Сообщения бота получает другой процесс.", 429: "Telegram просит подождать.",
                    400: "Telegram отклонил запрос; проверьте группу и исходное сообщение."}
        super().__init__(messages.get(self.code, "Telegram не подтвердил результат запроса."))


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


class TelegramAPI:
    def __init__(self, token, opener=None):
        if not re.fullmatch(r"\d{6,}:[A-Za-z0-9_-]{20,}", token):
            raise ValueError("Нужен корректный токен от BotFather в локальном файле.")
        self._token = token
        self._opener = opener or build_opener(ProxyHandler({}), NoRedirect())

    def call(self, method, **parameters):
        if method not in {"getMe", "getWebhookInfo", "getChat", "getChatMember", "getUpdates", "sendMessage", "sendChatAction", "getFile"}:
            raise ValueError("Метод Telegram не поддерживается.")
        request = Request(f"https://api.telegram.org/bot{self._token}/{method}",
                          data=json.dumps(parameters).encode("utf-8"),
                          headers={"Content-Type": "application/json"}, method="POST")
        try:
            with self._opener.open(request, timeout=3 if method == "sendChatAction" else 40) as response:
                body = json.loads(response.read())
        except HTTPError as error:
            try:
                body = json.loads(error.read())
                delay = int(body.get("parameters", {}).get("retry_after", 0))
            except (ValueError, TypeError, AttributeError):
                delay = 0
            finally:
                error.close()
            raise TelegramError(error.code, max(0, delay)) from None
        except (URLError, OSError, ValueError):
            raise TelegramError() from None
        if not isinstance(body, dict) or "ok" not in body:
            raise TelegramError()
        if not body["ok"]:
            raise TelegramError(body.get("error_code"), body.get("parameters", {}).get("retry_after", 0))
        if "result" not in body:
            raise TelegramError()
        return body["result"]

    def download(self, file_id, *, limit):
        info = self.call("getFile", file_id=file_id)
        path = info.get("file_path", "")
        if not re.fullmatch(r"[A-Za-z0-9_/.-]+", path) or path.startswith("/") or ".." in path.split("/"):
            raise ValueError("Telegram returned an unsupported file path")
        if info.get("file_size", 0) > limit:
            raise ValueError("Image exceeds the reading limit")
        try:
            with self._opener.open(f"https://api.telegram.org/file/bot{self._token}/{path}", timeout=40) as response:
                data = response.read(limit + 1)
        except HTTPError as error:
            error.close()
            raise TelegramError() from None
        except (URLError, OSError):
            raise TelegramError() from None
        if len(data) > limit:
            raise ValueError("Image exceeds the reading limit")
        return data
