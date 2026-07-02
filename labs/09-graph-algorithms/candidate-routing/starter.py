"""
Lab: Candidate Routing
Lesson: graphs-rl-combination

Let the graph algorithm generate a shortlist of strong candidate routes,
and let a policy choose among them. The planted bug: a generator that
only ever returns one option gives the policy nothing to learn from.
"""

from itertools import islice

import networkx as nx


def get_candidate_paths(G, source, target, k=3):
    """Return up to k distinct simple paths from source to target,
    ordered from lowest to highest total 'weight'.

    Hint: nx.shortest_simple_paths(G, source, target, weight="weight")
    yields paths in exactly that order -- take the first k.
    """
    # TODO: islice the generator to k paths, return as a list of node-lists
    raise NotImplementedError("get_candidate_paths is not implemented yet")


def choose_route(state, candidate_paths, policy):
    """policy(state, n_actions) returns an index into candidate_paths.
    Return the chosen path.

    The policy must be told the REAL number of candidates -- a hardcoded
    n_actions (or a single-candidate list) silently removes the choice
    the whole approach depends on.
    """
    # TODO: call policy with len(candidate_paths), return the chosen path
    raise NotImplementedError("choose_route is not implemented yet")


if __name__ == "__main__":
    G = nx.Graph()
    G.add_edge("feed", "a", weight=1)
    G.add_edge("a", "target", weight=1)
    G.add_edge("feed", "b", weight=2)
    G.add_edge("b", "target", weight=2)
    print(get_candidate_paths(G, "feed", "target", k=2))
