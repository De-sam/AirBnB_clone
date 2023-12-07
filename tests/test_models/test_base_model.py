#!/usr/bin/python3
"""
Module containing tests for the BaseModel class.
"""
import unittest
from datetime import datetime

from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Test cases for the BaseModel class.
    """

    def test_base_model_instance(self):
        """
        Test creation of a BaseModel instance.
        """
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89

        self.assertEqual(type(my_model), BaseModel)
        self.assertEqual(type(my_model.id), str)
        self.assertEqual(type(my_model.created_at), datetime)
        self.assertEqual(type(my_model.updated_at), datetime)
        self.assertEqual(type(my_model.name), str)
        self.assertEqual(type(my_model.my_number), int)

    def test_base_model_str(self):
        """
        Test the __str__ method of BaseModel.
        """
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89

        expected_str = "[BaseModel] ({}) {}".format(
            my_model.id, my_model.__dict__)
        self.assertEqual(str(my_model), expected_str)

    def test_base_model_save(self):
        """
        Test the save method of BaseModel.
        """
        my_model = BaseModel()
        updated_at_before = my_model.updated_at
        my_model.save()
        updated_at_after = my_model.updated_at

        self.assertNotEqual(updated_at_before, updated_at_after)

    def test_base_model_to_dict(self):
        """
        Test the to_dict method of BaseModel.
        """
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89

        obj_dict = my_model.to_dict()

        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertEqual(obj_dict['created_at'],
                         my_model.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'],
                         my_model.updated_at.isoformat())
        self.assertEqual(obj_dict['name'], 'My First Model')
        self.assertEqual(obj_dict['my_number'], 89)


if __name__ == '__main__':
    unittest.main()
