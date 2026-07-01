"""
Lab: Final Client
Lesson: apis-resilient-ingestion (boss battle)

Combine retry/backoff with a stale-cache fallback: if a live request
ultimately fails after retries, fall back to the last successful
response instead of returning nothing -- but ALWAYS flag it as stale
so a caller can tell the difference.
"""

import time

import requests


def fetch_weather_resilient(base_url, path, cache, max_retries=3, base_delay_seconds=0.01):
    """Fetch weather with retry/backoff, falling back to a stale cache entry.

    cache is a mutable dict shared across calls, e.g. {"last_good": None}.

    On success: store the parsed JSON in cache["last_good"] and return it
    (without a "stale" key).
    On failure after retries: if cache["last_good"] exists, return a COPY
    of it with "stale": True added. If there's no cached value at all,
    raise RuntimeError.
    Non-retryable failures (401, 404) should still fail fast, same as the
    backoff lab, before falling back to cache.
    """
    # TODO: implement using the same retry/backoff logic as the earlier lab
    # TODO: on success, update cache["last_good"] and return the fresh data
    # TODO: on failure after retries, fall back to cache["last_good"] with stale=True,
    #       or raise RuntimeError if there's nothing cached yet
    raise NotImplementedError("fetch_weather_resilient is not implemented yet")


if __name__ == "__main__":
    cache = {"last_good": None}
    print(fetch_weather_resilient("http://127.0.0.1:8000", "/current", cache))
