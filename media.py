import webbrowser


class Movie():
    '''Store your favorite movie, include many information like
     title, storyline, poster url and trailer url

    Note:
    Do not include the `self` parameter in the ``Args`` section.

    Args:
    movie_title (str): movie's title.
    movie_storyline (str): movie's storyline .
    poster_image (str): poster image url of the movie
    trailer_youtube (str): trailer video's url

    Attributes:
    movie_title (str): movie's title.
    movie_storyline (str): movie's storyline .
    poster_image (str): poster image url of the movie
    trailer_youtube (str): trailer video's url

    Methods:
    show_trailer (): open a browser window and play trailer video.
    '''
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
