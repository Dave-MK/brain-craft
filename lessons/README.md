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

Empty. Populated starting Phase 1, after `schemas/lesson.schema.json` exists (see [`docs/20-roadmap/overview.md`](../docs/20-roadmap/overview.md)).
