"""
Lab: Threshold Classifier
Lesson: python-control-flow

Classify a demand reading as "OVERLOAD", "WARNING", or "NORMAL".

A reading at or above safe_limit_kw is OVERLOAD (the limit itself counts
as unsafe -- watch your boundary operator). A reading above
warning_threshold_kw but below safe_limit_kw is WARNING. Anything else
is NORMAL.
"""


def classify_demand(demand_kw, safe_limit_kw=5000, warning_threshold_kw=4500):
    # TODO: return "OVERLOAD" if demand_kw is AT OR ABOVE safe_limit_kw
    # TODO: return "WARNING" if demand_kw is above warning_threshold_kw
    # TODO: otherwise return "NORMAL"
    raise NotImplementedError("classify_demand is not implemented yet")


if __name__ == "__main__":
    for reading in [4200, 4600, 5000, 5100]:
        print(reading, "->", classify_demand(reading))
