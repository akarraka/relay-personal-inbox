# Relay project plan

## Roadmap at a glance

| Step | Name | Outcome | Status |
|---|---|---|---|
| 0 | Product definition | Agree on purpose, first release boundary, and architecture direction. | Complete; PRD created |
| 1 | WhatsApp feasibility | Determine whether an officially supported route fits the intended account and personal-inbox use. | Deferred — current official routes reviewed do not provide a suitable whole-inbox path |
| 2 | Application foundation | Create the smallest runnable local application, configuration, SQLite schema, migrations, and local capture flow. | Initial capture slice prepared; project copied to `~/Repos/Relay`; private GitHub remote connected |
| 3 | Inbox and action workflow | Review captured items, link people/conversations, and manage evidence-backed actions. | Not started |
| 4 | WhatsApp inbound pilot | Add one adapter only after Step 1 confirms a viable route; show health, coverage, and recovery. | Not started |
| 5 | Semantic assistance | Add summaries, triage, and candidate action/memory extraction with evidence and human correction. | Not started |
| 6 | Drafts and approval | Prepare replies and implement deterministic, payload-bound approval before any supported send. | Not started |
| 7 | Pilot hardening | Backups, restore rehearsal, privacy controls, observability, recovery, and a measured personal pilot. | Not started |
| 8 | Expand carefully | Add another channel or narrow delegated autonomy only when the pilot demonstrates value. | Future |

## Step 0 completion record

The product is a universal personal inbox with communication capabilities. WhatsApp is the first source, but the architecture is channel-neutral. MVP includes one operational WhatsApp account and direct text-based capture from day one. The initial policy requires approval for all external effects. Long-term relationship context is evidence-based. Instinct is not a core dependency. The recommended architecture is a modular monolith with SQLite initially, channel adapters, deterministic policy/execution, and LLMs for semantic tasks.

See the [PRD and technical architecture](../outputs/universal_personal_inbox_prd_architecture.docx) for the detailed requirements and design.

The current recommendation is private GitHub for source and generic documents, with personal inbox data and credentials stored only on the Mac mini. See [data boundaries](DATA_BOUNDARIES.md). The user chose `~/Repos` and authorized a private GitHub repository. Project files are hosted in the private remote.

## Step 1 WhatsApp feasibility gate

### Goal

Make an evidence-based decision about whether any current official WhatsApp integration route fits this personal-use case. Local application development can continue separately.

### Work sequence

1. Confirm the account and use case. User confirmed the secondary number uses WhatsApp Business app but carries personal messages; there is no operating business.
2. Check current official documentation. Verified so far: current WhatsApp Business Platform and Business App terms are business-purpose-limited; WhatsApp's third-party-agent feature only handles messages the user shares with the agent and cannot access other chats.
3. Do not build a whole-inbox adapter on these routes for this personal-use case. Continue only if an officially supported method with suitable permissions and semantics is found, or if the product purpose changes.
4. Keep moving with local capture and action management, clearly labeled as user-assisted input while WhatsApp integration remains unresolved.
5. Revisit the gate if Meta publishes a supported route that fits the use case or if Relay's purpose changes.

### Current finding (30 October 2026)

The user confirmed that the pilot number is on the WhatsApp Business app but is used for personal communications, not an operating business. Current official WhatsApp Business Platform terms say the platform is solely for business or commercial use and not personal use. Current WhatsApp Business App terms also say Business App Services must not be used for personal, family, or household purposes. This is a product/platform compatibility gate based on published terms. Sources: [WhatsApp Business Platform terms](https://www.whatsapp.com/legal/WhatsApp-Terms-for-WhatsApp-Business-Platform) and [WhatsApp Business App terms](https://www.whatsapp.com/legal/WhatsApp-Terms-for-WhatsApp-Business-App).

WhatsApp's current [third-party-agent Help Center](https://faq.whatsapp.com/1050934623978152) says connected agents can read what the user shares in the agent chat but cannot be added to or access the user's other chats; availability is limited by region. This does not solve full personal-inbox ingestion.

This does not change the source-neutral product core. Local text capture, people, evidence, actions, and review workflows can be built now. Until a supported whole-inbox integration exists for this use case, the honest interim path is user-assisted capture (paste or type context) and no claim of automatic WhatsApp coverage. Do not rely on an unofficial bridge for the MVP without a separate, informed decision.

### Deliverables

- A short integration capability matrix with official source links and tested/unverified labels.
- A repository/runtime recommendation based on actual workspace inspection.
- A recorded go/no-go and the next implementation step.

### Exit criteria

- The pilot account and its personal purpose are documented.
- Message history, inbound coverage, and send capability are described only to the extent supported by current evidence.
- The product distinguishes user-assisted WhatsApp capture from automatic account ingestion.
- No channel-specific implementation choice is hidden inside generic architecture code.

## Definition of done for each step

A step is complete when its stated outcome is observable, its acceptance criteria have been reviewed, relevant project documents are updated, known limitations are recorded, and the next step is named. Completion does not mean every future capability is built.
