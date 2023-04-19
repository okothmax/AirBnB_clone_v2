#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ The city class, contains state ID and name 

    Inherits from SQLAlchemy Base and links to the MySQL table cities.

    Attributes:
        __tablename__ (str): name of the MySQL table to store Cities.
        name (sqlalchemy String): name of the City.
        state_id (sqlalchemy String): state id of the City.
    """
    __table__ = "cities"
    state_id = Column(String(128), nullable = False)
    name = Column(String(60), ForeignKey("states.id"), nullable = False)
    places = relationship("Place", backref="cities", cascade="delete")
