import inspect
import unittest

try:
    import classification
except ImportError:
    classification = None

try:
    import main
except ImportError:
    main = None


class TestPackageSplit(unittest.TestCase):
    def test_classification_module_exists(self):
        self.assertIsNotNone(
            classification, "Create classification.py in this folder with classify_demand()."
        )

    def test_main_module_exists(self):
        self.assertIsNotNone(main, "Create main.py in this folder with run_batch().")

    def test_classify_demand_behaves_correctly(self):
        self.assertEqual(classification.classify_demand(5000), "OVERLOAD")
        self.assertEqual(classification.classify_demand(4600), "WARNING")
        self.assertEqual(classification.classify_demand(1000), "NORMAL")

    def test_run_batch_matches_classify_demand_per_item(self):
        readings = [4821, 4790, 5100]
        expected = [classification.classify_demand(r) for r in readings]
        self.assertEqual(main.run_batch(readings), expected)

    def test_main_imports_from_classification_rather_than_duplicating(self):
        main_source = inspect.getsource(main)
        self.assertIn(
            "classification", main_source,
            "main.py should import classify_demand from classification.py, not redefine it.",
        )
        self.assertNotIn(
            "def classify_demand", main_source,
            "classify_demand should be defined only in classification.py, not duplicated in main.py.",
        )


if __name__ == "__main__":
    unittest.main()
