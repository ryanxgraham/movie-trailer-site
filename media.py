"""Contains definition for the Movie class used in entertainment_center.py."""

import webbrowser

class Movie(object):
    """
    Parent class of Movie objects.

    Requires: Movie title, release date, a brief summary, a URL for a poster,
    and a URL for a youtube trailer.
    """

    def __init__(self, movie_title, release_date, movie_storyline, poster_image,
    trailer_youtube):
        """Initialize Movie Class."""
        self.title = movie_title
        self.release_date = release_date
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """Open a movie trailer."""
        webbrowser.open(self.trailer_youtube_url)
