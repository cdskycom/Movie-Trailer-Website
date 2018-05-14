import media
import fresh_tomatoes
import shelve
import sys


# A file database for movie data persistence
MOVIE_DATABASE = "movie_data"


# Use six movies to init movie trailer database
def init_movie():
    blade_runner = media.Movie("Blade Runner",
                               "blade runner pursue and try to terminate" +
                               " replicants",
                               "https://img1.doubanio.com/view/photo/" +
                               "s_ratio_poster/public/p2501864539.webp",
                               "http://vt1.doubanio.com/201805110033/" +
                               "b201987e0147bac60b14e0aa6d405989/view/movie/" +
                               "M/302200566.mp4")

    coco = media.Movie("Coco",
                       "A 12-year-old boy transported to the land of the" +
                       " dead accidentally",
                       "https://img1.doubanio.com/view/photo/s_ratio_poster/" +
                       "public/p2503997609.webp",
                       "http://vt1.doubanio.com/201805110038/" +
                       "c179249bd768e13e18887f2fb48afcfc/view/movie/M/" +
                       "302170862.mp4")

    annihilation = media.Movie("Annihilation",
                               "A sifi movie about future",
                               "https://img1.doubanio.com/view/photo/m/" +
                               "public/p2516914607.webp",
                               "http://vt1.doubanio.com/201805102321/" +
                               "8e953617965932411d9c5af7bcdce55a/view/movie/" +
                               "M/402290589.mp4")

    black_panther = media.Movie("Black Panther",
                                "A story of a superman",
                                "https://img3.doubanio.com/view/photo/" +
                                "s_ratio_poster/public/p2512123434.webp",
                                "http://vt1.doubanio.com/201805102321/" +
                                "05955405f5410512443c060e01f4320c/view/" +
                                "movie/M/302260827.mp4")

    pacific_rim = media.Movie("Pacific Rim",
                              "Giant machine fight with Giant machine",
                              "https://img3.doubanio.com/view/photo/" +
                              "s_ratio_poster/public/p2512933684.webp",
                              "http://vt1.doubanio.com/201805102322/" +
                              "f69884fea227df41e39e8a4f806c6539/view/" +
                              "movie/M/302280429.mp4")

    wonder = media.Movie("Wonder",
                         "A ugly boy's school life",
                         "https://img1.doubanio.com/view/photo/" +
                         "s_ratio_poster/public/p2507709428.webp",
                         "http://vt1.doubanio.com/201805102322/" +
                         "1388b3ca402a08bc116bbeca08a42542/view/movie/" +
                         "M/302250963.mp4")

    with shelve.open(MOVIE_DATABASE) as db:
        db['Blade_Runner'] = blade_runner
        db['Coco'] = coco
        db['Annihilation'] = annihilation
        db['Black_Panther'] = black_panther
        db['Pacific_Rim'] = pacific_rim
        db['Wonder'] = wonder
    show_movie_trailer()


# Read all of movies from database and show movies list in a web page
def show_movie_trailer():
    movies = []
    with shelve.open(MOVIE_DATABASE) as db:
        for title in db.keys():
            movies.append(db[title])

    fresh_tomatoes.open_movies_page(movies)


# Accept movie's data from user, insert into movie database.
# movie title as key
def add_movie():
    movie_title = input("Movie_Title:")
    if not movie_title or movie_title.strip() == '':
        print("movie_title can not be empty")
        return

    storyline = input("Storyline:")
    if not storyline or storyline.strip() == '':
        print("storyline can not be empty")
        return

    poster_url = input("Poster_URL:")
    if not poster_url or poster_url.strip() == '':
        print("movie_title can not be empty")
        return

    trailer_url = input("Trailer_URL(pls input the online trailer's url):")
    if not trailer_url or trailer_url.strip() == '':
        print("movie_title can not be empty")
        return

    with shelve.open(MOVIE_DATABASE) as db:
        db[movie_title] = media.Movie(movie_title.strip(), storyline.strip(),
                                      poster_url.strip(), trailer_url.strip())


# delete movie from database
# title - a movie title and is the db's key of the movie
def del_movie(title):
    try:
        with shelve.open(MOVIE_DATABASE) as db:
            del db[title]
    except KeyError:
        print("There is no %s" % title)


if __name__ == "__main__":
    try:
        parameter = sys.argv[1]
        if parameter == "--list":
            show_movie_trailer()
        elif parameter == "--del":
            title = sys.argv[2]
            del_movie(title)
        elif parameter == "--add":
            add_movie()
        elif parameter == "--init":
            init_movie()
        else:
            print("Command line error: please input 'python xx.py --list' to" +
                  " list movies.+nThis program support" +
                  " --init |--list | --del xxx | --add ")
    except:
        print("Command line error: please input 'python xx.py --list' to" +
              " list movies.+nThis program support" +
              " --init |--list | --del xxx | --add ")
