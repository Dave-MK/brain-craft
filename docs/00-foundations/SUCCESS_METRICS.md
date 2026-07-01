# Success Metrics

## What actually counts

- **Retention after years, not weeks.** Measured via spaced-repetition performance on old material re-surfaced months later, not quiz scores taken immediately after a lesson.
- **Transfer to novel problems.** Can the learner solve a problem they haven't been explicitly taught the pattern for, using concepts they've mastered?
- **Ability to build real software.** Working code, shipped labs, a growing capstone — not a completion certificate.
- **Ability to conduct research.** Can the learner read a paper, form a hypothesis, and design an experiment to test it inside the simulator?
- **Measurable real-world contribution potential.** Ultimately: could what's been built and learned plausibly reduce energy waste or improve grid resilience if extended further?

## Explicit anti-metrics (defects if optimized for)

These are the metrics a typical ed-tech product optimizes for. In BrainCraft, improving these *at the expense of the metrics above* is treated as a bug:

- Daily active usage / streak length, if pursued for its own sake
- Course completion percentage
- Time on platform / session length
- Lesson count consumed
- Vanity XP or levels

Streaks, session length, and completion counts can still be *shown* to the learner as information, but they must never become optimization targets for the content or product itself. If a feature increases time-on-platform without increasing retention, transfer, or build capability, it is removed.

## How this gets measured in practice

- Spaced-repetition review performance over time (FSRS retrievability estimates), tracked per knowledge-graph node — see [`docs/08-knowledge-graph/overview.md`](../08-knowledge-graph/overview.md).
- Assessment variety and pass rates across code review, debugging, teach-back, and project-based assessments — see [`docs/05-assessments/overview.md`](../05-assessments/overview.md).
- Capstone artifact growth: does the AI Energy OS gain real, working capability at each mission milestone?
- Periodic "cold" reflection prompts: can the learner explain a concept taught weeks or months earlier, unprompted?
