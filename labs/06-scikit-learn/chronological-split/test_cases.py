import unittest

from starter import chronological_split, naive_baseline_mae


class TestChronologicalSplit(unittest.TestCase):
    def test_naive_baseline_mae_hand_computed(self):
        # y = [10, 12, 11, 15]
        # naive predictions = [10, 10, 12, 11] (first repeats itself, rest shift by 1)
        # errors = [0, 2, 1, 4] -> MAE = 7/4 = 1.75
        result = naive_baseline_mae([10, 12, 11, 15])
        self.assertAlmostEqual(result, 1.75)

    def test_naive_baseline_mae_is_zero_for_a_constant_series(self):
        result = naive_baseline_mae([5, 5, 5, 5])
        self.assertAlmostEqual(result, 0.0)

    def test_chronological_split_sizes(self):
        X = list(range(10))
        y = list(range(10))
        X_train, X_test, y_train, y_test = chronological_split(X, y, test_fraction=0.2)
        self.assertEqual(len(X_test), 2)
        self.assertEqual(len(X_train), 8)

    def test_chronological_split_does_not_shuffle(self):
        X = list(range(10))
        y = [v * 10 for v in X]
        X_train, X_test, y_train, y_test = chronological_split(X, y, test_fraction=0.3)
        # test set must be the LAST rows in original order, train must be the FIRST rows
        self.assertEqual(list(X_train), [0, 1, 2, 3, 4, 5, 6])
        self.assertEqual(list(X_test), [7, 8, 9])
        self.assertEqual(list(y_test), [70, 80, 90])

    def test_chronological_split_every_train_index_precedes_every_test_index(self):
        X = list(range(20))
        y = list(range(20))
        X_train, X_test, _, _ = chronological_split(X, y, test_fraction=0.25)
        self.assertLess(max(X_train), min(X_test), "train rows must all come chronologically before test rows")


if __name__ == "__main__":
    unittest.main()
