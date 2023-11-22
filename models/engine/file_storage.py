#!/usr/bin/python3
"""Defines 'FileStorage' class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.review import Review
from models.place import Place
from models.state import State
from models.city import City


class FileStorage:
    """Serializes instances to a JSON file and
    deserializes JSON file to instances."""

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Returns the list of objects of one type of class."""
        list_obj = []
        for key, value in FileStorage.__objects.items():
            if (value.__class__ == cls):
                list_obj.append(str(value))
        return list_obj

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        class_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(class_name, obj.id)] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        inst_dict = FileStorage.__objects
        inst_dict = {obj: inst_dict[obj].to_dict() for obj in inst_dict.keys()}
        with open(FileStorage.__file_path, "w") as file:
            json.dump(inst_dict, file)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        try:
            with open(FileStorage.__file_path) as file:
                inst_dict = json.load(file)
                for item in inst_dict.values():
                    class_name = item["__class__"]
                    del item["__class__"]
                    self.new(eval(class_name)(**item))
        except FileNotFoundError:
            return

    def delete(self, obj=None):
        """Delete obj from __objects."""
        if obj:
            key_to_delete = "{}.{}".format(obj.__class__.__name__, obj.id)
            if key_to_delete in self.__objects:
                del self.__objects[key_to_delete]
