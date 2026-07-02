import unittest

from starter import evaluate_scenarios, resulting_soc, safe_action


def always(action):
    return lambda state: action


class TestResultingSoc(unittest.TestCase):
    def test_discharge_reduces_soc(self):
        self.assertAlmostEqual(resulting_soc({"battery_soc": 0.5}, "discharge"), 0.4)

    def test_charge_is_capped_at_full(self):
        self.assertAlmostEqual(resulting_soc({"battery_soc": 0.95}, "charge"), 1.0)

    def test_discharge_is_floored_at_zero(self):
        self.assertAlmostEqual(resulting_soc({"battery_soc": 0.05}, "discharge"), 0.0)


class TestSafeAction(unittest.TestCase):
    def test_allows_a_clearly_safe_discharge(self):
        action, blocked = safe_action(always("discharge"), {"battery_soc": 0.8})
        self.assertEqual(action, "discharge")
        self.assertIsNone(blocked)

    def test_blocks_discharge_that_would_cross_the_floor(self):
        # THE discriminating case: current soc 0.15 is ABOVE the 0.1
        # floor, but discharging leaves 0.05, below it. A stale-state
        # check (current soc vs floor) would wrongly allow this.
        action, blocked = safe_action(always("discharge"), {"battery_soc": 0.15})
        self.assertEqual(action, "hold")
        self.assertIsNotNone(blocked)
        self.assertEqual(blocked["proposed"], "discharge")
        self.assertEqual(blocked["reason"], "hard floor violation")

    def test_allows_discharge_landing_exactly_on_the_floor(self):
        action, blocked = safe_action(always("discharge"), {"battery_soc": 0.2})
        self.assertEqual(action, "discharge")
        self.assertIsNone(blocked)

    def test_charge_is_never_blocked_by_the_floor(self):
        action, blocked = safe_action(always("charge"), {"battery_soc": 0.05})
        self.assertEqual(action, "charge")
        self.assertIsNone(blocked)

    def test_respects_a_custom_floor(self):
        action, blocked = safe_action(always("discharge"), {"battery_soc": 0.35}, hard_floor=0.3)
        self.assertEqual(action, "hold")
        self.assertIsNotNone(blocked)


class TestEvaluateScenarios(unittest.TestCase):
    def test_counts_blocks_across_scenarios(self):
        scenarios = [
            {"battery_soc": 0.8},   # safe discharge
            {"battery_soc": 0.15},  # would cross the floor -> blocked
            {"battery_soc": 0.12},  # would cross the floor -> blocked
        ]
        report = evaluate_scenarios(always("discharge"), scenarios)
        self.assertEqual(report["actions"], ["discharge", "hold", "hold"])
        self.assertEqual(report["blocked_count"], 2)


if __name__ == "__main__":
    unittest.main()
