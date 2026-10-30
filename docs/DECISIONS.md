# Relay decision record

Durable decisions are listed newest first. Revisit a decision by adding a new entry; do not erase the history.

| ID | Date | Decision | Reason / boundary | Status |
|---|---|---|---|---|
| D-013 | 2026-10-30 | Host source and generic project documents in a private GitHub repository; keep personal message data, notes, attachments, logs, backups, and credentials on the Mac mini. | User authorized this hosting choice and the move to `~/Repos/Relay`; runtime data remains outside the repository. | Accepted |
| D-012 | 2026-10-30 | Do not treat WhatsApp third-party agents as a whole-inbox integration. | WhatsApp says connected agents can read what the user shares with them and cannot access other chats; availability is limited. Source: [WhatsApp Help Center](https://faq.whatsapp.com/1050934623978152). | Accepted |
| D-011 | 2026-10-30 | The pilot number is on the WhatsApp Business app but is used for personal communications, not an operating business. | User clarification. This makes Business Platform suitability a product/platform mismatch to resolve, not an account setup detail. | Accepted |
| D-010 | 2026-10-30 | Do not assume official WhatsApp Business Platform access is appropriate for Relay's personal-use case. | Current Platform terms say it is for business/commercial use and not personal use. Current Business App terms also restrict personal, family, or household use. Sources: [Platform terms](https://www.whatsapp.com/legal/WhatsApp-Terms-for-WhatsApp-Business-Platform) and [Business App terms](https://www.whatsapp.com/legal/WhatsApp-Terms-for-WhatsApp-Business-App). | Gate |
| D-009 | 2026-10-30 | Use Relay as a provisional working name. | Suggested in conversation; user has not explicitly confirmed it as the final name. | Provisional |
| D-008 | 2026-10-30 | Instinct is not required for the core product. | The system should own communication triage and action follow-through; integrations can be considered later if they solve a concrete problem. | Accepted |
| D-007 | 2026-10-30 | Use a modular monolith, SQLite initially, adapters, deterministic policy/execution, and LLMs for semantic tasks. | Keeps the MVP operable on a Mac mini and avoids premature microservices. | Accepted |
| D-006 | 2026-10-30 | Store long-term relationship context with evidence and distinguish confirmed facts from inferred candidates. | Context should be useful and correctable, not an untraceable model assertion. | Accepted |
| D-005 | 2026-10-30 | Start with approval required for every external effect; make autonomy configurable by category and sensitivity for later use. | User wants control initially and flexibility to delegate once confidence is earned. | Accepted |
| D-004 | 2026-10-30 | Direct text capture for events outside observed channels is part of the initial scope. | Meetings and calls may create context or commitments the system cannot hear. | Accepted |
| D-003 | 2026-10-30 | Begin with one operational WhatsApp account; design the data model for future accounts and channels. | WhatsApp dominates current communication; expansion follows demonstrated value. | Accepted |
| D-002 | 2026-10-30 | Define the product as a universal personal inbox with communication capabilities. | Broader product direction, staged delivery. | Accepted |
| D-010 | 2026-10-30 | Treat official WhatsApp Business Platform access as unresolved for Relay's personal-use case. | Current official terms describe the service as business/commercial and exclude personal use. Confirm account type and intended use before selecting this connector. Source: [official terms](https://www.whatsapp.com/legal/WhatsApp-Terms-for-WhatsApp-Business-Platform). | Gate |
| D-001 | 2026-10-30 | Validate WhatsApp integration capabilities and platform constraints before promising or implementing them. | The available capabilities depend on account/product eligibility and must not be assumed. | Gate |
