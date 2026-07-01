"""
Lab: Secure Key Handling
Lesson: apis-authentication

Authenticate a request with a Bearer token sent via a header -- never a
hardcoded secret in the source.
"""

import requests


def fetch_current_weather(base_url, api_key):
    """GET {base_url}/current with an "Authorization: Bearer <api_key>" header.

    Return (status_code, body) where body is the parsed JSON on success,
    or None if the response wasn't valid JSON / the request failed.
    Do NOT hardcode any API key literal in this file -- api_key must be
    the only source of the credential.
    """
    # TODO: send the request with the Authorization header
    # TODO: return (status_code, parsed_json_or_none)
    raise NotImplementedError("fetch_current_weather is not implemented yet")


if __name__ == "__main__":
    print(fetch_current_weather("http://127.0.0.1:8000", "some-key"))
