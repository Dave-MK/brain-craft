import unittest

from starter import compare_on_same_split, improvement_percent

X = [[i] for i in range(40)]
Y = [3 * i + 5 for i in range(40)]


def make_recording_candidate(predict_fn):
    """A stub candidate that records exactly what data it was given."""
    calls = {}

    def fit_predict(X_train, y_train, X_test):
        calls["X_train"] = list(X_train)
        calls["y_train"] = list(y_train)
        calls["X_test"] = list(X_test)
        return [predict_fn(row) for row in X_test]

    return fit_predict, calls


class TestImprovementPercent(unittest.TestCase):
    def test_hand_computed_improvement(self):
        self.assertAlmostEqual(improvement_percent(10.0, 8.0), 20.0)

    def test_a_worse_model_reports_negative_improvement(self):
        self.assertAlmostEqual(improvement_percent(10.0, 12.0), -20.0)

    def test_equal_maes_report_zero(self):
        self.assertAlmostEqual(improvement_percent(5.0, 5.0), 0.0)


class TestCompareOnSameSplit(unittest.TestCase):
    def test_returns_one_mae_per_candidate(self):
        perfect, _ = make_recording_candidate(lambda row: 3 * row[0] + 5)
        offset, _ = make_recording_candidate(lambda row: 3 * row[0] + 5 + 2)
        results = compare_on_same_split({"perfect": perfect, "offset": offset}, X, Y)
        self.assertEqual(set(results.keys()), {"perfect", "offset"})

    def test_maes_are_correct_for_known_prediction_errors(self):
        perfect, _ = make_recording_candidate(lambda row: 3 * row[0] + 5)
        offset, _ = make_recording_candidate(lambda row: 3 * row[0] + 5 + 2)
        results = compare_on_same_split({"perfect": perfect, "offset": offset}, X, Y)
        self.assertAlmostEqual(results["perfect"], 0.0)
        self.assertAlmostEqual(results["offset"], 2.0)  # constant +2 error -> MAE exactly 2

    def test_every_candidate_receives_the_identical_split(self):
        # The lesson's planted bug: candidates evaluated on different
        # data. The recording stubs let us check both candidates saw
        # exactly the same train and test rows.
        a, calls_a = make_recording_candidate(lambda row: 0)
        b, calls_b = make_recording_candidate(lambda row: 0)
        compare_on_same_split({"a": a, "b": b}, X, Y, test_fraction=0.25)
        self.assertEqual(calls_a["X_train"], calls_b["X_train"])
        self.assertEqual(calls_a["X_test"], calls_b["X_test"])
        self.assertEqual(calls_a["y_train"], calls_b["y_train"])

    def test_split_is_chronological_not_shuffled(self):
        a, calls = make_recording_candidate(lambda row: 0)
        compare_on_same_split({"a": a}, X, Y, test_fraction=0.25)
        train_values = [row[0] for row in calls["X_train"]]
        test_values = [row[0] for row in calls["X_test"]]
        self.assertLess(max(train_values), min(test_values), "test rows must be the chronologically last rows, not a shuffled sample")

    def test_test_fraction_is_respected(self):
        a, calls = make_recording_candidate(lambda row: 0)
        compare_on_same_split({"a": a}, X, Y, test_fraction=0.25)
        self.assertEqual(len(calls["X_test"]), 10)
        self.assertEqual(len(calls["X_train"]), 30)


if __name__ == "__main__":
    unittest.main()
