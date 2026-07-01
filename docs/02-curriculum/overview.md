# Curriculum

## Two layers: Skills and Missions

`curriculum/` on disk is organized by **skill**, in acquisition order:

```
01-python  02-git  03-sql  04-apis  05-pandas  06-scikit-learn
07-pytorch  08-reinforcement-learning  09-graph-algorithms
10-power-systems  11-capstone-ai-energy-os
```

This is the implementation unit — lessons, labs, and assessments live under these folders. But the learner-facing narrative is organized by **Mission**, a motivational grouping that maps skills to a goal:

```
Mission 1 — Learn Programming        → 01-python, 02-git
Mission 2 — Manipulate Data          → 03-sql, 04-apis, 05-pandas
Mission 3 — Predict the Future       → 06-scikit-learn (time-series forecasting)
Mission 4 — Teach Machines           → 07-pytorch (neural networks)
Mission 5 — Optimise Decisions       → 08-reinforcement-learning, 09-graph-algorithms
Mission 6 — Understand Energy        → 10-power-systems
Mission 7 — Simulate a Grid          → digital twin (cross-cutting, built incrementally)
Mission 8 — Build the AI Energy OS   → 11-capstone-ai-energy-os
```

Do not collapse these two layers. A learner sees "Mission 3: Predict the Future"; the content underneath is authored and versioned under `curriculum/06-scikit-learn/`.

## Every skill's capstone contribution

| Skill | Contributes to AI Energy OS as |
|---|---|
| Python | Weather/data parsers, general scripting |
| Git | Version control discipline for every artifact built from here on |
| SQL | Grid/consumption data storage |
| APIs | Weather + price data ingestion |
| pandas | Consumption/generation analysis |
| scikit-learn | Demand and generation forecasting |
| PyTorch | Deep forecasting models |
| Reinforcement learning | Battery/EV scheduling optimisation |
| Graph algorithms | Grid routing and topology reasoning |
| Power systems | Digital twin fidelity |
| Capstone | Integration into the full AI Energy OS |

## Lesson generation

Curriculum content is authored as structured data (see [`docs/09-content-engine/overview.md`](../09-content-engine/overview.md)) and rendered into the [Lesson Flow](../00-foundations/PROJECT_GLOSSARY.md). No skill folder should contain hand-written one-off lesson pages that bypass the schema — that's exactly the pattern that makes courses rot.

## Sequencing rules

- A learner cannot start a skill folder until its prerequisite nodes in the knowledge graph are at mastery threshold (see [`docs/08-knowledge-graph/overview.md`](../08-knowledge-graph/overview.md)).
- The Architect may insert supplementary material between skill folders (e.g. a probability refresher between graph algorithms and reinforcement learning) without that material needing its own top-level skill folder — see [`docs/04-adaptive-learning/overview.md`](../04-adaptive-learning/overview.md).

## Open questions

- Whether "Mission 7 — Simulate a Grid" needs its own skill folder or stays purely cross-cutting/integrative.
- Exact granularity of concepts-per-lesson within each skill folder (see knowledge graph doc).
