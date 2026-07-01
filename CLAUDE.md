# CLAUDE.md — Operating Instructions for Claude Code in BrainCraft

This file is read by every Claude Code session working in this repository. It is not a suggestion — it is the contract. If a task conflicts with this document, stop and flag the conflict instead of silently picking one side.

## What this repo is

BrainCraft is a single-learner, AI-native engineering academy. The learner is teaching themselves Python → Git → SQL → APIs → pandas → scikit-learn → PyTorch → reinforcement learning → graph algorithms → power systems, in that order, with every concept in service of one capstone: an **AI Energy Operating System** (a platform that forecasts, optimises, and controls energy use — demand, batteries, EVs, renewables, grid routing).

This is not "a folder of markdown for an AI to skim." Treat `docs/` as a specification a 100-person engineering org would hand to its first engineer. When you build features, curriculum, or code, **read the relevant doc in `docs/` first** rather than inventing structure. If the doc doesn't exist yet or is a stub, that's a signal to write it properly before building on top of it — not to guess.

## The immutable rule

> This platform exists to create builders, not consumers. Every lesson, feature, design decision, and line of code must increase the learner's ability to understand complex systems, think independently, solve meaningful problems, and create technology that measurably improves the lives of people and the health of the planet. Simplicity is preferred over cleverness, evidence over opinion, curiosity over certainty, and long-term impact over short-term engagement. Features that maximise screen time at the expense of learning are considered defects. Success is measured not by course completion, but by the learner's ability to build things that previously seemed impossible.

Judge every feature against this. If it makes better engineers, it stays. If it exists only because "every learning platform has one" (streak counters for their own sake, meaningless XP, engagement-bait notifications), it goes.

## Non-negotiable principles

1. Every concept has purpose — stated explicitly, before the concept is taught.
2. Everything builds toward the mission (the AI Energy OS capstone). No toy todo-apps, no generic "hello world" filler.
3. Nothing is memorised without understanding. Understanding precedes abstraction.
4. Theory always leads to practice; practice always leads to creation; creation always leads to reflection; reflection strengthens retention.
5. Knowledge is interconnected — every concept is a node in the knowledge graph with explicit prerequisites.
6. Learning never ends — the curriculum is *living*, not frozen (see `docs/09-content-engine/`).
7. Evidence over opinion: pedagogical choices cite learning-science research (see `docs/01-learning-science/`), not intuition.
8. Simplicity over cleverness in both the platform's code and the concepts it teaches.
9. No dark patterns. No screen-time-maximising mechanics.
10. Progress is measured by mastery and retention, not completion percentage.

## How the curriculum is modeled

Skills are organized as ordered folders in `curriculum/` (`01-python` … `11-capstone-ai-energy-os`). A narrative layer of **Missions** groups these skills around motivation (e.g. Mission "Predict the Future" spans scikit-learn + time-series forecasting); see `docs/02-curriculum/overview.md`. Do not flatten these two layers into one — skill folders are the implementation unit, missions are the motivational framing shown to the learner.

Every lesson, regardless of skill, follows this flow (see `docs/01-learning-science/overview.md` for why each step exists):

```
Problem → Motivation → Theory → Visual Explanation → Interactive Demo →
Guided Coding → Independent Coding → Debugging → Reflection → Teach Back →
Flashcards (spaced repetition) → Mini Project → Boss Battle → Portfolio Evidence
```

Lesson content is **structured data first, prose second**. A lesson is authored as a schema-conformant JSON/YAML object (see `schemas/lesson.schema.json` once it exists, and `docs/09-content-engine/overview.md`), and rendered/regenerated from that data — not hand-written as a one-off markdown page. This is what lets the curriculum stay living and lets the AI Tutor reason over it.

## Tech stack (current defaults — revisit via ADR, don't silently change)

- **Frontend**: Next.js, React, TypeScript, Tailwind, shadcn/ui, Framer Motion (educational animation only), React Flow (knowledge graph / diagrams), Monaco Editor (in-browser code), D3 (visualisations), Three.js (deferred until needed).
- **Backend**: NestJS, PostgreSQL, Prisma, Supabase Auth, Redis, BullMQ (background jobs — content regeneration, spaced-repetition scheduling).
- **AI**: Anthropic + OpenAI for tutoring/content generation, local/embedded model for retrieval, RAG over `docs/` + curriculum content + official library docs for the living-curriculum system.
- **Python side** (labs, ML/RL curriculum, simulators): FastAPI, PyTorch, scikit-learn, NumPy, pandas — run in sandboxed Docker containers, never on the host directly.
- **Infra**: Docker, GitHub Actions, Vercel (web), Railway or Fly.io (API/services).
- **Spaced repetition**: FSRS algorithm, not naive SM-2.

None of this is built yet as of Phase 0. Do not scaffold `apps/` or `packages/` application code until the corresponding architecture doc in `docs/10-frontend/`, `docs/11-backend/`, `docs/12-database/` is written and the roadmap phase calls for it.

## Content standards

- Never generate filler lessons, generic "hello world," or examples disconnected from the energy mission. A Python loop lesson uses weather/demand data, not `for i in range(10): print(i)`.
- Every lesson must answer "why does this matter for the AI Energy OS?" explicitly, near the top, not implied.
- Cite sources for factual/technical claims (official docs, papers) — content in `docs/research/` should track what was cited and when, so the living-curriculum pipeline can detect staleness.
- Assessments are never multiple-choice-only. Prefer code review, debugging challenges, teach-back, and project work (see `docs/05-assessments/overview.md`).

## Coding standards (once application code exists)

- TypeScript strict mode everywhere in `apps/` and `packages/`.
- Python: type-hinted, `ruff`/`black` formatted.
- No comments explaining *what* code does; comments only for non-obvious *why*.
- No speculative abstraction — build for the current phase's actual requirements.

## Current phase

**Phase 0: Foundations.** The active work is documentation, curriculum skeleton, and content schemas in `docs/` and `curriculum/`. Do not start building `apps/` (Next.js app, NestJS API) until Phase 0's docs are substantially complete and the roadmap (`docs/20-roadmap/overview.md`) says to proceed. When in doubt about scope, extend documentation and schemas rather than writing application code.

## Extending this repo

- **New topic area** → add `docs/NN-topic/overview.md` following the existing doc pattern (problem framing → decisions → open questions → links).
- **New curriculum skill** → add `curriculum/NN-skill/README.md` linking to its mission, prerequisites, and capstone contribution.
- **New lesson** → author against `schemas/lesson.schema.json` (write the schema first if it doesn't exist), not as a freehand markdown file.
- Any structural decision that isn't obviously reversible (tech stack swap, curriculum reordering, dropping a principle above) should be recorded as an ADR-style note rather than made silently.
