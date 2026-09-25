import json
from pathlib import Path

# movies = [{"id":0, "title":"JungleBook", "year":1993},
#           {"id":1, "title":"Iron Man 3", "year":2018},
#           {"id":2, "title":"Animal", "year":2023}


#           ]

# data = json.dumps(movies)

# print(data)

# Path("movies.json").write_text(data)

data = Path("movies.json").read_text()

movies = json.loads(data)

print(movies)