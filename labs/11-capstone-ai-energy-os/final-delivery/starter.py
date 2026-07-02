"""
Lab: Final Delivery
Lesson: capstone-ai-energy-os (the final boss battle of the curriculum)

Make the mission's founding claim -- "this system reduces energy costs"
-- and make it honestly. The planted bug: a "baseline" that secretly
shares components with the optimised system, quietly corrupting the
claimed improvement.
"""


def check_baseline_independent(baseline_components, optimised_components):
    """Both arguments are sets of component names (e.g. {"rule_scheduler",
    "flat_pricing"} vs {"rl_scheduler", "marginal_pricing", ...}).

    Return the set of components they SHARE -- an empty set means the
    baseline is genuinely independent. Any overlap means the comparison
    is contaminated.
    """
    # TODO: set intersection
    raise NotImplementedError("check_baseline_independent is not implemented yet")


def improvement_percent(baseline_cost, optimised_cost):
    """(baseline - optimised) / baseline * 100. Positive = improvement."""
    # TODO: same formula as Mission 4's honest-comparison lab
    raise NotImplementedError("improvement_percent is not implemented yet")


def evaluate_full_system(simulate_fn, evaluation_periods,
                         baseline_policy, optimised_policy,
                         baseline_components, optimised_components):
    """The final evaluation.

    1. Refuse a contaminated comparison: if the component sets overlap,
       return {"error": "baseline shares components with the optimised system",
               "shared": <the overlap set>}.
    2. Otherwise, for each period in evaluation_periods, run
       simulate_fn(policy, period) -> total_cost for BOTH policies, and
       compute the per-period improvement percent.
    3. Return {"per_period_improvement": [...one percent per period...],
               "mean_improvement": <their mean>,
               "consistent": <True if every period's improvement is positive>}.
    """
    # TODO: gate on independence, then evaluate every period identically
    raise NotImplementedError("evaluate_full_system is not implemented yet")
