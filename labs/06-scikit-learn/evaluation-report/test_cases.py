import math
import unittest

from sklearn.ensemble import RandomForestRegressor

from starter import compute_mae_rmse, get_feature_importances


class TestEvaluationReport(unittest.TestCase):
    def test_mae_hand_computed(self):
        # errors: |10-11|=1, |20-19|=1, |30-33|=3, |40-37|=3 -> MAE = 8/4 = 2.0
        mae, _ = compute_mae_rmse([10, 20, 30, 40], [11, 19, 33, 37])
        self.assertAlmostEqual(mae, 2.0)

    def test_rmse_hand_computed(self):
        # squared errors: 1, 1, 9, 9 -> mean = 5 -> rmse = sqrt(5)
        _, rmse = compute_mae_rmse([10, 20, 30, 40], [11, 19, 33, 37])
        self.assertAlmostEqual(rmse, math.sqrt(5))

    def test_rmse_penalizes_one_big_error_more_than_mae_does(self):
        # same total absolute error (4), but concentrated in one point
        # for the second case -- RMSE should be larger there, MAE the same.
        mae_spread, rmse_spread = compute_mae_rmse([0, 0, 0, 0], [1, 1, 1, 1])
        mae_concentrated, rmse_concentrated = compute_mae_rmse([0, 0, 0, 0], [4, 0, 0, 0])
        self.assertAlmostEqual(mae_spread, mae_concentrated)
        self.assertGreater(rmse_concentrated, rmse_spread)

    def test_feature_importances_identifies_the_dominant_feature(self):
        # y depends heavily on x1, and is pure random noise with respect to x2
        import random
        random.seed(0)
        X = [[i, random.random() * 0.01] for i in range(200)]
        y = [i for i, _ in X]

        model = RandomForestRegressor(random_state=42, n_estimators=50)
        model.fit(X, y)

        importances = get_feature_importances(model, ["x1_strong_signal", "x2_pure_noise"])
        self.assertIn("x1_strong_signal", importances)
        self.assertIn("x2_pure_noise", importances)
        self.assertGreater(
            importances["x1_strong_signal"], importances["x2_pure_noise"],
            "the feature that actually drives the target should show higher importance than pure noise",
        )


if __name__ == "__main__":
    unittest.main()
