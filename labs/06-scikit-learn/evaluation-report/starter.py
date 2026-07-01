"""
Lab: Evaluation Report
Lesson: sklearn-feature-importance-evaluation
"""

from sklearn.metrics import mean_absolute_error, root_mean_squared_error


def compute_mae_rmse(y_true, y_pred):
    """Return (mae, rmse) for the given true/predicted values."""
    # TODO: use sklearn.metrics functions, don't hand-roll the formulas
    raise NotImplementedError("compute_mae_rmse is not implemented yet")


def get_feature_importances(fitted_model, feature_names):
    """Return a dict {feature_name: importance} from an already-fitted
    tree-based model (has a .feature_importances_ attribute)."""
    # TODO: zip feature_names with fitted_model.feature_importances_
    raise NotImplementedError("get_feature_importances is not implemented yet")


if __name__ == "__main__":
    print(compute_mae_rmse([10, 20, 30, 40], [11, 19, 33, 37]))
