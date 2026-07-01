-- Lab: Rolling Average
-- Lesson: sql-window-functions
--
-- Add a rolling 3-row average per source, ordered by time, WITHOUT
-- collapsing the individual reading rows the way GROUP BY would.

-- TODO: use OVER (PARTITION BY source_id ORDER BY timestamp ROWS BETWEEN 2 PRECEDING AND CURRENT ROW)
CREATE VIEW demand_with_rolling_avg AS
SELECT id, source_id, timestamp, demand_kw, demand_kw AS rolling_avg_3
FROM readings
WHERE 0;  -- placeholder: returns no rows until you replace this
