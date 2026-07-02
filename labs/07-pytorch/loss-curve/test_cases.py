import unittest

import torch
import torch.nn as nn

from starter import train


def make_linear_problem():
    torch.manual_seed(0)
    model = nn.Linear(1, 1)
    X = torch.tensor([[1.0], [2.0], [3.0], [4.0], [5.0], [6.0]])
    y = 2 * X + 1  # exactly learnable by nn.Linear(1, 1)
    return model, X, y


class TestLossCurve(unittest.TestCase):
    def test_returns_one_loss_per_epoch(self):
        model, X, y = make_linear_problem()
        losses = train(model, X, y, epochs=50, lr=0.05)
        self.assertEqual(len(losses), 50)

    def test_losses_are_plain_floats(self):
        model, X, y = make_linear_problem()
        losses = train(model, X, y, epochs=5, lr=0.05)
        for loss in losses:
            self.assertIsInstance(loss, float)

    def test_loss_decreases_substantially_over_training(self):
        # Relational, not exact: on an exactly-learnable problem the final
        # loss must be far below the initial loss. This is the assertion
        # style stochastic training requires -- direction, not exact value.
        model, X, y = make_linear_problem()
        losses = train(model, X, y, epochs=300, lr=0.05)
        self.assertLess(losses[-1], losses[0] * 0.05, "final loss should be at least 20x smaller than the initial loss")

    def test_model_actually_learns_the_underlying_relationship(self):
        model, X, y = make_linear_problem()
        train(model, X, y, epochs=1000, lr=0.05)
        with torch.no_grad():
            prediction = model(torch.tensor([[10.0]])).item()
        self.assertAlmostEqual(prediction, 21.0, delta=0.5)  # 2*10 + 1

    def test_gradients_do_not_accumulate_across_epochs(self):
        # The missing-zero_grad bug makes training erratic/divergent on a
        # high learning rate. With zero_grad done correctly, this stays stable.
        model, X, y = make_linear_problem()
        losses = train(model, X, y, epochs=300, lr=0.05)
        self.assertLess(
            losses[-1], 1.0,
            "loss failed to converge -- a classic symptom of a missing optimizer.zero_grad()",
        )


if __name__ == "__main__":
    unittest.main()
