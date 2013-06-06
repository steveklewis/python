from aglyph.binder import Binder

from movies.lister import MovieLister
from movies.finder import MovieFinder, CSVMovieFinder

class MoviesBinder(Binder):
    def __init__(self):
        super(MoviesBinder, self).__init__("movies-binder")
        self.bind(MovieLister).init(MovieFinder)
        self.bind(MovieFinder, to=CSVMovieFinder, strategy="singleton").init("movies.csv")
