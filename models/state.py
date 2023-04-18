#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column
from sqlalchemy import String
import models
from os import getenv
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class 
    Inherits from SQLAlchemy Base and links the MySQL table states.

    Attributes:
        __tablename__ (str): name of the MySQL table to store States.
        name (sqlalchemy String): name of the State.
        cities (sqlalchemy relationship): State-City relationship.
    """
    __table__ = "states"
    name = Column(String(128), nullable = False)
    cities = relationship("City",  backref="state", cascade="delete")

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """Get a list of all related City objects."""
            city_list = []
            for city in list(models.storage.all(City).values()):
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list

