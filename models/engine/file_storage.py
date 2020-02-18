#!/usr/bin/python3
"""
Define the FileStorage class
"""


import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage():
    """
    Handle JSON serialization of objects
    """
    engine_directory = os.path.dirname(os.path.abspath(__file__))
    parent_directory = os.getcwd()
    __file_path = parent_directory + '/file.json'
    __objects = dict()

    def all(self):
        """
        Return dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        Add object to __objects
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serealizes __object to json file
        """
        with open(self.__file_path, 'w', encoding="utf-8") as f:
            dic = {k: v.to_dict() for (k, v) in self.__objects.items()}
            f.write(json.dumps(dic))

    def reload(self):
        """
        Deserealizes the json file to __obnjests only if exist
        """
        cls_dict = {"BaseModel": BaseModel,
                    "User": User,
                    "State": State,
                    "City": City,
                    "Amenity": Amenity,
                    "Place": Place,
                    "Review": Review}

        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                dump = f.read()
                str_dict = json.loads(dump)
                for k, v in str_dict.items():
                    clss = v['__class__']
                    create_class = cls_dict[clss]
                    self.__objects[k] = create_class(**v)

    def get_filepath(self):
        """
        Get filepath for JSON file
        """
        return self.__file_path
