# create_db.py
import sqlite3

DB = "users.db"

conn = sqlite3.connect(DB)
cur = conn.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password_hash BLOB NOT NULL
)
""")
conn.commit()
conn.close()
print("users.db créé / table users présente")
