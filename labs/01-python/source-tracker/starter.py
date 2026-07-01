"""
Lab: Source Tracker
Lesson: python-sets

Track which sources report to which feeds using set operations.
"""


def distinct_sources(readings):
    """Return the set of distinct 'source' values across a list of reading dicts."""
    # TODO: build and return a set of readings' "source" values
    raise NotImplementedError("distinct_sources is not implemented yet")


def sources_in_both(feed_a_sources, feed_b_sources):
    """Return the set of sources present in both feeds."""
    # TODO: use set intersection (&)
    raise NotImplementedError("sources_in_both is not implemented yet")


def sources_only_in_a(feed_a_sources, feed_b_sources):
    """Return the set of sources present in feed_a but not feed_b."""
    # TODO: use set difference (-)
    raise NotImplementedError("sources_only_in_a is not implemented yet")


if __name__ == "__main__":
    demand_sources = {"substation-12", "substation-7"}
    weather_sources = {"substation-12", "substation-3"}
    print(sources_in_both(demand_sources, weather_sources))
    print(sources_only_in_a(demand_sources, weather_sources))
