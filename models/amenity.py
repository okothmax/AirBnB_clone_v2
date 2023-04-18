#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel,Base
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship


class Amenity(BaseModel):
    """
    Represntation of Ameniity in the database

    Attributes:
        __tablename__ (str): The name of the MySQL table to store Amenities.
        name (sqlalchemy String): The amenity name.
        place_amenities (sqlalchemy relationship): Place-Amenity relationship."""
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary="place_amenity",
                                   viewonly=False)
