"""
Lab: Extract the Duplicate
Lesson: python-functions

The two functions below both classify a demand reading, but they each
duplicate the exact same if/elif/else logic. Refactor so BOTH functions
call ONE shared classify_demand() function -- the duplication should
disappear entirely, not just be hidden.
"""


def classify_demand(reading_kw, safe_limit_kw=5000, warning_kw=4500):
    """The single, shared classification function both callers below should use."""
    # TODO: implement the classification logic here (and ONLY here)
    raise NotImplementedError("classify_demand is not implemented yet")


def classify_single(reading_kw):
    """Classify one reading. Should call classify_demand(), not reimplement it."""
    # TODO: call classify_demand(reading_kw) and return its result
    raise NotImplementedError("classify_single is not implemented yet")


def classify_many(readings):
    """Classify a list of readings. Should call classify_demand() for each one."""
    # TODO: return a list of classify_demand(r) results, one per reading
    raise NotImplementedError("classify_many is not implemented yet")


if __name__ == "__main__":
    print(classify_single(4821))
    print(classify_many([4821, 4790, 5100]))
