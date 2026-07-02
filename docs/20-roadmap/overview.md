# Roadmap

## Phase 0 — Foundations (current)

Documentation, curriculum skeleton, and content schemas. No application code. Deliverables:
- [x] `docs/00-foundations/` (mission, vision, philosophy, design principles, success metrics, glossary)
- [x] `docs/01-20` topic overviews + `research/`
- [x] `curriculum/` skill-folder skeleton with per-skill README
- [x] `CLAUDE.md`, top-level `README.md`
- [x] `schemas/lesson.schema.json`
- [ ] `schemas/concept-node.schema.json` for knowledge graph data
- [ ] Knowledge graph node/edge data for at least Mission 1-2 (Python, Git, SQL, APIs)
- [x] All 11 `01-python` lessons authored end to end and validated against `schemas/lesson.schema.json` via `jsonschema` (Draft 2020-12): Variables → Control Flow → Lists → Loops → Functions → Dictionaries → Sets → Error Handling → Files & I/O → Modules & Packages → Basic OOP (boss battle). Full dependency graph checked programmatically for missing edges and cycles — none found. `01-python` is the first fully complete skill folder.
- [x] All 6 `02-git` lessons authored end to end and validated: Init & Commits → Branches → Merging → {Resolving Conflicts, Remote Collaboration} → Rebasing (boss battle). Combined 17-lesson graph across `01-python` + `02-git` re-checked for missing edges/cycles — clean. **Mission 1 ("Learn Programming") is fully authored.**
- [ ] `schemas/concept-node.schema.json` and a real knowledge-graph data file capturing the node/edge structure these 17 lessons already imply
- [x] All 6 `03-sql` lessons authored end to end and validated: SELECT & WHERE → JOIN → Aggregation → Schema Design → Window Functions → Indexing & Performance (boss battle). Combined 23-lesson graph across `01-python` + `02-git` + `03-sql` re-checked — clean.
- [x] All 6 `04-apis` lessons authored end to end and validated: HTTP Fundamentals → Authentication → Consuming REST/JSON → {Rate Limits & Retries, Pagination} → Resilient Ingestion Client (boss battle). Combined 29-lesson graph re-checked — clean.
- [x] All 6 `05-pandas` lessons authored end to end and validated: DataFrames Basics → Filtering & GroupBy → Time Series → Merging Datasets → Data Cleaning → The Feature Table (boss battle). **Mission 2 ("Manipulate Data") is fully authored.** Combined 35-lesson graph across all of Mission 1 + Mission 2 re-checked — clean.
- [x] All 6 `06-scikit-learn` lessons authored end to end and validated: Regression Basics → Baselines & Leakage → {Time-Series CV, Classification Basics} → Evaluation & Feature Importance → The Demand Forecaster (boss battle). Combined 41-lesson graph re-checked — clean.
- [x] All 6 `07-pytorch` lessons authored end to end and validated: Tensors & Autograd → Building Networks → Training Loop → Overfitting & Regularization → Sequence Models → The Neural Forecaster (boss battle). **Mission 4 ("Teach Machines") is fully authored.** Combined 47-lesson graph re-checked — clean.
- [x] All 6 `08-reinforcement-learning` lessons authored end to end and validated: MDP Fundamentals → Reward Design → {Value-Based Methods, Policy Gradient Methods} → Training/Evaluation/Safety → The Battery Scheduler (boss battle). Combined 53-lesson graph re-checked — clean.
- [x] All 6 `09-graph-algorithms` lessons authored end to end and validated: Representation & Traversal → Shortest Path → {Flow Algorithms, Resilience & Critical Nodes} → RL + Graphs Combination → The Grid Router (boss battle). **Mission 5 ("Optimise Decisions") is fully authored** — both of its skill folders converge as designed. Combined 59-lesson graph re-checked — clean.
- [x] All 6 `10-power-systems` lessons authored end to end and validated: Generation/Transmission/Distribution → Load Balancing → {Renewable Intermittency, Grid Stability & Cascading Failures} → Energy Markets & Pricing → Digital Twin Fidelity (boss battle). **Mission 6 ("Understand Energy") is fully authored.** Combined 65-lesson graph re-checked — clean.
- [x] All 6 `11-capstone-ai-energy-os` lessons authored end to end and validated: System Integration → {Carbon Optimisation, Explainability Layer} → {Dashboard, Research Workspace} → The AI Energy OS (final boss battle). **The entire 71-lesson curriculum across all 11 skill folders and 7 missions is now fully authored**, with zero missing dependency edges and zero cycles verified after every addition throughout this build.

## Phase 0/1 curriculum-authoring milestone: complete

Every skill folder from `01-python` through `11-capstone-ai-energy-os` now has real, schema-validated lesson content — not skeletons. What remains before this becomes a usable product (not more curriculum content):

