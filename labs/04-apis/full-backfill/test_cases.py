import json
import sys
import unittest
from pathlib import Path
from urllib.parse import parse_qs, urlparse

REPO_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from mock_http_server import MockServer  # noqa: E402

from starter import fetch_all_records  # noqa: E402

PAGES = {
    None: {"records": ["A", "B"], "next_page_token": "p2"},
    "p2": {"records": ["C", "D"], "next_page_token": "p3"},
    "p3": {"records": ["E"], "next_page_token": None},
}


def make_respond():
    # Safety valve: if a buggy solution loops forever, the 21st request
    # gets a terminating empty page instead of hanging the test suite.
    call_count = {"n": 0}

    def respond(handler):
        call_count["n"] += 1
        if call_count["n"] > 20:
            return 200, {"Content-Type": "application/json"}, json.dumps({"records": [], "next_page_token": None}).encode()

        query = parse_qs(urlparse(handler.path).query)
        token = query.get("page_token", [None])[0]
        page = PAGES.get(token, {"records": [], "next_page_token": None})
        return 200, {"Content-Type": "application/json"}, json.dumps(page).encode()

    return respond, call_count


class TestFullBackfill(unittest.TestCase):
    def test_collects_records_from_every_page(self):
        respond, call_count = make_respond()
        with MockServer(respond) as server:
            records = fetch_all_records(server.base_url)
        self.assertEqual(records, ["A", "B", "C", "D", "E"])

    def test_stops_after_the_last_page_does_not_loop_forever(self):
        respond, call_count = make_respond()
        with MockServer(respond) as server:
            fetch_all_records(server.base_url)
        self.assertLessEqual(call_count["n"], 5, "made far more requests than the 3 pages required -- looks like an infinite pagination loop")


if __name__ == "__main__":
    unittest.main()
