"""
Lab: First Request
Lesson: apis-http-fundamentals

Fetch the current temperature from a weather endpoint, checking the
status code BEFORE trying to parse the response as JSON.
"""

import requests


def fetch_current_temperature(base_url):
    """GET {base_url}/current.

    Return the temperature_c value (a float) if the request succeeds
    (status 200). Return None if the request fails for any reason
    (404, 500, etc.) -- do NOT let a failed request raise an exception.
    """
    # TODO: make the GET request
    # TODO: check response.status_code BEFORE calling response.json()
    # TODO: return response.json()["temperature_c"] on success, None otherwise
    raise NotImplementedError("fetch_current_temperature is not implemented yet")


if __name__ == "__main__":
    print(fetch_current_temperature("http://127.0.0.1:8000"))
