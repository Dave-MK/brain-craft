"""
Lab: Grid Connectivity
Lesson: graphs-representation-traversal

Hand-rolled BFS/DFS over an adjacency-list grid -- no networkx here;
the point of this lesson is the traversal mechanics themselves.
"""


def bfs_order(grid, start):
    """Return the list of nodes in the order BFS visits them from start.

    grid is an adjacency list: {node: [neighbor, ...]}.
    Mark nodes visited when they are ENQUEUED, not when they are popped --
    otherwise the same node enters the queue multiple times and the
    order (and the work done) is wrong.
    """
    # TODO: queue-based BFS, visited-on-enqueue
    raise NotImplementedError("bfs_order is not implemented yet")


def find_unreachable(grid, start):
    """Return the set of nodes in `grid` that BFS/DFS from start never reaches."""
    # TODO: traverse from start, return set(grid) - visited
    raise NotImplementedError("find_unreachable is not implemented yet")


if __name__ == "__main__":
    grid = {
        "main-feed": ["substation-1", "substation-2"],
        "substation-1": ["main-feed", "substation-3"],
        "substation-2": ["main-feed"],
        "substation-3": ["substation-1"],
        "substation-99": [],  # isolated on purpose
    }
    print(bfs_order(grid, "main-feed"))
    print(find_unreachable(grid, "main-feed"))
