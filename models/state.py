#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel


class State(BaseModel):
    """ State class """
    __tablename__ = "states"
    cities = relationship('City', backref='state', cascade='all, delete-orphan')
    name = Column(String(128), nullable=False)
