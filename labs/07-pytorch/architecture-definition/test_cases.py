import unittest

import torch
import torch.nn as nn

from starter import DemandForecaster


class TestArchitectureDefinition(unittest.TestCase):
    def test_forward_pass_produces_correct_output_shape(self):
        model = DemandForecaster(n_features=3)
        output = model(torch.randn(8, 3))
        self.assertEqual(tuple(output.shape), (8, 1))

    def test_works_with_a_different_feature_count(self):
        model = DemandForecaster(n_features=5, hidden_size=32)
        output = model(torch.randn(4, 5))
        self.assertEqual(tuple(output.shape), (4, 1))

    def test_network_contains_at_least_three_linear_layers(self):
        model = DemandForecaster(n_features=3)
        linear_layers = [m for m in model.modules() if isinstance(m, nn.Linear)]
        self.assertGreaterEqual(len(linear_layers), 3, "expected two hidden layers plus an output layer")

    def test_network_is_actually_nonlinear(self):
        # The defining property the lesson teaches: with ReLU between
        # layers, the network is NOT equivalent to one linear map.
        # A purely linear network satisfies f(a) + f(b) == f(a+b) + f(0);
        # a ReLU network generally doesn't.
        torch.manual_seed(0)
        model = DemandForecaster(n_features=3)
        a, b = torch.randn(1, 3), torch.randn(1, 3)
        zero = torch.zeros(1, 3)
        with torch.no_grad():
            lhs = model(a) + model(b)
            rhs = model(a + b) + model(zero)
        self.assertFalse(
            torch.allclose(lhs, rhs, atol=1e-5),
            "the network behaves like a single linear layer -- did you forget the ReLU activations between layers?",
        )

    def test_gradients_flow_to_every_parameter(self):
        model = DemandForecaster(n_features=3)
        output = model(torch.randn(8, 3)).sum()
        output.backward()
        for name, param in model.named_parameters():
            self.assertIsNotNone(param.grad, f"parameter '{name}' received no gradient -- is it wired into forward()?")


if __name__ == "__main__":
    unittest.main()
