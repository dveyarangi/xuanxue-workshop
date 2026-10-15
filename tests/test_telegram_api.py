import io
import json
import unittest
from urllib.error import HTTPError, URLError

from workshop_bot.telegram_api import TelegramAPI, TelegramError


class APIBoundaryTests(unittest.TestCase):
    def test_image_download_is_bounded_and_credential_errors_are_hidden(self):
        token = "123456789:" + "c" * 35
        class Download:
            def open(self, request, timeout):
                return io.BytesIO(b"123456789")
        api = TelegramAPI(token, Download())
        api.call = lambda method, **parameters: {"file_path": "photos/image.png", "file_size": 9}
        self.assertEqual(api.download("retained-file", limit=9), b"123456789")
        with self.assertRaisesRegex(ValueError, "limit"):
            api.download("retained-file", limit=8)
        api.call = lambda method, **parameters: {"file_path": "../../private", "file_size": 1}
        with self.assertRaisesRegex(ValueError, "unsupported file path"):
            api.download("retained-file", limit=9)
        class Lost:
            def open(self, request, timeout):
                raise URLError(request)
        api = TelegramAPI(token, Lost())
        api.call = lambda method, **parameters: {"file_path": "photos/image.png"}
        with self.assertRaises(TelegramError) as caught:
            api.download("retained-file", limit=9)
        self.assertNotIn(token, str(caught.exception))

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
