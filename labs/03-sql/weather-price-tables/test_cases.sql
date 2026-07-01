-- Structural checks only, via SQLite's pragma_table_info / pragma_foreign_key_list
-- table-valued functions -- this lab is about schema shape, not data.

SELECT 'weather_stations must have an "id" column as its PRIMARY KEY' AS failure_reason
WHERE NOT EXISTS (SELECT 1 FROM pragma_table_info('weather_stations') WHERE name = 'id' AND pk = 1)

UNION ALL
SELECT 'weather_readings must have a PRIMARY KEY column'
WHERE NOT EXISTS (SELECT 1 FROM pragma_table_info('weather_readings') WHERE pk = 1)

UNION ALL
SELECT 'weather_readings.station_id must exist and be NOT NULL'
WHERE NOT EXISTS (SELECT 1 FROM pragma_table_info('weather_readings') WHERE name = 'station_id' AND "notnull" = 1)

UNION ALL
SELECT 'weather_readings.timestamp must exist and be NOT NULL'
WHERE NOT EXISTS (SELECT 1 FROM pragma_table_info('weather_readings') WHERE name = 'timestamp' AND "notnull" = 1)

UNION ALL
SELECT 'weather_readings.temperature_c must exist and be NOT NULL'
WHERE NOT EXISTS (SELECT 1 FROM pragma_table_info('weather_readings') WHERE name = 'temperature_c' AND "notnull" = 1)

UNION ALL
SELECT 'weather_readings.wind_speed_kmh must exist (NOT NULL is not required for it)'
WHERE NOT EXISTS (SELECT 1 FROM pragma_table_info('weather_readings') WHERE name = 'wind_speed_kmh')

UNION ALL
SELECT 'weather_readings.station_id must be a FOREIGN KEY referencing weather_stations'
WHERE NOT EXISTS (
    SELECT 1 FROM pragma_foreign_key_list('weather_readings')
    WHERE "table" = 'weather_stations' AND "from" = 'station_id'
);
