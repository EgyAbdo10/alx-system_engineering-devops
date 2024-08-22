#!/usr/bin/python3
"""create a flask web app"""

from flask import Flask
from os import environ

environ['FLASK_ENV'] = 'production'
app = Flask(__name__)


# get /airbnb-onepage page
@app.route("/airbnb-onepage", strict_slashes=False)
def say_hi():
    """return Hello HBNB!"""
    return "Hello HBNB!"


if __name__ == "__main__":
    # run the application on host 0.0.0.0 and port 5000
    app.run(host="0.0.0.0", port=5000)
