"""
Lab: Resample & Rolling
Lesson: pandas-time-series
"""

import pandas as pd


def to_datetime_index(df):
    """Convert df['timestamp'] to real datetimes and set it as the index.

    Return the new DataFrame, with the 'timestamp' column no longer
    present as a plain column (it's the index now).
    """
    # TODO: pd.to_datetime the timestamp column, then set_index it
    raise NotImplementedError("to_datetime_index is not implemented yet")


def hourly_mean(df, column):
    """Resample df[column] (already datetime-indexed) to hourly mean."""
    # TODO: df[column].resample("1h").mean()
    raise NotImplementedError("hourly_mean is not implemented yet")


def rolling_average(df, column, window):
    """Return the rolling `window`-period average of df[column]."""
    # TODO: df[column].rolling(window=window).mean()
    raise NotImplementedError("rolling_average is not implemented yet")


if __name__ == "__main__":
    df = pd.DataFrame({
        "timestamp": ["2026-07-01T00:00", "2026-07-01T00:30", "2026-07-01T01:00"],
        "demand_kw": [4200, 4300, 4100],
    })
    df = to_datetime_index(df)
    print(hourly_mean(df, "demand_kw"))
    print(rolling_average(df, "demand_kw", 2))
