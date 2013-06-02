import sys

from movies.finder import CSVMovieFinder
from movies.lister import MovieLister

app = MovieLister(CSVMovieFinder("movies.csv"))
for movie in app.movies_directed_by("Sergio Leone"):
    sys.stdout.write("%s\n" % movie.title)

