"""
Lab: Dijkstra Routing
Lesson: graphs-shortest-path

Hand-rolled Dijkstra with a priority queue. The fixture is built so the
fewest-hops path and the minimum-loss path are DIFFERENT routes -- if
your result matches BFS's answer, something is wrong.
"""

import heapq


def dijkstra(graph, start):
    """Return {node: minimum_total_weight_from_start} for every node.

    graph: {node: {neighbor: weight}}. Include the staleness check
    (skip a popped entry whose distance is worse than the best known) --
    without it, outdated queue entries get processed.
    """
    # TODO: heapq-based Dijkstra with the staleness check
    raise NotImplementedError("dijkstra is not implemented yet")


def shortest_path(graph, start, end):
    """Return the actual minimum-weight path from start to end as a list
    of nodes (including both endpoints).

    Track each node's predecessor while running Dijkstra, then walk the
    predecessors backward from `end`.
    """
    # TODO: Dijkstra with predecessor tracking, then reconstruct the path
    raise NotImplementedError("shortest_path is not implemented yet")


if __name__ == "__main__":
    grid = {
        "A": {"B": 5, "C": 1},
        "B": {"A": 5, "D": 5},
        "C": {"A": 1, "E": 1},
        "D": {"B": 5, "E": 1},
        "E": {"C": 1, "D": 1},
    }
    print(dijkstra(grid, "A"))
    print(shortest_path(grid, "A", "D"))
