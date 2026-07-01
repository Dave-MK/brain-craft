import os
import unittest

from starter import load_demand_csv, load_weather_json

HERE = os.path.dirname(__file__)
CSV_PATH = os.path.join(HERE, "demand_history.csv")
JSON_PATH = os.path.join(HERE, "weather_snapshot.json")
MISSING_PATH = os.path.join(HERE, "does_not_exist.csv")
MISSING_JSON_PATH = os.path.join(HERE, "does_not_exist.json")


class TestCsvJsonLoader(unittest.TestCase):
    def test_load_demand_csv_returns_correct_row_count(self):
        readings = load_demand_csv(CSV_PATH)
        self.assertEqual(len(readings), 3)

    def test_load_demand_csv_converts_demand_kw_to_float(self):
        readings = load_demand_csv(CSV_PATH)
        self.assertIsInstance(readings[0]["demand_kw"], float)
        self.assertEqual(readings[0]["demand_kw"], 4821.0)

    def test_load_demand_csv_preserves_string_fields(self):
        readings = load_demand_csv(CSV_PATH)
        self.assertEqual(readings[0]["source"], "substation-12")

    def test_load_demand_csv_missing_file_returns_empty_list(self):
        self.assertEqual(load_demand_csv(MISSING_PATH), [])

    def test_load_weather_json_parses_fields(self):
        weather = load_weather_json(JSON_PATH)
        self.assertEqual(weather["temperature_c"], 18.5)

    def test_load_weather_json_missing_file_returns_none(self):
        self.assertIsNone(load_weather_json(MISSING_JSON_PATH))


if __name__ == "__main__":
    unittest.main()
