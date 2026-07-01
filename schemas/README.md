# Schemas

JSON/YAML schemas that make the curriculum machine-readable rather than freehand prose — the mechanism that lets `lessons/`, `labs/`, and the knowledge graph stay structured, validated, and regenerable (see [`docs/09-content-engine/overview.md`](../docs/09-content-engine/overview.md)).

## Planned schemas

- `lesson.schema.json` — the core lesson object (concept, difficulty, dependencies, learningObjectives, labs, simulations, flashcards, assessment, references) described in [`docs/09-content-engine/overview.md`](../docs/09-content-engine/overview.md).
- `concept-node.schema.json` — knowledge graph node/edge structure (see [`docs/08-knowledge-graph/overview.md`](../docs/08-knowledge-graph/overview.md)).
- `assessment.schema.json` — rubric structure for non-multiple-choice assessment types (see [`docs/05-assessments/overview.md`](../docs/05-assessments/overview.md)).
- `flashcard.schema.json` — FSRS-compatible spaced-repetition card structure.

## Enforcement

Per [`CLAUDE.md`](../CLAUDE.md): no lesson ships without validating against `lesson.schema.json`. This should become a CI check (see [`docs/18-testing/overview.md`](../docs/18-testing/overview.md)) once schemas and content both exist.

## Status

`lesson.schema.json` is written (draft 2020-12). It enforces, at the schema level, the pedagogical non-negotiables from [`CLAUDE.md`](../CLAUDE.md) and [`docs/01-learning-science/overview.md`](../docs/01-learning-science/overview.md): every lesson must declare `whyItMatters` and `capstoneContribution` explicitly, ship at least one flashcard, ship at least one dated reference, and use a non-multiple-choice primary assessment type.

Remaining: `concept-node.schema.json`, `assessment.schema.json` (currently inlined into `lesson.schema.json` as `$defs/assessment` — may be extracted once the knowledge graph and assessment engine need to reference it independently), `flashcard.schema.json` (same — currently inlined as `$defs/flashcard`).
