import unittest

from starter import classify_demand


class TestThresholdClassifier(unittest.TestCase):
    def test_normal_below_warning(self):
        self.assertEqual(classify_demand(4200), "NORMAL")

    def test_exactly_at_warning_threshold_is_still_normal(self):
        # warning_threshold_kw is exclusive per spec: > 4500, not >=
        self.assertEqual(classify_demand(4500), "NORMAL")

    def test_just_above_warning_threshold_is_warning(self):
        self.assertEqual(classify_demand(4501), "WARNING")

    def test_just_below_safe_limit_is_warning(self):
        self.assertEqual(classify_demand(4999), "WARNING")

    def test_exactly_at_safe_limit_is_overload(self):
        # the classic boundary bug: safe_limit_kw is inclusive (>=), not exclusive (>)
        self.assertEqual(classify_demand(5000), "OVERLOAD")

    def test_above_safe_limit_is_overload(self):
        self.assertEqual(classify_demand(5100), "OVERLOAD")

    def test_custom_thresholds_are_respected(self):
        self.assertEqual(classify_demand(1000, safe_limit_kw=1000, warning_threshold_kw=800), "OVERLOAD")
        self.assertEqual(classify_demand(800, safe_limit_kw=1000, warning_threshold_kw=800), "NORMAL")


if __name__ == "__main__":
    unittest.main()
