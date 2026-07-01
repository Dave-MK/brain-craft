"""A tiny local HTTP server for testing API labs without any real network
access -- consistent with docs/16-security/overview.md's rule that
learner-submitted code never gets real internet access.

Every 04-apis lab's test_cases.py spins one of these up on 127.0.0.1 with
an ephemeral port, points the learner's code at it via base_url, and shuts
it down when the test finishes. This exercises real HTTP (real sockets,
real status codes, real JSON bodies) without ever leaving localhost.

Usage:
    from mock_http_server import MockServer

    def respond(handler):
        # handler is a BaseHTTPRequestHandler; inspect handler.path,
        # handler.headers, etc. Return (status_code, headers_dict, body_bytes).
        return 200, {"Content-Type": "application/json"}, b'{"ok": true}'

    server = MockServer(respond)
    try:
        response = requests.get(server.base_url + "/current")
    finally:
        server.stop()
"""

import http.server
import threading


def _make_handler(respond_fn):
    class Handler(http.server.BaseHTTPRequestHandler):
        def do_GET(self):
            self._respond()

        def do_POST(self):
            self._respond()

        def _respond(self):
            status, headers, body = respond_fn(self)
            self.send_response(status)
            for key, value in headers.items():
                self.send_header(key, value)
            self.end_headers()
            if body:
                self.wfile.write(body)

        def log_message(self, format_str, *args):  # noqa: A002 - stdlib signature
            pass  # silence default per-request console logging

    return Handler


class MockServer:
    """Wraps http.server so each test can define its own response logic."""

    def __init__(self, respond_fn):
        handler_cls = _make_handler(respond_fn)
        self.httpd = http.server.HTTPServer(("127.0.0.1", 0), handler_cls)
        self.port = self.httpd.server_address[1]
        self.base_url = f"http://127.0.0.1:{self.port}"
        self._thread = threading.Thread(target=self.httpd.serve_forever, daemon=True)
        self._thread.start()

    def stop(self):
        self.httpd.shutdown()
        self.httpd.server_close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop()
