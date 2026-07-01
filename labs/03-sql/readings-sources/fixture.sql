CREATE TABLE sources (
    id TEXT PRIMARY KEY,
    rated_capacity_kw NUMERIC NOT NULL
);

CREATE TABLE readings (
    id INTEGER PRIMARY KEY,
    source_id TEXT,
    timestamp TEXT NOT NULL,
    demand_kw NUMERIC NOT NULL,
    solar_output_kw NUMERIC NOT NULL
);

INSERT INTO sources (id, rated_capacity_kw) VALUES
    ('substation-12', 5200),
    ('substation-7', 4000);

-- reading id 9 has no matching source on purpose -- this lab is about
-- what a LEFT JOIN does with exactly that situation.
INSERT INTO readings (id, source_id, timestamp, demand_kw, solar_output_kw) VALUES
    (1, 'substation-12', '2026-07-01T00:00:00', 4200, 0),
    (2, 'substation-12', '2026-07-01T01:00:00', 4100, 0),
    (3, 'substation-12', '2026-07-01T02:00:00', 4050, 0),
    (4, 'substation-12', '2026-07-01T12:00:00', 5300, 800),
    (5, 'substation-12', '2026-07-01T13:00:00', 5400, 850),
    (6, 'substation-7', '2026-07-01T00:00:00', 3800, 0),
    (7, 'substation-7', '2026-07-01T12:00:00', 4600, 600),
    (8, 'substation-7', '2026-07-01T13:00:00', 4700, 650),
    (9, 'substation-99', '2026-07-01T00:00:00', 3000, 0),
    (10, 'substation-12', '2026-07-01T14:00:00', 4900, 700);
