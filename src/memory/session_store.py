import sqlite3
import json
import uuid
from datetime import datetime
from dataclasses import asdict
from src.state import ResearchState

DB_PATH = "sessions.db"


def init_db():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS sessions (
            id TEXT PRIMARY KEY,
            query TEXT NOT NULL,
            status TEXT NOT NULL,
            state_json TEXT NOT NULL,
            created_at TEXT NOT NULL,
            updated_at TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()


def create_session(query: str) -> str:
    session_id = str(uuid.uuid4())
    state = ResearchState(query=query)
    now = datetime.utcnow().isoformat()

    conn = sqlite3.connect(DB_PATH)
    conn.execute(
        "INSERT INTO sessions (id, query, status, state_json, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?)",
        (session_id, query, "pending", json.dumps(asdict(state)), now, now)
    )
    conn.commit()
    conn.close()
    return session_id


def update_session(session_id: str, state: ResearchState, status: str = "running"):
    now = datetime.utcnow().isoformat()
    conn = sqlite3.connect(DB_PATH)
    conn.execute(
        "UPDATE sessions SET state_json = ?, status = ?, updated_at = ? WHERE id = ?",
        (json.dumps(asdict(state)), status, now, session_id)
    )
    conn.commit()
    conn.close()


def get_session(session_id: str):
    conn = sqlite3.connect(DB_PATH)
    row = conn.execute(
        "SELECT id, query, status, state_json, created_at, updated_at FROM sessions WHERE id = ?",
        (session_id,)
    ).fetchone()
    conn.close()

    if row is None:
        return None

    return {
        "id": row[0],
        "query": row[1],
        "status": row[2],
        "state": json.loads(row[3]),
        "created_at": row[4],
        "updated_at": row[5],
    }