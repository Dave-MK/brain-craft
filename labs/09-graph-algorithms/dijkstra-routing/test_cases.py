import unittest

from starter import dijkstra, shortest_path

# Fewest hops A->D is A-B-D (2 hops, total loss 10).
# Minimum loss A->D is A-C-E-D (3 hops, total loss 3).
GRID = {
    "A": {"B": 5, "C": 1},
    "B": {"A": 5, "D": 5},
    "C": {"A": 1, "E": 1},
    "D": {"B": 5, "E": 1},
    "E": {"C": 1, "D": 1},
}


class TestDijkstra(unittest.TestCase):
    def test_hand_computed_distances(self):
        distances = dijkstra(GRID, "A")
        self.assertEqual(distances["A"], 0)
        self.assertEqual(distances["C"], 1)
        self.assertEqual(distances["E"], 2)
        self.assertEqual(distances["D"], 3)
        self.assertEqual(distances["B"], 5)

    def test_minimum_loss_beats_fewest_hops(self):
        # The whole point of the lesson: A-B-D is only 2 hops but costs
        # 10; the true minimum is 3 via the longer A-C-E-D route.
        self.assertEqual(dijkstra(GRID, "A")["D"], 3)

    def test_distances_from_a_different_start(self):
        distances = dijkstra(GRID, "D")
        self.assertEqual(distances["A"], 3)
        self.assertEqual(distances["C"], 2)


class TestShortestPath(unittest.TestCase):
    def test_returns_the_low_loss_route_not_the_few_hop_route(self):
        self.assertEqual(shortest_path(GRID, "A", "D"), ["A", "C", "E", "D"])

    def test_direct_neighbor_path(self):
        self.assertEqual(shortest_path(GRID, "A", "C"), ["A", "C"])

    def test_path_endpoints_are_included(self):
        path = shortest_path(GRID, "B", "E")
        self.assertEqual(path[0], "B")
        self.assertEqual(path[-1], "E")

    def test_path_total_weight_matches_dijkstra_distance(self):
        path = shortest_path(GRID, "A", "D")
        total = sum(GRID[a][b] for a, b in zip(path, path[1:]))
        self.assertEqual(total, dijkstra(GRID, "A")["D"])


if __name__ == "__main__":
    unittest.main()
