import unittest

from starter import weather_record_from_response


class TestJsonToRecord(unittest.TestCase):
    def test_extracts_all_fields_when_present(self):
        raw = {
            "current": {
                "last_updated": "2026-07-01T09:00",
                "temp_c": 18.5,
                "wind_kph": 12.0,
                "uv_index": 4,  # unrelated field, should be ignored, not crash
            },
            "location": {"name": "irrelevant"},
        }
        record = weather_record_from_response(raw)
        self.assertEqual(record["timestamp"], "2026-07-01T09:00")
        self.assertEqual(record["temperature_c"], 18.5)
        self.assertEqual(record["wind_speed_kmh"], 12.0)
        self.assertEqual(record["source"], "weather-api")

    def test_missing_wind_kph_defaults_to_none_without_crashing(self):
        raw = {"current": {"last_updated": "2026-07-01T10:00", "temp_c": 19.0}}
        record = weather_record_from_response(raw)
        self.assertIsNone(record["wind_speed_kmh"])
        self.assertEqual(record["temperature_c"], 19.0)

    def test_extra_unrelated_top_level_fields_are_ignored(self):
        raw = {
            "current": {"last_updated": "t", "temp_c": 1.0},
            "alerts": ["storm warning"],
            "forecast": {"days": []},
        }
        record = weather_record_from_response(raw)
        self.assertEqual(set(record.keys()), {"timestamp", "temperature_c", "wind_speed_kmh", "source"})


if __name__ == "__main__":
    unittest.main()
