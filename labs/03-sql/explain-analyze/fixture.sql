CREATE TABLE readings (
    id INTEGER PRIMARY KEY,
    source_id TEXT NOT NULL,
    timestamp TEXT NOT NULL,
    demand_kw NUMERIC NOT NULL
);

WITH RECURSIVE seq(n) AS (
    SELECT 1
    UNION ALL
    SELECT n + 1 FROM seq WHERE n < 500
)
INSERT INTO readings (source_id, timestamp, demand_kw)
SELECT
    'substation-' || (1 + (n % 20)),
    '2026-07-01T00:00:00',
    4000 + (n % 1500)
FROM seq;
