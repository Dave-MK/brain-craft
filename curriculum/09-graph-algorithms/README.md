# 09 — Graph Algorithms

**Mission:** Optimise Decisions (Mission 5)

## Capstone contribution

Grid routing and topology reasoning — modeling the electricity network itself as a graph so the AI Energy OS can reason about transmission losses, contingencies (e.g. "what if two substations fail"), and routing.

## Learning objectives

- Graph representations and traversal (BFS/DFS) fundamentals
- Shortest-path and flow algorithms, applied to network routing/loss minimization
- Reasoning about network resilience — identifying critical nodes/edges whose failure would be most damaging
- Where reinforcement learning (prior skill folder) and graph algorithms (this one) combine: RL over a graph-structured action space

## Prerequisites

[`python.dictionaries`](../01-python/README.md) technically (adjacency-list representation); [`08-reinforcement-learning`](../08-reinforcement-learning/README.md) converges with this folder at `graphs-rl-combination`, confirming the two are parallel, not strictly sequential, exactly as anticipated below.

## Leads into

[`10-power-systems`](../10-power-systems/README.md)

## Status

Complete. All 6 lessons authored and schema-validated in [`lessons/09-graph-algorithms/`](../../lessons/09-graph-algorithms/): Representation & Traversal → Shortest Path (Dijkstra) → {Flow Algorithms, Resilience & Critical Nodes} → RL + Graphs Combination (converges with `08-reinforcement-learning`) → The Grid Router (boss battle). This lesson set delivers concrete, numeric answers to both founding example questions from the mission's original scoping conversation: minimum-loss routing and two-substation contingency survival. **Mission 5 ("Optimise Decisions") is fully authored.**
