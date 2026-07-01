# Capstones

## Principle

There is no generic capstone menu (todo app, weather app, chat app). There is one capstone — the AI Energy Operating System — and every skill folder produces a real, integrated piece of it. See [`docs/02-curriculum/overview.md`](../02-curriculum/overview.md) for the skill → contribution mapping.

## Structure of the AI Energy OS

```
AI Energy OS
├── Digital Twin (grid/homes/solar/wind/batteries/EVs/weather/prices simulator)
├── Forecasting (demand, generation, price)
├── Neural Forecasting (deep models where they outperform classical ones)
├── Reinforcement Learning Optimiser (battery/EV scheduling)
├── Grid Routing (graph algorithms over network topology)
├── Carbon Optimisation
├── Explainable AI layer (why a recommendation was made)
├── Dashboard (operator-facing view, "Grid Copilot" framing)
└── Research Workspace (experiment tracking, hypothesis testing against the twin)
```

## Build order

Matches the skill order in `curriculum/`: the digital twin's data layer and simple scripting come first (Python, Git, SQL, APIs), then analysis (pandas), then forecasting (scikit-learn, PyTorch), then optimisation (reinforcement learning, graph algorithms), then domain fidelity (power systems), then integration (capstone folder).

## What "done" looks like at each mission

Each mission milestone should leave the learner with a demonstrably more capable version of the AI Energy OS — not a disconnected side-project. If a mission's project doesn't visibly plug into the existing system, the mission's design has failed the "everything builds toward the mission" principle (see [`docs/00-foundations/PHILOSOPHY.md`](../00-foundations/PHILOSOPHY.md)).

## Open questions

- How much of the digital twin is scaffolded/provided upfront (so early Python lessons have something real to parse/analyze) vs. built by the learner from nothing — likely a hybrid: a minimal seed twin exists early, and the learner's own code progressively replaces/extends it.
