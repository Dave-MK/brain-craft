import unittest

import pandas as pd

from starter import engineer_features


def make_df():
    return pd.DataFrame(
        {"demand_kw": [4200, 4300, 4100, 4900], "temp_c": [15.0, 15.5, 16.0, 16.5]},
        index=pd.to_datetime([
            "2026-07-01T00:00", "2026-07-01T01:00",
            "2026-07-01T02:00", "2026-07-01T03:00",
        ]),
    )


class TestFullPipeline(unittest.TestCase):
    def test_does_not_mutate_the_original_dataframe(self):
        df = make_df()
        engineer_features(df)
        self.assertNotIn("hour_of_day", df.columns, "engineer_features should return a copy, not mutate the original")

    def test_hour_of_day_matches_the_index(self):
        result = engineer_features(make_df())
        self.assertEqual(result["hour_of_day"].tolist(), [0, 1, 2, 3])

    def test_temp_c_lag_1h_shifts_forward_by_one_row(self):
        result = engineer_features(make_df())
        self.assertTrue(pd.isna(result["temp_c_lag_1h"].iloc[0]))
        self.assertEqual(result["temp_c_lag_1h"].iloc[1], 15.0)
        self.assertEqual(result["temp_c_lag_1h"].iloc[3], 16.0)

    def test_demand_kw_rolling_3h_matches_hand_computed_value(self):
        result = engineer_features(make_df())
        self.assertTrue(pd.isna(result["demand_kw_rolling_3h"].iloc[1]))
        self.assertAlmostEqual(result["demand_kw_rolling_3h"].iloc[2], (4200 + 4300 + 4100) / 3)
        self.assertAlmostEqual(result["demand_kw_rolling_3h"].iloc[3], (4300 + 4100 + 4900) / 3)

    def test_original_columns_are_preserved(self):
        result = engineer_features(make_df())
        self.assertIn("demand_kw", result.columns)
        self.assertIn("temp_c", result.columns)


if __name__ == "__main__":
    unittest.main()
