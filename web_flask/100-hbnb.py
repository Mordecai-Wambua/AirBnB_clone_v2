#!/usr/bin/python3
"""Starts a Flask web application and makes use of DB storage."""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place


app = Flask(__name__)


@app.route("/hbnb", strict_slashes=False)
def hbnb_filters():
    """Display a complete HTML inteface for AirBNB Project."""
    states = storage.all(State)
    amenities = storage.all(Amenity)
    places = storage.all(Place)
    return render_template("100-hbnb.html", states=states,
                            amenities=amenities,
                            places=places)


@app.teardown_appcontext
def teardown(exception):
    """Remove current SQLAlchemy Session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
