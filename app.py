import sqlite3

def login(user, password):
    conn = sqlite3.connect("users.db")
    query = f"SELECT * FROM users WHERE user='{user}' AND password='{password}'"
    conn.execute(query)
