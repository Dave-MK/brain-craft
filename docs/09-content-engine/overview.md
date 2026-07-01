# Content Engine & Living Curriculum

## The core problem this solves

Traditional curricula freeze the moment they're written. Libraries release breaking changes, APIs get deprecated, new research supersedes old approaches — and the course quietly becomes wrong while looking unchanged. BrainCraft's content is designed to never go stale.

## How

Lessons are **structured data, not prose-first markdown**. A lesson is authored/generated as an object conforming to a schema (see [`schemas/`](../../schemas/)), roughly:

```json
{
  "concept": "...",
  "difficulty": "...",
  "dependencies": [],
  "learningObjectives": [],
  "labs": [],
  "simulations": [],
  "flashcards": [],
  "assessment": {},
  "references": []
}
```

The `references` field is the load-bearing piece: every factual/technical claim in a lesson points to a specific, versioned source (official docs, a library version, a paper). Prose (the actual markdown/UI shown to the learner) is rendered *from* this structured data, not authored independently of it.

## The update pipeline

```
Official docs → GitHub releases → Research papers → Breaking API changes → Framework updates
       ↓
Curriculum regeneration (diff detection against tracked references)
       ↓
Lessons updated → Tests updated → Projects updated → Knowledge graph updated
```

Concretely: a background job (BullMQ, see [`docs/11-backend/overview.md`](../11-backend/overview.md)) periodically checks tracked references for changes. When a reference changes (a library ships a breaking release, a paper is superseded), affected lessons are flagged for regeneration, and regeneration re-runs the content-authoring process against the new reference before the change reaches the learner.

## Constraints

- Regeneration must never silently rewrite a lesson a learner is mid-progress on in a way that invalidates their current state in the knowledge graph — changes are versioned, and in-progress learners either finish the version they started or are explicitly told what changed.
- No lesson content ships without its `references` field populated and dated.

## Open questions

- Exact staleness-detection strategy per reference type (RSS/changelog polling vs. periodic re-fetch vs. webhook where available).
- How much of the regeneration step is automated (LLM-authored draft) vs. requires the learner/maintainer to approve before it goes live.
