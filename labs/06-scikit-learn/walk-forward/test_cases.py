import unittest

from sklearn.linear_model import LinearRegression

from starter import cross_validated_mae, get_time_series_splits


class TestWalkForward(unittest.TestCase):
    def test_returns_correct_number_of_folds(self):
        splits = get_time_series_splits(10, n_splits=3)
        self.assertEqual(len(splits), 3)

    def test_every_train_index_precedes_every_test_index_in_each_fold(self):
        # This is the property that distinguishes TimeSeriesSplit from
        # ordinary (shuffled) KFold: no fold may train on the future
        # relative to what it tests on.
        splits = get_time_series_splits(20, n_splits=4)
        for train_idx, test_idx in splits:
            self.assertLess(
                max(train_idx), min(test_idx),
                "found a fold where a training index comes chronologically after a test index -- this isn't walk-forward",
            )

    def test_training_set_grows_across_successive_folds(self):
        splits = get_time_series_splits(20, n_splits=4)
        train_sizes = [len(train_idx) for train_idx, _ in splits]
        self.assertEqual(train_sizes, sorted(train_sizes), "each fold's training set should be at least as large as the previous fold's")
        self.assertLess(train_sizes[0], train_sizes[-1], "the training set should actually grow, not stay flat")

    def test_cross_validated_mae_returns_one_positive_value_per_fold(self):
        # Perfectly linear, noise-free data -- a LinearRegression should
        # achieve near-zero MAE in every fold regardless of which points
        # land in train vs test, keeping this test deterministic.
        X = [[i] for i in range(30)]
        y = [3 * i + 5 for i in range(30)]
        maes = cross_validated_mae(LinearRegression(), X, y, n_splits=3)
        self.assertEqual(len(maes), 3)
        for mae in maes:
            self.assertGreaterEqual(mae, 0, "MAE values must be returned as positive numbers, not sklearn's negated scoring convention")
            self.assertLess(mae, 1e-6, "a LinearRegression on perfectly linear data should have near-zero MAE in every fold")


if __name__ == "__main__":
    unittest.main()
