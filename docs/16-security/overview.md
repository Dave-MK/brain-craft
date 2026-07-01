# Security

## Highest-risk surface: code execution

Learner-submitted code (Python labs, later RL/simulation code) runs in the sandboxed execution service ([`docs/11-backend/overview.md`](../11-backend/overview.md)), never on the host and never with network access or secrets by default. Resource and time limits are enforced per execution.

## Other surfaces

- **Auth** — Supabase Auth; no custom credential handling in application code.
- **Secrets** — API keys (Anthropic, OpenAI, weather/price data providers) stored via environment/secret manager, never committed (`.gitignore` already excludes `.env*`).
- **AI Tutor/Architect** — since these read the learner's full history, access to that data is scoped to the authenticated learner only; no cross-learner data leakage even as the platform potentially scales to more learners later.
- **Content engine** — the living-curriculum pipeline fetches external references (docs, papers); treat all fetched external content as untrusted input, never executed, only parsed for text/metadata.

## Open questions

- Sandbox runtime hardening level appropriate at single-learner scale vs. what's needed if BrainCraft is ever opened to other learners (see [`docs/20-roadmap/overview.md`](../20-roadmap/overview.md) for phase gating).
