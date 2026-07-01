-- Lab: Basic Queries
-- Lesson: sql-select-where
--
-- Define each answer as a VIEW (not a bare SELECT) so it can be checked
-- automatically. Replace each placeholder body below with a real query.

-- TODO: the single reading with the highest demand_kw
CREATE VIEW highest_demand_reading AS
SELECT id, source_id, timestamp, demand_kw, solar_output_kw
FROM readings
WHERE 0;  -- placeholder: returns no rows until you replace this

-- TODO: all OVERLOAD-range readings (demand_kw >= 5000) from substation-12
CREATE VIEW overload_readings_substation_12 AS
SELECT id, source_id, timestamp, demand_kw, solar_output_kw
FROM readings
WHERE 0;

-- TODO: the 5 readings with the lowest solar_output_kw
CREATE VIEW lowest_five_solar AS
SELECT id, source_id, timestamp, demand_kw, solar_output_kw
FROM readings
WHERE 0;
