"""
Lab: Q-Learning Battery
Lesson: rl-value-based-methods

Train a tabular Q-learning agent on the deterministic battery
environment in battery_env.py. All exploration randomness must come
from the seeded rng so results are reproducible.
"""

import random

from battery_env import N_ACTIONS, BatteryEnv


def greedy_action(q_table, state):
    """Return the action index with the highest Q-value for `state`.

    q_table maps state -> list of N_ACTIONS values.
    """
    # TODO: argmax over q_table[state]
    raise NotImplementedError("greedy_action is not implemented yet")


def train_q_learning(env, episodes=2000, alpha=0.1, gamma=0.9, epsilon=0.2, seed=0):
    """Train tabular Q-learning and return the q_table
    (dict: state -> list of N_ACTIONS floats, initialized to zeros).

    Use rng = random.Random(seed) for ALL exploration decisions:
      - explore when rng.random() < epsilon, choosing rng.randrange(N_ACTIONS)
      - otherwise exploit with greedy_action

    Update rule after each step:
      q[s][a] += alpha * (reward + gamma * max(q[s']) - q[s][a])
    """
    # TODO: initialize q_table with zeros for env.all_states()
    # TODO: loop episodes: reset, then step until done, applying the update rule
    raise NotImplementedError("train_q_learning is not implemented yet")


def run_greedy_episode(env, q_table):
    """Run one full episode always taking the greedy action.
    Return the total reward."""
    # TODO: reset, loop until done taking greedy_action, sum rewards
    raise NotImplementedError("run_greedy_episode is not implemented yet")


if __name__ == "__main__":
    env = BatteryEnv()
    q_table = train_q_learning(env)
    print("greedy episode reward:", run_greedy_episode(env, q_table))
