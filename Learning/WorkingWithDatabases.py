import json
import sqlite3
from pathlib import Path

# movies = json.loads(Path("movies.json").read_text())

# print(data)

with sqlite3.connect("db.sqlite3") as conn:
    # command = "INSERT INTO Movies VALUES(?, ?, ?)"
    command = "SELECT * FROM Movies"
    cursor = conn.execute(command)
    # for movie in movies:
    #     conn.execute(command, tuple(movie.values()))

    # for row in cursor:
    #     print(row)

    movies = cursor.fetchall()

    print(movies)
    # conn.commit()