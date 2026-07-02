"""
Lab: Safety Harness
Lesson: rl-training-evaluation-safety

Wrap an agent's proposed action in a hard safety constraint. The
planted bug this lab targets: checking the constraint against the
CURRENT state instead of the state the action would actually produce.
"""

DISCHARGE_STEP = 0.1


def resulting_soc(state, action):
    """Return the battery soc the action would leave behind.

    "charge": soc + DISCHARGE_STEP (capped at 1.0)
    "discharge": soc - DISCHARGE_STEP (floored at 0.0)
    "hold": unchanged
    """
    # TODO: compute the post-action soc with the clamps
    raise NotImplementedError("resulting_soc is not implemented yet")


def safe_action(propose_action, state, hard_floor=0.1):
    """Ask the agent (propose_action(state) -> action string) for its
    action, then enforce the hard constraint:

    If the RESULTING soc would fall below hard_floor, block the action:
    return ("hold", blocked_record) where blocked_record is a dict
    {"proposed": <original action>, "reason": "hard floor violation"}.

    Otherwise return (action, None).
    """
    # TODO: call propose_action(state)
    # TODO: check resulting_soc(state, action) -- NOT the current soc -- against hard_floor
    # TODO: return the (possibly overridden) action and the blocked record or None
    raise NotImplementedError("safe_action is not implemented yet")


def evaluate_scenarios(propose_action, scenarios, hard_floor=0.1):
    """Run safe_action over a list of scenario states. Return
    {"actions": [...], "blocked_count": int}."""
    # TODO: apply safe_action per scenario, collecting actions and counting blocks
    raise NotImplementedError("evaluate_scenarios is not implemented yet")


if __name__ == "__main__":
    always_discharge = lambda state: "discharge"
    print(safe_action(always_discharge, {"battery_soc": 0.15}))
