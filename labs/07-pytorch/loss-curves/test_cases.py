import unittest

import torch
import torch.nn as nn

from starter import train_with_early_stopping, train_with_validation


def make_problem(with_dropout=False):
    torch.manual_seed(0)
    layers = [nn.Linear(1, 16), nn.ReLU()]
    if with_dropout:
        layers.append(nn.Dropout(0.5))
    layers.append(nn.Linear(16, 1))
    model = nn.Sequential(*layers)

    X = torch.linspace(0, 1, 30).reshape(-1, 1)
    y = 2 * X + 1
    return model, X[:24], y[:24], X[24:], y[24:]


class TestLossCurves(unittest.TestCase):
    def test_returns_equal_length_train_and_val_curves(self):
        model, X_train, y_train, X_val, y_val = make_problem()
        train_losses, val_losses = train_with_validation(model, X_train, y_train, X_val, y_val, epochs=30, lr=0.05)
        self.assertEqual(len(train_losses), 30)
        self.assertEqual(len(val_losses), 30)

    def test_both_curves_descend_on_a_learnable_problem(self):
        model, X_train, y_train, X_val, y_val = make_problem()
        train_losses, val_losses = train_with_validation(model, X_train, y_train, X_val, y_val, epochs=300, lr=0.05)
        self.assertLess(train_losses[-1], train_losses[0] * 0.1)
        self.assertLess(val_losses[-1], val_losses[0] * 0.1)

    def test_validation_loss_is_computed_in_eval_mode(self):
        # With dropout(0.5) in the model, validation loss computed WITHOUT
        # model.eval() is noisy and systematically worse. On this easy
        # problem, correct eval-mode validation converges near zero;
        # dropout-corrupted validation loss stays visibly higher.
        # Measured empirically: correct eval-mode validation converges to
        # ~0.07 on this fixture; leaving dropout active during validation
        # leaves it around ~0.8. The 0.3 threshold sits between them with
        # a wide margin on both sides.
        model, X_train, y_train, X_val, y_val = make_problem(with_dropout=True)
        _, val_losses = train_with_validation(model, X_train, y_train, X_val, y_val, epochs=400, lr=0.05)
        self.assertLess(
            val_losses[-1], 0.3,
            "validation loss stayed high on an easy problem -- is model.eval() being called before validation?",
        )

    def test_early_stopping_stops_before_max_epochs_when_converged(self):
        model, X_train, y_train, X_val, y_val = make_problem()
        _, _, stopped_epoch = train_with_early_stopping(
            model, X_train, y_train, X_val, y_val, max_epochs=2000, lr=0.05, patience=10
        )
        self.assertLess(stopped_epoch, 1999, "on an easily-learnable problem, early stopping should trigger before max_epochs")

    def test_early_stopping_respects_patience_not_first_plateau_epoch(self):
        model, X_train, y_train, X_val, y_val = make_problem()
        _, val_losses, stopped_epoch = train_with_early_stopping(
            model, X_train, y_train, X_val, y_val, max_epochs=2000, lr=0.05, patience=15
        )
        self.assertGreaterEqual(len(val_losses), 16, "training stopped suspiciously early -- patience must allow that many non-improving epochs first")


if __name__ == "__main__":
    unittest.main()
