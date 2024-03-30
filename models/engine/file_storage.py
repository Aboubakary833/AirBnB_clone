#!/usr/bin/python3
"""Filestorage"""

import json
from models.base_model import BaseModel

class FileStorage:
    """FileStorage class
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """  returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        """get key of the form <obj class name>.id"""
        key = obj.__class__.__name__ + "." + str(obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Save json representation of instances in a file
        """
        json_repr = {}
        for key in self.__objects:
            json_repr[key] = self.__objects[key].to_dict()

        with open(self.__file_path, 'w') as file:
            json.dump(json_repr, file)

    def reload(self):
        """Deserialize the JSON file"""
        try:
            with open(self.__file_path, 'r', encoding="UTF8") as file:
                for key, value in json.load(file).items():
                    attribute = eval(value["__class__"])(**value)
                    self.__objects[key] = attribute
        except FileNotFoundError:
            pass
