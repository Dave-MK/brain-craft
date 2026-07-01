# Database

## Stack (current default)

PostgreSQL via Prisma, Supabase Auth for identity. Redis for caching/queues (BullMQ).

## Core domains to model (sketch — formal schema TBD once Phase 0 docs settle)

- **Learner** — profile, goals, preferences.
- **Knowledge graph state** — per-learner mastery/confidence/retention per concept node (see [`docs/08-knowledge-graph/overview.md`](../08-knowledge-graph/overview.md)); the graph *structure* itself (nodes/edges) is largely static reference data, while per-learner state is the high-write table.
- **Curriculum content** — versioned lesson/skill-folder structured data (see [`docs/09-content-engine/overview.md`](../09-content-engine/overview.md)), including the `references` used for staleness detection.
- **Sessions/interactions** — AI Tutor session logs, mistake history, timing data.
- **Assessments** — submissions, rubric evaluations, mastery outcomes (see [`docs/05-assessments/overview.md`](../05-assessments/overview.md)).
- **Spaced repetition state** — FSRS parameters and review schedule per concept per learner.
- **Capstone artifacts** — links/metadata for the growing AI Energy OS build (code, simulation results).

## Why Postgres, not something more exotic for the graph

A relational store with an adjacency/edge table is sufficient at single-learner scale and keeps the stack simple (see [`docs/00-foundations/PHILOSOPHY.md`](../00-foundations/PHILOSOPHY.md) — simplicity over cleverness). A dedicated graph database is not justified until/unless the knowledge graph needs to scale to many learners with complex graph queries Postgres can't express efficiently.

## Open questions

- Whether curriculum content versioning lives in Postgres directly or as versioned files in this repo with Postgres only storing the "currently active version" pointer per lesson (leaning toward the latter, to keep curriculum content reviewable via git).
