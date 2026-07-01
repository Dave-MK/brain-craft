# Roadmap

## Phase 0 — Foundations (current)

Documentation, curriculum skeleton, and content schemas. No application code. Deliverables:
- [x] `docs/00-foundations/` (mission, vision, philosophy, design principles, success metrics, glossary)
- [x] `docs/01-20` topic overviews + `research/`
- [x] `curriculum/` skill-folder skeleton with per-skill README
- [x] `CLAUDE.md`, top-level `README.md`
- [ ] `schemas/lesson.schema.json` and related content schemas
- [ ] Knowledge graph node/edge data for at least Mission 1-2 (Python, Git, SQL, APIs)
- [ ] First real authored lessons for `01-python`, validated against the schema

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
