#!/usr/bin/python3
"""
Module for FileStorage class
"""
import json
from models.base_model import BaseModel

class FileStorage:
    """
    Serializes instances to a JSON file and
    deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
       """Returns the dictionary __objects"""
       return self.__objects
        
    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        """
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path)
        """
        with open(self.__file_path, mode='w') as json_file:
            dictionary_storage = {}
            for key, value in self.__objects.items():
                dictionary_storage[key] = value.to_dict()
            json.dump(dictionary_storage, json_file)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists
        otherwise, do nothing. If the file doesn’t exist,
        no exception should be raised)
        """
        try:
            with open(self.__file_path, encoding="utf-8") as json_file:
                for object in json.load(json_file).values():
                    self.new(eval(object["__class__"])(**object))
        except FileNotFoundError:
            return
