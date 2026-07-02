"""
Lab: LSTM Forecaster
Lesson: pytorch-sequence-models

Reshape a flat time series into the sliding-window sequences an LSTM
expects, and define the LSTM forecaster itself.
"""

import torch
import torch.nn as nn


def build_sliding_windows(series, window_size):
    """series is a 1-D list/tensor of readings in chronological order.

    Return (X, y) tensors:
      X shape: (n_windows, window_size, 1)  -- each window is the
               `window_size` consecutive readings before the target
      y shape: (n_windows, 1)               -- the reading immediately
               after each window

    Example with series=[1,2,3,4,5], window_size=3:
      X = [[[1],[2],[3]], [[2],[3],[4]]]     y = [[4], [5]]
    """
    # TODO: slide a window of window_size across the series
    # TODO: return torch.tensor(...) pairs shaped exactly as documented
    raise NotImplementedError("build_sliding_windows is not implemented yet")


class LSTMForecaster(nn.Module):
    def __init__(self, n_features=1, hidden_size=32):
        super().__init__()
        # TODO: nn.LSTM(n_features, hidden_size, batch_first=True) and a
        #       Linear(hidden_size, 1) output layer
        raise NotImplementedError("LSTMForecaster.__init__ is not implemented yet")

    def forward(self, x):
        # TODO: run the LSTM, take the final hidden state, project to 1 output
        raise NotImplementedError("LSTMForecaster.forward is not implemented yet")


if __name__ == "__main__":
    X, y = build_sliding_windows([1, 2, 3, 4, 5], window_size=3)
    print(X.shape, y.shape)
    model = LSTMForecaster()
    print(model(X.float()).shape)
