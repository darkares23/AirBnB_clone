#!/usr/bin/python3
"""
File store class
"""


import json
import os
from models.base_model import BaseModel


class FileStorage():
    """ """
    engine_directory = os.path.dirname(os.path.abspath(__file__))
    parent_directory = os.getcwd()
    __file_path = parent_directory + '/file.json'
    __objects = dict()

    def all(self):
        """Return dictionary __objects """
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serealizes __object to json file"""
        with open(self, __file_path, 'w', encoding="utf-8") as f:
            f.write(str({k: v.to_dict() for (k, v) in self.__objects.items()}))

    def reload(self):
        """Deserealizes the json file to __obnjests only if exist"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                dump = f.read()
                str_dict = json.loads(dump)
                for k, v in str_dict.items():
                    clss = v['__class__']
                    create_class = validClasses[class_]
                    self.__objects[k] = create_class(**v)

    def get_filepath(self):
        """get filepath for JSON file
        """
        return self.__file_path