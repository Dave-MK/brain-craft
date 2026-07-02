import unittest

from starter import capacity_factor, seasonal_capacity_factors


class TestCapacityFactor(unittest.TestCase):
    def test_hand_computed_solar_day(self):
        # sum = 350 over 12 readings -> mean 29.1667; / 100 nameplate = 0.2917
        solar_day = [0, 0, 10, 40, 80, 90, 80, 40, 10, 0, 0, 0]
        self.assertAlmostEqual(capacity_factor(solar_day, 100), 0.29167, places=4)

    def test_constant_full_output_gives_factor_of_one(self):
        self.assertAlmostEqual(capacity_factor([500, 500, 500], 500), 1.0)

    def test_divides_by_nameplate_not_by_peak_observed(self):
        # THE planted bug's discriminating case: the source never reaches
        # its 200 kW rating (peak observed is only 100). Dividing by the
        # peak would give 0.5; the correct answer against nameplate is 0.25.
        series = [0, 100, 100, 0]
        self.assertAlmostEqual(capacity_factor(series, 200), 0.25)

    def test_zero_output_gives_zero_factor(self):
        self.assertAlmostEqual(capacity_factor([0, 0, 0], 100), 0.0)


class TestSeasonalCapacityFactors(unittest.TestCase):
    def test_computes_one_factor_per_season(self):
        output = {
            "summer": [50, 100, 50],   # mean 66.67 -> 0.6667
            "winter": [10, 30, 20],    # mean 20 -> 0.2
        }
        factors = seasonal_capacity_factors(output, 100)
        self.assertAlmostEqual(factors["summer"], 0.66667, places=4)
        self.assertAlmostEqual(factors["winter"], 0.2)

    def test_seasonal_variation_is_visible(self):
        output = {"summer": [80, 90], "winter": [20, 10]}
        factors = seasonal_capacity_factors(output, 100)
        self.assertGreater(factors["summer"], factors["winter"])


if __name__ == "__main__":
    unittest.main()
