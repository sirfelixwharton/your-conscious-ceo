import sqlite3

def create_connection():
    conn = sqlite3.connect("your_conscious_ceo.db")
    return conn

def create_tables():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS answers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id TEXT,
        question TEXT,
        answer TEXT
    )
    """)

    conn.commit()
    conn.close()

def save_answers(user_id, answers):
    conn = create_connection()
    cursor = conn.cursor()

    for item in answers:
        cursor.execute(
            "INSERT INTO answers (user_id, question, answer) VALUES (?, ?, ?)",
            (user_id, item['question'], item['answer'])
        )

    conn.commit()
    conn.close()

