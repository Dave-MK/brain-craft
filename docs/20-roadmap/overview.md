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
- [ ] Begin Mission 6 ("Understand Energy"): `10-power-systems` lessons

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
