# Learning Science

BrainCraft's pedagogy is not invented from intuition — it's assembled from established cognitive-science research, and every lesson is required to implement it rather than defaulting to the read → watch → quiz → done pattern most courses use (which reliably produces ~80% forgetting within weeks).

## Techniques in use

- **Active recall** — learners retrieve answers from memory rather than re-reading; every lesson ends in retrieval, not just exposure.
- **Spaced repetition (FSRS)** — concepts resurface at intervals tuned to individual forgetting curves, not fixed schedules. See [`docs/08-knowledge-graph/overview.md`](../08-knowledge-graph/overview.md) for how review scheduling ties to the graph.
- **Retrieval practice** — testing is treated as a learning event, not just measurement.
- **Interleaving** — related-but-distinct concepts are mixed in practice sets rather than blocked, which improves discrimination and long-term retention over blocked practice.
- **Dual coding** — concepts are taught with both verbal explanation and visual/diagrammatic representation simultaneously (see [`docs/14-design-system/overview.md`](../14-design-system/overview.md)).
- **Chunking** — complex topics are decomposed into knowledge-graph-sized nodes small enough to hold in working memory.
- **Elaboration** — learners are prompted to connect new concepts to what they already know (especially back to the AI Energy OS mission).
- **Generation effect** — learners produce answers/code themselves before seeing worked solutions.
- **Testing effect** — frequent low-stakes retrieval beats infrequent high-stakes exams.
- **Feynman technique / Teach Back** — the learner explains the concept as if teaching someone else; the AI Tutor evaluates the explanation for gaps.
- **Socratic questioning** — the AI Tutor asks rather than tells (see [`docs/03-ai-tutor/overview.md`](../03-ai-tutor/overview.md)).
- **Deliberate practice** — practice targets the specific edge of current ability, not comfortable repetition.
- **Cognitive load theory** — lesson UI and pacing are designed to avoid overloading working memory (one new concept at a time, worked examples before open problems).
- **Desirable difficulties** — some friction is intentionally preserved (e.g. delayed feedback in certain exercises) because struggle that resolves correctly improves retention more than frictionless learning.
- **Error-based learning** — mistakes are treated as data for the knowledge graph and AI Tutor, not just "wrong, try again."
- **Mastery learning** — a learner doesn't advance past a concept until reaching a defined mastery threshold, rather than a fixed time-in-course.
- **Metacognition** — learners are prompted to assess their own confidence, and confidence vs. actual performance gaps are surfaced back to them.
- **Bloom's taxonomy** — assessments are designed to span remember → understand → apply → analyze → evaluate → create, not just "remember."
- **Memory palace / dual coding for spatial concepts** — used selectively where spatial metaphor genuinely helps (e.g. the knowledge graph itself, grid topology).

## How this is enforced, not just described

Every lesson schema (see [`schemas/`](../../schemas/) and [`docs/09-content-engine/overview.md`](../09-content-engine/overview.md)) has required fields that map directly to these techniques — e.g. every lesson must declare its flashcards, its reflection prompt, and its teach-back requirement. A lesson missing these fields fails schema validation and cannot ship.

## Open questions

- Exact FSRS parameter tuning strategy for a single learner with sparse early data.
- How much interleaving is appropriate early in the curriculum, before enough concepts exist to interleave meaningfully.
