"""Utility file to seed ratings database from MovieLens data in seed_data/"""

from sqlalchemy import func
import json
from model import User, Rating, Movie, connect_to_db, db
from server import app


# def load_users(user_filename):
#     """Load users from u.user into database."""

# result['movies']['Title']

def load_movies():
    """Load movies from u.item into database."""
    # new_dictionary = {}

    with open ('test.json') as file:

        # for keys in file:
        #     new_dictionary = file[keys]

        #     id = new_dictionary["imdbID"]
        #     title = new_dictionary["Title"]
        #     year = new_dictionary["Year"]
        #     genre = new_dictionary["Genre"]
        #     imdb_rating = new_dictionary["imdbRating"]
        #     image_url = new_dictionary["Poster"]
        data = json.loads(file.read())
        id = data['movies']["imdbID"]
        title = data["movies"]["Title"]
        year = data["movies"]["Year"]
        genre = data["movies"]["Genre"]
        imdb_rating = data["movies"]["imdbRating"]
        image_url = data['movies']['Poster']
    # for i, row in enumerate(open(movie_filename)):
    #     row = row.rstrip()

    #     movie_id, title, released_str, junk, imdb_url = row.split("|")[:5]


        movie = Movie(id=id,
                  title=title,
                  year=year,
                  genre=genre,
                  imdb_rating=imdb_rating,
                  image_url=image_url)

        # We need to add to the session or it won't ever be stored
        db.session.add(movie)

    db.session.commit()


# def load_ratings(rating_filename):
#     """Load ratings from u.data into database."""

    db.session.commit()


if __name__ == "__main__":
    connect_to_db(app)


    # In case tables haven't been created, create them
    db.create_all()

    # Import different types of data
    # load_users()
    load_movies()
    # load_ratings()

