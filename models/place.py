#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models.review import Review
from models.amenity import Amenity
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
import os
from sqlalchemy.orm import relationship
import models


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'), primary_key=True),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'), primary_key=True))


class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship(
                'Review',
                cascade='all, delete, delete-orphan',
                backref='place')
        amenities = relationship(
                'Amenity',
                secondary=place_amenity,
                viewonly=False,
                backref="place_amenities")
    else:
        @property
        def reviews(self):
            """Returns list of Review instances."""
            from models import storage
            output = []
            for i in storage.all(Review).values():
                if i.place_id == self.id:
                    output.append(i)
            return output

        @property
        def amenities(self):
            """Return a list of Amenity instances."""
            from models import storage
            output = []
            for i in storage.all(Amenity).values():
                if i.place_id == self.id:
                    output.append(i)
            return output
