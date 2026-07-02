import unittest

import networkx as nx

from starter import choose_route, get_candidate_paths


def three_route_grid():
    G = nx.Graph()
    G.add_edge("feed", "a", weight=1)
    G.add_edge("a", "target", weight=1)   # loss 2 (cheapest)
    G.add_edge("feed", "b", weight=2)
    G.add_edge("b", "target", weight=2)   # loss 4
    G.add_edge("feed", "c", weight=3)
    G.add_edge("c", "target", weight=3)   # loss 6
    return G


def path_loss(G, path):
    return sum(G[u][v]["weight"] for u, v in zip(path, path[1:]))


class TestGetCandidatePaths(unittest.TestCase):
    def test_returns_k_distinct_paths(self):
        candidates = get_candidate_paths(three_route_grid(), "feed", "target", k=3)
        self.assertEqual(len(candidates), 3)
        self.assertEqual(len({tuple(p) for p in candidates}), 3)

    def test_k_greater_than_one_actually_returns_more_than_one(self):
        # The lesson's planted bug: a generator stuck at k=1 gives the
        # policy no real choice.
        candidates = get_candidate_paths(three_route_grid(), "feed", "target", k=3)
        self.assertGreater(len(candidates), 1, "only one candidate returned -- the policy has nothing to choose between")

    def test_candidates_are_ordered_cheapest_first(self):
        G = three_route_grid()
        candidates = get_candidate_paths(G, "feed", "target", k=3)
        losses = [path_loss(G, p) for p in candidates]
        self.assertEqual(losses, sorted(losses))
        self.assertEqual(losses[0], 2)

    def test_k_larger_than_available_paths_returns_all_of_them(self):
        candidates = get_candidate_paths(three_route_grid(), "feed", "target", k=10)
        self.assertEqual(len(candidates), 3)


class TestChooseRoute(unittest.TestCase):
    def test_returns_the_path_the_policy_picked(self):
        candidates = [["feed", "a", "target"], ["feed", "b", "target"]]
        pick_second = lambda state, n_actions: 1
        self.assertEqual(choose_route({}, candidates, pick_second), ["feed", "b", "target"])

    def test_policy_is_told_the_real_candidate_count(self):
        seen = {}

        def recording_policy(state, n_actions):
            seen["n_actions"] = n_actions
            return 0

        candidates = [["p1"], ["p2"], ["p3"]]
        choose_route({}, candidates, recording_policy)
        self.assertEqual(seen["n_actions"], 3, "the policy must be told how many candidates actually exist")

    def test_state_is_passed_through_to_the_policy(self):
        seen = {}

        def recording_policy(state, n_actions):
            seen["state"] = state
            return 0

        choose_route({"price": 0.3}, [["p1"]], recording_policy)
        self.assertEqual(seen["state"], {"price": 0.3})


if __name__ == "__main__":
    unittest.main()
