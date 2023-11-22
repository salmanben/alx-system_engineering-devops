#!/usr/bin/python3
""" Place Module for HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
import models
import shlex

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    id = Column(String(60), primary_key=True, nullable=False)
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE") == "db":
         place_amenity = Table("place_amenity", Base.metadata,
                              Column("place_id", String(60), ForeignKey("places.id"),
                                     primary_key=True, nullable=False),
                              Column("amenity_id", String(60), ForeignKey("amenities.id"),
                                     primary_key=True, nullable=False))

        reviews = relationship("Review", cascade='all, delete, delete-orphan', backref="place")
        amenities = relationship("Amenity", secondary=place_amenity,
                                 viewonly=False,
                                 back_populates="place_amenities")
    else:
        @property
        def reviews(self):
            """ Returns list of reviews.id """
            sd = models.storage.all()
            li = []  # List to store review instances
            r = []  # Result list
            for k in sd:
                review = k.replace('.', ' ')
                review = shlex.split(review)
                if review[0] == 'Review':
                    li.append(sd[k])
            for o in li:
                if o.place_id == self.id:
                    r.append(o)
            return r
        
