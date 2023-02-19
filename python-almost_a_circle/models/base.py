#!/usr/bin/python3
"""
Base Class
"""
import json


class Base:
    """
    Base Class
    """
    __nb_objects = 0

    def __init__(self, id=None):

        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns json string od list_dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        write json string to file
        """
        stor = []
        with open(cls.__name__ + ".json", "w", encoding="utf-8") as f:
            if list_objs:
                for ele in list_objs:
                    stor.append(ele.to_dictionary())
            f.write(cls.to_json_string(stor))

    @staticmethod
    def from_json_string(json_string):
        """
        return json_string as list of dict
        """
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        returns a dummy instance
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dum.update(**dictionary)
        return dummy
