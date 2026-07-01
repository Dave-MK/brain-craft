"""
Lab: Mask & GroupBy
Lesson: pandas-filtering-aggregation
"""

import pandas as pd


def filter_overload(df, threshold=5000):
    """Return the rows where demand_kw >= threshold, as a boolean-mask filter."""
    # TODO: use a boolean mask, e.g. df[df["demand_kw"] >= threshold]
    raise NotImplementedError("filter_overload is not implemented yet")


def filter_overload_from_source(df, threshold, source):
    """Return rows where demand_kw >= threshold AND source == source.

    Remember: each condition needs its own parentheses when combined with &.
    """
    # TODO: combine two conditions with &, each wrapped in parentheses
    raise NotImplementedError("filter_overload_from_source is not implemented yet")


def summarize_by_source(df):
    """Return a DataFrame indexed by source with columns 'mean' and 'max' of demand_kw."""
    # TODO: use df.groupby("source")["demand_kw"].agg(["mean", "max"])
    raise NotImplementedError("summarize_by_source is not implemented yet")


if __name__ == "__main__":
    df = pd.DataFrame({
        "source": ["substation-12", "substation-12", "substation-7"],
        "demand_kw": [4821, 5100, 4600],
    })
    print(filter_overload(df))
    print(summarize_by_source(df))
