# Vision

## What BrainCraft is not

Not Codecademy. Not Coursera. Not Moodle. Not "ChatGPT embedded in a course wrapper."

## What BrainCraft is

Imagine if Codecademy, Duolingo, Brilliant, Linear, Cursor, GitHub, Obsidian, and LeetCode had one child obsessed with producing exceptional engineers. Interactive, visual, mission-driven, unapologetically opinionated about how humans actually retain knowledge, and permanently up to date.

The learner isn't a "user" accumulating XP. They're an engineer-in-training whose curriculum is a knowledge graph, whose tutor is a mentor that remembers everything, and whose "final project" is a real platform they're incrementally building across every single skill they learn.

## The AI Tutor

Not a chatbot bolted onto lessons. A tutor that maintains state across the learner's entire history:

- current lesson and where they are in the flow
- every past mistake and every past success
- time taken, hesitation patterns, confidence signals
- position in the knowledge graph — what's mastered, what's fragile, what's forgotten
- how this maps back to the AI Energy OS mission

It behaves like a tutor, coach, mentor, senior engineer, and research supervisor combined — and it almost never simply answers. It asks the next question that gets the learner to the answer themselves. See [`docs/03-ai-tutor/overview.md`](../03-ai-tutor/overview.md).

## The Architect

A second, longer-horizon AI role, distinct from the AI Tutor: while the Tutor helps *in the moment*, the Architect continuously redesigns the learner's education *ahead of time*. Learning SQL today, it already knows window functions matter in three months for a later lab. Learning Python, it quietly prepares groundwork for PyTorch. Struggling with graph theory, it inserts extra reinforcement before reinforcement learning begins, without being asked. See [`docs/04-adaptive-learning/overview.md`](../04-adaptive-learning/overview.md).

## The Knowledge Graph

Every concept — from "variables" to "grid optimisation" — is a node with explicit prerequisite edges. The system can answer "you cannot understand reinforcement learning yet because you're weak on probability" and route the learner back before they hit a wall they don't understand. See [`docs/08-knowledge-graph/overview.md`](../08-knowledge-graph/overview.md).

## The Living Curriculum

Traditional courses freeze the moment they're published. BrainCraft's curriculum is stored as structured data with tracked references (official docs, library versions, papers), and a pipeline continuously checks those references against reality — new releases, deprecations, new research — and regenerates affected lessons. Nothing becomes obsolete silently. See [`docs/09-content-engine/overview.md`](../09-content-engine/overview.md).

## The feel of the product

Dark mode first. Minimal. Closer to Linear than to Moodle. Animation only where it teaches something (a sorting algorithm visualized mid-comparison, a neural net's activations lighting up) — never decorative. Fully keyboard accessible. See [`docs/14-design-system/overview.md`](../14-design-system/overview.md).

## The end state

A learner who can ask and *answer* questions like:

- How can an AI reduce national electricity demand without reducing quality of life?
- How can reinforcement learning optimise battery storage across millions of homes?
- Can new optimisation algorithms outperform existing approaches while using less compute?
- How should an AI coordinate renewables, EVs, and industrial loads in real time?
- Could an AI discover new algorithms or architectures that make computation dramatically more energy-efficient?

These are research questions, not homework. A platform built around them trains a contributor to one of this century's defining engineering challenges — not just a software developer.
