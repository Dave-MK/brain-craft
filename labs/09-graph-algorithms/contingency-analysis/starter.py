"""
Lab: Contingency Analysis
Lesson: graphs-resilience-critical-nodes

Single-node articulation analysis is NOT enough: the mission's founding
question is about TWO substations failing at once. Two individually
non-critical nodes can still disconnect the grid together.
"""

import networkx as nx


def find_articulation_points(G):
    """Return the set of nodes whose individual removal disconnects G."""
    # TODO: nx.articulation_points
    raise NotImplementedError("find_articulation_points is not implemented yet")


def find_bridges(G):
    """Return the set of edges (as (u, v) tuples) whose individual
    removal disconnects G."""
    # TODO: nx.bridges
    raise NotImplementedError("find_bridges is not implemented yet")


def simulate_failures(G, failed_nodes, source):
    """Remove failed_nodes from a COPY of G (never mutate the input) and
    return the set of surviving nodes no longer reachable from `source`.

    (source is assumed not to be in failed_nodes.)
    """
    # TODO: copy, remove nodes, return the unreachable survivors
    raise NotImplementedError("simulate_failures is not implemented yet")


if __name__ == "__main__":
    G = nx.Graph([("feed", "x"), ("feed", "y"), ("x", "b"), ("y", "b")])
    print(find_articulation_points(G))
    print(simulate_failures(G, {"x", "y"}, "feed"))
