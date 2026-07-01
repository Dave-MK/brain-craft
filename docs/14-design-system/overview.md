# Design System

Extends [`docs/00-foundations/DESIGN_PRINCIPLES.md`](../00-foundations/DESIGN_PRINCIPLES.md) into concrete tokens and components once frontend work begins.

## Anticipated scope

- **Tokens** — dark-mode-first color palette, spacing, typography scale (Tailwind config).
- **Component library** — built on shadcn/ui primitives, extended with BrainCraft-specific components: lesson-flow-step containers, knowledge-graph node/edge renderers, flashcard review cards, mastery fill-bars, the AI Tutor interaction surface.
- **Motion guidelines** — concrete rules for when Framer Motion animation is/isn't appropriate (educational vs. decorative), operationalizing the principle in the design-principles doc.
- **Data-viz conventions** — consistent D3 chart styling across forecasting charts, simulation dashboards, and algorithm visualisations.

## Open questions

- Exact component library scaffold — deferred until [`docs/10-frontend/overview.md`](../10-frontend/overview.md)'s monorepo layout question is resolved (likely lives in `packages/ui`).
