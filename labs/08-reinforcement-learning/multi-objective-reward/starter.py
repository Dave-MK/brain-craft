"""
Lab: Multi-Objective Reward
Lesson: rl-reward-design

Combine cost, emissions, and overload risk into one scalar reward --
and close the reward-hacking loophole where risky behavior pays.
"""


def compute_reward(action_result, weights):
    """action_result: {"cost": float, "emissions_kg": float, "overload_penalty": float}
    weights: {"emissions": float, "overload": float}

    reward = -cost - weights["emissions"] * emissions_kg
                    - weights["overload"] * overload_penalty
    """
    # TODO: implement the weighted sum exactly as documented
    raise NotImplementedError("compute_reward is not implemented yet")


def choose_safe_weights(max_possible_savings, base_weights):
    """Return a copy of base_weights with the "overload" weight raised
    (if needed) so that risky behavior NEVER pays.

    The reward-hacking scenario from the lesson: an overload event has
    overload_penalty = 1.0, and the most a risky strategy could ever save
    is max_possible_savings in cost. If
        weights["overload"] * 1.0 <= max_possible_savings
    then a rational agent will accept overloads to save money.

    Fix: ensure weights["overload"] is strictly greater than
    max_possible_savings (leave it unchanged if it already is; never
    lower an already-safe weight).
    """
    # TODO: return a NEW dict; raise the overload weight only if needed
    raise NotImplementedError("choose_safe_weights is not implemented yet")


if __name__ == "__main__":
    result = {"cost": 2.0, "emissions_kg": 1.5, "overload_penalty": 0.0}
    print(compute_reward(result, {"emissions": 0.5, "overload": 10.0}))
    print(choose_safe_weights(5.0, {"emissions": 0.5, "overload": 3.0}))
