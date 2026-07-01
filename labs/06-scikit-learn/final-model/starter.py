"""
Lab: Final Model
Lesson: sklearn-demand-forecaster (boss battle)

Compare several candidate models against each other AND against a naive
baseline, using identical cross-validation for every candidate.
"""

from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import TimeSeriesSplit, cross_val_score


def naive_baseline_mae(y):
    """MAE of predicting each value as the previous value (see chronological-split lab)."""
    # TODO: same logic as the earlier lab's naive_baseline_mae
    raise NotImplementedError("naive_baseline_mae is not implemented yet")


def compare_models_cv(models, X, y, n_splits=3):
    """models is a dict {name: unfitted_estimator}.

    For each model, run cross_val_score with TimeSeriesSplit(n_splits),
    scoring="neg_mean_absolute_error". Return {name: mean_of_fold_maes}
    where each value is a POSITIVE mean MAE across folds.

    Every candidate MUST be evaluated with the exact same TimeSeriesSplit
    configuration -- that's the whole point of a fair comparison.
    """
    # TODO: loop over models.items(), cross_val_score each with the same TimeSeriesSplit
    raise NotImplementedError("compare_models_cv is not implemented yet")


if __name__ == "__main__":
    from sklearn.linear_model import LinearRegression

    X = [[i] for i in range(30)]
    y = [3 * i + 5 for i in range(30)]
    print(naive_baseline_mae(y))
    print(compare_models_cv({"linear": LinearRegression()}, X, y))
