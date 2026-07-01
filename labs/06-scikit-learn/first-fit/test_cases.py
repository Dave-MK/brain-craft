import unittest

import numpy as np

from starter import fit_and_predict

# y = 2*x1 + 3*x2 exactly, no noise -- LinearRegression's closed-form
# solution recovers these coefficients essentially exactly, so this test
# can use tight tolerances despite being "machine learning."
X_TRAIN = [[1, 2], [2, 1], [3, 4], [4, 3], [5, 5], [1, 5]]
Y_TRAIN = [2 * x1 + 3 * x2 for x1, x2 in X_TRAIN]


class TestFirstFit(unittest.TestCase):
    def test_recovers_the_true_coefficients(self):
        model, _ = fit_and_predict(X_TRAIN, Y_TRAIN, [[0, 0]])
        np.testing.assert_allclose(model.coef_, [2.0, 3.0], atol=1e-6)
        self.assertAlmostEqual(model.intercept_, 0.0, places=5)

    def test_predicts_correctly_on_unseen_points(self):
        _, predictions = fit_and_predict(X_TRAIN, Y_TRAIN, [[7, 1], [0, 10]])
        np.testing.assert_allclose(predictions, [17.0, 30.0], atol=1e-4)

    def test_returns_a_fitted_model_object_not_just_predictions(self):
        model, _ = fit_and_predict(X_TRAIN, Y_TRAIN, [[1, 1]])
        self.assertTrue(hasattr(model, "predict"), "fit_and_predict should return the fitted model, not just predictions")


if __name__ == "__main__":
    unittest.main()
