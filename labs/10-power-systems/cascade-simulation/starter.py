"""
Lab: Cascade Simulation
Lesson: power-grid-stability-cascading-failures

Simulate a capacity-driven cascading failure: a failed line's flow
redistributes onto survivors, any survivor pushed past its capacity
fails next, and the chain continues until the grid stabilizes or
nothing is left.

Modeling note: this lab redistributes a failed line's flow EQUALLY
across all surviving lines. The lesson is explicit that real rerouting
follows the network's actual topology (Mission 5's routing algorithms);
the equal split is a documented simplification so the cascade LOOP
mechanics -- redistribute, detect overload, fail the worst, repeat --
stay hand-checkable.
"""


def redistribute_equally(lines, failed_id):
    """Remove failed_id from lines and add its flow, split equally,
    to every surviving line. Return a NEW dict (don't mutate the input).

    lines: {line_id: {"capacity": kw, "flow": kw}}
    """
    # TODO: build the new dict with the failed line's flow spread equally
    raise NotImplementedError("redistribute_equally is not implemented yet")


def most_overloaded(lines):
    """Return the id of the line whose flow exceeds its capacity by the
    largest amount, or None if no line is overloaded."""
    # TODO: max over (flow - capacity) where positive; None if none positive
    raise NotImplementedError("most_overloaded is not implemented yet")


def simulate_cascade(lines, initial_failure):
    """Fail initial_failure, then repeatedly redistribute and fail the
    most-overloaded survivor until no line is overloaded (or none remain).

    Return the ordered list of failed line ids, starting with
    initial_failure.
    """
    # TODO: loop redistribute_equally -> most_overloaded until stable
    raise NotImplementedError("simulate_cascade is not implemented yet")


if __name__ == "__main__":
    lines = {
        "A": {"capacity": 100, "flow": 90},
        "B": {"capacity": 100, "flow": 80},
        "C": {"capacity": 200, "flow": 60},
    }
    print(simulate_cascade(lines, "A"))
