# Accessibility

First-class requirement, not a post-launch pass (see [`docs/00-foundations/DESIGN_PRINCIPLES.md`](../00-foundations/DESIGN_PRINCIPLES.md)).

## Requirements

- Full keyboard navigation for every interactive surface, including the knowledge graph explorer and Monaco-based labs.
- Screen-reader support for lesson content, including alt-text/ARIA descriptions for data visualisations (D3 charts, algorithm animations) that convey the same information non-visually.
- Color-contrast compliance (WCAG AA minimum) across dark and light modes.
- Reduced-motion support respecting `prefers-reduced-motion`, with educational animations offering a static/step-through alternative rather than being disabled outright (the teaching value shouldn't disappear for motion-sensitive learners).

## Open questions

- How to make genuinely visual/spatial concepts (graph algorithms, neural network activations) accessible to screen-reader users without diluting the visual learners' experience — likely parallel textual/structured descriptions authored alongside each visualisation in the lesson schema.
