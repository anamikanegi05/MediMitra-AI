import sqlite3

def init_db():
    conn = sqlite3.connect("chat.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS chats (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_input TEXT,
        response TEXT
    )
    """)

    conn.commit()
    conn.close()


def save_chat(user_input, response):
    conn = sqlite3.connect("chat.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO chats (user_input, response) VALUES (?, ?)", (user_input, response))

    conn.commit()
    conn.close()


def get_chats():
    conn = sqlite3.connect("chat.db")
    cursor = conn.cursor()

    cursor.execute("SELECT user_input, response FROM chats ORDER BY id DESC")
    data = cursor.fetchall()

    conn.close()
    return data
