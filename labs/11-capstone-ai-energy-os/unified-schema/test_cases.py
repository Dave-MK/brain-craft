import unittest

from starter import UNIFIED_KEYS, unify_explanation, verify_unified

FORECASTER_RAW = {
    "model_choice": "random_forest",
    "mae_improvement": 12.5,
    "candidates": ["linear_regression", "random_forest"],
    "limitations": "not validated for heatwave conditions",
}
SCHEDULER_RAW = {
    "recommended_action": "discharge",
    "estimated_cost_impact": -1.5,
    "estimated_emissions_impact": 0.2,
    "candidate_actions": ["charge", "hold"],
    "rationale": "best combined score",
}
ROUTER_RAW = {
    "recommendation": ["feed", "b", "target"],
    "loss_percent": 2.1,
    "rejected_cheaper": 1,
    "trade_off_note": "cheapest route fails the two-substation scenario",
}


class TestUnifyExplanation(unittest.TestCase):
    def test_all_three_subsystems_produce_the_identical_key_set(self):
        for name, raw in [("forecaster", FORECASTER_RAW), ("battery_scheduler", SCHEDULER_RAW), ("router", ROUTER_RAW)]:
            unified = unify_explanation(name, raw)
            self.assertEqual(set(unified.keys()), UNIFIED_KEYS, f"{name} adapter produced a different shape")

    def test_forecaster_mapping(self):
        unified = unify_explanation("forecaster", FORECASTER_RAW)
        self.assertEqual(unified["recommendation"], "random_forest")
        self.assertEqual(unified["supporting_quantities"], {"mae_vs_baseline": 12.5})
        self.assertEqual(unified["confidence_statement"], "not validated for heatwave conditions")

    def test_scheduler_mapping(self):
        unified = unify_explanation("battery_scheduler", SCHEDULER_RAW)
        self.assertEqual(unified["recommendation"], "discharge")
        self.assertEqual(unified["supporting_quantities"], {"cost": -1.5, "emissions": 0.2})
        self.assertEqual(unified["alternatives_considered"], ["charge", "hold"])

    def test_router_mapping(self):
        unified = unify_explanation("router", ROUTER_RAW)
        self.assertEqual(unified["recommendation"], ["feed", "b", "target"])
        self.assertEqual(unified["supporting_quantities"], {"loss_percent": 2.1, "rejected_cheaper": 1})

    def test_every_adapters_output_passes_the_verifier(self):
        for name, raw in [("forecaster", FORECASTER_RAW), ("battery_scheduler", SCHEDULER_RAW), ("router", ROUTER_RAW)]:
            self.assertEqual(verify_unified(unify_explanation(name, raw)), [])


class TestVerifyUnified(unittest.TestCase):
    def make_valid(self):
        return {
            "recommendation": "discharge",
            "supporting_quantities": {"cost": -1.5},
            "alternatives_considered": ["hold"],
            "confidence_statement": "validated on 3 periods",
        }

    def test_valid_explanation_returns_no_problems(self):
        self.assertEqual(verify_unified(self.make_valid()), [])

    def test_flags_a_string_where_a_number_belongs(self):
        # THE planted bug: a plausible-sounding word passed through into
        # a slot the whole schema exists to keep numeric.
        bad = self.make_valid()
        bad["supporting_quantities"]["cost"] = "low"
        self.assertGreater(len(verify_unified(bad)), 0)

    def test_flags_empty_supporting_quantities(self):
        bad = self.make_valid()
        bad["supporting_quantities"] = {}
        self.assertGreater(len(verify_unified(bad)), 0)

    def test_flags_a_missing_unified_key(self):
        bad = self.make_valid()
        del bad["confidence_statement"]
        self.assertGreater(len(verify_unified(bad)), 0)

    def test_booleans_do_not_count_as_checkable_numbers(self):
        bad = self.make_valid()
        bad["supporting_quantities"]["cost"] = True
        self.assertGreater(len(verify_unified(bad)), 0)


if __name__ == "__main__":
    unittest.main()
