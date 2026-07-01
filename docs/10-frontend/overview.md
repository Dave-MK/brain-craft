# Frontend Architecture

## Stack (current default — see [`CLAUDE.md`](../../CLAUDE.md))

Next.js, React, TypeScript, Tailwind, shadcn/ui, Framer Motion, React Flow, Monaco Editor, TanStack Query, D3, Three.js (deferred).

## Why these, specifically

- **React Flow** — the knowledge graph and Architect-driven sequencing views need a real interactive graph, not a static diagram image.
- **Monaco Editor** — in-browser coding exercises need a real editor experience (the one VS Code uses), not a plain textarea.
- **D3** — bespoke visualisations (algorithm step-through, energy simulation charts) that off-the-shelf chart libraries can't express.
- **Framer Motion** — reserved for *educational* motion only (see [`docs/00-foundations/DESIGN_PRINCIPLES.md`](../00-foundations/DESIGN_PRINCIPLES.md)) — not page-transition flourish.
- **TanStack Query** — server state (lesson content, tutor session state, knowledge graph state) is fetched/cached consistently rather than ad hoc.

## Key surfaces to design (not yet built — Phase 0)

- Lesson runner (renders the 14-step lesson flow from structured lesson data)
- Knowledge graph explorer (React Flow-based "Knowledge Network" view)
- AI Tutor chat/interaction surface (distinct visual treatment from a generic chatbot)
- In-browser lab/sandbox surface (Monaco + sandboxed execution, see [`docs/11-backend/overview.md`](../11-backend/overview.md) for how execution is isolated)
- Digital twin / simulation dashboards

## Standards

TypeScript strict mode. Dark-mode-first design tokens (see [`docs/14-design-system/overview.md`](../14-design-system/overview.md)). Full keyboard accessibility (see [`docs/15-accessibility/overview.md`](../15-accessibility/overview.md)).

## Open questions

- Monorepo layout for `apps/web` vs. shared `packages/ui` — to be decided when Phase 0 docs are complete and scaffolding begins.
- Whether the lesson runner is server-rendered per step or a client-side state machine over pre-fetched lesson data.
