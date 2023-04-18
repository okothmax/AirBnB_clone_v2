#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
import models
from models import storage
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import Column
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models
    Attributes:
        id (sqlachemy String): The basemodel id
        created_at (sqlachemy datetime): the time of creation
        updated_at (sqlalchemy datetime): the time an update was made
    """

    id = Column(String(60), primary_key = True, nulllable = False)
    created_at = Column(DateTime, nullable = False, default = datetime.utcnow())
    updated_at = Column(DateTime, nullable = False, default = datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model
        
        Args:
            *args (any): aruements(unsed)
            **kwargs (in form of a dict): key, value pairs
        """

        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at =  self.updated_at = datetime.now()
        else:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = str(type(self).__name__)
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        my_dict.pop("_sa_instance_state", None)
        return my_dict
    
    def delete(self):
        """Delete the instance from storage."""
        models.storage.delete(self)
