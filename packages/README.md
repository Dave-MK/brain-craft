# Packages

Shared code across applications in `apps/` — a standard monorepo `packages/` directory. Not yet populated: no application code exists until Phase 1 (see [`docs/20-roadmap/overview.md`](../docs/20-roadmap/overview.md)) and the architecture questions in [`docs/10-frontend/overview.md`](../docs/10-frontend/overview.md) and [`docs/11-backend/overview.md`](../docs/11-backend/overview.md) are resolved.

## Anticipated packages

- `packages/ui` — shared component library (shadcn/ui-based, see [`docs/14-design-system/overview.md`](../docs/14-design-system/overview.md))
- `packages/types` — shared TypeScript types (lesson schema types, knowledge graph types) used by both frontend and NestJS backend
- `packages/config` — shared lint/tsconfig/tailwind config across apps

## Status

Empty by design — do not scaffold this until the Phase 1 architecture decisions are made (per [`CLAUDE.md`](../CLAUDE.md): "do not scaffold apps/ or packages/ application code until the corresponding architecture doc is written and the roadmap phase calls for it").
