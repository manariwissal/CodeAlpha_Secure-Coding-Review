# app_fixed.py
import sqlite3
import bcrypt
from typing import Optional, Dict

DB_PATH = "users.db"

def get_user_by_username(username: str) -> Optional[sqlite3.Row]:
    with sqlite3.connect(DB_PATH) as conn:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT id, username, password_hash FROM users WHERE username = ?", (username,))
        return cur.fetchone()

def login(username: str, password_plaintext: str) -> Optional[Dict]:
    row = get_user_by_username(username)
    if row is None:
        return None
    stored_hash = row["password_hash"]
    if isinstance(stored_hash, str):
        stored_hash = stored_hash.encode('utf-8')
    if bcrypt.checkpw(password_plaintext.encode('utf-8'), stored_hash):
        return {"id": row["id"], "username": row["username"]}
    return None

def create_user(username: str, password_plaintext: str) -> None:
    pwd_hash = bcrypt.hashpw(password_plaintext.encode('utf-8'), bcrypt.gensalt())
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO users(username, password_hash) VALUES (?, ?)", (username, pwd_hash))
        conn.commit()
