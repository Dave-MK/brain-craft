import unittest

import numpy as np

from starter import evaluate, fit_classifier

# Cleanly separable by a threshold around 5 -- a LogisticRegression should
# achieve perfect classification deterministically, keeping this test
# reliable rather than flaky.
X_TRAIN = [[1], [2], [3], [3.5], [8], [8.5], [9], [10]]
Y_TRAIN = [0, 0, 0, 0, 1, 1, 1, 1]


class TestOverloadRisk(unittest.TestCase):
    def test_classifier_separates_the_two_classes(self):
        model = fit_classifier(X_TRAIN, Y_TRAIN)
        predictions = model.predict([[1.5], [9.5]])
        self.assertEqual(list(predictions), [0, 1])

    def test_evaluate_returns_a_2x2_confusion_matrix(self):
        model = fit_classifier(X_TRAIN, Y_TRAIN)
        result = evaluate(model, X_TRAIN, Y_TRAIN)
        cm = np.array(result["confusion_matrix"])
        self.assertEqual(cm.shape, (2, 2))

    def test_evaluate_reports_perfect_accuracy_on_this_clean_data(self):
        model = fit_classifier(X_TRAIN, Y_TRAIN)
        result = evaluate(model, X_TRAIN, Y_TRAIN)
        self.assertAlmostEqual(result["accuracy"], 1.0)

    def test_confusion_matrix_has_no_off_diagonal_errors_on_clean_data(self):
        model = fit_classifier(X_TRAIN, Y_TRAIN)
        result = evaluate(model, X_TRAIN, Y_TRAIN)
        cm = np.array(result["confusion_matrix"])
        off_diagonal_total = cm.sum() - np.trace(cm)
        self.assertEqual(off_diagonal_total, 0)


if __name__ == "__main__":
    unittest.main()
