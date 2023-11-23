#!/usr/bin/python3
"""
This module handles the details of how to connect to the database and execute SQL commands.
"""
from models.base_model import Base, BaseModel
from models.review import Review
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.user import User
from models.place import Place
from sqlalchemy.orm import scoped_session, sessionmaker, Session
from sqlalchemy import create_engine
from sqlalchemy.exc import InvalidRequestError
from os import getenv


class DBStorage:
    """
    Handles the details of how to connect to the database and execute SQL commands.
    """

    __engine = None
    __session = None

    def __init__(self) -> None:
        """
        Initializes a new instance of DBStorage.
        """
        username = getenv("HBNB_MYSQL_USER")
        password = getenv("HBNB_MYSQL_PWD")
        database_name = getenv("HBNB_MYSQL_DB")
        database_url = "mysql+mysqldb://{}:{}@{}/{}".format(username, password, host, database_name)
        host = getenv("HBNB_MYSQL_HOST")
        self.__engine = create_engine(database_url, pool_pre_ping=True)

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Returns a dictionary of objects based on the class name (optional).
        """
        list_objs = []
        if cls:
            if isinstance(cls, str):
                try:
                    cls = globals()[cls]
                except KeyError:
                    pass
            if issubclass(cls, Base):
                list_objs = self.__session.query(cls).all()
        else:
            for subclass in Base.__subclasses__():
                list_objs.extend(self.__session.query(subclass).all())
        dict_objs = {}
        for obj in list_objs:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            dict_objs[key] = obj
        return dict_objs
    
    def new(self, obj):
        """
        Adds a new object to the current database session.
        """
        self.__session.add(obj)
        self.__session.commit()

    def save(self):
        """
        Commits changes to the current database session.
        """
        self.__session.commit()    

                
    def delete(self, obj=None):
        """
        Deletes the given object from the current database session.
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        Creates all tables in the database and initializes a new session.
        """
        Base.metadata.drop_all(self.__engine)
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
