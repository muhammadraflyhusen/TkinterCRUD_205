import sqlite3
con = sqlite3.connect("tutorial.db")
cur = con.cursor ()

_tittle=input("Masukkan Judul Movie : ")
_year=input("Masukkan Tahun Movie : ")
_rating=input("Masukkan Rating Movie : ")
#cur.execute("CREATE TABLE movie
#           (title text, year int, score double)""")
cur.execute ('create table if not exists movie (title text, year int, rating double)')
con.commit()
cur.execute("""
    INSERT INTO movie(title, year, rating) VALUES
    ('{}', {}, {})
""".format(_tittle, _year, _rating))
con.commit()