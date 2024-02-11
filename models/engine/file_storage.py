#!/usr/bin/pythonu3

"""Definition of FileStorage class"""

import json
import os.path
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """FileStorage class for Airbnb project."""

    __file_path = "./file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id."""
        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)."""
        obj_dct = {}
        for key, val in FileStorage.__objects.items():
            obj_dct[key] = val.to_dict()
        with open(FileStorage.__file_path, "w") as fp:
            json.dump(obj_dct, fp)

    def reload(self):
        """Deserializes the JSON file to __objects (only if the JSON file \
                (__file_path) exists ; otherwise, does nothing.
        """
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as read_file:
                fd = json.load(read_file)
                for val in fd.values():
                    cls = val["__class__"]
                    del val["__class__"]
                    c = eval(cls)(**val)
                    self.new(c)
