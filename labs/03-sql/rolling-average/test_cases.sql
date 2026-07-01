SELECT 'demand_with_rolling_avg should include all 9 readings, not collapse them like GROUP BY would' AS failure_reason
WHERE (SELECT COUNT(*) FROM demand_with_rolling_avg) != 9

UNION ALL
SELECT 'the first substation-12 reading (id 1, no prior rows) should have rolling_avg_3 = 4200 (itself)'
WHERE ABS((SELECT rolling_avg_3 FROM demand_with_rolling_avg WHERE id = 1) - 4200.0) > 0.01

UNION ALL
SELECT 'the 6th substation-12 reading (id 10) should have rolling_avg_3 = 5200 (avg of ids 4, 5, 10: 5300+5400+4900)/3'
WHERE ABS((SELECT rolling_avg_3 FROM demand_with_rolling_avg WHERE id = 10) - 5200.0) > 0.01

UNION ALL
SELECT 'substation-7''s rolling average must not include substation-12''s readings (partitions must not leak into each other)'
WHERE ABS((SELECT rolling_avg_3 FROM demand_with_rolling_avg WHERE id = 6) - 3800.0) > 0.01;
