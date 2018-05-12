# Movie-Trailer-Website

Movie-Trailer-Website will accept your favorate movie information interactively and store it in a database file, after init or add movie information you can show movie in a web page and you can click the poster and play the trailer video. 

This project consist of three mainly files: entertainment_center.py media.py fresh_tomatoes.py. Once you run this project there will be a auto created data file called movie_data that store movie information persistence.

entertainment_center.py is entrance file
media.py defined the Movie class
fresh_tomatoes.py will read movie inforamtion and produce a HTML file.

## Installation
- git clone https://github.com/cdskycom/Movie-Trailer-Website.git

## Python version
This project tested under python 3.6. It's recommendation to use 3.6 or above.

## Usage:
Command Line

   - python entertainment_center.py _--init_   use a predefined movies list to init a movie list - of course this list is my favorate movies :)
   - python entertainment_center.py _--list_   open a web page show movies list.
   - python entertainment_center.py _--add_    open a interactive model to add movie information to database.
   - python entertainment_center.py _--del_  _movie_title_  delete a movie from database. **movie_title** is the movie's title string.

