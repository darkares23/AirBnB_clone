#!/usr/bin/python3
"""

"""
import json
import copy
from datetime import datetime
from uuid import uuid4
import models

class BaseModel:
    """Base Model"""
    def __init__(self, *args, **kwargs):
        """ """
        if len(kwargs) is not 0:
            for k, v in kwargs.items():
                if (k == 'created_at' or k == 'updated_at'):
                    setattr(self, k, datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f"))
                elif(k != '__class__'):
                    setattr(self, k, v)
        else:
            self.id = str(uuid4())
            self.created_at = (datetime.now())
            self.updated_at = (datetime.now())
            models.storage.new(self)

    def __str__(self):
        """ """
        return("[{}] ({}) {}").format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
       """ """
       dic = copy.deepcopy(self.__dict__)
       dic['updated_at'] = dic['updated_at'].isoformat()
       dic['created_at'] = dic['created_at'].isoformat()
       dic['__class__'] = self.__class__.__name__
       return (dic)