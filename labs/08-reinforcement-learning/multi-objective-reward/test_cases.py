import unittest

from starter import choose_safe_weights, compute_reward


class TestComputeReward(unittest.TestCase):
    def test_hand_computed_weighted_sum(self):
        result = {"cost": 2.0, "emissions_kg": 1.5, "overload_penalty": 0.0}
        reward = compute_reward(result, {"emissions": 0.5, "overload": 10.0})
        self.assertAlmostEqual(reward, -2.0 - 0.5 * 1.5)

    def test_overload_penalty_term_is_applied(self):
        result = {"cost": 0.0, "emissions_kg": 0.0, "overload_penalty": 1.0}
        reward = compute_reward(result, {"emissions": 0.5, "overload": 10.0})
        self.assertAlmostEqual(reward, -10.0)

    def test_zero_everything_gives_zero_reward(self):
        result = {"cost": 0.0, "emissions_kg": 0.0, "overload_penalty": 0.0}
        self.assertAlmostEqual(compute_reward(result, {"emissions": 1.0, "overload": 1.0}), 0.0)

    def test_higher_emissions_weight_makes_dirty_actions_score_worse(self):
        dirty = {"cost": 1.0, "emissions_kg": 5.0, "overload_penalty": 0.0}
        low_w = compute_reward(dirty, {"emissions": 0.1, "overload": 10.0})
        high_w = compute_reward(dirty, {"emissions": 2.0, "overload": 10.0})
        self.assertLess(high_w, low_w)


class TestChooseSafeWeights(unittest.TestCase):
    def test_raises_an_unsafe_overload_weight(self):
        safe = choose_safe_weights(5.0, {"emissions": 0.5, "overload": 3.0})
        self.assertGreater(safe["overload"], 5.0)

    def test_leaves_an_already_safe_weight_unchanged(self):
        safe = choose_safe_weights(5.0, {"emissions": 0.5, "overload": 20.0})
        self.assertEqual(safe["overload"], 20.0)

    def test_does_not_mutate_the_input_weights(self):
        base = {"emissions": 0.5, "overload": 3.0}
        choose_safe_weights(5.0, base)
        self.assertEqual(base["overload"], 3.0)

    def test_preserves_the_emissions_weight(self):
        safe = choose_safe_weights(5.0, {"emissions": 0.7, "overload": 3.0})
        self.assertEqual(safe["emissions"], 0.7)

    def test_risky_behavior_never_pays_after_the_fix(self):
        # End-to-end reward-hacking check: with the fixed weights, an
        # overloading action that saves the theoretical maximum must still
        # score worse than a safe action that saves nothing.
        max_savings = 5.0
        weights = choose_safe_weights(max_savings, {"emissions": 0.0, "overload": 3.0})
        risky = {"cost": -max_savings, "emissions_kg": 0.0, "overload_penalty": 1.0}
        safe = {"cost": 0.0, "emissions_kg": 0.0, "overload_penalty": 0.0}
        self.assertLess(
            compute_reward(risky, weights), compute_reward(safe, weights),
            "an overloading action that saves the maximum possible amount still out-scores playing it safe -- the loophole isn't closed",
        )


if __name__ == "__main__":
    unittest.main()
