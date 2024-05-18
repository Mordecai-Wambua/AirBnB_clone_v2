#!/usr/bin/python3
"""Starts a Flask web application and makes use of DB storage."""

from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states():
    """Display HTML page with State objects from DB."""
    states = storage.all("State").values()
    return render_template("7-states_list.html", states=states)

@app.teardown_appcontext
def teardown(exc):
    """Remove current SQLAlchemy Session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
