#!/usr/bin/python3
"""
Module containing tests for the BaseModel class.
"""
import unittest

from models.base_model import BaseModel




class TestBaseModelDict(unittest.TestCase):
    """
    Test cases for the BaseModel class dictionary representation.
    """

    def test_base_model_dict(self):
        """
        Test the recreation of a BaseModel instance from a dictionary.
        """
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89

        my_model_json = my_model.to_dict()

        my_new_model = BaseModel(**my_model_json)

        self.assertEqual(my_model.id, my_new_model.id)
        self.assertEqual(my_model.created_at, my_new_model.created_at)
        self.assertEqual(my_model.updated_at, my_new_model.updated_at)
        self.assertEqual(my_model.name, my_new_model.name)
        self.assertEqual(my_model.my_number, my_new_model.my_number)


if __name__ == '__main__':
    unittest.main()
