# Gamification

## What's explicitly rejected

Meaningless XP, levels, streak-for-streak's-sake mechanics, and any progress indicator that doesn't correspond to actual capability. See [`docs/00-foundations/SUCCESS_METRICS.md`](../00-foundations/SUCCESS_METRICS.md) for why these are treated as defects when optimized for.

## What's used instead

Progress is represented across dimensions that actually mean something:

- **Mastery** — per knowledge-graph-node fill bar (e.g. "SQL JOINS ██░░░░░░░░"), not an aggregate level number.
- **Confidence** — self-reported vs. measured, surfaced so gaps are visible rather than hidden.
- **Retention** — FSRS-derived retrievability per concept, visible over time (does old material actually stay retained?).
- **Research** — evidence of papers read, hypotheses formed, experiments run.
- **Engineering** — real commits, real working labs, real bugs fixed.
- **Contribution** — growth of the AI Energy OS capstone itself, the most legible form of progress.
- **Portfolio / Knowledge Network** — a visual, explorable map of everything mastered, structured as the knowledge graph itself rather than a list.

## Design intent

Every one of these should be something the learner could show someone else and have it mean something — "here's my knowledge graph, here's what I've built" — rather than a number that only means something inside the platform.

## Open questions

- Exact visual treatment of the mastery/knowledge-graph view (ties to [`docs/14-design-system/overview.md`](../14-design-system/overview.md) and React Flow usage in [`docs/10-frontend/overview.md`](../10-frontend/overview.md)).
- Whether any lightweight streak/consistency signal is worth keeping purely as *information* (not an optimization target) given spaced repetition benefits from regularity.
