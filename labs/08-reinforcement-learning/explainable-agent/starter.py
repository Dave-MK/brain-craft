"""
Lab: Explainable Agent
Lesson: rl-battery-scheduler (boss battle)

Two halves: generate a checkable explanation for a chosen action, and
build the verifier that refuses to pass explanations that merely SOUND
detailed but contain no checkable numbers.
"""


def explain_action(state, chosen_action, action_estimates, weights):
    """Build a checkable explanation dict.

    action_estimates: {action_name: {"cost": float, "emissions": float,
                                      "resulting_soc": float}} for every
    candidate action, including the chosen one.

    Return:
      {
        "recommended_action": chosen_action,
        "supporting_quantities": <the chosen action's estimates dict>,
        "alternatives_considered": [
            {"action": <name>, **<that action's estimates>}
            for every action EXCEPT the chosen one
        ],
        "rationale": <a string that mentions the weights used, e.g.
                      f"best combined score under emissions weight
                      {weights['emissions']} and overload weight
                      {weights['overload']}">,
      }
    """
    # TODO: build the dict exactly as documented
    raise NotImplementedError("explain_action is not implemented yet")


def verify_explanation(explanation):
    """Return a list of problem strings; an empty list means the
    explanation is genuinely checkable.

    Checks:
      - "recommended_action" key present
      - "supporting_quantities" present, non-empty, and EVERY value is a
        real number (int/float) -- a value like "low" or "acceptable" is
        exactly the plausible-sounding-but-unverifiable failure this
        verifier exists to catch
      - "alternatives_considered" present with at least one entry
    """
    # TODO: collect and return the list of problems (empty if none)
    raise NotImplementedError("verify_explanation is not implemented yet")


if __name__ == "__main__":
    estimates = {
        "discharge": {"cost": -1.5, "emissions": 0.2, "resulting_soc": 0.4},
        "hold": {"cost": 0.0, "emissions": 0.0, "resulting_soc": 0.5},
    }
    explanation = explain_action({"battery_soc": 0.5}, "discharge", estimates, {"emissions": 0.5, "overload": 10.0})
    print(explanation)
    print(verify_explanation(explanation))
