import unittest

import pandas as pd

from starter import attach_daily_price, merge_demand_weather

DEMAND = pd.DataFrame({
    "timestamp": ["2026-07-01T09:00", "2026-07-01T10:00", "2026-07-02T09:00"],
    "demand_kw": [4821, 4790, 4950],
})
WEATHER = pd.DataFrame({
    # note: 2026-07-01T10:00 is deliberately missing here
    "timestamp": ["2026-07-01T09:00", "2026-07-02T09:00"],
    "temp_c": [18.5, 20.0],
})
PRICE_DAILY = pd.DataFrame({
    "date": ["2026-07-01", "2026-07-02"],
    "price_per_kwh": [0.28, 0.31],
})


class TestUnifiedTable(unittest.TestCase):
    def test_inner_join_drops_unmatched_timestamps(self):
        merged = merge_demand_weather(DEMAND, WEATHER)
        # 2026-07-01T10:00 has no weather row, so it must be dropped
        self.assertEqual(len(merged), 2)
        self.assertNotIn("2026-07-01T10:00", merged["timestamp"].tolist())

    def test_inner_join_keeps_matching_columns_from_both_sides(self):
        merged = merge_demand_weather(DEMAND, WEATHER)
        self.assertIn("demand_kw", merged.columns)
        self.assertIn("temp_c", merged.columns)

    def test_attach_daily_price_gives_every_hour_of_a_day_the_same_price(self):
        result = attach_daily_price(DEMAND, PRICE_DAILY)
        july_1_rows = result[result["timestamp"].str.startswith("2026-07-01")]
        self.assertTrue((july_1_rows["price_per_kwh"] == 0.28).all())

    def test_attach_daily_price_distinguishes_different_days(self):
        result = attach_daily_price(DEMAND, PRICE_DAILY)
        july_2_row = result[result["timestamp"].str.startswith("2026-07-02")]
        self.assertTrue((july_2_row["price_per_kwh"] == 0.31).all())

    def test_attach_daily_price_preserves_all_original_hourly_rows(self):
        result = attach_daily_price(DEMAND, PRICE_DAILY)
        self.assertEqual(len(result), len(DEMAND))


if __name__ == "__main__":
    unittest.main()
