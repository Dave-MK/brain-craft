"""
Lab: Structured Record
Lesson: python-dictionaries

Build structured battery-reading records and filter them safely, even
when a record is missing an expected field.
"""


def build_reading_record(timestamp, soc_percent, source=None):
    """Return a dict record. If source is not given, use "unknown"."""
    # TODO: return {"timestamp": ..., "soc_percent": ..., "source": ...}
    # TODO: default source to "unknown" when it's None
    raise NotImplementedError("build_reading_record is not implemented yet")


def filter_low_battery(records, threshold=25):
    """Return only the records whose soc_percent is below threshold.

    Some records may be missing the "soc_percent" key entirely -- those
    should be safely skipped, never crash the function.
    """
    # TODO: use record.get("soc_percent") so a missing key doesn't raise KeyError
    # TODO: skip records where soc_percent is missing (None) entirely
    # TODO: include records where soc_percent is present and below threshold
    raise NotImplementedError("filter_low_battery is not implemented yet")


if __name__ == "__main__":
    records = [
        build_reading_record("2026-07-01T09:00", 18),
        build_reading_record("2026-07-01T10:00", 40),
        {"timestamp": "2026-07-01T11:00"},  # missing soc_percent on purpose
    ]
    print(filter_low_battery(records))
