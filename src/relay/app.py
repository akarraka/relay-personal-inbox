"""Minimal local-first Relay capture inbox using only the Python standard library."""

from contextlib import closing
from datetime import date, datetime, timezone
from html import escape
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs
import os
import sqlite3


HOST = "127.0.0.1"
PORT = int(os.environ.get("RELAY_PORT", "8765"))
DB_PATH = Path.home() / "Library" / "Application Support" / "Relay" / "relay.sqlite3"
MAX_NOTE_LENGTH = 5000


def connect_db() -> sqlite3.Connection:
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA foreign_keys = ON")
    connection.execute("""
        CREATE TABLE IF NOT EXISTS user_notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            body TEXT NOT NULL,
            person TEXT NOT NULL DEFAULT '',
            occurred_on TEXT NOT NULL DEFAULT '',
            captured_at TEXT NOT NULL,
            source_type TEXT NOT NULL DEFAULT 'user_note'
        )
    """)
    return connection


def page(notes, message=""):
    cards = []
    for note in notes:
        person = f'<span class="tag">{escape(note["person"])}</span>' if note["person"] else ""
        occurred = f'<span class="tag">Happened {escape(note["occurred_on"])}</span>' if note["occurred_on"] else ""
        stamp = escape(note["captured_at"].replace("T", " ").replace("+00:00", " UTC"))
        cards.append(
            '<article class="note">'
            f'<p class="note-body">{escape(note["body"])}</p>'
            f'<div class="meta">{person}{occurred}<span>Captured {stamp}</span></div>'
            '</article>'
        )
    listing = "".join(cards) or '<p class="empty">Your captured context will appear here.</p>'
    notice = f'<p class="notice" role="status">{escape(message)}</p>' if message else ""
    html = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Relay | Capture inbox</title>
  <style>
    :root {{ color-scheme: light; --ink:#182534; --muted:#607080; --line:#dce4eb; --blue:#24547a; --pale:#f4f7fa; }}
    * {{ box-sizing:border-box; }}
    body {{ margin:0; background:#f7f9fb; color:var(--ink); font:16px/1.5 -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif; }}
    header {{ border-bottom:1px solid var(--line); background:white; }}
    .top {{ max-width:940px; margin:auto; padding:22px 24px; display:flex; align-items:center; gap:12px; }}
    .mark {{ width:38px;height:38px;border-radius:12px;background:var(--blue);color:white;display:grid;place-items:center;font-size:21px;font-weight:700; }}
    h1 {{ margin:0;font-size:23px;letter-spacing:-.02em; }}
    .sub {{ margin:2px 0 0;color:var(--muted);font-size:13px; }}
    main {{ max-width:940px;margin:32px auto;padding:0 24px;display:grid;grid-template-columns:minmax(280px, .92fr) minmax(320px,1.08fr);gap:24px;align-items:start; }}
    section {{ background:white;border:1px solid var(--line);border-radius:14px;padding:22px;box-shadow:0 2px 8px #18253408; }}
    h2 {{ font-size:17px;margin:0 0 5px; }}
    .hint {{ margin:0 0 18px;color:var(--muted);font-size:13px; }}
    label {{ display:block;font-size:13px;font-weight:650;margin:14px 0 6px; }}
    textarea,input {{ display:block;width:100%;border:1px solid #c7d2dc;border-radius:8px;padding:11px 12px;font:inherit;color:var(--ink);background:white; }}
    textarea {{ min-height:150px;resize:vertical; }}
    textarea:focus,input:focus {{ outline:3px solid #24547a25;border-color:var(--blue); }}
    .row {{ display:grid;grid-template-columns:1fr 1fr;gap:12px; }}
    button {{ margin-top:18px;background:var(--blue);color:white;border:0;border-radius:8px;padding:11px 16px;font:inherit;font-weight:650;cursor:pointer; }}
    button:hover {{ background:#183f61; }}
    .notice {{ margin:14px 0 0;color:#17623b;font-size:13px; }}
    .note {{ padding:15px 0;border-top:1px solid var(--line); }}
    .note:first-child {{ border-top:0;padding-top:4px; }}
    .note-body {{ white-space:pre-wrap;overflow-wrap:anywhere;margin:0 0 10px; }}
    .meta {{ display:flex;align-items:center;gap:7px;flex-wrap:wrap;color:var(--muted);font-size:11px; }}
    .tag {{ border:1px solid var(--line);border-radius:99px;padding:2px 8px;background:var(--pale); }}
    .empty {{ color:var(--muted);padding:14px 0; }}
    .foot {{ max-width:940px;margin:0 auto;padding:0 24px 26px;color:var(--muted);font-size:12px; }}
    @media(max-width:700px) {{ main {{ grid-template-columns:1fr;margin-top:18px; }} .top {{ padding:17px 20px; }} }}
  </style>
</head>
<body>
  <header><div class="top"><div class="mark" aria-hidden="true">R</div><div><h1>Relay</h1><p class="sub">Capture context and keep it close to your follow-through</p></div></div></header>
  <main>
    <section aria-labelledby="capture-heading">
      <h2 id="capture-heading">Capture a note</h2>
      <p class="hint">Add something Relay did not observe, such as a meeting, call, promise, or reminder.</p>
      <form method="post" action="/notes">
        <label for="body">What happened or needs follow-up?</label>
        <textarea id="body" name="body" maxlength="{MAX_NOTE_LENGTH}" required placeholder="Met Maya today. I said I would send the revised proposal by Friday."></textarea>
        <div class="row">
          <div><label for="person">Person (optional)</label><input id="person" name="person" maxlength="160" placeholder="Maya"></div>
          <div><label for="occurred_on">When it happened (optional)</label><input id="occurred_on" name="occurred_on" type="date"></div>
        </div>
        <button type="submit">Save note</button>
        {notice}
      </form>
    </section>
    <section aria-labelledby="inbox-heading">
      <h2 id="inbox-heading">Recent captures</h2>
      <p class="hint">These notes are stored on this Mac. They are user-provided source material, not verified messages.</p>
      {listing}
    </section>
  </main>
  <p class="foot">Local preview · No WhatsApp connection or AI analysis is active yet.</p>
</body>
</html>"""
    return html.encode("utf-8")


class RelayHandler(BaseHTTPRequestHandler):
    server_version = "RelayLocal/0.1"

    def send_page(self, message: str = "", status: int = 200) -> None:
        with closing(connect_db()) as db:
            notes = db.execute("SELECT * FROM user_notes ORDER BY id DESC LIMIT 100").fetchall()
        content = page(notes, message)
        self.send_response(status)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(content)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Content-Security-Policy", "default-src 'none'; style-src 'unsafe-inline'; form-action 'self'; base-uri 'none'; frame-ancestors 'none'")
        self.end_headers()
        self.wfile.write(content)

    def do_GET(self) -> None:
        if self.path != "/":
            self.send_error(404)
            return
        self.send_page()

    def do_POST(self) -> None:
        if self.path != "/notes":
            self.send_error(404)
            return
        origin = self.headers.get("Origin")
        if origin and origin != f"http://{HOST}:{PORT}":
            self.send_error(403, "Cross-origin form submission rejected")
            return
        if self.headers.get_content_type() != "application/x-www-form-urlencoded":
            self.send_error(415, "Expected a form submission")
            return
        try:
            length = int(self.headers.get("Content-Length", "0"))
        except ValueError:
            self.send_error(400, "Invalid form length")
            return
        if length <= 0 or length > 12_000:
            self.send_error(413, "Form is empty or too large")
            return
        fields = parse_qs(self.rfile.read(length).decode("utf-8", errors="replace"), keep_blank_values=True)
        body = fields.get("body", [""])[0].strip()
        person = fields.get("person", [""])[0].strip()
        occurred_on = fields.get("occurred_on", [""])[0].strip()
        if not body or len(body) > MAX_NOTE_LENGTH or len(person) > 160:
            self.send_page("Please enter a note of up to 5,000 characters and a person name of up to 160 characters.", 400)
            return
        if occurred_on:
            try:
                date.fromisoformat(occurred_on)
            except ValueError:
                self.send_page("Please use a valid date.", 400)
                return
        captured_at = datetime.now(timezone.utc).isoformat(timespec="seconds")
        with closing(connect_db()) as db:
            with db:
                db.execute(
                    "INSERT INTO user_notes(body, person, occurred_on, captured_at) VALUES (?, ?, ?, ?)",
                    (body, person, occurred_on, captured_at),
                )
        self.send_response(303)
        self.send_header("Location", "/")
        self.send_header("Content-Length", "0")
        self.end_headers()

    def log_message(self, format: str, *args: object) -> None:
        # Avoid writing note text or request payloads into logs.
        print(f"Relay local server: {self.address_string()} - {format % args}")


def main() -> None:
    connect_db().close()
    server = ThreadingHTTPServer((HOST, PORT), RelayHandler)
    print(f"Relay is available at http://{HOST}:{PORT}")
    print(f"Local notes database: {DB_PATH}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping Relay.")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
