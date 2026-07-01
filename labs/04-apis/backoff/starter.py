"""
Lab: Backoff
Lesson: apis-rate-limits-retries

Retry transient failures (429, 500) with exponential backoff. Fail
immediately on non-retryable failures (401, 404) -- don't waste a
single retry on those.
"""

import time

import requests


def fetch_with_backoff(base_url, path, max_retries=4, base_delay_seconds=0.01):
    """GET {base_url}{path}, retrying on 429/500 with exponential backoff.

    On 401 or 404, raise RuntimeError immediately -- no retry at all.
    On repeated 429/500 that never succeed, raise RuntimeError after
    max_retries attempts total.
    On success (200), return response.json().

    base_delay_seconds is deliberately tiny so tests run fast -- use it
    (not a hardcoded real-world delay) as your backoff base.
    """
    # TODO: loop up to max_retries times
    # TODO: on 200, return response.json()
    # TODO: on 401/404, raise RuntimeError immediately (no sleep, no retry)
    # TODO: on 429/500, sleep base_delay_seconds * 2**attempt, then retry
    # TODO: after max_retries attempts with no success, raise RuntimeError
    raise NotImplementedError("fetch_with_backoff is not implemented yet")


if __name__ == "__main__":
    print(fetch_with_backoff("http://127.0.0.1:8000", "/current"))
