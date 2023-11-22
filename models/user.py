#!/usr/bin/python3
"""This module defines a class User"""
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.review import Review
from models.place import Place

class User(BaseModel, Base):
    """This class defines a user
            email : Email
            password: Password
            first_name: First name
            last_name: Last name
            places = Places
    """
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    places = relationship("Place", cascade='all, delete, delete-orphan', backref="user")
    #reviews = relationship("Review", cascade='all, delete, delete-orphan', backref="user")
