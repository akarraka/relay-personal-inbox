# Relay data boundaries

## Recommendation

Keep the application source code and generic project documentation in a private GitHub repository under `~/Repos/Relay`. Keep all live personal information on the Mac mini. Private GitHub source control provides a remote copy of the code and a useful history of changes without making GitHub the inbox database.

This is a proposed hosting decision, not yet applied. The current working copy remains in `~/LocalRepos/Relay`, with a local Git repository and no remote.

## Keep in the private source repository

- Application source code, generic schemas, migration files, and configuration examples with placeholder values.
- PRD, architecture, project plan, decision record, and other non-personal project notes.
- Documentation and synthetic sample data that contains no real conversation details.

## Keep on the Mac mini only

- WhatsApp messages, user-entered meeting/call notes, contact identifiers, relationship memory, and action history.
- Attachments, exports, logs containing message content, database files, and database backups.
- API credentials, session tokens, and encryption keys. Store credentials in macOS Keychain; do not commit them.

The current prototype stores its SQLite database outside the repository at `~/Library/Application Support/Relay/relay.sqlite3`. The repository `.gitignore` also excludes common local database, data, backup, attachment, log, and secret files as a second line of defense.

## Important limit

A private GitHub repository is access-controlled, not a vault for live personal records. GitHub says private repositories are accessible to the owner and anyone explicitly granted access, and its service terms describe limited circumstances where personnel may access content (for example, security or support). Do not put live messages, exports, credentials, or real personal notes in Git history. Review enabled integrations and automated workflows before giving repository access to any third party.

If an LLM is added later, treat text sent to a hosted model as leaving the Mac. The model provider and retention settings must be selected deliberately, and the application should send only the minimum context needed for each task.
