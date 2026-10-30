# Relay local preview

This first application slice lets you capture context from meetings, calls, and other events the system did not observe. Notes are saved in SQLite on this Mac and shown in a recent-captures list. It does not connect to WhatsApp, call an AI model, or send messages.

## Start it

1. Open Terminal.
2. Change into the Relay project folder.
3. Run `python3 src/relay/app.py`.
4. Open `http://127.0.0.1:8765` in a browser.
5. To stop it, return to Terminal and press Control-C.

The application stores notes at `~/Library/Application Support/Relay/relay.sqlite3`. The server listens only on this Mac (`127.0.0.1`). Do not put sensitive production data into this early preview; it has not yet had a privacy, backup, or security review.

If port 8765 is already in use, start with `RELAY_PORT=8766 python3 src/relay/app.py` and open `http://127.0.0.1:8766`.
