#!/usr/bin/python3
""" Base class"""
import json
# import turtle


class Base:
    """Class Atributes"""
    __nb_objects = 0

    """Contructor"""

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    """#15 salida identica"""
    @staticmethod
    def to_json_string(list_dictionaries):
        """String -> JSON"""
        if list_dictionaries is None or list_dictionaries == []:
            return '[]'
        return json.dumps(list_dictionaries)

    """#16 salida identica JSON string representation"""
    @classmethod
    def save_to_file(cls, list_objs):
        file = cls.__name__ + ".json"
        with open(file, 'w') as js_file:
            if list_objs is None:
                js_file.write("[]")
            else:
                dicty = [object.to_dictionary() for object in list_objs]
                js_file.write(Base.to_json_string(dicty))
    """#17 problema en la salida __str__? (return list of JSON)"""
    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)
    # """#18"""
    # @classmethod
    # def create(cls, **dictionary):
