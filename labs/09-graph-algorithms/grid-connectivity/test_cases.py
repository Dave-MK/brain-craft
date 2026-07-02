import unittest

from starter import bfs_order, find_unreachable

GRID = {
    "main-feed": ["substation-1", "substation-2"],
    "substation-1": ["main-feed", "substation-3"],
    "substation-2": ["main-feed", "substation-3"],
    "substation-3": ["substation-1", "substation-2"],
    "substation-99": [],  # isolated
}


class TestBfsOrder(unittest.TestCase):
    def test_visits_level_by_level(self):
        order = bfs_order(GRID, "main-feed")
        # level 0: main-feed; level 1: substations 1 and 2 (in adjacency
        # order); level 2: substation-3
        self.assertEqual(order, ["main-feed", "substation-1", "substation-2", "substation-3"])

    def test_no_node_is_visited_twice(self):
        # substation-3 is reachable via BOTH substation-1 and substation-2;
        # a visited-check done on pop instead of on enqueue lets it enter
        # the queue twice and appear twice in the order.
        order = bfs_order(GRID, "main-feed")
        self.assertEqual(len(order), len(set(order)), "a node appears more than once -- mark nodes visited when ENQUEUED, not when popped")

    def test_start_node_is_first(self):
        self.assertEqual(bfs_order(GRID, "substation-3")[0], "substation-3")

    def test_isolated_start_visits_only_itself(self):
        self.assertEqual(bfs_order(GRID, "substation-99"), ["substation-99"])


class TestFindUnreachable(unittest.TestCase):
    def test_detects_the_isolated_substation(self):
        self.assertEqual(find_unreachable(GRID, "main-feed"), {"substation-99"})

    def test_fully_connected_grid_has_no_unreachable_nodes(self):
        connected = {
            "a": ["b"],
            "b": ["a", "c"],
            "c": ["b"],
        }
        self.assertEqual(find_unreachable(connected, "a"), set())

    def test_from_the_isolated_node_everything_else_is_unreachable(self):
        result = find_unreachable(GRID, "substation-99")
        self.assertEqual(result, {"main-feed", "substation-1", "substation-2", "substation-3"})


if __name__ == "__main__":
    unittest.main()
