import unittest

import pandas as pd

from starter import drop_duplicate_readings, fill_price_forward, remove_negative_demand, report_missing


def make_messy_df():
    return pd.DataFrame({
        "timestamp": ["t1", "t2", "t2", "t3"],
        "source": ["a", "b", "b", "a"],
        "demand_kw": [100, 200, 200, -50],
        "price_per_kwh": [0.20, None, None, 0.25],
    })


class TestQualityPass(unittest.TestCase):
    def test_report_missing_counts_price_nans(self):
        report = report_missing(make_messy_df())
        self.assertEqual(report["price_per_kwh"], 2)
        self.assertEqual(report["demand_kw"], 0)

    def test_fill_price_forward_does_not_mutate_the_original(self):
        df = make_messy_df()
        filled = fill_price_forward(df)
        self.assertTrue(df["price_per_kwh"].isna().any(), "the original DataFrame should be untouched")
        self.assertFalse(filled["price_per_kwh"].isna().any(), "the returned copy should have no missing prices left")

    def test_fill_price_forward_carries_the_last_known_value(self):
        filled = fill_price_forward(make_messy_df())
        self.assertEqual(filled["price_per_kwh"].iloc[1], 0.20)
        self.assertEqual(filled["price_per_kwh"].iloc[2], 0.20)

    def test_drop_duplicate_readings_keeps_first_occurrence_only(self):
        deduped = drop_duplicate_readings(make_messy_df())
        self.assertEqual(len(deduped), 3)
        self.assertEqual(len(deduped[(deduped["timestamp"] == "t2") & (deduped["source"] == "b")]), 1)

    def test_remove_negative_demand_drops_the_impossible_reading(self):
        cleaned = remove_negative_demand(make_messy_df())
        self.assertTrue((cleaned["demand_kw"] >= 0).all())
        self.assertEqual(len(cleaned), 3)

    def test_full_cleaning_pipeline_composes(self):
        df = make_messy_df()
        df = drop_duplicate_readings(df)
        df = remove_negative_demand(df)
        df = fill_price_forward(df)
        self.assertEqual(len(df), 2)  # t1 and one t2 survive; t3 (negative demand) is dropped
        self.assertFalse(df["price_per_kwh"].isna().any())


if __name__ == "__main__":
    unittest.main()
