#!/usr/bin/python3
"""Defines the BaseModel class."""
import models
import uuid
import sqlalchemy
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class BaseModel:
    """Define all common attributes/methods for other classes."""

    id = Column(String(60), primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Initialize attributes.

        Args:
            *args: unused
            *kwargs (dict): attribures
        """
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k != '__class__':
                    if k in ['created_at', 'updated_at']:
                        setattr(self, k, datetime.fromisoformat(v))
                    else:
                        setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4().hex)
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def save(self):
        """Update the attribute update_at with the current datetime."""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Return a dictionary containing all keys/values."""
        new = self.__dict__.copy()
        new['__class__'] = self.__class__.__name__
        new['created_at'] = self.created_at.isoformat()
        new['updated_at'] = self.updated_at.isoformat()
        new.pop('_sa_instance_state', None)
        return new

    def __str__(self):
        """Return string representation of the class."""
        new = self.__dict__.copy()
        new.pop('_sa_instance_state', None)
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                self.id, new))

    def delete(self):
        """Delete the current instance from the storage."""
        models.storage.delete(self)
