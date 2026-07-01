import sys
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from mock_http_server import MockServer  # noqa: E402

from starter import fetch_current_temperature  # noqa: E402


def respond_success(handler):
    return 200, {"Content-Type": "application/json"}, b'{"temperature_c": 21.5}'


def respond_not_found(handler):
    return 404, {"Content-Type": "text/plain"}, b"not found"


def respond_server_error_bad_body(handler):
    # Deliberately NOT JSON -- a naive implementation that calls .json()
    # before checking status_code will raise trying to parse this.
    return 500, {"Content-Type": "text/html"}, b"<html>Internal Server Error</html>"


class TestFirstRequest(unittest.TestCase):
    def test_successful_request_returns_temperature(self):
        with MockServer(respond_success) as server:
            result = fetch_current_temperature(server.base_url)
        self.assertEqual(result, 21.5)

    def test_not_found_returns_none_without_raising(self):
        with MockServer(respond_not_found) as server:
            result = fetch_current_temperature(server.base_url)
        self.assertIsNone(result)

    def test_server_error_with_non_json_body_returns_none_without_raising(self):
        with MockServer(respond_server_error_bad_body) as server:
            result = fetch_current_temperature(server.base_url)
        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
