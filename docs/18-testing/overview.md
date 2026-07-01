# Testing

## Two distinct things need testing

1. **Application code** — standard unit/integration/e2e testing once `apps/`/`packages/` exist (Phase 1+). TypeScript strict + typed Python are the first line of defense; test suites verify behavior, not just types.
2. **Curriculum content correctness** — a different concern: lesson schema validation (every lesson conforms to `schemas/lesson.schema.json`), reference freshness checks (living curriculum, see [`docs/09-content-engine/overview.md`](../09-content-engine/overview.md)), and pedagogical completeness checks (every lesson has flashcards, a reflection prompt, a teach-back step — see [`docs/01-learning-science/overview.md`](../01-learning-science/overview.md)).

## Principle

A lesson that "renders" but is missing a required pedagogical field (per [`docs/01-learning-science/overview.md`](../01-learning-science/overview.md)) is a test failure, not a style nitpick — content quality is enforced the same way code correctness is.

## Open questions

- Whether content-schema validation runs as a CI check against `curriculum/` on every commit (yes, by default) once the schema exists.
