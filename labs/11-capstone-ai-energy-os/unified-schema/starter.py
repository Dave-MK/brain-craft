"""
Lab: Unified Schema
Lesson: capstone-explainability-layer

Adapters map three subsystems' different explanation formats onto ONE
shared schema, and a verifier refuses anything that isn't genuinely
checkable. The planted bug: an adapter that copies a plausible-sounding
string straight into a field that must hold a real number.
"""

UNIFIED_KEYS = {"recommendation", "supporting_quantities", "alternatives_considered", "confidence_statement"}


def unify_explanation(subsystem_name, raw):
    """Map a subsystem's raw explanation onto the unified schema.

    forecaster raw:        {"model_choice", "mae_improvement", "candidates", "limitations"}
      -> supporting_quantities = {"mae_vs_baseline": mae_improvement}
    battery_scheduler raw: {"recommended_action", "estimated_cost_impact",
                            "estimated_emissions_impact", "candidate_actions", "rationale"}
      -> supporting_quantities = {"cost": ..., "emissions": ...}
    router raw:            {"recommendation", "loss_percent", "rejected_cheaper", "trade_off_note"}
      -> supporting_quantities = {"loss_percent": ..., "rejected_cheaper": ...}

    Every unified dict has exactly the keys in UNIFIED_KEYS:
      recommendation           <- model_choice / recommended_action / recommendation
      supporting_quantities    <- per the mapping above
      alternatives_considered  <- candidates / candidate_actions / [] for router
      confidence_statement     <- limitations / rationale / trade_off_note
    """
    # TODO: branch on subsystem_name and build the unified dict
    raise NotImplementedError("unify_explanation is not implemented yet")


def verify_unified(explanation):
    """Return a list of problem strings (empty = genuinely checkable):
      - every key in UNIFIED_KEYS present
      - supporting_quantities non-empty, and every value a real number
        (int/float, bools don't count) -- 'low' or 'acceptable' fails
    """
    # TODO: collect problems, return the list
    raise NotImplementedError("verify_unified is not implemented yet")
