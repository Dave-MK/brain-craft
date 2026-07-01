"""
Lab: Chronological Split
Lesson: sklearn-baselines-and-leakage
"""

from sklearn.metrics import mean_absolute_error


def naive_baseline_mae(y_true):
    """Compute the MAE of the naive 'tomorrow equals today' baseline.

    y_true is a list/array in chronological order. The naive prediction
    for each point is the PREVIOUS point's value (the first point has no
    previous value -- use the first value itself as its own "prediction").
    """
    # TODO: build the naive predictions (shifted by one, first value repeats itself)
    # TODO: return mean_absolute_error(y_true, naive_predictions)
    raise NotImplementedError("naive_baseline_mae is not implemented yet")


def chronological_split(X, y, test_fraction=0.2):
    """Split X, y into (X_train, X_test, y_train, y_test) WITHOUT shuffling.

    The last test_fraction of rows (in their original order) becomes the
    test set; everything before that is train.
    """
    # TODO: compute the split index from len(X) and test_fraction
    # TODO: slice X/y by position -- do NOT use train_test_split with shuffle=True
    raise NotImplementedError("chronological_split is not implemented yet")


if __name__ == "__main__":
    y = [100, 102, 101, 105, 110, 108]
    print(naive_baseline_mae(y))
    print(chronological_split(list(range(10)), list(range(10)), test_fraction=0.3))
