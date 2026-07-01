import sys
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from mock_http_server import MockServer  # noqa: E402

from starter import fetch_with_backoff  # noqa: E402


def make_fails_then_succeeds(fail_status, n_failures):
    call_count = {"n": 0}

    def respond(handler):
        call_count["n"] += 1
        if call_count["n"] <= n_failures:
            return fail_status, {"Content-Type": "text/plain"}, b"try again"
        return 200, {"Content-Type": "application/json"}, b'{"ok": true}'

    return respond, call_count


def make_always_fails(status):
    call_count = {"n": 0}

    def respond(handler):
        call_count["n"] += 1
        return status, {"Content-Type": "text/plain"}, b"failure"

    return respond, call_count


class TestBackoff(unittest.TestCase):
    def test_succeeds_after_two_429s(self):
        respond, call_count = make_fails_then_succeeds(429, n_failures=2)
        with MockServer(respond) as server:
            result = fetch_with_backoff(server.base_url, "/current", max_retries=5)
        self.assertEqual(result, {"ok": True})
        self.assertEqual(call_count["n"], 3, "expected exactly 3 requests: 2 failures + 1 success")

    def test_404_raises_immediately_without_retrying(self):
        respond, call_count = make_always_fails(404)
        with MockServer(respond) as server:
            with self.assertRaises(RuntimeError):
                fetch_with_backoff(server.base_url, "/current", max_retries=5)
        self.assertEqual(call_count["n"], 1, "a 404 should never be retried -- expected exactly 1 request")

    def test_401_raises_immediately_without_retrying(self):
        respond, call_count = make_always_fails(401)
        with MockServer(respond) as server:
            with self.assertRaises(RuntimeError):
                fetch_with_backoff(server.base_url, "/current", max_retries=5)
        self.assertEqual(call_count["n"], 1, "a 401 should never be retried -- expected exactly 1 request")

    def test_persistent_429_gives_up_after_max_retries(self):
        respond, call_count = make_always_fails(429)
        with MockServer(respond) as server:
            with self.assertRaises(RuntimeError):
                fetch_with_backoff(server.base_url, "/current", max_retries=3)
        self.assertEqual(call_count["n"], 3, "expected exactly max_retries=3 requests before giving up")


if __name__ == "__main__":
    unittest.main()
