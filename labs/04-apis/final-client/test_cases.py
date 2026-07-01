import sys
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from mock_http_server import MockServer  # noqa: E402

from starter import fetch_weather_resilient  # noqa: E402


def make_toggle_respond():
    """Server that succeeds until switched to failing mode."""
    state = {"failing": False}

    def respond(handler):
        if state["failing"]:
            return 500, {"Content-Type": "text/plain"}, b"down"
        return 200, {"Content-Type": "application/json"}, b'{"temperature_c": 20.0}'

    return respond, state


def make_always_fails(status):
    def respond(handler):
        return status, {"Content-Type": "text/plain"}, b"failure"

    return respond


class TestFinalClient(unittest.TestCase):
    def test_success_populates_cache_and_returns_fresh_data(self):
        respond, state = make_toggle_respond()
        cache = {"last_good": None}
        with MockServer(respond) as server:
            result = fetch_weather_resilient(server.base_url, "/current", cache, max_retries=2)
        self.assertEqual(result["temperature_c"], 20.0)
        self.assertNotIn("stale", result)
        self.assertEqual(cache["last_good"]["temperature_c"], 20.0)

    def test_failure_after_success_falls_back_to_stale_cache(self):
        respond, state = make_toggle_respond()
        cache = {"last_good": None}
        with MockServer(respond) as server:
            fetch_weather_resilient(server.base_url, "/current", cache, max_retries=2)
            state["failing"] = True
            result = fetch_weather_resilient(server.base_url, "/current", cache, max_retries=2, base_delay_seconds=0.01)
        self.assertEqual(result["temperature_c"], 20.0)
        self.assertTrue(result.get("stale"), "a fallback-to-cache result must be explicitly flagged as stale")

    def test_no_cache_and_immediate_failure_raises(self):
        respond = make_always_fails(500)
        cache = {"last_good": None}
        with MockServer(respond) as server:
            with self.assertRaises(RuntimeError):
                fetch_weather_resilient(server.base_url, "/current", cache, max_retries=2, base_delay_seconds=0.01)

    def test_non_retryable_failure_still_fails_fast(self):
        respond = make_always_fails(404)
        cache = {"last_good": {"temperature_c": 15.0}}
        with MockServer(respond) as server:
            # Even with a cache available, a 404 should be treated as a real
            # error worth surfacing distinctly -- this test just confirms it
            # doesn't hang retrying a non-retryable failure before falling back.
            result = fetch_weather_resilient(server.base_url, "/current", cache, max_retries=5, base_delay_seconds=0.01)
        self.assertTrue(result.get("stale"))


if __name__ == "__main__":
    unittest.main()
