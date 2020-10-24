#!/usr/bin/python3
""" Base class"""
import json
import csv
import turtle


class Base:
    __nb_objects = 0

    """[principal class of the project]
    """

    def __init__(self, id=None):
        """[Contructor]

        Args:
            id ([int], optional): [inherits from base]. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """[from object to json format]

        Returns:
            [dictionary]: [from ]
        """
        if list_dictionaries is None or list_dictionaries == []:
            return '[]'
        return json.dumps(list_dictionaries)

    """  # 16 salida identica JSON string representation"""
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

    # @classmethod
    # def save_to_file_csv(cls, list_objs):

    # @classmethod
    # def load_from_file_csv(cls):
    @staticmethod
    def draw(list_rectangles, list_squares):
        """ Draw figures """
        t = turtle.Turtle()
        t.screen.bgcolor("#000000")
        t.color("gold")
        colors = ["Teal", "Chartreuse"]
        colors2 = ["DarkOrange", "Yellow"]
        # drae rectangles
        for rectangle in list_rectangles:
            t.showturtle()
            t.up()
            if rectangle.x == 0 or rectangle.y == 0:
                t.goto(-300, 100)
            else:
                t.goto(rectangle.x - 150, rectangle.y * 2 - 180)
            t.down()

            for i in range(2):
                t.pencolor(colors[i % 6])
                t.forward(rectangle.width)
                t.left(90)
                t.forward(rectangle.height)
                t.left(90)
            t.hideturtle()
        # draw squares
        for square in list_squares:
            t.showturtle()
            t.up()
            t.goto(square.x - 50, square.y + 20)
            t.down()
            for i in range(2):
                t.pencolor(colors2[i % 6])
                t.forward(square.width)
                t.left(90)
                t.forward(square.height)
                t.left(90)
            t.hideturtle()

        turtle.mainloop()
