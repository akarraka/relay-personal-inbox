# Relay

**Working name:** Relay (provisional)

**Workspace:** `~/Repos/Relay` (private GitHub repository: [akarraka/relay-personal-inbox](https://github.com/akarraka/relay-personal-inbox))

**Recommended storage split:** private GitHub for source and generic docs; personal inbox data and credentials stay on the Mac mini. See [data boundaries](docs/DATA_BOUNDARIES.md). Source and generic project documents are hosted in the private repository. Runtime data and credentials remain local.

Relay is a personal inbox and action assistant. It brings messages and user-entered context into one place, helps identify what matters and what needs follow-through, and keeps the user in control of external actions.

## Current status

The product requirements and initial architecture are documented, and a preliminary local note-capture page exists in `src/relay/app.py`. It has not yet been run or reviewed. WhatsApp automatic ingestion is gated: the intended number is used for personal messages, and no supported whole-inbox route has been established for that purpose.

## Product boundaries

- MVP: one operational WhatsApp account plus direct text capture from day one.
- Future channels: email, SMS, Telegram, and other sources use adapters over a shared message and action model.
- Initial external-action policy: prepare drafts and ask for approval before every external effect.
- Relationship memory must retain evidence and distinguish confirmed facts from inferred candidates.
- Core triage and follow-through do not depend on Instinct.
- Recommended implementation: a modular monolith, SQLite initially, deterministic policy and execution, and LLMs for semantic work.

## Project documents

- [PRD and technical architecture](outputs/universal_personal_inbox_prd_architecture.docx)
- [Project plan and next step](docs/PROJECT_PLAN.md)
- [Run the local capture preview](docs/LOCAL_PREVIEW.md)
- [Working rules](docs/WORKING_RULES.md)
- [Data boundaries](docs/DATA_BOUNDARIES.md)
- [Decision record](docs/DECISIONS.md)
- [Progress log](docs/PROGRESS_LOG.md)
- [Next-session handoff](docs/SESSION_HANDOFF.md)

## Where to begin

Read `docs/SESSION_HANDOFF.md`, then follow `docs/LOCAL_PREVIEW.md` to open the capture page. The next build milestone is evidence-linked action tracking. Revisit WhatsApp only if a supported whole-inbox route for personal use is identified or the product purpose changes.
