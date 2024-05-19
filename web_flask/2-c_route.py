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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
