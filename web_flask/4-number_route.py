#!/usr/bin/python3
"""Starts a Flask web application."""

from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """Display Hello HBNB for the route /."""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Display HBNB for the route /hbnb."""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def replace(text):
    """Display C followed by text variable for route /c/text."""
    x = text.replace("_", " ")
    return f"C {x}"


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def defaults(text=None):
    """Display Python followed by text variable for route /python/<text>."""
    if text is None:
        text = "is cool"
    x = text.replace("_", " ")
    return f"Python {x}"


@app.route("/number/<int:n>", strict_slashes=False)
def numbers(n):
    """Display n is a number only if n is an integer."""
    return f"{n} is a number"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
