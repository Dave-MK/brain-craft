"""
Lab: Loss Curves
Lesson: pytorch-overfitting-regularization

Track training AND validation loss, switch between train/eval modes
correctly, and implement early stopping on validation loss.
"""

import torch
import torch.nn as nn
import torch.optim as optim


def train_with_validation(model, X_train, y_train, X_val, y_val, epochs=100, lr=0.01):
    """Train with MSELoss/Adam, tracking validation loss each epoch.

    Return (train_losses, val_losses), two equal-length lists of floats.

    CRITICAL: call model.train() before the training step and model.eval()
    (plus torch.no_grad()) before computing validation loss -- otherwise
    dropout stays active during validation and corrupts the number.
    """
    # TODO: the usual four-step loop for training
    # TODO: model.eval() + torch.no_grad() for the validation loss each epoch
    # TODO: model.train() again before the next training step
    raise NotImplementedError("train_with_validation is not implemented yet")


def train_with_early_stopping(model, X_train, y_train, X_val, y_val, max_epochs=500, lr=0.01, patience=10):
    """Same as above, but stop early once validation loss hasn't improved
    for `patience` consecutive epochs.

    Return (train_losses, val_losses, stopped_epoch) where stopped_epoch
    is the epoch index training actually stopped at (== max_epochs - 1 if
    it never stopped early).
    """
    # TODO: track best_val_loss and a patience counter
    # TODO: break out of the loop when patience is exhausted
    raise NotImplementedError("train_with_early_stopping is not implemented yet")


if __name__ == "__main__":
    torch.manual_seed(0)
    model = nn.Sequential(nn.Linear(1, 8), nn.ReLU(), nn.Linear(8, 1))
    X = torch.linspace(0, 1, 20).reshape(-1, 1)
    y = 2 * X + 1
    print(train_with_validation(model, X[:15], y[:15], X[15:], y[15:], epochs=10))
