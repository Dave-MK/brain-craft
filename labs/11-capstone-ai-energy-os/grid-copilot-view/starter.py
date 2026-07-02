"""
Lab: Grid Copilot View
Lesson: capstone-dashboard

Turn a unified explanation into a priority-ordered dashboard summary.
The planted bug: giving every field equal weight, burying the
safety-critical alert among routine detail.
"""


def summarize_top_trade_off(supporting_quantities):
    """Return the two quantities with the largest ABSOLUTE values, as a
    dict of {name: value} -- the headline trade-off, not the full list."""
    # TODO: sort by abs(value), keep the top two
    raise NotImplementedError("summarize_top_trade_off is not implemented yet")


def render_dashboard_summary(unified_explanation, safety_status):
    """Build the dashboard's priority-ordered summary:

      {
        "alert_banner": "UNSAFE" if not safety_status["is_safe"] else None,
        "primary_recommendation": unified_explanation["recommendation"],
        "key_trade_off": summarize_top_trade_off(...supporting_quantities...),
        "details_expandable": unified_explanation,   # full detail NESTED, not flattened
      }

    The hierarchy is the point: the banner and recommendation are
    top-level; everything else stays tucked inside details_expandable.
    """
    # TODO: build exactly this structure
    raise NotImplementedError("render_dashboard_summary is not implemented yet")
