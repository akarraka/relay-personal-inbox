Project: Relay (provisional working name)
Workspace: /Users/ananddubey/Repos/Relay (private GitHub repository: https://github.com/akarraka/relay-personal-inbox)
Current step: 2 — Application foundation
Status: Local capture prototype prepared; project copy at `~/Repos/Relay` is committed and synced to private GitHub `main`
Completed: User confirmed the secondary number uses WhatsApp Business app but carries personal messages; there is no operating business. Current platform/business-app terms are business-purpose-limited, and third-party agents cannot access other chats. No supported whole-inbox route is established for Relay's personal-use goal. A local web capture page with SQLite storage is in `src/relay/app.py`; startup instructions are in `docs/LOCAL_PREVIEW.md`.
Decisions: D-001 through D-008 accepted or gated; D-009 name is provisional; D-010 is a platform-purpose gate; D-011 and D-012 record the account context and third-party-agent limits.
Open question/blocker: None for local capture/action work. Automatic WhatsApp ingestion remains unresolved and should not be assumed.
Next action: Review the local capture preview and continue with evidence-linked action tracking. Keep all real communication data, credentials, attachments, and backups local on the Mac mini.
Acceptance check: User can save a person/date-linked note and see it in the local capture list; automatic WhatsApp ingestion stays gated until validated.
Relevant files: README.md; src/relay/app.py; docs/LOCAL_PREVIEW.md; docs/DATA_BOUNDARIES.md; docs/PROJECT_PLAN.md; docs/WORKING_RULES.md; docs/DECISIONS.md; docs/PROGRESS_LOG.md; outputs/universal_personal_inbox_prd_architecture.docx
