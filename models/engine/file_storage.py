#!/usr/bin/python3
"""
Module that defines the FileStorage class responsible for serialization
and deserialization of instances to and from a JSON file.
"""

import json
from models.base_model import BaseModel

class FileStorage:
    """
    The FileStorage class manages the serialization and deserialization
    of instances to and from a JSON file.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary containing all serialized objects.
        """
        return self.__objects

    def new(self, obj):
        """
        Adds a new object to the dictionary of serialized objects.

        Parameters:
        obj (BaseModel): The BaseModel object to be serialized and added.
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        Serializes the objects dictionary and writes it to the JSON file.
        """
        obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, mode='w') as json_file:
            json.dump(obj_dict, json_file)

    def reload(self):
        """
        Deserializes the objects from the JSON file and populates the objects dictionary.
        If the file doesn't exist, no exception is raised.
        """
        try:
            with open(self.__file_path, encoding="utf-8") as json_file:
                obj_dict = json.load(json_file)

            for key, obj_data in obj_dict.items():
                class_name, obj_id = key.split('.')
                obj = BaseModel(**obj_data)
                self.__objects[key] = obj
        except FileNotFoundError:
            return
