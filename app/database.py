import sqlite3

DATABASE = 'people.db'

def init_db():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS people
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT,
                  height REAL,
                  weight REAL)''')
    conn.commit()
    conn.close()

def add_person(name, height, weight):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("INSERT INTO people (name, height, weight) VALUES (?, ?, ?)",
              (name, height, weight))
    conn.commit()
    conn.close()

def get_all_data():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("SELECT height, weight FROM people")
    data = c.fetchall()
    conn.close()
    return data

# 新しく追加する関数
def add_sample_data():
    sample_data = [
        ("田中太郎", 170.5, 65.0),
        ("佐藤花子", 158.0, 50.5),
        ("鈴木一郎", 180.0, 75.5),
        ("山田美咲", 165.5, 55.0)
    ]
    
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    
    # テーブルが空の場合のみサンプルデータを追加
    c.execute("SELECT COUNT(*) FROM people")
    if c.fetchone()[0] == 0:
        c.executemany("INSERT INTO people (name, height, weight) VALUES (?, ?, ?)", sample_data)
        conn.commit()
    
    conn.close()

def reset_database():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("DELETE FROM people")
    conn.commit()
    conn.close()
    add_sample_data()
