class MediaItem():
    def __init__ (self, title, year, genres):
        self.title = title
        self.year = year
        self.genres = genres
    

class Book(MediaItem):
    def __init__ (self, title, author, year, language):
        super().__init__(title, year)
        self.author = author
        self.language = language
        self.format = "book"

class Record(MediaItem):
    def__init__(self, title, artist, label, year, tracklist=[]):
        super().__init__(title, year, genres)
        self.artist = artist
        self.label = label
        self.tracklist = tracklist

