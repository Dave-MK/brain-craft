import unittest

from starter import carbon_intensity_g_per_kwh, cheapest_hour, cleanest_hour


class TestCarbonIntensity(unittest.TestCase):
    def test_hand_computed_weighted_intensity(self):
        # (3000*40 + 2000*450) / 5000 = (120000 + 900000) / 5000 = 204
        self.assertAlmostEqual(carbon_intensity_g_per_kwh({"solar": 3000, "gas": 2000}), 204.0)

    def test_single_source_mix_equals_that_sources_intensity(self):
        self.assertAlmostEqual(carbon_intensity_g_per_kwh({"wind": 1000}), 10.0)

    def test_weighting_is_by_actual_generation_not_flat(self):
        # THE planted bug's discriminating case: a lopsided mix. Flat
        # average of solar(40) and coal(900) is 470 regardless of output;
        # the correct weighted answer with 90% solar is much lower.
        lopsided = {"solar": 9000, "coal": 1000}
        # (9000*40 + 1000*900) / 10000 = (360000 + 900000)/10000 = 126
        self.assertAlmostEqual(carbon_intensity_g_per_kwh(lopsided), 126.0)

    def test_more_renewables_in_the_mix_lowers_intensity(self):
        dirty = carbon_intensity_g_per_kwh({"solar": 1000, "gas": 4000})
        clean = carbon_intensity_g_per_kwh({"solar": 4000, "gas": 1000})
        self.assertLess(clean, dirty)


class TestCheapestVsCleanest(unittest.TestCase):
    # A day where the cheapest hour and the cleanest hour DISAGREE:
    # hour 0: cheap (windy night, coal covering the rest)
    # hour 1: expensive but very clean (midday solar flood)
    # hour 2: middling on both
    PRICES = [0.05, 0.20, 0.12]
    MIXES = [
        {"wind": 2000, "coal": 3000},   # intensity (2000*10+3000*900)/5000 = 544
        {"solar": 4500, "gas": 500},    # intensity (4500*40+500*450)/5000 = 81
        {"gas": 5000},                  # intensity 450
    ]

    def test_cheapest_hour_is_hour_zero(self):
        self.assertEqual(cheapest_hour(self.PRICES), 0)

    def test_cleanest_hour_is_hour_one(self):
        self.assertEqual(cleanest_hour(self.MIXES), 1)

    def test_cheapest_and_cleanest_genuinely_disagree_here(self):
        # the lesson's core observation, held directly in the fixture
        self.assertNotEqual(cheapest_hour(self.PRICES), cleanest_hour(self.MIXES))


if __name__ == "__main__":
    unittest.main()
