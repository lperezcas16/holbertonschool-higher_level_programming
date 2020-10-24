#!/usr/bin/python3
"""Square Class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """[create a Square]

    Args:
        Rectangle ([class]): [inherits from Rectangle]
    """

    def __init__(self, size, x=0, y=0, id=None):
        """[Contructor]

        Args:
            size ([int]): [size in height and width]
            x (int, optional): [position in x]. Defaults to 0.
            y (int, optional): [position in y]. Defaults to 0.
            id ([int], optional): [inherit from base]. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """[toString of square]

        Returns:
            [text]: [shows the atributes of the square]
        """
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """[update the square]
        """
        if len(args):
            key = ['id', 'size', 'x', 'y']
            idx = 0
            for value in args:
                if idx < 4:
                    setattr(self, key[idx], value)
                    idx += 1
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """[from object to dictionary]

        Returns:
            [dictionary]: [print the dictionary of atributes]
        """
        return {'id': self.id,
                'x': self.x,
                'size': self.size,
                'y': self.y}

    @property
    def size(self):
        """[getter of size]

        Returns:
            [int]: [value of size]
        """
        return self.width

    @size.setter
    def size(self, value):
        """[setter size and widht and height beacuse there are the same in squares]

        Args:
            value ([int]): [an integer value]
        """
        self.width = value
        self.height = value
