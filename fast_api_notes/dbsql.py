import sqlite3

abc = sqlite3.connect("vipin.db")
cur = abc.cursor()

cur.execute("CREATE TABLE movie(title, year, score)")

cur.execute("""
    INSERT INTO movie VALUES
        ('Monty Python and the Holy Grail', 1975, 8.2),
        ('And Now for Something Completely Different', 1971, 7.5)
""")

abc.commit()
