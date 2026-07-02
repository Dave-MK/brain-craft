import unittest

import networkx as nx

from starter import recommend_route, route_loss, survives_contingency


def three_route_grid():
    G = nx.Graph()
    G.add_edge("feed", "a", weight=1)
    G.add_edge("a", "target", weight=1)   # loss 2 (cheapest)
    G.add_edge("feed", "b", weight=2)
    G.add_edge("b", "target", weight=2)   # loss 4
    G.add_edge("feed", "c", weight=3)
    G.add_edge("c", "target", weight=3)   # loss 6
    return G


class TestHelpers(unittest.TestCase):
    def test_route_loss_hand_computed(self):
        self.assertEqual(route_loss(three_route_grid(), ["feed", "b", "target"]), 4)

    def test_survives_when_no_failed_node_is_on_the_path(self):
        self.assertTrue(survives_contingency(["feed", "b", "target"], {"a", "c"}))

    def test_fails_when_a_failed_node_is_on_the_path(self):
        self.assertFalse(survives_contingency(["feed", "a", "target"], {"a"}))


class TestRecommendRoute(unittest.TestCase):
    def test_with_no_contingencies_the_cheapest_route_wins(self):
        result = recommend_route(three_route_grid(), "feed", "target", [])
        self.assertEqual(result["recommendation"], ["feed", "a", "target"])
        self.assertEqual(result["loss"], 2)
        self.assertEqual(result["rejected_cheaper"], 0)

    def test_cheapest_route_is_rejected_when_it_fails_a_scenario(self):
        # THE planted bug's discriminating case: the raw lowest-loss route
        # (via a, loss 2) dies in the {a} scenario. An implementation that
        # skips the contingency check would recommend it anyway.
        result = recommend_route(three_route_grid(), "feed", "target", [{"a"}])
        self.assertEqual(result["recommendation"], ["feed", "b", "target"])
        self.assertEqual(result["loss"], 4)
        self.assertEqual(result["rejected_cheaper"], 1)

    def test_survivor_must_pass_every_scenario_not_just_one(self):
        result = recommend_route(three_route_grid(), "feed", "target", [{"a"}, {"b"}])
        self.assertEqual(result["recommendation"], ["feed", "c", "target"])
        self.assertEqual(result["loss"], 6)
        self.assertEqual(result["rejected_cheaper"], 2)

    def test_reports_explicitly_when_nothing_survives(self):
        result = recommend_route(three_route_grid(), "feed", "target", [{"a"}, {"b"}, {"c"}])
        self.assertIsNone(result["recommendation"])
        self.assertEqual(result["reason"], "no candidate survives all specified contingencies")

    def test_a_scenario_with_two_simultaneous_failures(self):
        # the mission's founding two-substation scenario, end to end
        result = recommend_route(three_route_grid(), "feed", "target", [{"a", "b"}])
        self.assertEqual(result["recommendation"], ["feed", "c", "target"])


if __name__ == "__main__":
    unittest.main()
