# Relay working rules

These rules keep the work understandable, reviewable, and economical across sessions. The user is new to building software with ChatGPT, so explain decisions in plain language and define unfamiliar terms when they first matter.

## 1. Work in small, named steps

Every unit of work has a step ID from `PROJECT_PLAN.md`, a clear outcome, and a visible completion condition. Work on one primary step at a time. If a new discovery changes scope, record it and update the plan before expanding the implementation.

## 2. Start each session with a short orientation

At the beginning of a session:

1. Read `SESSION_HANDOFF.md` and the current step in `PROJECT_PLAN.md`.
2. Check the relevant source files and project documents instead of asking the user to repeat known context.
3. State the goal, the expected result, and any decision that genuinely blocks progress.
4. Continue with independent work while waiting for optional clarification.

## 3. Keep decisions visible

- Put durable product, architecture, security, and integration choices in `DECISIONS.md` with a date and a short reason.
- Put completed work, meaningful discoveries, and open issues in `PROGRESS_LOG.md`.
- Update `PROJECT_PLAN.md` when a step changes state, scope, sequence, or exit criteria.
- Update `SESSION_HANDOFF.md` at the end of every work session, even if the step is not complete.
- Update the PRD only when requirements or product boundaries change; do not duplicate the entire PRD in status notes.

## 4. Explain before changing foundations

Before introducing a framework, service, database migration, new channel, model provider, or account permission, describe the choice briefly: what it does, why it is needed now, and the practical alternative. Prefer the simplest design that meets the current step.

## 5. Keep token use proportional to the task

- Read only the files and history needed for the current step; search before opening large trees.
- Prefer focused changes and concise progress updates. Avoid re-summarizing settled decisions.
- Use primary/official sources for current platform capabilities and cite the specific facts that affect a decision.
- Ask one bundled question only when a user choice blocks meaningful progress. Use a reversible default for routine choices and record it.
- Do not explore future channels, tools, or optimizations until the current milestone needs them.
- Keep session handoffs compact: current state, decisions, next action, and any blocker.

## 6. Make changes reviewable

- Before implementation, define the observable behavior and acceptance criteria for the step.
- Keep configuration, secrets, and personal data out of source control and logs.
- Make changes in small coherent batches; summarize files changed and behavior affected.
- Do not silently broaden scope or perform external communication/actions. External effects remain approval-gated under the product policy.
- Verification is scoped to the requested step and stated clearly; distinguish what was inspected from what was actually run.

## 7. End every session with a handoff

Before ending:

1. Update the status and exit criteria in `PROJECT_PLAN.md`.
2. Add a dated entry to `PROGRESS_LOG.md`.
3. Record new durable choices in `DECISIONS.md`.
4. Replace `SESSION_HANDOFF.md` with a short, ready-to-paste next-session brief.
5. Tell the user in plain language what changed, what remains, and the next step.

## Session handoff format

Use this structure in `SESSION_HANDOFF.md`:

```text
Project: Relay
Current step: [ID and name]
Status: [not started / in progress / blocked / complete]
Completed: [brief facts]
Decisions: [decision IDs or “none”]
Open question/blocker: [only if it blocks work]
Next action: [one concrete action]
Acceptance check: [observable result]
Relevant files: [small list]
```
