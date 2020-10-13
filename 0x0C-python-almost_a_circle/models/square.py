#!/usr/bin/python3
"""Square Class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Construtor"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.width)

    """Methods"""

    def update(self, *args, **kwargs):
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

    """Getter"""
    @property
    def size(self):
        return self.width

    """Setter"""
    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
