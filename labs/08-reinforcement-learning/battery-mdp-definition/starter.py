"""
Lab: Battery MDP Definition
Lesson: rl-mdp-fundamentals

Define the battery MDP's transition function. The reward must reflect
the action's ACTUAL effect -- computed from what the action did, never
from the stale pre-action state.
"""

CHARGE_STEP = 0.1
SAFETY_FLOOR = 0.1


def take_action(state, action):
    """Apply `action` to `state` and return (next_state, reward).

    state is a dict: {"battery_soc": 0.0-1.0, "price_per_kwh": float}
    action is one of "charge", "hold", "discharge".

    Rules:
      - "charge": soc increases by CHARGE_STEP (capped at 1.0). The energy
        actually stored is (new_soc - old_soc); it costs
        price_per_kwh * energy_stored, so reward = -that cost.
        (At full battery, no energy is stored, so the cost is 0.)
      - "discharge": soc decreases by CHARGE_STEP (floored at 0.0). The
        energy actually released earns price_per_kwh * energy_released,
        so reward = +that amount.
      - "hold": nothing changes, reward = 0.
      - Safety penalty: if the RESULTING soc is below SAFETY_FLOOR,
        subtract 1.0 from the reward (this is about where the action
        LEFT the battery, not where it started).

    Return (next_state, reward) where next_state is a NEW dict (don't
    mutate the input state).
    """
    # TODO: compute new_soc from the action (with the 0.0/1.0 clamps)
    # TODO: compute reward from the ACTUAL soc change, not the nominal step
    # TODO: apply the safety penalty based on the RESULTING soc
    raise NotImplementedError("take_action is not implemented yet")


if __name__ == "__main__":
    state = {"battery_soc": 0.5, "price_per_kwh": 0.30}
    print(take_action(state, "discharge"))
