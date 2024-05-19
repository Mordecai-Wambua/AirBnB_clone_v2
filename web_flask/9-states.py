#!/usr/bin/python3
"""Starts a Flask web application and makes use of DB storage."""

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """Display HTML page with list of State objects from DB."""
    states = storage.all(State)
    return render_template("9-states.html", state=states)


@app.route("/states/<id>", strict_slashes=False)
def states_city(id):
    """Display a particular state with its cities else Not found."""
    states = storage.all(State).values()
    for state in states:
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


@app.teardown_appcontext
def teardown(exception):
    """Remove current SQLAlchemy Session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
