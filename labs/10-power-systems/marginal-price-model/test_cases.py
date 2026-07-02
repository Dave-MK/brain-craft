import unittest

from starter import marginal_price, price_curve

# cumulative supply: 2000 @ 0.02 | 3500 @ 0.08 | 4500 @ 0.15 | 5300 @ 0.35
BIDS = [(0.02, 2000), (0.08, 1500), (0.15, 1000), (0.35, 800)]


class TestMarginalPrice(unittest.TestCase):
    def test_low_demand_clears_at_the_cheapest_tier(self):
        self.assertAlmostEqual(marginal_price(BIDS, 1000), 0.02)

    def test_demand_spanning_tiers_clears_at_the_marginal_tier_not_the_average(self):
        # 4200 kW needs tiers 1-3 (cumulative 4500 >= 4200): marginal
        # price is 0.15. The averaged-bids bug would give something like
        # (0.02+0.08+0.15)/3 = 0.083 -- clearly different.
        self.assertAlmostEqual(marginal_price(BIDS, 4200), 0.15)

    def test_demand_exactly_at_a_tier_boundary(self):
        # 3500 is exactly covered by tiers 1-2: the marginal tier is 0.08
        self.assertAlmostEqual(marginal_price(BIDS, 3500), 0.08)

    def test_demand_beyond_the_whole_stack_pays_the_top_tier(self):
        self.assertAlmostEqual(marginal_price(BIDS, 6000), 0.35)

    def test_negative_price_tier_can_clear_the_market(self):
        # high-renewable, low-demand conditions: the cheapest tier bids
        # negative and low demand clears there
        renewable_heavy = [(-0.01, 3000), (0.05, 2000)]
        self.assertAlmostEqual(marginal_price(renewable_heavy, 2000), -0.01)


class TestPriceCurve(unittest.TestCase):
    def test_curve_matches_per_level_marginal_prices(self):
        curve = price_curve(BIDS, [1000, 3000, 4200, 6000])
        self.assertEqual(curve, [0.02, 0.08, 0.15, 0.35])

    def test_price_is_monotonically_nondecreasing_in_demand(self):
        curve = price_curve(BIDS, [500, 1500, 2500, 3500, 4500, 5500])
        self.assertEqual(curve, sorted(curve))


if __name__ == "__main__":
    unittest.main()
