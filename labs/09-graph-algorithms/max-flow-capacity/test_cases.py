import unittest

from starter import bottleneck_edges, build_flow_network, max_deliverable_kw

# main-feed -> substation-4 has two parallel routes:
#   via substation-1: min(4000, 3000) = 3000 deliverable
#   via substation-2: min(3000, 2500) = 2500 deliverable
# so max flow = 5500, limited by the {s1->s4 (3000), s2->s4 (2500)} cut.
LINES = [
    ("main-feed", "substation-1", 4000),
    ("substation-1", "substation-4", 3000),
    ("main-feed", "substation-2", 3000),
    ("substation-2", "substation-4", 2500),
]


class TestBuildFlowNetwork(unittest.TestCase):
    def test_every_line_becomes_two_directed_edges(self):
        G = build_flow_network(LINES)
        self.assertTrue(G.has_edge("main-feed", "substation-1"))
        self.assertTrue(G.has_edge("substation-1", "main-feed"))

    def test_capacities_are_symmetric(self):
        # The lesson's planted bug: a bidirectional line modeled with
        # different capacities per direction.
        G = build_flow_network(LINES)
        for a, b, capacity in LINES:
            self.assertEqual(G[a][b]["capacity"], capacity)
            self.assertEqual(G[b][a]["capacity"], capacity, f"line {a}<->{b} has asymmetric capacities")


class TestMaxDeliverable(unittest.TestCase):
    def test_hand_computed_max_flow(self):
        G = build_flow_network(LINES)
        self.assertEqual(max_deliverable_kw(G, "main-feed", "substation-4"), 5500)

    def test_single_path_is_limited_by_its_weakest_line(self):
        G = build_flow_network([("a", "b", 4000), ("b", "c", 1500)])
        self.assertEqual(max_deliverable_kw(G, "a", "c"), 1500)


class TestBottleneckEdges(unittest.TestCase):
    def test_identifies_the_true_bottleneck_cut(self):
        G = build_flow_network(LINES)
        cut = bottleneck_edges(G, "main-feed", "substation-4")
        self.assertEqual(cut, {("substation-1", "substation-4"), ("substation-2", "substation-4")})

    def test_cut_capacity_equals_max_flow(self):
        # the max-flow min-cut theorem, checked directly on the learner's
        # own two answers
        G = build_flow_network(LINES)
        cut = bottleneck_edges(G, "main-feed", "substation-4")
        cut_capacity = sum(G[u][v]["capacity"] for u, v in cut)
        self.assertEqual(cut_capacity, max_deliverable_kw(G, "main-feed", "substation-4"))


if __name__ == "__main__":
    unittest.main()
