# Adaptive Learning — "The Architect"

## Role, distinct from the AI Tutor

The AI Tutor ([`docs/03-ai-tutor/overview.md`](../03-ai-tutor/overview.md)) helps *in the moment*, inside a lesson. The Architect operates on a longer horizon: it continuously redesigns the learner's path *ahead of time*, based on the full knowledge graph state and performance history.

Examples of what it does, unprompted:

- Learning SQL today, it already knows window functions matter for a lab three months out — it can pre-seed lighter exposure earlier rather than a sudden jump later.
- Learning Python, it quietly sequences groundwork that will matter once PyTorch starts.
- Detecting weakness in graph theory, it inserts extra reinforcement weeks *before* reinforcement learning begins, rather than letting the learner hit a wall mid-mission.

## Inputs

- Accuracy, confidence, and speed per exercise
- Full mistake history and mistake *type* (conceptual vs. careless vs. prerequisite-gap)
- Retention scores per knowledge-graph node (FSRS retrievability estimates)
- Learning preferences observed over time
- Declared goals/timeline from the learner

## Outputs

- Reordering or inserting supplementary material between/within skill folders (without necessarily creating new top-level curriculum folders — see [`docs/02-curriculum/overview.md`](../02-curriculum/overview.md))
- Adjusting spaced-repetition intervals per concept
- Flagging when a learner is ready to skip ahead (mastery achieved faster than expected) vs. needs to slow down
- Feeding "readiness" signals to the AI Tutor so it calibrates difficulty within a session

## Guardrails

- The Architect must never silently skip a prerequisite the learner hasn't actually mastered — the knowledge graph's edges are hard constraints, not suggestions (see [`docs/08-knowledge-graph/overview.md`](../08-knowledge-graph/overview.md)).
- Every adaptive change should be explainable to the learner on request ("why am I doing this now?").

## Open questions

- How aggressively to reorder curriculum vs. preserving a predictable, motivating sense of linear progress toward missions.
- Cold-start behavior before enough performance data exists to adapt meaningfully.
