# Assessments

## Principle

Multiple-choice-only assessment is banned as a primary evaluation method. It measures recognition, not the abilities BrainCraft is optimizing for (see [`docs/00-foundations/SUCCESS_METRICS.md`](../00-foundations/SUCCESS_METRICS.md)).

## Assessment types in rotation

- **Code review** — the learner reviews (correct, working but flawed) code and identifies issues, mirroring real engineering practice.
- **Debugging** — the learner is handed intentionally broken code tied to the current concept and must fix it.
- **Architecture/design** — the learner proposes a design for a small system and defends trade-offs.
- **Teach back** — the learner explains a concept as if teaching someone else; evaluated for gaps (Feynman technique, see [`docs/01-learning-science/overview.md`](../01-learning-science/overview.md)).
- **Oral/written explanation** — free-form explanation, evaluated by the AI Tutor for conceptual accuracy, not just keyword matching.
- **Project work** — the primary evidence of mastery; every skill folder culminates in one.
- **Research** — reading a paper/doc and forming a hypothesis or comparison, used more heavily from the ML/RL missions onward.
- **Simulation-based** — running an experiment inside the digital twin and interpreting results.
- **Reflection** — structured self-assessment tied into the metacognition loop.

## Mastery, not scores

Assessment outcomes feed the knowledge graph as mastery/retention signals (see [`docs/08-knowledge-graph/overview.md`](../08-knowledge-graph/overview.md)), not a letter grade. A learner doesn't "pass" a skill folder by scoring 70% on a quiz — they reach a defined mastery threshold across its concepts, demonstrated through varied assessment types, before advancing (mastery learning).

## Boss Battles

End-of-skill/end-of-mission assessments that are deliberately less scaffolded than routine exercises, requiring synthesis of everything taught in that unit. See [`docs/00-foundations/PROJECT_GLOSSARY.md`](../00-foundations/PROJECT_GLOSSARY.md).

## Open questions

- Automated grading strategy for open-ended code/design assessments (rubric-based AI grading + spot-check, most likely) — depends on [`docs/03-ai-tutor/overview.md`](../03-ai-tutor/overview.md) architecture decisions.
- How "portfolio evidence" (the last lesson-flow step) is captured and displayed as it accumulates across missions.
