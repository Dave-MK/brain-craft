# Knowledge Graph

## What it is

Every taught concept — from "variable" to "grid optimisation" — is a node. Edges represent prerequisite relationships. The graph, not the skill-folder ordering alone, is the true source of truth for what a learner is ready to learn next.

```
Python → Variables → Functions → Objects → DataFrames → Feature Engineering → Forecasting → Energy Demand Prediction
```

## What it must support

- Determining what the learner currently knows (mastery threshold reached).
- Determining what they *nearly* know (in progress, below threshold).
- Determining what they've forgotten (retention decayed below an FSRS-derived threshold, even if once mastered).
- Determining what they're ready for next (all prerequisite edges satisfied).
- Explaining gaps causally: "you cannot yet understand reinforcement learning because you're weak on probability" — a real inference over the graph, not a canned message.

## Data model (sketch)

Each node stores: concept identifier, skill-folder membership, prerequisite edges, mastery threshold definition, current mastery/confidence/retention state per learner, and links to the lesson(s)/lab(s)/assessment(s) that teach and test it. See [`schemas/`](../../schemas/) for the eventual formal schema, and [`docs/12-database/overview.md`](../12-database/overview.md) for storage.

## Who reads/writes it

- The **AI Tutor** reads it to calibrate in-session difficulty.
- The **Architect** reads and writes to it to resequence upcoming material (see [`docs/04-adaptive-learning/overview.md`](../04-adaptive-learning/overview.md)).
- The **content engine** reads it to know which lessons are safe to regenerate without breaking a learner's in-progress state (see [`docs/09-content-engine/overview.md`](../09-content-engine/overview.md)).
- The **frontend** renders it directly as an explorable visual (React Flow) for the learner's own "Knowledge Network" view (see [`docs/06-gamification/overview.md`](../06-gamification/overview.md)).

## Open questions

- Right granularity per node (too fine-grained: graph becomes unmanageable; too coarse: mastery signal becomes mushy).
- Whether prerequisite edges are authored by hand per skill folder or partially inferred/suggested by an LLM pass and then human-approved.
