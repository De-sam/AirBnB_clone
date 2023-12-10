#!/usr/bin/python3
"""
Module: base_model
Defines the BaseModel class, a parent class with
common members for other classes.
"""
from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel:
    """
    BaseModel class represents a parent class with
common members for other classes.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes an instance of the BaseModel.

        Parameters:
        - args: Unused variable number of non-keyworded arguments.
        - kwargs: Keyworded variable number of arguments.
        """
        if not kwargs:
            # If kwargs is empty, it's a new instance
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            # If kwargs is not empty, it's a reconstructed instance
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key in ["created_at", "updated_at"]:
                    setattr(self, key, datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, key, value)

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
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary representation
of attributes belonging to an instance.

        Returns:
            dict: A dictionary containing the instance attributes.
        """
        obj_dict = {
            key: value.isoformat() if "_at" in key else value
            for key, value in self.__dict__.items() if key != "__class__"
        }
        obj_dict["__class__"] = type(self).__name__

        return obj_dict
