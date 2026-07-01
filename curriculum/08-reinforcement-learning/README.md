# 08 — Reinforcement Learning

**Mission:** Optimise Decisions (Mission 5)

## Capstone contribution

Battery and EV charging scheduling optimisation — the core "Act" decision-maker of the AI Energy OS (see [`docs/00-foundations/MISSION.md`](../../docs/00-foundations/MISSION.md) Layer 3), learned from a reward signal (cost, emissions, stability) rather than hand-written rules.

## Learning objectives

- MDP fundamentals: states, actions, rewards, policies, value functions
- Core algorithms (value-based and policy-gradient approaches) with enough breadth to choose sensibly, not just one memorized recipe
- Designing a reward function for a real system (cost, emissions, equipment overload avoidance) — this is as much a modeling skill as an algorithmic one
- Training and evaluating an RL agent against the digital twin, safely, before any claim about real infrastructure
- Explainability: producing a rationale for a recommended action, not just the action itself (ties to [`docs/07-capstones/overview.md`](../../docs/07-capstones/overview.md) "explainable AI layer")

## Prerequisites

[`07-pytorch`](../07-pytorch/README.md), sufficient probability foundation (the Architect may insert reinforcement material here per [`docs/04-adaptive-learning/overview.md`](../../docs/04-adaptive-learning/overview.md))

## Leads into

[`09-graph-algorithms`](../09-graph-algorithms/README.md)

## Status

Complete. All 6 lessons authored and schema-validated in [`lessons/08-reinforcement-learning/`](../../lessons/08-reinforcement-learning/): MDP Fundamentals → Reward Design → {Value-Based Methods, Policy Gradient Methods} → Training/Evaluation/Safety → The Battery Scheduler (boss battle — the first AI Energy OS component that recommends and explains a decision, not just predicts one).
