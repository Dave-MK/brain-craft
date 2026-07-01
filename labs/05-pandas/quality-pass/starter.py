"""
Lab: Quality Pass
Lesson: pandas-data-cleaning
"""

import pandas as pd


def report_missing(df):
    """Return a dict {column_name: missing_count} for every column."""
    # TODO: df.isna().sum(), converted to a plain dict
    raise NotImplementedError("report_missing is not implemented yet")


def fill_price_forward(df, column="price_per_kwh"):
    """Return a copy of df with missing values in `column` forward-filled."""
    # TODO: df[column] = df[column].ffill() (on a copy, not the original)
    raise NotImplementedError("fill_price_forward is not implemented yet")


def drop_duplicate_readings(df):
    """Return a copy of df with duplicate (timestamp, source) rows removed,
    keeping the first occurrence of each."""
    # TODO: df.drop_duplicates(subset=["timestamp", "source"], keep="first")
    raise NotImplementedError("drop_duplicate_readings is not implemented yet")


def remove_negative_demand(df):
    """Return a copy of df with rows where demand_kw < 0 removed
    (a negative demand reading is a sensor error, not a real measurement)."""
    # TODO: df[df["demand_kw"] >= 0]
    raise NotImplementedError("remove_negative_demand is not implemented yet")


if __name__ == "__main__":
    df = pd.DataFrame({
        "timestamp": ["t1", "t1", "t2"],
        "source": ["a", "a", "a"],
        "demand_kw": [100, 100, -50],
        "price_per_kwh": [0.2, None, 0.25],
    })
    print(report_missing(df))
