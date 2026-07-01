# Project Glossary

**AI Energy Operating System (AI Energy OS)** — The capstone platform every skill in the curriculum builds toward: forecasts demand/generation, optimises decisions (batteries, EVs, routing), and eventually acts on them within a digital twin.

**Mission (curriculum)** — A motivational grouping of skills around a goal the learner cares about (e.g. "Predict the Future" spans scikit-learn and time-series forecasting). Distinct from a "skill folder" in `curriculum/`, which is the implementation unit. See [`docs/02-curriculum/overview.md`](../02-curriculum/overview.md).

**Digital Twin** — The simulated grid/energy environment (homes, solar, wind, batteries, EVs, weather, prices) the learner builds and experiments against before any claim is made about real infrastructure.

**Knowledge Graph** — The dependency graph of every taught concept, used to determine readiness, detect gaps, and drive adaptive sequencing. See [`docs/08-knowledge-graph/overview.md`](../08-knowledge-graph/overview.md).

**AI Tutor** — The in-the-moment mentor AI that knows the learner's full history and teaches via questions rather than answers. See [`docs/03-ai-tutor/overview.md`](../03-ai-tutor/overview.md).

**The Architect** — The longer-horizon AI role that continuously redesigns the curriculum ahead of the learner's current position, inserting reinforcement or prep material before it's needed. See [`docs/04-adaptive-learning/overview.md`](../04-adaptive-learning/overview.md).

**Living Curriculum** — The system that keeps lesson content from going stale by tracking references (docs, library versions, papers) and regenerating affected lessons automatically. See [`docs/09-content-engine/overview.md`](../09-content-engine/overview.md).

**Boss Battle** — A milestone assessment at the end of a skill/mission that requires synthesizing everything taught so far into a harder, less-scaffolded challenge, distinct from routine mini-projects.

**FSRS** — Free Spaced Repetition Scheduler; the specific spaced-repetition algorithm BrainCraft uses over legacy SM-2-style approaches, because it models memory more accurately.

**Lesson Flow** — The canonical 14-step sequence every lesson follows: Problem → Motivation → Theory → Visual Explanation → Interactive Demo → Guided Coding → Independent Coding → Debugging → Reflection → Teach Back → Flashcards → Mini Project → Boss Battle → Portfolio Evidence.

**Capstone Contribution** — The specific piece of the AI Energy OS a given skill/lesson produces (e.g. Python → weather data parser; SQL → grid data store; scikit-learn → demand forecaster).

**Grid Copilot** — A named example of what the AI Energy OS becomes at maturity: decision support (not autonomous control) that monitors signals, simulates futures, explains recommendations, and quantifies cost/stability/emissions trade-offs, earning trust for greater autonomy over time.
