#!/usr/bin/python3
"""
Module:file_storage.py
"""

import os
import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review


class FileStorage():
    """
    create file storage
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        return __objects dictionary
        """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """ Serializes __objects to the JSON file (path: __file_path) """
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict().copy()

        with open(self.__file_path, mode="w", encoding="utf-8") as my_file:
            json.dump(new_dict, my_file)

    def reload(self):
        """
            deserializes the JSON file to __objects,
            (only if the JSON file (__file_path) exists;
            otherwise, do nothing.
            If the file doesn’t exist, no exception should be raised)
        """
        try:
            with open(self.__file_path, mode="r", encoding="utf-8") as my_file:
                dict_obj = json.load(my_file)

            for obj in dict_obj.values():
                cls_name = obj['__class__']
                del obj['__class__']
                class_gl = globals()[cls_name]
                inst = class_gl(**obj)
                self.new(inst)
        except FileNotFoundError:
            pass
