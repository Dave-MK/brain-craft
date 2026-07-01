"""
Lab: Unified Table
Lesson: pandas-merging-datasets
"""

import pandas as pd


def merge_demand_weather(demand_df, weather_df):
    """INNER JOIN demand_df and weather_df on 'timestamp'.

    Rows whose timestamp doesn't exist in both DataFrames should be
    dropped -- that's what an inner join means.
    """
    # TODO: pd.merge(demand_df, weather_df, on="timestamp", how="inner")
    raise NotImplementedError("merge_demand_weather is not implemented yet")


def attach_daily_price(hourly_df, price_daily_df):
    """hourly_df has an hourly 'timestamp' column. price_daily_df has a
    'date' column and a 'price_per_kwh' column, one row per day.

    Add a 'price_per_kwh' column to hourly_df: every hour of a given day
    gets that day's price. Do this by deriving each hourly row's date and
    merging on it -- don't assume the hourly and daily timestamps line up
    directly.
    """
    # TODO: derive a "date" column from hourly_df["timestamp"] (first 10 chars, or pd.to_datetime(...).dt.date)
    # TODO: merge hourly_df with price_daily_df on "date"
    # TODO: drop the helper "date" column before returning, if you added one
    raise NotImplementedError("attach_daily_price is not implemented yet")


if __name__ == "__main__":
    demand = pd.DataFrame({"timestamp": ["2026-07-01T09:00", "2026-07-01T10:00"], "demand_kw": [4821, 4790]})
    weather = pd.DataFrame({"timestamp": ["2026-07-01T09:00", "2026-07-01T10:00"], "temp_c": [18.5, 19.0]})
    print(merge_demand_weather(demand, weather))
