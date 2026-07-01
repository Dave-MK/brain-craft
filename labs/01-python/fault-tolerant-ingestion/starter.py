"""
Lab: Fault-Tolerant Ingestion
Lesson: python-error-handling

Process a batch of readings where some are malformed (missing the
demand_kw key, or demand_kw is a non-numeric string). Classify the good
ones and count skips by reason -- never let one bad reading crash the
whole batch, and never use a bare `except:`.
"""


def process_batch(readings):
    """Return (classified, skip_counts).

    classified: list of "OK: <value>" strings for readings that parsed fine.
    skip_counts: dict with keys "missing_key" and "invalid_value" counting
                 how many readings were skipped for each reason.
    """
    # TODO: for each reading, try float(reading["demand_kw"])
    # TODO: catch KeyError specifically -> increment skip_counts["missing_key"]
    # TODO: catch ValueError specifically -> increment skip_counts["invalid_value"]
    # TODO: do NOT use a bare `except:` anywhere in this function
    raise NotImplementedError("process_batch is not implemented yet")


if __name__ == "__main__":
    readings = [
        {"demand_kw": 4821},
        {"demand_kw": "4790"},
        {"demand_kw": "not-a-number"},
        {},
    ]
    print(process_batch(readings))
