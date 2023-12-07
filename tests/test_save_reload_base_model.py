#!/usr/bin/python3
""" Module for testing FileStorage class """

import unittest
from models import storage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """ Test cases for FileStorage class """

    def test_all(self):
        """ Test the all() method """
        all_objs = storage.all()
        self.assertIsInstance(all_objs, dict)

    def test_new(self):
        """ Test the new() method """
        my_model = BaseModel()
        storage.new(my_model)
        key = "{}.{}".format(my_model.__class__.__name__, my_model.id)
        self.assertIn(key, storage.all())

    def test_save(self):
        """ Test the save() method """
        my_model = BaseModel()
        my_model.name = "Test_Model"
        my_model.save()
        key = "{}.{}".format(my_model.__class__.__name__, my_model.id)
        with open("file.json", 'r', encoding='utf-8') as file:
            saved_data = file.read()
            self.assertIn(key, saved_data)

    def test_reload(self):
        """ Test the reload() method """
        my_model = BaseModel()
        my_model.name = "Reload_Model"
        my_model.save()
        storage.reload()
        key = "{}.{}".format(my_model.__class__.__name__, my_model.id)
        self.assertIn(key, storage.all())


if __name__ == '__main__':
    unittest.main()
