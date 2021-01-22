# testsqlite

import sqlite3


conn = sqlite3.connect('vocab.db')
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS vocab (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        vocab text,
        meaning text,
        score int)""")

def insert_vocab(vocab,meaning):
    ID = None
    score = 0
    with conn:
        c.execute("""INSERT INTO vocab VALUES (?,?,?,?)""",
                    (ID,vocab,meaning,score))
    conn.commit()
    print('Data was inserted')

# insert_vocab('cat','แมว')

def view_vocab():
    with conn:
        c.execute("SELECT * FROM vocab")
        vocab = c.fetchall()
        print(vocab)

    return vocab

