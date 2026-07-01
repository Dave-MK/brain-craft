# Labs

Interactive coding sandboxes, one per lesson/concept where a hands-on lab is applicable (not every concept needs one — see [`docs/00-foundations/DESIGN_PRINCIPLES.md`](../docs/00-foundations/DESIGN_PRINCIPLES.md) on avoiding manufactured interactivity).

## What belongs here

- Starter code + task description for a given lab
- Expected test cases the sandboxed execution service (see [`docs/11-backend/overview.md`](../docs/11-backend/overview.md)) runs against learner submissions
- Debugging-challenge variants (intentionally broken code, tied to [`docs/05-assessments/overview.md`](../docs/05-assessments/overview.md))

## Constraints

Every lab must connect to the AI Energy OS mission — no generic, disconnected exercises (see [`CLAUDE.md`](../CLAUDE.md) content standards). A Python loop lab uses weather/demand data, not `range(10)`.

## Status

All 11 Mission 1 labs are written and verified: 9 pure-Python labs (`01-python/`, each with `starter.py` + `test_cases.py`, run via `python -m unittest test_cases`) and 6 Git labs (`02-git/`, each with a `starter/` folder containing a `digital_twin/` package + `setup_repo.py` to seed a reproducible starting repo state, plus a sibling `test_cases.py` that inspects real git state via `subprocess` — commit messages, branch ancestry, fast-forward vs. merge commit, conflict-marker absence).

Every lab was validated against a real reference solution (not just read for plausibility) and confirmed to fail cleanly, not crash, before the solution is written. The Git labs were specifically checked to reject the "shortcut" they're designed to catch — e.g. `clean-history`'s tests correctly fail a plain merge that skips the rebase step.

Convention for future labs: Python labs get `starter.py` + `test_cases.py` importing from it via `unittest`; Git labs get a `starter/` directory (never containing a committed `.git` — that's for the learner to create) plus a `setup_repo.py` that seeds a reproducible starting state, and a `test_cases.py` that locates the repo via `./starter` or the current directory and asserts on real git plumbing output, not on any assumed learner-chosen naming beyond what the lesson's own guided example specifies.

All 6 `03-sql` labs are also written and verified, using SQLite (stdlib, no install needed) as the lab-execution engine — a deliberate, explicitly-noted simplification distinct from whatever database Phase 1 eventually chooses for the real app (see [`docs/12-database/overview.md`](../docs/12-database/overview.md)). Two new patterns for SQL labs, run via [`scripts/run_sql_lab.py`](../scripts/run_sql_lab.py):

- **Pure-`SELECT` exercises** (`basic-queries`, `readings-sources`, `daily-summary`, `rolling-average`): the learner's answer is a `CREATE VIEW`, not a bare `SELECT` — this is what makes a read-only query automatically checkable, since the runner can query the resulting view afterward.
- **Schema-shape exercises** (`weather-price-tables`): checked structurally via SQLite's `pragma_table_info`/`pragma_foreign_key_list` table-valued functions (columns, `NOT NULL`, `PRIMARY KEY`, `FOREIGN KEY`) rather than behaviorally, since testing "does an invalid insert get rejected" needs statements a single `SELECT`-based runner can't express.
- **`explain-analyze`** is the one exception with its own `test_cases.py`: SQLite's `EXPLAIN QUERY PLAN` (used here in place of Postgres's `EXPLAIN ANALYZE` — noted explicitly in the lab, no real execution timing) can't be queried from inside a plain `SELECT`, so it needs a real script comparing the query plan before and after the learner's `CREATE INDEX`.

Two real bugs were caught and fixed during verification, not just assumed away: an arithmetic error in an expected test value (recomputed by hand, wrong the first time), and a substring check in `explain-analyze/test_cases.py` that was fooled by a commented-out `CREATE INDEX` line — fixed by relying purely on the actual before/after query-plan comparison instead of source-text inspection.

All 6 `04-apis` labs are also written and verified, using a new [`scripts/mock_http_server.py`](../scripts/mock_http_server.py) helper: a real `http.server` on `127.0.0.1` with an ephemeral port, so learner code makes genuine HTTP requests (real sockets, real status codes, real JSON bodies) without ever touching the real internet, per the sandboxing rule in [`docs/16-security/overview.md`](../docs/16-security/overview.md). Each lab's mock server response function is injected per-test (success, 401/403, 429/500-then-recovers, paginated, toggle-to-failing), letting the same tiny server double as every failure mode the corresponding lesson teaches.

Two things worth flagging from verification, not just assumed:
- The `backoff` lab's exponential-backoff test actually sleeps real (tiny, test-scaled) delays and still completes in ~2s — confirming the lesson's `base_delay_seconds` parameterization is what keeps automated grading fast, not a mocked `time.sleep`.
- The `full-backfill` (pagination) lab includes a deliberate safety valve: after 20 requests the mock server force-terminates the page sequence, so a genuinely buggy infinite-loop learner solution fails the test in ~1s instead of hanging the grader forever. Verified directly against a deliberately broken solution that never reads `next_page_token`.

All 6 `05-pandas` labs are also written and verified — the most conventional of the three Mission 2 lab types (pure `unittest` against real `pandas.DataFrame` objects, no external service, no mocking). **Mission 2 is now fully lab-covered: 18/18 lessons across `03-sql`, `04-apis`, and `05-pandas`.**

One real test bug caught during verification: `mask-groupby`'s "excludes other sources" test originally asserted an impossible result (expected a reading below its own filter threshold to pass it) — fixed by choosing a threshold that actually isolates the source-filter behavior being tested, not the demand-threshold behavior already covered elsewhere.

All 6 `06-scikit-learn` labs are also written and verified (scikit-learn installed as a real dependency). The key design move for ML labs: choose fixtures where the "correct" answer is deterministic even though the tool is statistical —

- **Regression/classification labs** use perfectly linear or perfectly separable synthetic data, so `LinearRegression`/`LogisticRegression`'s closed-form/convex fits are exact and testable with tight tolerances, not loose ones.
- **`walk-forward`** tests the actual defining property of `TimeSeriesSplit` structurally (every fold's train indices precede its test indices; the training set grows across folds) rather than trying to infer it from a score. I verified this two ways: a correct `TimeSeriesSplit` solution passes, and a deliberately swapped-in `KFold(shuffle=True)` solution — the exact bug the lesson's debugging exercise targets — fails both checks.
- **`final-model`** compares candidates against a `DummyRegressor(strategy="mean")` baseline (a real, honest floor) rather than a hand-rolled naive predictor, on data with a strong trend, so "a real model should beat a dummy" is a safe, non-flaky assertion.

Remaining: Missions 4–6 and 8 (30 lessons: `07-pytorch`, `08-reinforcement-learning`, `09-graph-algorithms`, `10-power-systems`, `11-capstone-ai-energy-os`). PyTorch labs will need genuinely tolerance-based assertions ("loss decreased over training," not exact values) since neural network training has real stochasticity even with fixed seeds across some operations.
