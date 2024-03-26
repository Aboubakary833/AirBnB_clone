#!/usr/bin/python3
"""Filestorage"""

import json
import os


class FileStorage:
    """FileStorage class
    """
    __file_path = "file.json"
    __objects = {}

    def all(self) -> dict:
        """Get all instance
        Returns:
        dict: Dict of all stored instances
        """
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj
        Args:
        obj (dict): Instance to be set
        """
        key = "{}.{}".format(obj.__class__.name, str(obj.id))
        self.__objects[key] = obj

    def save(self):
        """Save json representation of instances in a file
        """
        __json_repr = {}
        for k in self.__objects:
            __json_repr[k] = self.__objects[k].to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(__json_repr, file)

    def reload(self):
        try:
            with open(self.__file_path, 'r', encoding="UTF8") as file:
                for k, v in json.load(file).items():
                    value = eval(v["__class__"])(**v)
                    self.__objects[k] = value
        except FileNotFoundError:
            pass
