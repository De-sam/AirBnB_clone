#!/usr/bin/python3
""" Module for BaseModel class """

from datetime import datetime
from uuid import uuid4

from models import storage


class BaseModel:
    """ Base class for other classes """

    def __init__(self, *args, **kwargs):
        """ Constructor method """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        value = datetime.strptime(
                            value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.now()
            storage.new(self)

    def save(self):
        """ Updates the public instance attribute updated_at
            with the current datetime """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ Returns a dictionary containing all keys/values of __dict__ """
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict

    def __str__(self):
        """ Returns a string representation of the object """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)
