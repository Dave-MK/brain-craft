"""
Lab: CSV & JSON Loader
Lesson: python-files-io

Load the provided demand_history.csv and weather_snapshot.json (in this
same folder) into Python structures, converting numeric CSV fields from
string to float, and handle a missing file gracefully.
"""

import csv
import json


def load_demand_csv(path):
    """Return a list of dicts from the CSV at path, with demand_kw as float.

    If the file doesn't exist, return an empty list instead of crashing.
    """
    # TODO: wrap the open() call in try/except FileNotFoundError, returning []
    # TODO: use csv.DictReader to read rows
    # TODO: convert row["demand_kw"] from string to float for every row
    raise NotImplementedError("load_demand_csv is not implemented yet")


def load_weather_json(path):
    """Return the parsed JSON dict at path, or None if the file doesn't exist."""
    # TODO: wrap the open()/json.load() call in try/except FileNotFoundError
    # TODO: return None if the file is missing
    raise NotImplementedError("load_weather_json is not implemented yet")


if __name__ == "__main__":
    import os

    here = os.path.dirname(__file__)
    readings = load_demand_csv(os.path.join(here, "demand_history.csv"))
    weather = load_weather_json(os.path.join(here, "weather_snapshot.json"))
    print(readings)
    print(weather)
