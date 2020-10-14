#!/usr/bin/python3
"""Square Class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Construtor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """atributes"""
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """Methods update square"""
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
        """Obj -> DIC"""
        return {'id': self.id,
                'x': self.x,
                'size': self.size,
                'y': self.y}

    @property
    def size(self):
        """Getter"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter"""
        self.width = value
        self.height = value
