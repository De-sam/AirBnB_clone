#!/usr/bin/python3
"""
Module: base_model
Defines the BaseModel class, a parent class with common members for other classes.
"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    BaseModel class represents a parent class with common members for other classes.
    """

    def __init__(self):
        """
        Initializes an instance of the BaseModel.
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns a string representation for an instance.
        """
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the `updated_at` attribute with the current date time.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary representation of attributes belonging to an instance.

        Returns:
            dict: A dictionary containing the instance attributes.
        """
        obj_dict = {
            key: value.isoformat() if "_at" in key else value
            for key, value in self.__dict__.items() if key != "__class__"
        }
        obj_dict["__class__"] = type(self).__name__

        return obj_dict
