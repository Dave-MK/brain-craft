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

All 6 `07-pytorch` labs are also written and verified (CPU-only PyTorch installed — `pip install torch --index-url https://download.pytorch.org/whl/cpu` — much smaller than the CUDA build and sufficient for every lab). **Mission 4 is fully lab-covered.** The stochastic-training testing patterns established here:

- **Exact where math allows it**: autograd gradients of known expressions (`manual-gradient-descent`) are pure calculus, checked to 4 decimal places; convergence targets on convex problems are checked to 2 places.
- **Structural/mathematical property checks instead of score-sniffing**: `architecture-definition` detects a missing ReLU by testing actual linearity (`f(a)+f(b) == f(a+b)+f(0)` holds only for a purely linear network) — verified to catch the no-activation bug directly. Gradient-flow-to-every-parameter catches layers defined but not wired into `forward()`.
- **Relational assertions for training**: "final loss < 5% of initial loss," "prediction within delta of the known answer" — never exact loss values. `loss-curve`'s missing-`zero_grad` detection was verified against a deliberately broken loop.
- **Empirically calibrated thresholds**: `loss-curves`' eval-mode check originally used a guessed 0.05 threshold that a *correct* solution failed (scored 0.069); measuring both correct (~0.07) and broken (~0.8, dropout active at validation) runs gave a 0.3 threshold with wide margins both ways — the threshold is documented in the test with its measurement basis.
- **Harness-under-test via recording stubs**: `honest-comparison` (boss battle) tests the fairness harness itself — stub candidates record exactly what train/test data they received, so "every candidate saw the identical chronological split" is asserted directly rather than inferred.

One wrong test assumption caught and fixed during verification: `nn.LSTM` legitimately accepts 2-D `(seq_len, features)` input as an unbatched sequence, so my original "rejects missing batch dimension" test asserted behavior PyTorch doesn't have — replaced with the feature-count mismatch check PyTorch actually enforces.

All 6 `08-reinforcement-learning` labs are also written and verified. The central design problem — RL training is stochastic and convergence isn't guaranteed — was solved two ways:

- **A deterministic environment with a provably unique optimum** ([`q-learning-battery/battery_env.py`](08-reinforcement-learning/q-learning-battery/battery_env.py)): all randomness comes from a seeded exploration RNG, so training is bit-reproducible and tests can assert the *exact* learned policy. This was hard-won: the first env design (4-phase price cycle, capacity 2) let Q-learning reliably converge to a locally-stable one-unit strategy (profit 12) instead of the true optimum (24) at the lab's default hyperparameters — discovered by dumping the trained Q-table, not by assumption. The redesigned 2-phase/capacity-1 env has a wide value gap around a unique optimum; verified to reach exactly 24.0 across 5 different seeds. The design note is documented in the env file itself.
- **Pure-function decomposition everywhere else**: reward computation, safety wrapping, and explanation building are deterministic functions with hand-computable expected values, so the RL *concepts* (reward hacking closure, post-action-state safety checks, checkable explanations) get exact tests without training anything.

Planted-bug scenarios verified to fail correctly: stale-state reward computation (`battery-mdp-definition`), unweighted policy-gradient loss (`continuous-battery` — zero rewards must give zero loss), and the stale-state safety check (`safety-harness` — discharge at soc 0.15 with floor 0.1 must be blocked because the *resulting* 0.05 violates the floor, even though the current soc doesn't).

All 6 `09-graph-algorithms` labs are also written and verified (`networkx` installed). **Mission 5 is fully lab-covered.** Graph labs are fully deterministic, so tests use exact hand-computed fixtures throughout:

- **`dijkstra-routing`'s fixture is built so fewest-hops ≠ minimum-loss** (a 2-hop path costing 10 vs. a 3-hop path costing 3) — the defining distinction of the lesson, asserted directly.
- **`contingency-analysis` uses a diamond topology** where two individually non-critical nodes disconnect the grid together — the mission's founding "two substations fail" scenario as an exact test case.
- **`max-flow-capacity` asserts the max-flow min-cut theorem directly** on the learner's own two answers (cut capacity must equal max flow).
- **Planted bugs verified to fail**: the k=1 candidate generator (policy left with nothing to choose), and `final-system`'s missing contingency check (recommending the raw cheapest route that dies in the stated scenario).
- One deliberate test-design call: `grid-connectivity`'s visited-check test fails the *genuinely wrong* variant (duplicate visits in the output) but passes the wasteful-but-functionally-correct `continue`-on-pop style — tests punish wrong results, not style choices.

All 6 `10-power-systems` labs are also written and verified — pure physics/economics functions with hand-computed expected values throughout. **Mission 6 is fully lab-covered.** Highlights:

- **`real-loss` asserts the physical relationships, not just values**: doubling voltage quarters the loss, doubling power quadruples it — directly disproving Mission 5's flat-loss-percentage assumption inside the test itself.
- **`cascade-simulation` documents its own simplification**: equal-split rerouting (with the lesson's realism caveat quoted in the module docstring) keeps the cascade loop mechanics hand-traceable — the fragile-grid fixture cascades A→B→C in exactly the hand-computed order.
- **Planted bugs verified to fail**: peak-observed-instead-of-nameplate capacity-factor denominator, averaged-bids-instead-of-marginal pricing, and the boss battle's disconnected fidelity toggle (implemented but never wired — caught by tests that flip each flag and assert the output actually changes).

All 6 `11-capstone-ai-energy-os` labs are also written and verified — integration-harness territory, tested with recording stubs standing in for cross-mission components:

- **`unified-pipeline`'s planted bug is the lesson's exact kW/MW mismatch**: a recording-stub agent captures the state it receives, so "the agent saw 4.821 MW, not 4821" is asserted directly; verified to fail when the conversion is removed.
- **`controlled-experiment` and `final-delivery` both REFUSE bad science rather than compute it**: a confounded config (two variables changed) and a contaminated baseline (shared component with the optimised system) each return an error instead of a subtly-wrong number — the refusal itself is what's tested.
- **`final-delivery`** — the last lab of the entire curriculum — evaluates the mission's founding cost-reduction claim across multiple periods with a consistency flag, hand-checkable stub economics, and the leaked-baseline detection the boss-battle lesson is built around.

## Coverage: complete

**All 71 lessons across all 11 skill folders now have verified lab starter code and test suites.** Every lab was validated three ways where a planted bug exists (pre-implementation fails cleanly, reference solution passes, the lesson's planted bug fails the discriminating test), and two ways otherwise. Dependencies used: Python stdlib, `jsonschema`, `requests`, `pandas`, `scikit-learn`, CPU-only `torch`, `networkx`, and SQLite via stdlib — no services, no network, no GPU.
