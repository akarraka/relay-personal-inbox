# Relay progress log

## 2026-10-30 — Product definition and project workflow

- Created the combined PRD and technical architecture document.
- Captured the agreed vision, MVP boundary, one-account WhatsApp start, direct user capture, autonomy policy, relationship memory, architecture, roadmap, and WhatsApp validation gate.
- No source code existed at the start of the work; the initial local capture slice was added later in this session.
- Added project working rules, project roadmap, durable decision record, and session handoff format.
- Inspected current official WhatsApp Business Platform terms: the platform is framed for business/commercial use and excludes personal use. This may conflict with Relay's personal-inbox purpose; documented as D-010 instead of assuming the API is suitable.
- User clarified the secondary number is on the WhatsApp Business app but carries personal messages, with no operating business. Current Business App terms also restrict personal use. WhatsApp's third-party agents cannot access other chats; they handle messages shared with the agent. Recorded as D-011 and D-012.
- The workspace contained the PRD authoring script and project documents but no application source code before the local capture slice was added.
- Created an initial local capture page and SQLite note store in `src/relay/app.py`. It binds to localhost, separates user-entered notes from channel messages, and does not use AI or connect to WhatsApp.
- Added `docs/LOCAL_PREVIEW.md` with startup instructions. The app has not been run or tested in this session.
- Next: inspect/run the local preview and refine capture/action flow. Keep automatic WhatsApp ingestion out of the first code milestone unless an officially supported whole-inbox route for this personal use is found or the product purpose changes.

## 2026-10-30 — Project location

- Moved the project files from the temporary Codex workspace into `/Users/ananddubey/LocalRepos/Relay`, matching the user's existing local-project folder convention.
- Initialized a local Git repository on `main`; it has no GitHub remote and no initial commit yet.
- Added `.gitignore` rules for Python cache files, local configuration secrets, virtual environments, and SQLite runtime files.
- Recorded a proposed data boundary: private GitHub for source and generic docs, Mac mini only for personal messages, notes, relationships, attachments, credentials, logs, and backups. Hosting change awaits the user's decision.


## 2026-10-30 — Repository location and hosting

- User authorized moving Relay into the GitHub-synced `~/Repos` folder and creating a private GitHub repository.
- Copied the project, including its local Git repository, to `/Users/ananddubey/Repos/Relay`; the original folder remains in `~/LocalRepos/Relay` because the cross-folder move was blocked by filesystem permissions.
- Updated the project documents to reflect the accepted data boundary and hosting decision.
- The user created `https://github.com/akarraka/relay-personal-inbox` and supplied the URL. An authenticated `git ls-remote` check succeeded with no refs, confirming the remote is empty and ready for the initial push. The GitHub connector lists no repositories, so the supplied URL was used directly.
- Next: create the initial commit and push `main`. No real message data or credentials are included in this project copy.
