import inspect
import unittest

import starter
from starter import classify_demand, classify_many, classify_single


class TestExtractTheDuplicate(unittest.TestCase):
    def test_classify_single_normal(self):
        self.assertEqual(classify_single(4200), "NORMAL")

    def test_classify_single_boundary_overload(self):
        self.assertEqual(classify_single(5000), "OVERLOAD")

    def test_classify_many_matches_classify_single_per_item(self):
        readings = [4200, 4600, 5000, 5100]
        expected = [classify_single(r) for r in readings]
        self.assertEqual(classify_many(readings), expected)

    def test_classify_many_empty(self):
        self.assertEqual(classify_many([]), [])

    def test_no_duplicated_threshold_logic_outside_classify_demand(self):
        # Structural check: classify_single and classify_many should each be
        # short delegating functions, not reimplementations. A real
        # implementation of the if/elif chain is much longer than a call.
        single_src = inspect.getsource(classify_single)
        many_src = inspect.getsource(classify_many)
        self.assertLess(
            len(single_src.splitlines()), 6,
            "classify_single looks too long to be a simple delegate to classify_demand()",
        )
        self.assertIn("classify_demand", single_src)
        self.assertIn("classify_demand", many_src)


if __name__ == "__main__":
    unittest.main()
