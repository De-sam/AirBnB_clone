#!/usr/bin/python3
"""
Module containing the BaseModel class.
"""
import uuid
from datetime import datetime


class BaseModel:
    """
    BaseModel class defines all common attributes/methods for other classes.
    """

    def __init__(self):
        """
        Initializes a new instance of the BaseModel class.
        """
        self.id = str(uuid.uuid4())
        self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.
        """
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__
        )

    def save(self):
        """updates the public instance
updated_at with current time and saves it to database."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing
all keys/values of __dict__ of the instance.
"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
