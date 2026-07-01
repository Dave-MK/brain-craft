# Scripts

Build, content-generation, and living-curriculum update scripts.

## Anticipated scripts

- Content-schema validation (run in CI once `schemas/lesson.schema.json` exists — see [`docs/18-testing/overview.md`](../docs/18-testing/overview.md))
- Living-curriculum staleness check (checks tracked references in `docs/research/` and lesson `references` fields against upstream sources — see [`docs/09-content-engine/overview.md`](../docs/09-content-engine/overview.md))
- Knowledge graph consistency check (detects cycles, orphan nodes, missing prerequisite edges — see [`docs/08-knowledge-graph/overview.md`](../docs/08-knowledge-graph/overview.md))

## Status

[`generate_knowledge_graph.py`](generate_knowledge_graph.py) is written and run: it validates every lesson in `lessons/**/*.lesson.json` against `schemas/lesson.schema.json`, derives a `concept-node.schema.json`-conformant node per lesson, checks the whole graph for missing prerequisite edges and cycles, and writes [`docs/08-knowledge-graph/knowledge-graph.json`](../docs/08-knowledge-graph/knowledge-graph.json). This is the script that formalizes the ad-hoc validation run by hand after every lesson added during curriculum authoring — re-run it after any future lesson change.

Remaining: a CI wrapper that runs this on every commit (see [`docs/18-testing/overview.md`](../docs/18-testing/overview.md)) rather than manually.
