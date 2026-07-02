"""
Lab: Loss Curve
Lesson: pytorch-training-loop

Implement the four-step training loop: forward, loss, backward,
optimizer step (with zero_grad).
"""

import torch
import torch.nn as nn
import torch.optim as optim


def train(model, X, y, epochs=100, lr=0.01):
    """Train `model` on (X, y) with MSELoss and the Adam optimizer.

    Return a list of the loss value (a plain float) at every epoch, in
    order -- the caller uses this to see the loss curve descend.

    Remember: optimizer.zero_grad() every iteration, or gradients
    accumulate across epochs and training misbehaves.
    """
    # TODO: create loss_fn = nn.MSELoss() and optimizer = optim.Adam(model.parameters(), lr=lr)
    # TODO: each epoch: forward -> loss -> zero_grad -> backward -> step
    # TODO: append loss.item() to a list each epoch; return the list
    raise NotImplementedError("train is not implemented yet")


if __name__ == "__main__":
    torch.manual_seed(0)
    model = nn.Linear(1, 1)
    X = torch.tensor([[1.0], [2.0], [3.0], [4.0]])
    y = torch.tensor([[3.0], [5.0], [7.0], [9.0]])  # y = 2x + 1
    losses = train(model, X, y, epochs=200, lr=0.05)
    print(losses[0], "->", losses[-1])
