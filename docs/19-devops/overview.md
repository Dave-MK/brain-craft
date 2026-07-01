# DevOps

## Stack (current default)

Docker (sandboxed execution + local dev parity), GitHub Actions (CI — lint, typecheck, test, content-schema validation), Vercel (web app), Railway or Fly.io (API/services).

## CI responsibilities (once code exists)

- Lint + typecheck (TS strict, Python ruff/black)
- Test suites (application + content-schema validation, see [`docs/18-testing/overview.md`](../18-testing/overview.md))
- Living-curriculum staleness check as a scheduled job, not blocking normal CI (see [`docs/09-content-engine/overview.md`](../09-content-engine/overview.md))

## Open questions

- Railway vs. Fly.io final choice for API/service hosting — deferred until [`docs/11-backend/overview.md`](../11-backend/overview.md) service boundaries are finalized.
