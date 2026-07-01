# BrainCraft

**An AI-native engineering academy with one mission: create engineers capable of solving humanity's hardest technical problems — starting with energy.**

BrainCraft is not a course library. It is a single, evolving learning system in which every skill taught — Python, Git, SQL, APIs, pandas, scikit-learn, PyTorch, reinforcement learning, graph algorithms, power systems — exists to serve one capstone: building an **AI Energy Operating System**, a platform that predicts, optimises, and controls energy use across homes, buildings, EVs, batteries, renewables, and data centres.

Success is not measured by course completion, streaks, or certificates. It's measured by whether the learner can build things that previously seemed impossible.

## Start here

| If you want... | Read... |
|---|---|
| The why | [`docs/00-foundations/MISSION.md`](docs/00-foundations/MISSION.md) |
| The product vision | [`docs/00-foundations/VISION.md`](docs/00-foundations/VISION.md) |
| The non-negotiable rules | [`docs/00-foundations/PHILOSOPHY.md`](docs/00-foundations/PHILOSOPHY.md) |
| How Claude Code should work in this repo | [`CLAUDE.md`](CLAUDE.md) |
| The full topic index | [`docs/`](docs/) |
| The skill-by-skill curriculum | [`curriculum/`](curriculum/) |

## Repository map

```
brain-craft/
├── README.md                  You are here
├── CLAUDE.md                   Operating instructions for Claude Code sessions
├── docs/                       Source of truth: philosophy, architecture, specs (00-20 + research)
├── curriculum/                 Skill-ordered course content (Python → AI Energy OS)
├── lessons/                    Individual lesson content, generated from curriculum/ schemas
├── labs/                       Interactive coding sandboxes, one per lesson/concept where applicable
├── simulations/                Visual/interactive concept simulators (sorting, grids, neural nets, etc.)
├── projects/                   Weekly projects and "boss battle" milestone projects
├── prompts/                    Reusable prompt templates (AI Tutor, Architect, content generation)
├── schemas/                    JSON/YAML schemas for lessons, concepts, assessments, knowledge graph
├── packages/                   Shared code (frontend, backend, shared types) — monorepo packages
├── apps/                       Deployable applications (web app, API, content pipeline)
└── scripts/                    Build, content-generation, and living-curriculum update scripts
```

## Status

This repository is in **Phase 0: Foundations**. The documentation, curriculum skeleton, and content schemas are being established before any application code is written. See [`docs/20-roadmap/overview.md`](docs/20-roadmap/overview.md) for the phased plan.

## Origin

BrainCraft was scoped out of a single realisation: coordinating energy systems — grids, batteries, renewables, EVs — is one of the defining engineering problems of the next several decades, and the fastest way to become capable of contributing to it is to build a learning system where every lesson is in service of that goal, not an isolated tutorial. See [`docs/00-foundations/MISSION.md`](docs/00-foundations/MISSION.md) for the full reasoning.
