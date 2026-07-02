import unittest

from starter import most_overloaded, redistribute_equally, simulate_cascade


def stable_grid():
    return {
        "A": {"capacity": 100, "flow": 40},
        "B": {"capacity": 100, "flow": 50},
        "C": {"capacity": 200, "flow": 60},
    }


def fragile_grid():
    return {
        "A": {"capacity": 100, "flow": 90},
        "B": {"capacity": 100, "flow": 80},
        "C": {"capacity": 200, "flow": 60},
    }


class TestRedistributeEqually(unittest.TestCase):
    def test_failed_flow_splits_equally_across_survivors(self):
        result = redistribute_equally(stable_grid(), "A")
        self.assertNotIn("A", result)
        self.assertAlmostEqual(result["B"]["flow"], 70)   # 50 + 40/2
        self.assertAlmostEqual(result["C"]["flow"], 80)   # 60 + 40/2

    def test_capacities_are_untouched(self):
        result = redistribute_equally(stable_grid(), "A")
        self.assertEqual(result["B"]["capacity"], 100)
        self.assertEqual(result["C"]["capacity"], 200)

    def test_input_dict_is_not_mutated(self):
        lines = stable_grid()
        redistribute_equally(lines, "A")
        self.assertIn("A", lines)
        self.assertEqual(lines["B"]["flow"], 50)


class TestMostOverloaded(unittest.TestCase):
    def test_returns_none_when_nothing_is_over_capacity(self):
        self.assertIsNone(most_overloaded(stable_grid()))

    def test_picks_the_worst_offender(self):
        lines = {
            "B": {"capacity": 100, "flow": 125},  # over by 25
            "C": {"capacity": 200, "flow": 210},  # over by 10
        }
        self.assertEqual(most_overloaded(lines), "B")


class TestSimulateCascade(unittest.TestCase):
    def test_stable_grid_stops_after_the_initial_failure(self):
        # A's 40 kW spreads as +20 each: B->70, C->80, both within capacity
        self.assertEqual(simulate_cascade(stable_grid(), "A"), ["A"])

    def test_fragile_grid_cascades_step_by_step_to_total_blackout(self):
        # Hand-traced: A fails (90 -> +45 each): B=125 (over 25), C=105 (ok).
        # B fails (125 -> all to C): C=230 > 200. C fails. Full blackout.
        self.assertEqual(simulate_cascade(fragile_grid(), "A"), ["A", "B", "C"])

    def test_grid_that_stays_connected_can_still_cascade(self):
        # The lesson's core claim: no disconnection needed -- pure
        # capacity overload propagates the failure.
        failed = simulate_cascade(fragile_grid(), "A")
        self.assertGreater(len(failed), 1)


if __name__ == "__main__":
    unittest.main()
