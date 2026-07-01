import unittest

from starter import build_reading_record, filter_low_battery


class TestStructuredRecord(unittest.TestCase):
    def test_build_reading_record_default_source(self):
        record = build_reading_record("2026-07-01T09:00", 50)
        self.assertEqual(record["source"], "unknown")

    def test_build_reading_record_explicit_source(self):
        record = build_reading_record("2026-07-01T09:00", 50, source="battery-3")
        self.assertEqual(record["source"], "battery-3")

    def test_filter_low_battery_basic(self):
        records = [
            build_reading_record("t1", 10),
            build_reading_record("t2", 40),
            build_reading_record("t3", 24),
        ]
        result = filter_low_battery(records, threshold=25)
        self.assertEqual([r["timestamp"] for r in result], ["t1", "t3"])

    def test_filter_low_battery_skips_missing_field_without_crashing(self):
        records = [
            build_reading_record("t1", 10),
            {"timestamp": "t2"},  # no soc_percent at all
        ]
        result = filter_low_battery(records, threshold=25)
        self.assertEqual([r["timestamp"] for r in result], ["t1"])

    def test_filter_low_battery_empty_input(self):
        self.assertEqual(filter_low_battery([]), [])


if __name__ == "__main__":
    unittest.main()
