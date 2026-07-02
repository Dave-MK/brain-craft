import unittest

import torch
import torch.nn as nn
import torch.optim as optim

from starter import LSTMForecaster, build_sliding_windows


class TestSlidingWindows(unittest.TestCase):
    def test_shapes_match_the_documented_contract(self):
        X, y = build_sliding_windows([1, 2, 3, 4, 5], window_size=3)
        self.assertEqual(tuple(X.shape), (2, 3, 1))
        self.assertEqual(tuple(y.shape), (2, 1))

    def test_windows_contain_consecutive_readings(self):
        X, y = build_sliding_windows([10, 20, 30, 40, 50], window_size=2)
        self.assertEqual(X[0].flatten().tolist(), [10, 20])
        self.assertEqual(X[1].flatten().tolist(), [20, 30])
        self.assertEqual(X[2].flatten().tolist(), [30, 40])

    def test_targets_are_the_reading_immediately_after_each_window(self):
        X, y = build_sliding_windows([10, 20, 30, 40, 50], window_size=2)
        self.assertEqual(y.flatten().tolist(), [30, 40, 50])

    def test_window_count_is_correct(self):
        X, y = build_sliding_windows(list(range(100)), window_size=24)
        self.assertEqual(len(X), 100 - 24)


class TestLSTMForecaster(unittest.TestCase):
    def test_forward_pass_output_shape(self):
        model = LSTMForecaster()
        batch = torch.randn(4, 24, 1)
        self.assertEqual(tuple(model(batch).shape), (4, 1))

    def test_contains_an_lstm_layer_not_just_linear_ones(self):
        model = LSTMForecaster()
        lstm_layers = [m for m in model.modules() if isinstance(m, nn.LSTM)]
        self.assertGreaterEqual(len(lstm_layers), 1, "the forecaster must actually contain an nn.LSTM")

    def test_rejects_input_with_the_wrong_feature_count(self):
        # The lesson's planted bug is a shape mismatch. Note: nn.LSTM
        # legitimately accepts 2-D (seq_len, features) input as an
        # unbatched sequence, so (4, 1) does NOT raise -- the error
        # PyTorch actually enforces is a feature-count mismatch on the
        # last dimension.
        model = LSTMForecaster(n_features=1)
        with self.assertRaises(Exception):
            model(torch.randn(4, 24, 3))

    def test_learns_a_trivially_predictable_sequence(self):
        # Constant series: every window of [5,5,5] predicts 5. Even a tiny
        # LSTM learns this fast, keeping the test quick and reliable.
        torch.manual_seed(0)
        series = [5.0] * 40
        X, y = build_sliding_windows(series, window_size=5)
        X, y = X.float(), y.float()

        model = LSTMForecaster(hidden_size=8)
        loss_fn = nn.MSELoss()
        optimizer = optim.Adam(model.parameters(), lr=0.02)
        for _ in range(200):
            optimizer.zero_grad()
            loss = loss_fn(model(X), y)
            loss.backward()
            optimizer.step()

        with torch.no_grad():
            prediction = model(X[:1]).item()
        self.assertAlmostEqual(prediction, 5.0, delta=0.5)


if __name__ == "__main__":
    unittest.main()
