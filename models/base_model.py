#!/usr/bin/python3
"""
Module: base_model
Defines the BaseModel class, a parent class with
common members for other classes.
"""

from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    aseModel class represents a parent class with
    common members for other classes.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes an instance of the BaseModel.

        Parameters:
        - args: Unused variable number of non-keyworded arguments.
        - kwargs: Keyworded variable number of arguments.
        """
        from models import storage
        if not kwargs:
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            self.id = str(uuid4())
            storage.new(self)
        else:
            if '__class__' in kwargs:
                del kwargs['__class__']
            for value in ('created_at', 'updated_at'):
                if value in kwargs:
                    kwargs[value] = datetime.fromisoformat(
                        kwargs[value])
            self.__dict__.update(kwargs)

    def __str__(self):
       """
        Returns a string representation for an instance.
       """
       return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        from models import storage
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
        custom_dict = {}
        custom_dict.update(self.__dict__)
        custom_dict.update({'__class__': type(self).__name__})
        custom_dict['created_at'] = self.created_at.isoformat()
        custom_dict['updated_at'] = self.updated_at.isoformat()
        return custom_dict