"""
Lab: JSON to Record
Lesson: apis-consuming-rest

Convert a raw, nested weather-API response into the standard flat
structured-record shape, defending against a sometimes-missing field.
"""


def weather_record_from_response(raw_json):
    """Extract a flat record from a raw weather API response dict.

    raw_json looks like:
        {
            "current": {
                "last_updated": "...",
                "temp_c": ...,
                "wind_kph": ...,   # sometimes ABSENT entirely
                ... other fields you should ignore ...
            },
            ... other top-level fields you should ignore ...
        }

    Return {"timestamp": ..., "temperature_c": ..., "wind_speed_kmh": ...,
    "source": "weather-api"}. wind_speed_kmh should be None if wind_kph
    is missing from the response -- never raise a KeyError.
    """
    # TODO: extract last_updated -> timestamp, temp_c -> temperature_c
    # TODO: use .get() for wind_kph -> wind_speed_kmh, defaulting to None
    # TODO: set source to "weather-api"
    raise NotImplementedError("weather_record_from_response is not implemented yet")


if __name__ == "__main__":
    sample = {"current": {"last_updated": "2026-07-01T09:00", "temp_c": 18.5, "wind_kph": 12.0}}
    print(weather_record_from_response(sample))
