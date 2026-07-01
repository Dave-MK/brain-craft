"""
Lab: Full Pipeline
Lesson: pandas-capstone-feature-table (boss battle)

Engineer features on top of an already-clean, datetime-indexed
DataFrame: a time-of-day signal, a lagged weather value, and a rolling
demand average.
"""

import pandas as pd


def engineer_features(df):
    """df has a DatetimeIndex and columns 'demand_kw' and 'temp_c'.

    Add three columns and return the updated DataFrame (a copy, not a
    mutation of the original):
      - hour_of_day: df.index.hour
      - temp_c_lag_1h: temp_c shifted forward by 1 row (yesterday's/last
        hour's temperature -- the first row will be NaN, that's expected)
      - demand_kw_rolling_3h: rolling 3-row mean of demand_kw
    """
    # TODO: work on a copy, not the original df
    # TODO: add hour_of_day, temp_c_lag_1h, demand_kw_rolling_3h
    raise NotImplementedError("engineer_features is not implemented yet")


if __name__ == "__main__":
    df = pd.DataFrame(
        {"demand_kw": [4200, 4300, 4100, 4900], "temp_c": [15.0, 15.5, 16.0, 16.5]},
        index=pd.to_datetime(["2026-07-01T00:00", "2026-07-01T01:00", "2026-07-01T02:00", "2026-07-01T03:00"]),
    )
    print(engineer_features(df))
