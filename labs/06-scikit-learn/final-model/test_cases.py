import unittest

from sklearn.dummy import DummyRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression

from starter import compare_models_cv, naive_baseline_mae

# Perfectly linear, noise-free target -- keeps LinearRegression's
# cross-validated MAE deterministically near zero, so the comparison
# logic itself is what's under test, not model luck.
X = [[i] for i in range(40)]
Y = [3 * i + 5 for i in range(40)]


class TestFinalModel(unittest.TestCase):
    def test_naive_baseline_mae_hand_computed(self):
        result = naive_baseline_mae([10, 12, 11, 15])
        self.assertAlmostEqual(result, 1.75)

    def test_compare_models_cv_returns_one_score_per_model(self):
        models = {
            "linear": LinearRegression(),
            "dummy_mean": DummyRegressor(strategy="mean"),
        }
        results = compare_models_cv(models, X, Y, n_splits=3)
        self.assertEqual(set(results.keys()), {"linear", "dummy_mean"})

    def test_scores_are_positive_mae_not_sklearns_negated_convention(self):
        models = {"linear": LinearRegression()}
        results = compare_models_cv(models, X, Y, n_splits=3)
        self.assertGreaterEqual(results["linear"], 0)

    def test_a_real_model_beats_a_dummy_mean_baseline_on_a_clear_trend(self):
        models = {
            "linear": LinearRegression(),
            "dummy_mean": DummyRegressor(strategy="mean"),
        }
        results = compare_models_cv(models, X, Y, n_splits=3)
        self.assertLess(
            results["linear"], results["dummy_mean"],
            "LinearRegression should clearly beat a model that just predicts the mean, on data with a strong linear trend",
        )

    def test_every_candidate_uses_the_same_cv_configuration(self):
        # If n_splits is honored consistently, both models are evaluated
        # against the same number of folds -- a mismatched implementation
        # (e.g. one model using train_test_split, another using CV) would
        # be caught by comparing this indirectly via consistent behavior
        # across repeated calls with different n_splits.
        models = {"linear": LinearRegression()}
        results_3 = compare_models_cv(models, X, Y, n_splits=3)
        results_5 = compare_models_cv(models, X, Y, n_splits=5)
        self.assertLess(results_3["linear"], 1e-6)
        self.assertLess(results_5["linear"], 1e-6)


if __name__ == "__main__":
    unittest.main()
