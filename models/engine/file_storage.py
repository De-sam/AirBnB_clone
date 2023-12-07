#!/usr/bin/python3
""" This module would be for file storage """

import json
from os.path import exists

from models.base_model import BaseModel
from models import storage



class FileStorage:
    """ Class for serializing and deserializing instances """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ Sets in __objects the obj with key <obj class name>.id """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ Serializes __objects to the JSON file """
        serial_objs = {k: v.to_dict()
                       for k, v in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            json.dump(serial_objs, file)

    def reload(self):
        """ Deserializes the JSON file to __objects """
        if exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                loaded_objs = json.load(file)
                for k, v in loaded_objs.items():
                    cls_name, obj_id = k.split('.')
                    obj_dict = v
                    obj_dict['__class__'] = cls_name
                    obj = eval(cls_name)(**obj_dict)
                    FileStorage.__objects[k] = obj


# Create a unique FileStorage instance for the application
storage = FileStorage()
storage.reload()
