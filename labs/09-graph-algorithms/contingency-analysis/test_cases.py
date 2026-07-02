import unittest

import networkx as nx

from starter import find_articulation_points, find_bridges, simulate_failures


def diamond_grid():
    """feed connects to b via two parallel paths (through x and through y).
    Neither x nor y is individually critical -- but losing BOTH cuts b off.
    A bridge hangs off b to the leaf substation."""
    return nx.Graph([
        ("feed", "x"), ("feed", "y"),
        ("x", "b"), ("y", "b"),
        ("b", "leaf"),
    ])


class TestArticulationPoints(unittest.TestCase):
    def test_finds_the_single_critical_node(self):
        # b is the only articulation point: removing it strands leaf
        self.assertEqual(find_articulation_points(diamond_grid()), {"b"})

    def test_parallel_path_nodes_are_not_individually_critical(self):
        points = find_articulation_points(diamond_grid())
        self.assertNotIn("x", points)
        self.assertNotIn("y", points)


class TestBridges(unittest.TestCase):
    def test_finds_the_single_bridge(self):
        bridges = find_bridges(diamond_grid())
        self.assertEqual(len(bridges), 1)
        self.assertIn(tuple(sorted(next(iter(bridges)))), {("b", "leaf")})

    def test_parallel_path_edges_are_not_bridges(self):
        bridges = {tuple(sorted(edge)) for edge in find_bridges(diamond_grid())}
        self.assertNotIn(("feed", "x"), bridges)
        self.assertNotIn(("b", "x"), bridges)


class TestSimulateFailures(unittest.TestCase):
    def test_single_noncritical_failure_disconnects_nothing(self):
        self.assertEqual(simulate_failures(diamond_grid(), {"x"}, "feed"), set())

    def test_two_individually_safe_nodes_disconnect_the_grid_together(self):
        # THE founding scenario: x and y are each fine to lose alone, but
        # losing both cuts off b and leaf. Single-node articulation
        # analysis alone would have called this grid "resilient."
        unreachable = simulate_failures(diamond_grid(), {"x", "y"}, "feed")
        self.assertEqual(unreachable, {"b", "leaf"})

    def test_removing_the_articulation_point_strands_the_leaf(self):
        self.assertEqual(simulate_failures(diamond_grid(), {"b"}, "feed"), {"leaf"})

    def test_input_graph_is_not_mutated(self):
        G = diamond_grid()
        simulate_failures(G, {"x", "y"}, "feed")
        self.assertIn("x", G.nodes, "simulate_failures must work on a copy, not mutate the input graph")


if __name__ == "__main__":
    unittest.main()
