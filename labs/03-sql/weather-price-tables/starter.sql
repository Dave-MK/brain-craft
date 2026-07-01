-- Lab: Weather & Price Tables
-- Lesson: sql-schema-design
--
-- Design weather_stations + weather_readings with appropriate keys and
-- constraints. No fixture.sql for this lab -- you're creating the schema
-- from nothing.

-- TODO: weather_stations needs a PRIMARY KEY id column, at minimum.
CREATE TABLE weather_stations (
    id TEXT PRIMARY KEY
);

-- TODO: weather_readings needs:
--   - a PRIMARY KEY column
--   - station_id: NOT NULL, and a FOREIGN KEY referencing weather_stations(id)
--   - timestamp: NOT NULL
--   - temperature_c: NOT NULL
--   - wind_speed_kmh: no NOT NULL requirement (a station might not report wind)
CREATE TABLE weather_readings (
    id INTEGER PRIMARY KEY
);
