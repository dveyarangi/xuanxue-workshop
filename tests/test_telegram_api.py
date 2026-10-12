import io
import json
import unittest
from urllib.error import HTTPError, URLError

from workshop_bot.telegram_api import TelegramAPI, TelegramError


class APIBoundaryTests(unittest.TestCase):
    def test_http_errors_hide_the_credential_and_preserve_retry_instructions(self):
        token = "123456789:" + "a" * 35

        class Limited:
            def open(self, request, timeout):
                raise HTTPError(request.full_url, 429, "contains " + token, {},
                                io.BytesIO(json.dumps({"ok": False, "parameters": {"retry_after": 17}}).encode()))

        with self.assertRaises(TelegramError) as caught:
            TelegramAPI(token, Limited()).call("sendMessage", chat_id=-100123, text="hello")
        self.assertEqual(caught.exception.retry_after, 17)
        self.assertFalse(caught.exception.uncertain)
        self.assertNotIn(token, str(caught.exception))

    def test_network_failure_never_claims_that_delivery_failed_definitely(self):
        token = "123456789:" + "b" * 35

        class Lost:
            def open(self, request, timeout):
                raise URLError(request.full_url)

        with self.assertRaises(TelegramError) as caught:
            TelegramAPI(token, Lost()).call("sendMessage", chat_id=-100123, text="hello")
        self.assertTrue(caught.exception.uncertain)
        self.assertNotIn(token, str(caught.exception))


if __name__ == "__main__":
    unittest.main()
