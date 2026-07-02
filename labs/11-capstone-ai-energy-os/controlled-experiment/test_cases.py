import unittest

from starter import check_controlled, run_experiment

BASELINE = {"solar_capacity_kw": 5000, "battery_kwh": 100, "demand_profile": "2026-07"}
MODIFIED_OK = {"solar_capacity_kw": 6000, "battery_kwh": 100, "demand_profile": "2026-07"}
MODIFIED_CONFOUNDED = {"solar_capacity_kw": 6000, "battery_kwh": 200, "demand_profile": "2026-07"}


def stub_simulate(config):
    # deterministic: cost falls with solar, emissions fall with solar
    return {
        "total_cost": 10000 - config["solar_capacity_kw"],
        "total_emissions": 500 - config["solar_capacity_kw"] / 100,
    }


class TestCheckControlled(unittest.TestCase):
    def test_a_clean_single_variable_change_passes(self):
        self.assertEqual(check_controlled(BASELINE, MODIFIED_OK, "solar_capacity_kw"), [])

    def test_flags_a_second_differing_variable(self):
        # THE planted bug: battery_kwh also changed, confounding the result
        problems = check_controlled(BASELINE, MODIFIED_CONFOUNDED, "solar_capacity_kw")
        self.assertGreater(len(problems), 0)

    def test_flags_a_tested_variable_that_did_not_actually_change(self):
        problems = check_controlled(BASELINE, dict(BASELINE), "solar_capacity_kw")
        self.assertGreater(len(problems), 0)

    def test_flags_mismatched_key_sets(self):
        missing_key = {"solar_capacity_kw": 6000, "battery_kwh": 100}
        problems = check_controlled(BASELINE, missing_key, "solar_capacity_kw")
        self.assertGreater(len(problems), 0)


class TestRunExperiment(unittest.TestCase):
    def test_computes_hand_checkable_deltas(self):
        result = run_experiment("more solar cuts cost", BASELINE, MODIFIED_OK, "solar_capacity_kw", stub_simulate)
        self.assertAlmostEqual(result["cost_change"], -1000)      # (10000-6000) - (10000-5000)
        self.assertAlmostEqual(result["emissions_change"], -10)   # (500-60) - (500-50)
        self.assertEqual(result["hypothesis"], "more solar cuts cost")

    def test_refuses_to_run_a_confounded_experiment(self):
        result = run_experiment("more solar cuts cost", BASELINE, MODIFIED_CONFOUNDED, "solar_capacity_kw", stub_simulate)
        self.assertIn("error", result)
        self.assertNotIn("cost_change", result)

    def test_confounded_refusal_carries_the_specific_problems(self):
        result = run_experiment("h", BASELINE, MODIFIED_CONFOUNDED, "solar_capacity_kw", stub_simulate)
        self.assertGreater(len(result["error"]), 0)


if __name__ == "__main__":
    unittest.main()
