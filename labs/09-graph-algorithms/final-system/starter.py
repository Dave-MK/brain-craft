"""
Lab: Final System
Lesson: graphs-grid-router (boss battle)

The complete routing pipeline: generate candidates, check EVERY one
against EVERY contingency scenario, and only recommend a route that
survives them all -- with an explicit trade-off when the cheapest
route had to be rejected. The planted bug this lab targets: returning
the raw lowest-loss candidate without ever running the contingency check.
"""

from itertools import islice

import networkx as nx


def route_loss(G, path):
    """Total 'weight' along the path."""
    # TODO: sum the edge weights between consecutive path nodes
    raise NotImplementedError("route_loss is not implemented yet")


def survives_contingency(path, failed_nodes):
    """True if the path uses none of the failed nodes."""
    # TODO: set intersection check
    raise NotImplementedError("survives_contingency is not implemented yet")


def recommend_route(G, source, target, contingency_scenarios, k=3):
    """Full pipeline:
      1. Generate up to k candidate paths (cheapest first, by 'weight').
      2. Keep only candidates that survive EVERY scenario in
         contingency_scenarios (each scenario is a set of failed nodes).
      3. Recommend the cheapest survivor.

    Return a dict:
      {"recommendation": <path>, "loss": <total weight>,
       "rejected_cheaper": <count of cheaper candidates that failed a scenario>}
    or, when no candidate survives everything:
      {"recommendation": None, "reason": "no candidate survives all specified contingencies"}
    """
    # TODO: candidates -> survivors -> cheapest survivor (or the None dict)
    # TODO: rejected_cheaper = how many candidates cheaper than the chosen
    #       one were rejected by the contingency filter
    raise NotImplementedError("recommend_route is not implemented yet")


if __name__ == "__main__":
    G = nx.Graph()
    G.add_edge("feed", "a", weight=1)
    G.add_edge("a", "target", weight=1)
    G.add_edge("feed", "b", weight=2)
    G.add_edge("b", "target", weight=2)
    print(recommend_route(G, "feed", "target", [{"a"}]))