- [x] `schemas/concept-node.schema.json` written; `scripts/generate_knowledge_graph.py` derives `docs/08-knowledge-graph/knowledge-graph.json` from all 71 lessons (71 nodes, 81 edges, zero missing edges, zero cycles) — the knowledge graph is now a real, generated, re-checkable artifact, not just an implication of scattered `dependencies` fields
- [ ] Phase 1 architecture decisions in `docs/10-frontend/`, `docs/11-backend/`, `docs/12-database/` — still open per `CLAUDE.md`'s "no `apps/`/`packages/` code until these are resolved and the roadmap calls for it"
- [ ] `apps/web` lesson runner that can actually render this content through the 14-step lesson flow
- [ ] The AI Tutor (`docs/03-ai-tutor/`) and Architect (`docs/04-adaptive-learning/`) — currently pure specification, no implementation
- [x] All 11 Mission 1 lab `starter.*`/`test_cases.*` files written and verified against real reference solutions (9 Python labs + 6 Git labs with reproducible `setup_repo.py` seeding).
- [x] All 6 `03-sql` labs written and verified using SQLite via a new [`scripts/run_sql_lab.py`](../../scripts/run_sql_lab.py) runner (view-based pattern for pure-SELECT exercises, `pragma_table_info`/`pragma_foreign_key_list` for schema-shape checks, a dedicated `test_cases.py` for the one lab needing real `EXPLAIN QUERY PLAN` inspection).
- [x] All 6 `04-apis` labs written and verified using a new [`scripts/mock_http_server.py`](../../scripts/mock_http_server.py) helper (a real local `http.server`, never real internet). Verified the backoff lab's real (test-scaled) exponential sleeps stay fast, and the pagination lab's 20-request safety valve actually stops a deliberately broken infinite-loop solution rather than hanging.
- [x] All 6 `05-pandas` labs written and verified with plain `unittest` against real `pandas` DataFrames. **Mission 2 is fully lab-covered (18/18 lessons).**
- [x] All 6 `06-scikit-learn` labs written and verified with scikit-learn installed as a real dependency, using deterministic synthetic fixtures (perfectly linear/separable data) so ML labs stay exactly-checkable rather than flaky. `walk-forward`'s TimeSeriesSplit-vs-KFold distinction was verified both ways (correct solution passes, swapped-in KFold fails).
- [x] All 6 `07-pytorch` labs written and verified with CPU-only PyTorch installed. **Mission 4 is fully lab-covered.** Established the stochastic-training test patterns (relational loss assertions, mathematical linearity detection for missing activations, empirically calibrated thresholds, recording-stub fairness checks). Three planted-bug scenarios verified to fail correctly: no-activation network, missing `zero_grad()`, missing `model.eval()`.
- [x] All 6 `08-reinforcement-learning` labs written and verified. Key artifact: a deterministic battery environment with a provably unique optimal policy ([`labs/08-reinforcement-learning/q-learning-battery/battery_env.py`](../../labs/08-reinforcement-learning/q-learning-battery/battery_env.py)) — the first design converged to a local optimum at default hyperparameters (caught by dumping the trained Q-table), redesigned and verified to reach the exact optimum across 5 seeds.
- [x] All 6 `09-graph-algorithms` labs written and verified with `networkx` installed. **Mission 5 is fully lab-covered.** Exact hand-computed fixtures throughout (fewest-hops-vs-minimum-loss Dijkstra fixture, the diamond two-node contingency topology, a direct max-flow-min-cut theorem assertion); planted k=1 and missing-contingency-check bugs verified to fail.
- [x] All 6 `10-power-systems` labs written and verified — pure physics/economics with hand-computed values; tests assert the physical relationships themselves (double voltage → quarter loss); planted peak-denominator, averaged-bids, and disconnected-toggle bugs verified to fail.
- [x] All 6 `11-capstone-ai-energy-os` labs written and verified — integration harnesses with recording stubs; the kW/MW mismatch, confounded experiment, and contaminated baseline all detected and refused. **LAB COVERAGE IS COMPLETE: all 71 lessons across all 11 skill folders have verified starter code and test suites.** See [`labs/README.md`](../../labs/README.md) for the full pattern catalog.
- [ ] `simulations/*` — every lesson references a named simulation, but none have been built
- [ ] License decision (still explicitly deferred per the user's earlier choice)

## Phase 1 — Seed content + minimal runner

- Build the minimal Next.js lesson runner that can render a schema-conformant lesson through the full lesson flow.
- Author real Mission 1 content (Python, Git) end to end, including labs and flashcards.
- Stand up Postgres/Prisma schema for learner progress and knowledge graph state.

## Phase 2 — AI Tutor v1

- Basic Socratic AI Tutor scoped to Mission 1-2 content, backed by RAG over lesson content + learner history.
- Spaced repetition (FSRS) review loop live for flashcards.

## Phase 3 — Data + ML missions

- SQL, APIs, pandas, scikit-learn missions authored; digital twin seed data/environment stood up.
- Sandbox execution service live for Python labs.

## Phase 4 — Deep learning + RL missions

- PyTorch and reinforcement learning missions; digital twin gains a real optimisation target (battery/EV scheduling).

## Phase 5 — Adaptive learning + Living Curriculum

- The Architect goes live (cross-mission resequencing).
- Content engine's staleness-detection and regeneration pipeline goes live.

## Phase 6 — Graph algorithms + power systems + capstone integration

- Grid routing, power systems fidelity, and full AI Energy OS integration.

## Not scheduled / explicitly deferred

- Multi-learner/opening the platform to others — a possible future direction (see closing notes in project origin conversation) but out of scope until the single-learner system is proven end to end.
- Three.js-based visualisation — deferred until a concrete need (e.g. 3D grid topology) justifies the added complexity.
