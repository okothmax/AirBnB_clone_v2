#!/usr/bin/python3
""" defines unitests for models/base_model.py"""
from models.base_model import BaseModel
import unittest
from datetime import datetime
import os
import pep8
from models.engine.file_storage import FileStorage


class TestBaseModel(unittest.TestCase):
    """base_model class test """


    def __init__(self, *args, **kwargs):
        """ Initialize the class"""
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    @classmethod
    def setUp(self):
        """ test class for set up method

	Rename existing file.json temporarily
	Reset objects dictionary of FileStorage
	Create instance of BaseModel to test
	"""
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}
        cls.storage = FileStorage()
        cls.base = BaseModel()
    
    @classmethod
    def tearDown(self):
	"""test teardown for BaseModel.

        Original file.json restoration
        Delete instance of test BaseModel
        """
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        del cls.storage
        del cls.base

    def test_default(self):
        """ base model default testing"""
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """ base model testing with kwargs"""
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """ base model testing with int kwargs"""
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """ Testing save method"""
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """ testing str method of model"""
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.__dict__))

    def test_todict(self):
        """ testing to dict method"""
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """ test kwargs with none"""
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_kwargs_one(self):
        """ test kwargs with one arg"""
        n = {'Name': 'test'}
        with self.assertRaises(KeyError):
            new = self.value(**n)

    def test_id(self):
        """ test id attribute of model"""
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """ test created_at attribute"""
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """ test updated at attribute"""
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)
