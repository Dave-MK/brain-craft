"""
Lab: Intensity Trade-off
Lesson: capstone-carbon-optimisation

Compute a mix-weighted carbon intensity (the planted bug: a flat average
across sources regardless of how much each actually produced), then find
where the cheapest and cleanest hours genuinely disagree.
"""

INTENSITY_BY_SOURCE = {"solar": 40, "wind": 10, "gas": 450, "coal": 900, "nuclear": 15}


def carbon_intensity_g_per_kwh(generation_mix):
    """generation_mix: {source: kwh_generated}. Return the mix-WEIGHTED
    average intensity: sum(kwh * intensity) / total kwh."""
    # TODO: weight each source by its actual generation, not a flat average
    raise NotImplementedError("carbon_intensity_g_per_kwh is not implemented yet")


def cheapest_hour(price_by_hour):
    """Return the hour index with the lowest price."""
    # TODO: argmin over the list
    raise NotImplementedError("cheapest_hour is not implemented yet")


def cleanest_hour(mix_by_hour):
    """mix_by_hour: list of generation-mix dicts, one per hour.
    Return the hour index with the lowest carbon intensity."""
    # TODO: argmin over carbon_intensity_g_per_kwh per hour
    raise NotImplementedError("cleanest_hour is not implemented yet")


if __name__ == "__main__":
    print(carbon_intensity_g_per_kwh({"solar": 3000, "gas": 2000}))
