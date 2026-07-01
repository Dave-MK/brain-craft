"""
Lab: Walk-Forward
Lesson: sklearn-time-series-cv
"""

from sklearn.model_selection import TimeSeriesSplit, cross_val_score


def get_time_series_splits(n_samples, n_splits=3):
    """Return a list of (train_idx, test_idx) numpy-array tuples using
    sklearn's TimeSeriesSplit over a range of n_samples indices.
    """
    # TODO: build a TimeSeriesSplit(n_splits=n_splits) and .split() over range(n_samples)
    # TODO: return list(splitter.split(range(n_samples)))
    raise NotImplementedError("get_time_series_splits is not implemented yet")


def cross_validated_mae(model, X, y, n_splits=3):
    """Cross-validate `model` using TimeSeriesSplit(n_splits), scoring
    negative MAE, and return a list of POSITIVE MAE values, one per fold.
    """
    # TODO: cross_val_score(model, X, y, cv=TimeSeriesSplit(n_splits=n_splits), scoring="neg_mean_absolute_error")
    # TODO: negate the result so the returned values are positive MAEs
    raise NotImplementedError("cross_validated_mae is not implemented yet")


if __name__ == "__main__":
    print(get_time_series_splits(10, n_splits=3))
