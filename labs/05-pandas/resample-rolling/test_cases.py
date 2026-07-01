import unittest

import pandas as pd

from starter import hourly_mean, rolling_average, to_datetime_index

RAW = pd.DataFrame({
    "timestamp": [
        "2026-07-01T00:00", "2026-07-01T00:30",
        "2026-07-01T01:00", "2026-07-01T01:30",
    ],
    "demand_kw": [4200, 4400, 4100, 4300],
})


class TestResampleRolling(unittest.TestCase):
    def test_to_datetime_index_removes_timestamp_column_and_sets_datetime_index(self):
        df = to_datetime_index(RAW.copy())
        self.assertNotIn("timestamp", df.columns)
        self.assertIsInstance(df.index, pd.DatetimeIndex)

    def test_hourly_mean_averages_the_two_half_hour_readings_per_hour(self):
        df = to_datetime_index(RAW.copy())
        result = hourly_mean(df, "demand_kw")
        self.assertEqual(len(result), 2)
        self.assertAlmostEqual(result.iloc[0], (4200 + 4400) / 2)
        self.assertAlmostEqual(result.iloc[1], (4100 + 4300) / 2)

    def test_rolling_average_is_nan_until_the_window_is_full(self):
        df = to_datetime_index(RAW.copy())
        result = rolling_average(df, "demand_kw", 2)
        self.assertTrue(pd.isna(result.iloc[0]), "with window=2, the very first row has no full window yet and should be NaN")

    def test_rolling_average_matches_hand_computed_value(self):
        df = to_datetime_index(RAW.copy())
        result = rolling_average(df, "demand_kw", 2)
        self.assertAlmostEqual(result.iloc[1], (4200 + 4400) / 2)
        self.assertAlmostEqual(result.iloc[3], (4100 + 4300) / 2)


if __name__ == "__main__":
    unittest.main()
