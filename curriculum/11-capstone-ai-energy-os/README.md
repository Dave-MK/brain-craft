# 11 — Capstone: AI Energy Operating System

**Mission:** Build the AI Energy OS (Mission 8)

## What this folder is

Not a new skill — the integration point where every prior skill folder's output is assembled into one working system. See [`docs/07-capstones/overview.md`](../../docs/07-capstones/overview.md) for the target architecture:

```
AI Energy OS
├── Digital Twin
├── Forecasting
├── Neural Forecasting
├── Reinforcement Learning Optimiser
├── Grid Routing
├── Carbon Optimisation
├── Explainable AI layer
├── Dashboard ("Grid Copilot")
└── Research Workspace
```

## Prerequisites

All of [`01-python`](../01-python/README.md) through [`10-power-systems`](../10-power-systems/README.md).

## Definition of done (v1)

A working simulation in which the system can be asked something like "how do I reduce energy costs by 12%?" or "how do I avoid overloading the grid if two substations fail?" and produce a tested, explainable answer validated against the digital twin — not a slide deck.

## Beyond v1

Per the original scoping discussion, once the system demonstrates a consistent improvement (e.g. 3-5%) in simulated scenarios, that becomes the concrete evidence base for approaching real utilities, researchers, or investors — a much stronger position than an idea alone. This is a future phase, not a Phase 0 concern (see [`docs/20-roadmap/overview.md`](../../docs/20-roadmap/overview.md)).

## Status

Complete. All 6 lessons authored and schema-validated in [`lessons/11-capstone-ai-energy-os/`](../../lessons/11-capstone-ai-energy-os/): System Integration (assembles all ten prior skill folders' artifacts into one running codebase) → {Carbon Optimisation, Explainability Layer} → {Dashboard, Research Workspace} → The AI Energy OS (final boss battle — the mission's founding "reduce energy costs" claim, evaluated rigorously and honestly against a genuinely independent baseline).

**The entire BrainCraft curriculum is now fully authored: 71 lessons across 11 skill folders and 7 missions (M1–M6, M8), one continuous knowledge graph, verified after every addition to have zero missing dependency edges and zero cycles.**
