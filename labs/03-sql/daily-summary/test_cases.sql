SELECT 'high_avg_demand_sources should return exactly 1 row (only substation-12 averages above 4500)' AS failure_reason
WHERE (SELECT COUNT(*) FROM high_avg_demand_sources) != 1

UNION ALL
SELECT 'the one row should be substation-12'
WHERE (SELECT source_id FROM high_avg_demand_sources) != 'substation-12'

UNION ALL
SELECT 'peak_demand for substation-12 should be 5400'
WHERE (SELECT peak_demand FROM high_avg_demand_sources) != 5400

UNION ALL
SELECT 'avg_demand for substation-12 should be approximately 4658.33 (sum of its 6 readings / 6)'
WHERE ABS((SELECT avg_demand FROM high_avg_demand_sources) - 4658.33) > 0.5;
