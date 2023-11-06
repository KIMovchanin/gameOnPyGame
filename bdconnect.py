import sqlite3

top = []


def addindb(name=str, seconds=int, score=int):
    with sqlite3.connect("scores.db") as con:
        cur = con.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS scores (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT DEFAULT JOHN_DOE,
        time INTEGER DEFAULT 0,
        score INTEGER DEFAULT 0
        )""")

        # print(name)

        cur.execute(f"INSERT OR IGNORE INTO scores (name, time, score) VALUES (?, ?, ?)",
                    (name, seconds, score))
        names = []

        for el in cur.execute("SELECT name, score FROM scores"):
            names.append(el)

        names.sort(key=lambda k: k[1], reverse=True)

        for index, i in enumerate(names):
            top.append(list(names[index]))
            print(index + 1, ' ', names[index])
