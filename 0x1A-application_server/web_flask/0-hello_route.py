from flask import Flask
"""create a flask web app"""


app = Flask(__name__)


@app.route("/airbnb-onepage", strict_slashes=False)
def say_hi():
    """return Hello HBNB!"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
