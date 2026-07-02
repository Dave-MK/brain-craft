"""
Lab: Architecture Definition
Lesson: pytorch-building-networks

Define the DemandForecaster network: two hidden layers with ReLU
activations between them. Remember why the activations matter -- two
linear layers with nothing between them collapse into one.
"""

import torch.nn as nn


class DemandForecaster(nn.Module):
    def __init__(self, n_features, hidden_size=16):
        super().__init__()
        # TODO: define layer1 (n_features -> hidden_size), layer2
        #       (hidden_size -> hidden_size), output (hidden_size -> 1),
        #       and a ReLU activation to use between them
        raise NotImplementedError("DemandForecaster.__init__ is not implemented yet")

    def forward(self, x):
        # TODO: layer1 -> ReLU -> layer2 -> ReLU -> output
        raise NotImplementedError("DemandForecaster.forward is not implemented yet")


if __name__ == "__main__":
    import torch

    model = DemandForecaster(n_features=3)
    print(model(torch.randn(8, 3)).shape)  # should be (8, 1)
