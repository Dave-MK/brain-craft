SELECT 'readings_with_capacity should include all 10 readings (LEFT JOIN, not INNER JOIN)' AS failure_reason
WHERE (SELECT COUNT(*) FROM readings_with_capacity) != 10

UNION ALL
SELECT 'the substation-99 reading (id 9) should have a NULL rated_capacity_kw since it has no matching source'
WHERE (SELECT rated_capacity_kw FROM readings_with_capacity WHERE id = 9) IS NOT NULL

UNION ALL
SELECT 'a substation-12 reading (id 1) should show rated_capacity_kw = 5200'
WHERE (SELECT rated_capacity_kw FROM readings_with_capacity WHERE id = 1) != 5200;
