# app_secure.py - exemple sécurisé
import sqlite3
import bcrypt  # pip install bcrypt

def get_user_hashed_password(username):
    conn = sqlite3.connect("users.db")
    cur = conn.cursor()
    # Requête paramétrée : pas de concaténation
    cur.execute("SELECT password_hash FROM users WHERE username = ?", (username,))
    row = cur.fetchone()
    conn.close()
    return row[0] if row else None

def check_login(username, password_plaintext):
    stored_hash = get_user_hashed_password(username)
    if not stored_hash:
        return False
    # bcrypt attend des bytes
    return bcrypt.checkpw(password_plaintext.encode('utf-8'), stored_hash)

# Exemple pour créer un utilisateur (ne l'exécute qu'une seule fois)
def create_user(username, password_plaintext):
    pwd_hash = bcrypt.hashpw(password_plaintext.encode('utf-8'), bcrypt.gensalt())
    conn = sqlite3.connect("users.db")
    cur = conn.cursor()
    # Requête paramétrée pour insertion
    cur.execute("INSERT INTO users(username, password_hash) VALUES (?, ?)", (username, pwd_hash))
    conn.commit()
    conn.close()
