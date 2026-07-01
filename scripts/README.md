# Scripts

Build, content-generation, and living-curriculum update scripts.

## Anticipated scripts

- Content-schema validation (run in CI once `schemas/lesson.schema.json` exists — see [`docs/18-testing/overview.md`](../docs/18-testing/overview.md))
- Living-curriculum staleness check (checks tracked references in `docs/research/` and lesson `references` fields against upstream sources — see [`docs/09-content-engine/overview.md`](../docs/09-content-engine/overview.md))
- Knowledge graph consistency check (detects cycles, orphan nodes, missing prerequisite edges — see [`docs/08-knowledge-graph/overview.md`](../docs/08-knowledge-graph/overview.md))

## Status

Empty. First scripts are the schema validators, written alongside `schemas/` in the remainder of Phase 0.
