# API

Formal API contracts (OpenAPI/tRPC-style definitions) are deferred until [`docs/11-backend/overview.md`](../11-backend/overview.md) and [`docs/12-database/overview.md`](../12-database/overview.md) settle their open questions — writing a contract before the service boundaries are decided risks locking in the wrong shape.

## Anticipated surface areas

- **Content API** — serve curriculum/lesson structured data to the frontend lesson runner.
- **Progress API** — read/write knowledge graph state, spaced-repetition schedules.
- **Tutor API** — session-based interaction with the AI Tutor/Architect, likely streaming.
- **Execution API** — submit code to the sandboxed Python execution service, receive results.
- **Assessment API** — submit assessment work, receive rubric-based evaluation.

## Principles

- Auth on every endpoint via Supabase Auth-issued tokens; no anonymous write access.
- Tutor/execution endpoints are rate- and resource-limited by design (see [`docs/16-security/overview.md`](../16-security/overview.md), [`docs/17-performance/overview.md`](../17-performance/overview.md)).

## Open questions

- REST vs. tRPC vs. GraphQL — leaning tRPC given a TypeScript-first NestJS + Next.js stack, but not decided.
