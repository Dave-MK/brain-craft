import inspect
import unittest

import starter
from starter import process_batch


class TestFaultTolerantIngestion(unittest.TestCase):
    def test_good_readings_are_classified(self):
        classified, _ = process_batch([{"demand_kw": 4821}])
        self.assertEqual(classified, ["OK: 4821.0"])

    def test_string_number_is_parsed_successfully(self):
        classified, skips = process_batch([{"demand_kw": "4790"}])
        self.assertEqual(classified, ["OK: 4790.0"])
        self.assertEqual(skips["invalid_value"], 0)

    def test_missing_key_is_counted_and_skipped(self):
        classified, skips = process_batch([{}])
        self.assertEqual(classified, [])
        self.assertEqual(skips["missing_key"], 1)

    def test_invalid_value_is_counted_and_skipped(self):
        classified, skips = process_batch([{"demand_kw": "not-a-number"}])
        self.assertEqual(classified, [])
        self.assertEqual(skips["invalid_value"], 1)

    def test_mixed_batch_does_not_crash_and_counts_correctly(self):
        readings = [
            {"demand_kw": 4821},
            {"demand_kw": "4790"},
            {"demand_kw": "bad"},
            {},
            {},
        ]
        classified, skips = process_batch(readings)
        self.assertEqual(len(classified), 2)
        self.assertEqual(skips["missing_key"], 2)
        self.assertEqual(skips["invalid_value"], 1)

    def test_no_bare_except_used(self):
        source = inspect.getsource(starter)
        self.assertNotIn("except:", source, "process_batch must not use a bare except:")


if __name__ == "__main__":
    unittest.main()
