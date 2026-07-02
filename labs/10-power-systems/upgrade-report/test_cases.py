import unittest

from starter import DigitalTwinV2

BIDS = [(0.02, 2000), (0.08, 1500), (0.15, 1000), (0.35, 800)]
EDGE = {"voltage_kv": 11, "resistance_ohms": 0.5, "flat_loss_percent": 0.02}


def make_twin(**kwargs):
    return DigitalTwinV2(supply_bids=BIDS, flat_price=0.10, **kwargs)


class TestEdgeLoss(unittest.TestCase):
    def test_realistic_mode_uses_the_physics(self):
        twin = make_twin(use_realistic_loss=True)
        # I = 5,000,000/11,000 A; loss = I^2 * 0.5 / 1000 = 103.3 kW
        self.assertAlmostEqual(twin.edge_loss(EDGE, 5000), 103.3058, places=2)

    def test_flat_mode_uses_the_flat_percentage(self):
        twin = make_twin(use_realistic_loss=False)
        self.assertAlmostEqual(twin.edge_loss(EDGE, 5000), 100.0)  # 5000 * 0.02

    def test_the_toggle_is_actually_wired(self):
        # THE planted bug: a toggle that exists but changes nothing.
        realistic = make_twin(use_realistic_loss=True).edge_loss(EDGE, 3000)
        flat = make_twin(use_realistic_loss=False).edge_loss(EDGE, 3000)
        self.assertNotAlmostEqual(realistic, flat, places=4,
                                  msg="flipping use_realistic_loss changed nothing -- the toggle isn't wired in")


class TestCurrentPrice(unittest.TestCase):
    def test_marginal_mode_prices_net_demand(self):
        twin = make_twin(use_marginal_pricing=True)
        # net demand 4200 - 1000 = 3200 -> tiers 1-2 (cumulative 3500) -> 0.08
        self.assertAlmostEqual(twin.current_price(4200, 1000), 0.08)

    def test_renewables_actually_reduce_the_clearing_price(self):
        twin = make_twin(use_marginal_pricing=True)
        without_renewables = twin.current_price(4200, 0)     # 0.15
        with_renewables = twin.current_price(4200, 1000)     # 0.08
        self.assertLess(with_renewables, without_renewables)

    def test_flat_mode_ignores_conditions_entirely(self):
        twin = make_twin(use_marginal_pricing=False)
        self.assertAlmostEqual(twin.current_price(4200, 1000), 0.10)
        self.assertAlmostEqual(twin.current_price(500, 0), 0.10)

    def test_the_pricing_toggle_is_actually_wired(self):
        marginal = make_twin(use_marginal_pricing=True).current_price(4200, 0)
        flat = make_twin(use_marginal_pricing=False).current_price(4200, 0)
        self.assertNotAlmostEqual(marginal, flat, places=4,
                                  msg="flipping use_marginal_pricing changed nothing -- the toggle isn't wired in")

    def test_net_demand_is_floored_at_zero(self):
        twin = make_twin(use_marginal_pricing=True)
        # renewables exceed demand: net demand 0 clears at the cheapest tier
        self.assertAlmostEqual(twin.current_price(1000, 5000), 0.02)


if __name__ == "__main__":
    unittest.main()
