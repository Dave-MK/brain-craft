"""
Lab: First Fit
Lesson: sklearn-regression-basics
"""

from sklearn.linear_model import LinearRegression


def fit_and_predict(X_train, y_train, X_test):
    """Fit a LinearRegression on X_train/y_train.

    Return (model, predictions) where predictions is the model's output
    on X_test.
    """
    # TODO: create a LinearRegression, fit it, predict on X_test
    raise NotImplementedError("fit_and_predict is not implemented yet")


if __name__ == "__main__":
    X_train = [[1, 2], [2, 1], [3, 4], [4, 3]]
    y_train = [8, 7, 18, 17]  # exactly 2*x1 + 3*x2
    model, predictions = fit_and_predict(X_train, y_train, [[5, 6]])
    print(model.coef_, model.intercept_, predictions)
