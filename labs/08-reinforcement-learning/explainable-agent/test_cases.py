import unittest

from starter import explain_action, verify_explanation

ESTIMATES = {
    "charge": {"cost": 0.8, "emissions": 0.5, "resulting_soc": 0.6},
    "hold": {"cost": 0.0, "emissions": 0.0, "resulting_soc": 0.5},
    "discharge": {"cost": -1.5, "emissions": 0.2, "resulting_soc": 0.4},
}
WEIGHTS = {"emissions": 0.5, "overload": 10.0}


class TestExplainAction(unittest.TestCase):
    def setUp(self):
        self.explanation = explain_action({"battery_soc": 0.5}, "discharge", ESTIMATES, WEIGHTS)

    def test_names_the_recommended_action(self):
        self.assertEqual(self.explanation["recommended_action"], "discharge")

    def test_supporting_quantities_are_the_chosen_actions_actual_numbers(self):
        support = self.explanation["supporting_quantities"]
        self.assertEqual(support["cost"], -1.5)
        self.assertEqual(support["emissions"], 0.2)
        self.assertEqual(support["resulting_soc"], 0.4)

    def test_alternatives_cover_every_non_chosen_action(self):
        alternatives = self.explanation["alternatives_considered"]
        names = {alt["action"] for alt in alternatives}
        self.assertEqual(names, {"charge", "hold"})

    def test_alternatives_carry_their_own_numbers(self):
        alternatives = {alt["action"]: alt for alt in self.explanation["alternatives_considered"]}
        self.assertEqual(alternatives["charge"]["cost"], 0.8)
        self.assertEqual(alternatives["hold"]["emissions"], 0.0)

    def test_rationale_mentions_the_weights_used(self):
        rationale = self.explanation["rationale"]
        self.assertIn("0.5", rationale)
        self.assertIn("10.0", rationale)

    def test_own_explanation_passes_its_own_verifier(self):
        self.assertEqual(verify_explanation(self.explanation), [])


class TestVerifyExplanation(unittest.TestCase):
    def make_valid(self):
        return {
            "recommended_action": "discharge",
            "supporting_quantities": {"cost": -1.5, "emissions": 0.2},
            "alternatives_considered": [{"action": "hold", "cost": 0.0}],
            "rationale": "best combined score",
        }

    def test_valid_explanation_returns_no_problems(self):
        self.assertEqual(verify_explanation(self.make_valid()), [])

    def test_flags_a_plausible_sounding_but_unverifiable_quantity(self):
        # "low" SOUNDS like information but can't be checked against
        # anything -- this is the exact failure mode the lesson targets.
        explanation = self.make_valid()
        explanation["supporting_quantities"]["cost"] = "low"
        problems = verify_explanation(explanation)
        self.assertGreater(len(problems), 0)

    def test_flags_empty_supporting_quantities(self):
        explanation = self.make_valid()
        explanation["supporting_quantities"] = {}
        self.assertGreater(len(verify_explanation(explanation)), 0)

    def test_flags_missing_alternatives(self):
        explanation = self.make_valid()
        explanation["alternatives_considered"] = []
        self.assertGreater(len(verify_explanation(explanation)), 0)

    def test_flags_missing_recommended_action(self):
        explanation = self.make_valid()
        del explanation["recommended_action"]
        self.assertGreater(len(verify_explanation(explanation)), 0)


if __name__ == "__main__":
    unittest.main()
