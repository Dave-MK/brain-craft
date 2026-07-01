"""
Lab: Full Backfill
Lesson: apis-pagination

Follow a next-page-token style paginated API until every record has
been collected -- don't stop at the first page, and don't loop forever.
"""

import requests


def fetch_all_records(base_url):
    """GET {base_url}/records, following next_page_token until it's absent/None.

    Each response looks like: {"records": [...], "next_page_token": "..."}
    (next_page_token is missing or null on the last page).

    Return the combined list of every record across every page, in order.
    """
    # TODO: start with no page_token
    # TODO: loop: request /records (with ?page_token=... once you have one),
    #       extend your results list with data["records"],
    #       stop when data.get("next_page_token") is falsy
    raise NotImplementedError("fetch_all_records is not implemented yet")


if __name__ == "__main__":
    print(fetch_all_records("http://127.0.0.1:8000"))
