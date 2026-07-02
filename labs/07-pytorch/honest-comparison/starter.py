"""
Lab: Honest Comparison
Lesson: pytorch-neural-forecaster (boss battle)

Build the fair-comparison harness itself: both candidate models must be
evaluated on the IDENTICAL chronological test split, with the same
metric, and the improvement must be reported against the correct
baseline. The models are passed in as fit-and-predict callables so the
harness works for sklearn and PyTorch models alike.
"""

from sklearn.metrics import mean_absolute_error


def improvement_percent(baseline_mae, model_mae):
    """Percentage improvement of model_mae over baseline_mae.

    Positive means the model is better (lower MAE) than the baseline.
    Example: baseline 10.0, model 8.0 -> 20.0 (percent).
    """
    # TODO: (baseline_mae - model_mae) / baseline_mae * 100
    raise NotImplementedError("improvement_percent is not implemented yet")


def compare_on_same_split(candidates, X, y, test_fraction=0.25):
    """candidates is a dict {name: fit_predict_fn} where each
    fit_predict_fn(X_train, y_train, X_test) returns predictions for X_test.

    Split X, y chronologically (last test_fraction of rows is the test
    set -- no shuffling), then evaluate EVERY candidate on that same
    train/test split with mean_absolute_error.

    Return {name: mae} for every candidate.
    """
    # TODO: one chronological split, computed once
    # TODO: call each candidate with the SAME X_train, y_train, X_test
    # TODO: score each candidate's predictions against the SAME y_test
    raise NotImplementedError("compare_on_same_split is not implemented yet")


if __name__ == "__main__":
    X = [[i] for i in range(20)]
    y = [2 * i for i in range(20)]

    def perfect(X_train, y_train, X_test):
        return [2 * row[0] for row in X_test]

    print(compare_on_same_split({"perfect": perfect}, X, y))
    print(improvement_percent(10.0, 8.0))
