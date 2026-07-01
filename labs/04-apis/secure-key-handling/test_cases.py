import inspect
import re
import sys
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from mock_http_server import MockServer  # noqa: E402

import starter  # noqa: E402
from starter import fetch_current_weather  # noqa: E402

VALID_KEY = "test-suite-secret-key-9f8e7d"


def respond(handler):
    auth = handler.headers.get("Authorization")
    if auth is None:
        return 401, {"Content-Type": "text/plain"}, b"missing credentials"
    if auth != f"Bearer {VALID_KEY}":
        return 403, {"Content-Type": "text/plain"}, b"invalid credentials"
    return 200, {"Content-Type": "application/json"}, b'{"temperature_c": 19.0}'


class TestSecureKeyHandling(unittest.TestCase):
    def test_valid_key_returns_200_and_body(self):
        with MockServer(respond) as server:
            status, body = fetch_current_weather(server.base_url, VALID_KEY)
        self.assertEqual(status, 200)
        self.assertEqual(body["temperature_c"], 19.0)

    def test_wrong_key_returns_403(self):
        with MockServer(respond) as server:
            status, _ = fetch_current_weather(server.base_url, "wrong-key")
        self.assertEqual(status, 403)

    def test_key_is_sent_as_bearer_authorization_header(self):
        # If the header were sent incorrectly (wrong format, wrong header
        # name), the server would see it as missing -> 401, not 403.
        with MockServer(respond) as server:
            status, _ = fetch_current_weather(server.base_url, "wrong-key")
        self.assertNotEqual(status, 401, "the Authorization header doesn't appear to be sent in the expected format")

    def test_no_hardcoded_key_literal_in_source(self):
        source = inspect.getsource(starter)
        self.assertNotRegex(
            source,
            re.compile(r'api_key\s*=\s*["\']'),
            "api_key should never be reassigned to a hardcoded string literal in the source.",
        )
        self.assertNotIn(VALID_KEY, source, "the test's key should never be findable in your source code.")


if __name__ == "__main__":
    unittest.main()
