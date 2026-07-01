"""
Lab: Rolling Window
Lesson: python-lists

Maintain a rolling window of demand readings and summarize it.
"""


def add_reading(readings, new_reading):
    """Append new_reading to readings and return the updated list."""
    # TODO: append new_reading to readings
    # TODO: return the updated list
    raise NotImplementedError("add_reading is not implemented yet")


def window_summary(readings):
    """Return {'min': ..., 'max': ..., 'latest': ...} for a non-empty list of readings."""
    # TODO: latest is the most recent reading (last element), not the maximum
    # TODO: compute min and max across the whole window
    raise NotImplementedError("window_summary is not implemented yet")


if __name__ == "__main__":
    readings = [4821, 4790, 4650, 4700]
    readings = add_reading(readings, 4680)
    print(window_summary(readings))
