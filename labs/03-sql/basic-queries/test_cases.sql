SELECT 'highest_demand_reading should return exactly 1 row: id 5, demand_kw 5400' AS failure_reason
WHERE (SELECT COUNT(*) FROM highest_demand_reading) != 1
   OR NOT EXISTS (SELECT 1 FROM highest_demand_reading WHERE id = 5 AND demand_kw = 5400)

UNION ALL
SELECT 'overload_readings_substation_12 should return exactly the 2 rows with demand_kw >= 5000 for substation-12 (ids 4 and 5)'
WHERE (SELECT COUNT(*) FROM overload_readings_substation_12) != 2
   OR (SELECT COUNT(*) FROM overload_readings_substation_12 WHERE source_id != 'substation-12') != 0
   OR (SELECT COUNT(*) FROM overload_readings_substation_12 WHERE demand_kw < 5000) != 0

UNION ALL
SELECT 'lowest_five_solar should return exactly 5 rows, all with solar_output_kw = 0 (the true 5 lowest)'
WHERE (SELECT COUNT(*) FROM lowest_five_solar) != 5
   OR (SELECT MAX(solar_output_kw) FROM lowest_five_solar) > 0;
