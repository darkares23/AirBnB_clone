#!/usr/bin/python3
"""

"""
import json
from datetime import datetime
from uuid import uuid4

class BaseModel:
    """Base Model"""
    def __init__(self, *args, **kwargs):
        """ """
        if (kwargs):
            for k, v in kwargs.items():
                if (k == 'created_at' or k == 'updated_at'):
                    setattr(self, k, datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f"))
                elif(k != '__class__'):
                    setattr(self, k, v)
        else:
            self.id = str(uuid4())
            self.created_at = (datetime.now())
            self.updated_at = (datetime.now())

    def __str__(self):
        """ """
        return("[{}] ({}) {}").format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ """
        key = self.__dict__
        key['__class__'] = self.__class__.__name__
        key['created_at'] = key['created_at'].isoformat()
        key['updated_at'] =  key['updated_at'].isoformat()
        return key
