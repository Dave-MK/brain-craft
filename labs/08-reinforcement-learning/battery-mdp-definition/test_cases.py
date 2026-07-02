import unittest

from starter import take_action


class TestBatteryMdpDefinition(unittest.TestCase):
    def test_charge_increases_soc_and_costs_money(self):
        next_state, reward = take_action({"battery_soc": 0.5, "price_per_kwh": 0.30}, "charge")
        self.assertAlmostEqual(next_state["battery_soc"], 0.6)
        self.assertAlmostEqual(reward, -0.30 * 0.1)

    def test_discharge_decreases_soc_and_earns_money(self):
        next_state, reward = take_action({"battery_soc": 0.5, "price_per_kwh": 0.30}, "discharge")
        self.assertAlmostEqual(next_state["battery_soc"], 0.4)
        self.assertAlmostEqual(reward, 0.30 * 0.1)

    def test_hold_changes_nothing(self):
        next_state, reward = take_action({"battery_soc": 0.5, "price_per_kwh": 0.30}, "hold")
        self.assertAlmostEqual(next_state["battery_soc"], 0.5)
        self.assertAlmostEqual(reward, 0.0)

    def test_charge_at_full_battery_stores_nothing_and_costs_nothing(self):
        # reward computed from the ACTUAL soc change: full battery stores 0
        next_state, reward = take_action({"battery_soc": 1.0, "price_per_kwh": 0.30}, "charge")
        self.assertAlmostEqual(next_state["battery_soc"], 1.0)
        self.assertAlmostEqual(reward, 0.0)

    def test_charge_near_full_only_pays_for_energy_actually_stored(self):
        # from 0.95, only 0.05 fits -- a stale-state implementation that
        # charges the nominal 0.1 step would compute the wrong cost
        next_state, reward = take_action({"battery_soc": 0.95, "price_per_kwh": 0.40}, "charge")
        self.assertAlmostEqual(next_state["battery_soc"], 1.0)
        self.assertAlmostEqual(reward, -0.40 * 0.05)

    def test_safety_penalty_applies_based_on_resulting_soc(self):
        # The lesson's planted bug: checking the PRE-action soc (0.15,
        # above the floor) instead of the resulting soc (0.05, below it).
        next_state, reward = take_action({"battery_soc": 0.15, "price_per_kwh": 0.30}, "discharge")
        self.assertAlmostEqual(next_state["battery_soc"], 0.05)
        self.assertAlmostEqual(reward, 0.30 * 0.1 - 1.0)

    def test_no_safety_penalty_when_resulting_soc_stays_at_or_above_floor(self):
        next_state, reward = take_action({"battery_soc": 0.25, "price_per_kwh": 0.30}, "discharge")
        self.assertAlmostEqual(next_state["battery_soc"], 0.15)
        self.assertAlmostEqual(reward, 0.30 * 0.1)

    def test_input_state_is_not_mutated(self):
        state = {"battery_soc": 0.5, "price_per_kwh": 0.30}
        take_action(state, "charge")
        self.assertAlmostEqual(state["battery_soc"], 0.5, msg="take_action must return a new state, not mutate the input")


if __name__ == "__main__":
    unittest.main()
