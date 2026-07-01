# Design Principles

## Visual tone

- **Dark mode first.** Light mode is a supported alternative, not the default design target.
- **Minimal.** No clutter, no decorative chrome. Closer in spirit to Linear or Obsidian than to Moodle or a typical MOOC platform.
- **Animation only where educational.** Motion is used to show *how something works* (an algorithm mid-step, activations propagating through a network, a battery charge curve responding to a policy change) — never purely decorative transitions.
- **Keyboard accessible everywhere.** Every interactive surface — lesson navigation, code editor, knowledge graph, flashcard review — must be usable without a mouse.

## Interaction model

Concepts that can be made interactive, are:

- Sorting/searching/graph algorithms: the learner manipulates the data directly and watches the algorithm run step by step, with the AI explaining each comparison or decision.
- Neural networks: visualized as the model trains, not just described.
- SQL: query results and joins are visualized, not only returned as tables.
- Git: the commit graph is a real, manipulable diagram, not a diff snippet.

Where a concept truly can't be made interactive (e.g. some power-systems theory), it stays purely theoretical rather than forcing a gimmicky interaction that doesn't teach anything — see [`docs/01-learning-science/overview.md`](../01-learning-science/overview.md) on avoiding manufactured interactivity that adds cognitive load without adding understanding.

## The canonical lesson flow

Every lesson, regardless of subject, follows the same shape so the learner's mental model of "how a BrainCraft lesson works" never has to be relearned:

```
Problem → Motivation → Theory → Visual Explanation → Interactive Demo →
Guided Coding → Independent Coding → Debugging → Reflection → Teach Back →
Flashcards (spaced repetition) → Mini Project → Boss Battle → Portfolio Evidence
```

## Progress visualization

No meaningless XP bars. Mastery is shown as per-concept retention/confidence (e.g. a fill bar per knowledge-graph node), because "level 12" tells the learner nothing about what they can actually do. See [`docs/06-gamification/overview.md`](../06-gamification/overview.md).

## Accessibility

Full accessibility (screen reader support, keyboard navigation, color-contrast compliance, reduced-motion support) is a first-class requirement, not a post-launch pass. See [`docs/15-accessibility/overview.md`](../15-accessibility/overview.md).
