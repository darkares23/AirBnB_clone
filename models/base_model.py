#!/usr/bin/python3
"""
BaseModel class for AirBnB
"""


import json
import copy
from datetime import datetime
from uuid import uuid4
import models
import os
import pep8


class BaseModel:
    """
    This class will defines all common attributes/methods
    for other classes
    """

    def __init__(self, *args, **kwargs):
        """
        Instantiation of base model class
        Args:
            args: it won't used
            kwargs: arguments for the constructor of the BaseModel
        Attributes:
            id: unique id generated
            created_at: creation date
            updated_at: updated date
        """
        if len(kwargs) is not 0:
            for k, v in kwargs.items():
                if (k == 'created_at' or k == 'updated_at'):
                    setattr(self, k, datetime.strptime
                            (v, "%Y-%m-%dT%H:%M:%S.%f"))
                elif(k != '__class__'):
                    setattr(self, k, v)
        else:
            self.id = str(uuid4())
            self.created_at = (datetime.now())
            self.updated_at = (datetime.now())
            models.storage.new(self)

    def __str__(self):
        """
        Returns a string of class name, id, and dictionary
        """
        a = self.__dict__
        return("[{}] ({}) {}").format(self.__class__.__name__, self.id, a)

    def save(self):
        """
        Updates the public instance attribute updated_at to current
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Creates dictionary of the class  and
        returns a dictionary of all the key values in __dict__
        """
        dic = copy.deepcopy(self.__dict__)
        dic['updated_at'] = dic['updated_at'].isoformat()
        dic['created_at'] = dic['created_at'].isoformat()
        dic['__class__'] = self.__class__.__name__
        return (dic)
