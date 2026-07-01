# Labs

Interactive coding sandboxes, one per lesson/concept where a hands-on lab is applicable (not every concept needs one — see [`docs/00-foundations/DESIGN_PRINCIPLES.md`](../docs/00-foundations/DESIGN_PRINCIPLES.md) on avoiding manufactured interactivity).

## What belongs here

- Starter code + task description for a given lab
- Expected test cases the sandboxed execution service (see [`docs/11-backend/overview.md`](../docs/11-backend/overview.md)) runs against learner submissions
- Debugging-challenge variants (intentionally broken code, tied to [`docs/05-assessments/overview.md`](../docs/05-assessments/overview.md))

## Constraints

Every lab must connect to the AI Energy OS mission — no generic, disconnected exercises (see [`CLAUDE.md`](../CLAUDE.md) content standards). A Python loop lab uses weather/demand data, not `range(10)`.

## Status

Empty. First real labs land alongside Mission 1 (`curriculum/01-python`, `curriculum/02-git`) content in Phase 1.
