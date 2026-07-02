import unittest

from starter import check_baseline_independent, evaluate_full_system, improvement_percent

BASELINE_COMPONENTS = {"rule_scheduler", "flat_pricing", "static_routing"}
OPTIMISED_COMPONENTS = {"rl_scheduler", "marginal_pricing", "adaptive_routing"}
LEAKED_COMPONENTS = {"rule_scheduler", "marginal_pricing", "static_routing"}  # shares marginal_pricing


def stub_simulate(policy, period):
    """Deterministic per-period costs: the optimised policy is 10% cheaper
    in 'spring', 20% cheaper in 'summer', 5% cheaper in 'winter'."""
    baseline_costs = {"spring": 1000.0, "summer": 2000.0, "winter": 1500.0}
    cost = baseline_costs[period]
    if policy == "optimised":
        return cost * {"spring": 0.9, "summer": 0.8, "winter": 0.95}[period]
    return cost


class TestCheckBaselineIndependent(unittest.TestCase):
    def test_disjoint_component_sets_share_nothing(self):
        self.assertEqual(check_baseline_independent(BASELINE_COMPONENTS, OPTIMISED_COMPONENTS), set())

    def test_a_leaked_component_is_detected(self):
        shared = check_baseline_independent(LEAKED_COMPONENTS, OPTIMISED_COMPONENTS)
        self.assertEqual(shared, {"marginal_pricing"})


class TestImprovementPercent(unittest.TestCase):
    def test_hand_computed(self):
        self.assertAlmostEqual(improvement_percent(1000.0, 900.0), 10.0)

    def test_a_regression_is_negative(self):
        self.assertAlmostEqual(improvement_percent(1000.0, 1100.0), -10.0)


class TestEvaluateFullSystem(unittest.TestCase):
    PERIODS = ["spring", "summer", "winter"]

    def test_per_period_improvements_are_hand_checkable(self):
        result = evaluate_full_system(
            stub_simulate, self.PERIODS, "baseline", "optimised",
            BASELINE_COMPONENTS, OPTIMISED_COMPONENTS,
        )
        self.assertEqual(len(result["per_period_improvement"]), 3)
        self.assertAlmostEqual(result["per_period_improvement"][0], 10.0)
        self.assertAlmostEqual(result["per_period_improvement"][1], 20.0)
        self.assertAlmostEqual(result["per_period_improvement"][2], 5.0)

    def test_mean_improvement_matches_the_periods(self):
        result = evaluate_full_system(
            stub_simulate, self.PERIODS, "baseline", "optimised",
            BASELINE_COMPONENTS, OPTIMISED_COMPONENTS,
        )
        self.assertAlmostEqual(result["mean_improvement"], (10.0 + 20.0 + 5.0) / 3)

    def test_consistency_flag_reflects_every_period(self):
        result = evaluate_full_system(
            stub_simulate, self.PERIODS, "baseline", "optimised",
            BASELINE_COMPONENTS, OPTIMISED_COMPONENTS,
        )
        self.assertTrue(result["consistent"])

    def test_a_contaminated_baseline_is_refused_outright(self):
        # THE final planted bug of the curriculum: the baseline secretly
        # uses the optimised system's pricing model. The evaluation must
        # refuse, not report a subtly-wrong improvement number.
        result = evaluate_full_system(
            stub_simulate, self.PERIODS, "baseline", "optimised",
            LEAKED_COMPONENTS, OPTIMISED_COMPONENTS,
        )
        self.assertIn("error", result)
        self.assertEqual(result["shared"], {"marginal_pricing"})
        self.assertNotIn("mean_improvement", result)

    def test_a_period_where_the_system_regresses_breaks_consistency(self):
        def simulate_with_bad_winter(policy, period):
            if policy == "optimised" and period == "winter":
                return 2000.0  # worse than the 1500 baseline
            return stub_simulate(policy, period)

        result = evaluate_full_system(
            simulate_with_bad_winter, self.PERIODS, "baseline", "optimised",
            BASELINE_COMPONENTS, OPTIMISED_COMPONENTS,
        )
        self.assertFalse(result["consistent"])


if __name__ == "__main__":
    unittest.main()
