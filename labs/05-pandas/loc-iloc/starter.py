"""
Lab: loc & iloc
Lesson: pandas-dataframes-basics
"""

import pandas as pd


def build_dataframe(records):
    """records is a list of dicts. Return a pandas DataFrame built from it."""
    # TODO: build and return a DataFrame from records
    raise NotImplementedError("build_dataframe is not implemented yet")


def set_timestamp_index(df):
    """Return a new DataFrame with the 'timestamp' column set as the index."""
    # TODO: set_index("timestamp") and return the result
    raise NotImplementedError("set_timestamp_index is not implemented yet")


def select_by_label(df, row_label, column_label):
    """Return the value at (row_label, column_label) using .loc."""
    # TODO: use df.loc[...]
    raise NotImplementedError("select_by_label is not implemented yet")


def select_by_position(df, row_position, column_position):
    """Return the value at (row_position, column_position) using .iloc."""
    # TODO: use df.iloc[...]
    raise NotImplementedError("select_by_position is not implemented yet")


if __name__ == "__main__":
    df = build_dataframe([
        {"timestamp": "2026-07-01T09:00", "demand_kw": 4821, "source": "substation-12"},
        {"timestamp": "2026-07-01T10:00", "demand_kw": 4790, "source": "substation-12"},
    ])
    df = set_timestamp_index(df)
    print(select_by_label(df, "2026-07-01T09:00", "demand_kw"))
    print(select_by_position(df, 0, 0))
