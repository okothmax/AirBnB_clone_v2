#!/usr/bin/python3
""" module to test amenity class"""
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity
import os


class test_Amenity(test_basemodel):
    """ testing amenity class"""

    def __init__(self, *args, **kwargs):
        """initialisation of test class """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """name type testing """
        new = self.value()
        self.assertEqual(type(new.name), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))
