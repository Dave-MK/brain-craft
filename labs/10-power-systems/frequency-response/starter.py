"""
Lab: Frequency Response
Lesson: power-load-balancing

Simulate frequency deviation under imbalance, and recovery under
generation with real ramp-rate limits. The planted bug: treating slow
generation as if it could correct an imbalance instantly.
"""


def frequency_deviation_hz(generation_kw, demand_kw, grid_inertia_constant=5.0):
    """Simplified deviation: (generation - demand) / (inertia * 1000)."""
    # TODO: implement exactly as documented
    raise NotImplementedError("frequency_deviation_hz is not implemented yet")


def recovery_timeline(imbalance_kw, response_capacity_kw, ramp_rate_kw_per_step):
    """Simulate step-by-step recovery from a sudden demand spike.

    Each step, the responding generation increases its output by at most
    ramp_rate_kw_per_step (never exceeding response_capacity_kw), reducing
    the remaining imbalance. Return the list of remaining-imbalance values
    AFTER each step, ending with (and including) the first step where it
    reaches 0. If the response capacity can never fully cover the
    imbalance, return the timeline up to the step where output has
    plateaued at capacity (imbalance stops improving) -- don't loop forever.
    """
    # TODO: step loop: output += ramp (capped at capacity);
    #       remaining = max(0, imbalance - output); append; stop at 0 or plateau
    raise NotImplementedError("recovery_timeline is not implemented yet")


if __name__ == "__main__":
    print(frequency_deviation_hz(4950, 5000))
    print(recovery_timeline(200, response_capacity_kw=500, ramp_rate_kw_per_step=50))
