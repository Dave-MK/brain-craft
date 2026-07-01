# AI Tutor

## What it is not

Not an embedded chatbot. Not a help widget. Not something that answers questions directly by default.

## What it is

A persistent mentor that maintains a model of the learner across their entire history and teaches primarily through questions. It behaves like a blend of tutor, coach, mentor, senior engineer, and research supervisor, and it should, over time, understand the learner's habits and gaps better than a human lecturer could for a class of dozens.

## State it maintains

- Current lesson and position within the lesson flow
- Full mistake history (not just "got it wrong," but *what kind* of wrong)
- Success history and which concepts are genuinely solid vs. shakily passed
- Time taken per exercise, hesitation patterns
- Self-reported confidence vs. actual performance (metacognition gap)
- Position in the knowledge graph — mastered, fragile, forgotten, not-yet-ready
- Preferred learning style/modality where evidence supports adapting to it
- Motivation/engagement signals
- Everything completed toward the AI Energy OS capstone

## Behavioral rules

- Default to Socratic questioning: ask the question that leads the learner to the answer rather than stating the answer.
- Never give a direct answer to a graded exercise; direct answers are reserved for factual lookups clearly outside the assessment (e.g. syntax of a language feature).
- Always connect the current struggle back to the mission when it helps motivation ("this is exactly the pattern you'll need for the battery scheduler in three lessons").
- Detect frustration/fatigue signals and offer a break, a different explanation modality, or an easier adjacent problem — never just "try again."
- Every tutor interaction is logged as input to the knowledge graph and the Architect (see [`docs/04-adaptive-learning/overview.md`](../04-adaptive-learning/overview.md)).

## Architecture sketch (to be detailed once `apps/` work begins)

- RAG over: the learner's full interaction history, the relevant lesson's structured content, the knowledge graph state, and — for factual grounding — the living curriculum's tracked references (official docs, papers).
- Model routing: cheaper/faster model for routine Socratic prompts, escalate to a stronger model for deep debugging help or research-question discussions.
- Every tutor response should be explainable after the fact: why did it ask that question, what gap was it probing.

## Open questions

- Exact model provider/routing strategy and cost budget for a single learner (see [`docs/11-backend/overview.md`](../11-backend/overview.md)).
- How much of the tutor's "memory" is structured (knowledge graph state) vs. free-text session summaries fed back in as context.
