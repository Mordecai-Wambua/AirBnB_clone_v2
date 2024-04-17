#!/usr/bin/python3
"""The new engine: DBStorage."""

from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv

class DBStorage:
    """Storage engine utilizing a database."""
    __engine = None
    __session = None


    def __init__(self):
        """Create the engine."""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            getenv("HBNB_MYSQL_USER"),
            getenv("HBNB_MYSQL_PWD"),
            getenv("HBNB_MYSQL_HOST"),
            getenv("HBNB_MYSQL_DB")),
            pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.dropall(self.__engine)

    def all(self, cls=None):
        """Query on current database session."""
        objects = {}
        classes = [User, State, City, Amenity, Place, Review]
        for i in classes:
            if cls is None or cls is classes[i] or cls is i:
                obj = self.__session.query(classes[i]).all()
                for i in obj:
                    k = '{}.{}'.format(i.__class__.__name__, i.id)
                    obj[k] = i
        return (objects)

    def new(self, obj):
        """Add the object to the current database session."""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of current database session."""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from current database session."""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database."""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                        expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
