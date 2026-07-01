# Backend Architecture

## Stack (current default — see [`CLAUDE.md`](../../CLAUDE.md))

NestJS, PostgreSQL, Prisma, Supabase Auth, Redis, BullMQ. Python side (labs, ML/RL, simulators): FastAPI, PyTorch, scikit-learn, NumPy, pandas, run in sandboxed Docker containers.

## Why a separate Python service

The curriculum's own subject matter (ML, RL, simulation) needs a real Python execution environment for labs — this cannot be faked in Node. Rather than embedding Python execution inside the main NestJS API, a dedicated FastAPI service handles sandboxed code execution and any Python-native ML/simulation work, called from the main API.

## Core services (sketch — not yet built, Phase 0)

- **API service (NestJS)** — auth, lesson/content serving, progress tracking, knowledge graph reads/writes.
- **Sandbox/execution service (FastAPI + Docker)** — runs learner-submitted Python/labs in isolation; never on the host directly.
- **Content engine worker (BullMQ)** — living-curriculum staleness detection and regeneration jobs (see [`docs/09-content-engine/overview.md`](../09-content-engine/overview.md)).
- **AI Tutor/Architect service** — RAG + model routing over learner state and curriculum content (see [`docs/03-ai-tutor/overview.md`](../03-ai-tutor/overview.md), [`docs/04-adaptive-learning/overview.md`](../04-adaptive-learning/overview.md)).

## Security posture for code execution

Learner-submitted code must never execute with access to secrets, the network by default, or the host filesystem. Docker sandboxing with strict resource/time limits is non-negotiable — see [`docs/16-security/overview.md`](../16-security/overview.md).

## Open questions

- Exact sandbox runtime (Docker-per-execution vs. a pooled sandbox runner like gVisor/Firecracker) — Docker-per-execution is the simple starting point; revisit under load.
- Whether Supabase is used purely for auth or also as the primary Postgres host (see [`docs/12-database/overview.md`](../12-database/overview.md)).
