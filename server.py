"""Movie Ratings"""

# from jinja2 import StrictUndefined

from flask import Flask, render_template, request, flash, redirect, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension
import requests



app = Flask(__name__)

# app.jinja_env.undefined = StrictUndefined


# @app.route('/')
# def index():
#     """Homepage."""

#     return render_template('homepage.html')

# @app.route('/test')
# def get():

#     r = requests.get("http://www.omdbapi.com/?i=tt0107290&apikey=ff058cb3")
#     movie_desc = r.json()
#     return jsonify(movies=movie_desc)


@app.route('/')
def index():
    """Homepage."""

    return render_template('homepage_search.html')



@app.route('/search')
def get():

    r = requests.get("http://www.omdbapi.com/?i=tt0107290&apikey=ff058cb3")
    movie_desc = r.json()
    return jsonify(movies=movie_desc)

 





if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
