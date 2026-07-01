"""
Lab: Overload Risk
Lesson: sklearn-classification-basics
"""

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix


def fit_classifier(X_train, y_train):
    """Fit and return a LogisticRegression classifier."""
    # TODO: create, fit, and return a LogisticRegression
    raise NotImplementedError("fit_classifier is not implemented yet")


def evaluate(model, X_test, y_test):
    """Return a dict: {"confusion_matrix": 2x2 array, "accuracy": float}."""
    # TODO: predict on X_test
    # TODO: return confusion_matrix(y_test, predictions) and accuracy
    raise NotImplementedError("evaluate is not implemented yet")


if __name__ == "__main__":
    X_train = [[1], [2], [3], [8], [9], [10]]
    y_train = [0, 0, 0, 1, 1, 1]
    model = fit_classifier(X_train, y_train)
    print(evaluate(model, [[2], [9]], [0, 1]))
