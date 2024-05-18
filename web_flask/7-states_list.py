#!/usr/bin/python3
"""Starts a Flask web application and makes use of DB storage."""

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states():
    """Display HTML page with State objects from DB."""
    return render_template("7-states_list.html",
            states=storage.all('State').values())


@app.teardown_appcontext
def teardown(self):
    """Remove current SQLAlchemy Session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
