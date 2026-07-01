-- Lab: Daily Summary
-- Lesson: sql-aggregation
--
-- GROUP BY source_id, keeping only groups whose average demand is above 4500.

-- TODO: per-source average and peak demand, filtered with HAVING AVG(demand_kw) > 4500
CREATE VIEW high_avg_demand_sources AS
SELECT source_id, NULL AS avg_demand, NULL AS peak_demand
FROM readings
WHERE 0;  -- placeholder: returns no rows until you replace this
