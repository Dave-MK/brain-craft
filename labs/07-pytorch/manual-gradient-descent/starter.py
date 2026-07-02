"""
Lab: Manual Gradient Descent
Lesson: pytorch-tensors-autograd

Use raw tensors and autograd -- no nn.Module, no optimizer -- to compute
a gradient and minimize a simple function by hand.
"""

import torch


def gradient_at(x_value):
    """Return dy/dx of y = 3*x**2 - 5*x + 1, evaluated at x_value, using autograd.

    Hand-check: dy/dx = 6x - 5.
    """
    # TODO: create x = torch.tensor(x_value, requires_grad=True)
    # TODO: compute y, call y.backward(), return x.grad as a plain float
    raise NotImplementedError("gradient_at is not implemented yet")


def minimize_quadratic(start_x, learning_rate=0.1, steps=50):
    """Minimize y = (x - 4)**2 by manual gradient descent from start_x.

    Each step: compute the gradient via autograd, then update
    x <- x - learning_rate * gradient. Return the final x as a plain float.

    The true minimum is at x = 4 -- with these defaults you should land
    very close to it.

    Hint: after each step you must zero/detach the gradient before the
    next backward() call, or gradients will accumulate incorrectly.
    """
    # TODO: implement the manual descent loop with autograd
    raise NotImplementedError("minimize_quadratic is not implemented yet")


if __name__ == "__main__":
    print(gradient_at(3.0))       # should print 13.0 (6*3 - 5)
    print(minimize_quadratic(0.0))  # should print something very close to 4.0
