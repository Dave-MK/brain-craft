# Lessons

Rendered/generated lesson instances live conceptually here, keyed by skill folder and concept, once the content engine exists (see [`docs/09-content-engine/overview.md`](../docs/09-content-engine/overview.md)).

## Relationship to `curriculum/`

`curriculum/<skill>/README.md` describes *what* a skill folder teaches and why. This folder holds the actual generated lesson artifacts — each conforming to `schemas/lesson.schema.json` (not yet written) — following the canonical lesson flow defined in [`docs/00-foundations/DESIGN_PRINCIPLES.md`](../docs/00-foundations/DESIGN_PRINCIPLES.md):

```
Problem → Motivation → Theory → Visual Explanation → Interactive Demo →
Guided Coding → Independent Coding → Debugging → Reflection → Teach Back →
Flashcards → Mini Project → Boss Battle → Portfolio Evidence
```

## Do not hand-author freehand lesson pages here

Per [`CLAUDE.md`](../CLAUDE.md), lessons are structured data first. This directory should never accumulate one-off markdown lessons that bypass the schema — that's the exact failure mode ("curriculum rot") the Living Curriculum system exists to prevent.

## Status

`01-python/` is complete: 11 lessons, all validated against `schemas/lesson.schema.json`, forming one continuous path —

```
variables → control-flow → lists → loops → functions → dictionaries
                                                              ↓
                                            sets, error-handling → files-io → modules → oop-basics (boss battle)
```

(see each lesson's `dependencies` field for the exact knowledge-graph edges; the full chain was verified programmatically for missing edges and cycles). Organized as `lessons/<skillFolder>/<lesson-id>.lesson.json`, mirroring `curriculum/`.

`02-git/` is also complete: 6 lessons — `git-init-and-commits` (depends on `python.oop-basics`, tying the two skill folders together) → `git-branches` → `git-merging` → {`git-resolving-conflicts`, `git-remote-collaboration`} → `git-rebasing-basics` (boss battle). 17 lessons total across both folders; the combined dependency graph has been checked for missing edges and cycles.

**Mission 1 ("Learn Programming") is fully authored.** `03-sql/` is also complete: 6 lessons — `sql-select-where` (depends on `python.files-io`) → `sql-joins` → `sql-aggregation` → `sql-schema-design` → `sql-window-functions` → `sql-indexing-performance` (boss battle). 23 lessons total across `01-python` + `02-git` + `03-sql`; the combined dependency graph has no missing edges or cycles.

`04-apis/` is also complete: 6 lessons — `apis-http-fundamentals` (depends on `python.error-handling`) → `apis-authentication` → `apis-consuming-rest` → {`apis-rate-limits-retries`, `apis-pagination`} → `apis-resilient-ingestion` (boss battle). 29 lessons total across `01-python` + `02-git` + `03-sql` + `04-apis`; combined graph re-checked — clean.

`05-pandas/` is also complete: 6 lessons — `pandas-dataframes-basics` (depends on `sql.aggregation`) → `pandas-filtering-aggregation` → `pandas-time-series` → `pandas-merging-datasets` → `pandas-data-cleaning` → `pandas-capstone-feature-table` (boss battle — Mission 2's final deliverable, the actual feature table Mission 3 trains on). 35 lessons total; combined graph re-checked — clean.

**Missions 1 ("Learn Programming") and 2 ("Manipulate Data") are both fully authored.** `06-scikit-learn/` is also complete: 6 lessons — `sklearn-regression-basics` (depends on `pandas.capstone-feature-table`) → `sklearn-baselines-and-leakage` → `sklearn-time-series-cv` and `sklearn-classification-basics` (parallel) → `sklearn-feature-importance-evaluation` → `sklearn-demand-forecaster` (boss battle — the Digital Twin's first production-shaped forecasting model). 41 lessons total; combined graph re-checked — clean.

`07-pytorch/` is also complete: 6 lessons — `pytorch-tensors-autograd` (depends on `sklearn.demand-forecaster`) → `pytorch-building-networks` → `pytorch-training-loop` → `pytorch-overfitting-regularization` → `pytorch-sequence-models` → `pytorch-neural-forecaster` (boss battle — the honest neural-vs-classical verdict that decides what feeds Mission 5). 47 lessons total across Missions 1-4; combined graph re-checked — clean.

**Missions 1-4 are fully authored.** `08-reinforcement-learning/` is also complete: 6 lessons — `rl-mdp-fundamentals` (depends on `pytorch.neural-forecaster`) → `rl-reward-design` → {`rl-value-based-methods`, `rl-policy-gradient-methods`} → `rl-training-evaluation-safety` → `rl-battery-scheduler` (boss battle — the literal "Grid Copilot" behavior from the original mission vision, now built as an explainable decision-maker). 53 lessons total; combined graph re-checked — clean.

`09-graph-algorithms/` is also complete: 6 lessons — `graphs-representation-traversal` (depends on `python.dictionaries`) → `graphs-shortest-path` → {`graphs-flow-algorithms`, `graphs-resilience-critical-nodes`} → `graphs-rl-combination` (depends on `rl.battery-scheduler` + both graph-algorithm branches — the actual convergence point of Mission 5's two parallel skill folders) → `graphs-grid-router` (boss battle — concrete numeric answers to both of the mission's founding example questions). 59 lessons total; combined graph re-checked — clean.

**Missions 1-5 are fully authored.** `10-power-systems/` is also complete: 6 lessons — `power-generation-transmission-distribution` (depends on `graphs.grid-router`) → `power-load-balancing` → {`power-renewable-intermittency`, `power-grid-stability-cascading-failures`} → `power-energy-markets-pricing` → `power-digital-twin-fidelity` (boss battle — upgrades the Digital Twin with real physics/economics and re-validates an earlier mission's result against it). 65 lessons total; combined graph re-checked — clean.

`11-capstone-ai-energy-os/` is also complete: 6 lessons — `capstone-system-integration` (depends on `power.digital-twin-fidelity`, assembling all ten prior skill folders' artifacts) → {`capstone-carbon-optimisation`, `capstone-explainability-layer`} → {`capstone-dashboard`, `capstone-research-workspace`} → `capstone-ai-energy-os` (the final boss battle of the entire curriculum).

**The entire BrainCraft curriculum is now fully authored: 71 lessons across 11 skill folders and 7 missions (M1–M6, M8). The combined dependency graph has been checked after every single addition throughout this build — zero missing edges, zero cycles, 11 boss battles (one per skill folder) culminating in `capstone-ai-energy-os`.**
