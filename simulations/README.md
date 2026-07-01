# Simulations

Visual/interactive concept simulators — the "learner drags numbers and watches the algorithm run" pieces described in [`docs/00-foundations/VISION.md`](../docs/00-foundations/VISION.md) and [`docs/00-foundations/DESIGN_PRINCIPLES.md`](../docs/00-foundations/DESIGN_PRINCIPLES.md).

## Two categories

1. **Concept simulators** — sorting/searching/graph-traversal visualisations, neural network training visualisations, SQL join visualisations, Git commit-graph manipulation. Scoped to teaching one concept clearly.
2. **The Digital Twin** — the larger, persistent simulated grid (homes, solar, wind, batteries, EVs, weather, prices) that the AI Energy OS capstone is built and tested against across multiple missions. This is cross-cutting and grows incrementally rather than belonging to one skill folder.

## Technology

D3 for bespoke concept visualisations, React Flow where a graph structure is the primary object (grid topology, knowledge graph), per [`docs/10-frontend/overview.md`](../docs/10-frontend/overview.md).

## Status

Empty. The Digital Twin's minimal seed version is the first thing built here, in Phase 1, so early Python/SQL/pandas lessons have something real to parse and analyze (see [`docs/07-capstones/overview.md`](../docs/07-capstones/overview.md) open questions).
