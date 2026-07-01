import unittest

from starter import classify_batch


class TestBatchClassifier(unittest.TestCase):
    def test_classifies_each_reading_independently(self):
        result = classify_batch([4821, 4790, 5100, 4650])
        self.assertEqual(result, ["WARNING", "WARNING", "OVERLOAD", "WARNING"])

    def test_preserves_order_and_length(self):
        readings = [100, 200, 300, 400, 500]
        result = classify_batch(readings)
        self.assertEqual(len(result), len(readings))

    def test_boundary_value_in_a_batch(self):
        result = classify_batch([4500, 5000])
        self.assertEqual(result, ["NORMAL", "OVERLOAD"])

    def test_empty_list_returns_empty_list(self):
        self.assertEqual(classify_batch([]), [])

    def test_respects_custom_thresholds(self):
        result = classify_batch([950, 1000], safe_limit_kw=1000, warning_threshold_kw=900)
        self.assertEqual(result, ["WARNING", "OVERLOAD"])


if __name__ == "__main__":
    unittest.main()
