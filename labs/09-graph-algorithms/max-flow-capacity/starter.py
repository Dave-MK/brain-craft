"""
Lab: Max-Flow Capacity
Lesson: graphs-flow-algorithms

Model the grid as a capacity-constrained flow network and find both the
maximum deliverable power and the bottleneck (min-cut) limiting it.
"""

import networkx as nx


def build_flow_network(lines):
    """lines is a list of (node_a, node_b, capacity_kw) tuples, each
    representing one BIDIRECTIONAL transmission line.

    Return an nx.DiGraph where every line becomes TWO directed edges --
    one in each direction -- with the SAME capacity on both. (The
    lesson's planted bug: mismatched capacities per direction.)
    """
    # TODO: build the DiGraph with symmetric capacities
    raise NotImplementedError("build_flow_network is not implemented yet")


def max_deliverable_kw(G, source, sink):
    """Return the maximum power (float) deliverable from source to sink."""
    # TODO: nx.maximum_flow
    raise NotImplementedError("max_deliverable_kw is not implemented yet")


def bottleneck_edges(G, source, sink):
    """Return the set of edges (as (u, v) tuples) in the minimum cut --
    the actual bottleneck limiting deliverable power."""
    # TODO: nx.minimum_cut gives (cut_value, (reachable, non_reachable));
    #       the cut edges are those from `reachable` into `non_reachable`
    raise NotImplementedError("bottleneck_edges is not implemented yet")


if __name__ == "__main__":
    lines = [
        ("main-feed", "substation-1", 4000),
        ("substation-1", "substation-4", 3000),
        ("main-feed", "substation-2", 3000),
        ("substation-2", "substation-4", 2500),
    ]
    G = build_flow_network(lines)
    print(max_deliverable_kw(G, "main-feed", "substation-4"))
    print(bottleneck_edges(G, "main-feed", "substation-4"))
