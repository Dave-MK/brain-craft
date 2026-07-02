"""
Lab: Continuous Battery
Lesson: rl-policy-gradient-methods

Implement the policy network and the reward-weighted policy gradient
loss. The classic planted bug: a loss that ignores the reward trains
the policy to repeat EVERY action taken, good or bad.
"""

import torch
import torch.nn as nn


class PolicyNetwork(nn.Module):
    """Maps a state vector to a probability distribution over actions."""

    def __init__(self, state_size, n_actions):
        super().__init__()
        # TODO: a single nn.Linear(state_size, n_actions) is enough
        raise NotImplementedError("PolicyNetwork.__init__ is not implemented yet")

    def forward(self, state):
        # TODO: return torch.softmax(self.fc(state), dim=-1)
        raise NotImplementedError("PolicyNetwork.forward is not implemented yet")


def policy_gradient_loss(log_probs, rewards):
    """log_probs: tensor of log-probabilities of the actions actually taken.
    rewards: tensor of the (return) reward observed for each of them.

    Return the REINFORCE loss: -(log_probs * rewards).mean()

    The reward weighting is the whole point: actions that led to zero
    reward must contribute zero loss (no update), and higher-reward
    actions must be reinforced proportionally more.
    """
    # TODO: implement exactly as documented
    raise NotImplementedError("policy_gradient_loss is not implemented yet")


if __name__ == "__main__":
    policy = PolicyNetwork(state_size=2, n_actions=3)
    probs = policy(torch.tensor([0.5, 0.3]))
    print(probs, probs.sum())
