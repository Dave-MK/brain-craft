import unittest

from starter import add_reading, window_summary


class TestRollingWindow(unittest.TestCase):
    def test_add_reading_appends(self):
        readings = [1, 2, 3]
        result = add_reading(readings, 4)
        self.assertEqual(result, [1, 2, 3, 4])

    def test_add_reading_does_not_reorder_existing_values(self):
        readings = [10, 20]
        result = add_reading(readings, 5)
        self.assertEqual(result[:2], [10, 20])

    def test_window_summary_min_max(self):
        summary = window_summary([4821, 4790, 4650, 4700])
        self.assertEqual(summary["min"], 4650)
        self.assertEqual(summary["max"], 4821)

    def test_window_summary_latest_is_last_element_not_max(self):
        # the most recent reading is the LAST item, even if it's not the largest
        summary = window_summary([4821, 4790, 4650, 4700])
        self.assertEqual(summary["latest"], 4700)

    def test_window_summary_single_element(self):
        summary = window_summary([100])
        self.assertEqual(summary, {"min": 100, "max": 100, "latest": 100})


if __name__ == "__main__":
    unittest.main()
