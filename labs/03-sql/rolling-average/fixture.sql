CREATE TABLE readings (
    id INTEGER PRIMARY KEY,
    source_id TEXT NOT NULL,
    timestamp TEXT NOT NULL,
    demand_kw NUMERIC NOT NULL
);

INSERT INTO readings (id, source_id, timestamp, demand_kw) VALUES
    (1, 'substation-12', '2026-07-01T00:00:00', 4200),
    (2, 'substation-12', '2026-07-01T01:00:00', 4100),
    (3, 'substation-12', '2026-07-01T02:00:00', 4050),
    (4, 'substation-12', '2026-07-01T12:00:00', 5300),
    (5, 'substation-12', '2026-07-01T13:00:00', 5400),
    (10, 'substation-12', '2026-07-01T14:00:00', 4900),
    (6, 'substation-7', '2026-07-01T00:00:00', 3800),
    (7, 'substation-7', '2026-07-01T12:00:00', 4600),
    (8, 'substation-7', '2026-07-01T13:00:00', 4700);
