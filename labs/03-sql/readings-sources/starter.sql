-- Lab: Readings & Sources
-- Lesson: sql-joins
--
-- Build a LEFT JOIN so every reading is kept, even the one whose
-- source_id has no matching row in sources.

-- TODO: LEFT JOIN readings to sources; keep every reading; NULL rated_capacity_kw when unknown
CREATE VIEW readings_with_capacity AS
SELECT r.id, r.source_id, r.demand_kw, NULL AS rated_capacity_kw
FROM readings r
WHERE 0;  -- placeholder: returns no rows until you replace this
