"""
Lab: Capacity Factor
Lesson: power-renewable-intermittency

Compute capacity factor correctly. The planted bug: dividing by the
peak OBSERVED output instead of the nameplate capacity, which inflates
the number whenever the source never actually hit its rating.
"""


def capacity_factor(actual_output_series_kw, nameplate_capacity_kw):
    """Average actual output divided by nameplate capacity (0.0-1.0)."""
    # TODO: mean of the series / nameplate -- NOT / max(series)
    raise NotImplementedError("capacity_factor is not implemented yet")


def seasonal_capacity_factors(output_by_season, nameplate_capacity_kw):
    """output_by_season: {"winter": [...], "summer": [...], ...}
    Return {season: capacity_factor} per season."""
    # TODO: apply capacity_factor per season
    raise NotImplementedError("seasonal_capacity_factors is not implemented yet")


if __name__ == "__main__":
    solar_day = [0, 0, 10, 40, 80, 90, 80, 40, 10, 0, 0, 0]
    print(capacity_factor(solar_day, nameplate_capacity_kw=100))
