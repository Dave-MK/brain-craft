# Performance

## Where it matters most

- **Code execution latency** — labs need fast feedback loops; sandboxed execution should return results quickly enough to not break the guided-coding → independent-coding flow.
- **AI Tutor response latency** — Socratic back-and-forth should feel conversational; model routing (cheaper/faster model for routine prompts, escalate only when needed — see [`docs/03-ai-tutor/overview.md`](../03-ai-tutor/overview.md)) is a performance decision as much as a cost one.
- **Knowledge graph queries** — the "what am I ready for next" computation must stay fast even as the graph grows across the full curriculum.
- **Content regeneration jobs** — background, not blocking any learner-facing path (BullMQ queue, see [`docs/11-backend/overview.md`](../11-backend/overview.md)).

## Open questions

- Caching strategy for lesson content (largely static, high read volume) vs. per-learner progress state (write-heavy, small).
