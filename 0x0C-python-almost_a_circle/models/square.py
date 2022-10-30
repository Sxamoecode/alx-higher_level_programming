#!/usr/bin/python3
"""Import Rectangle to Square
"""
Rectangle = __import__('rectangle').Rectangle


class Square(Rectangle):
    """Represent Square class
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(id=id, x=x, y=y, width=size, height=size)

    @property
    def size(self):
        """size setter
        """
        return self.width

    @size.setter
    def size(self, value):
        """size needs to be an int
        """

        self.width = value
        self.height = value

    def __str__(self):
        """Returns formatted information display
        """

        return "[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                                             self.id, self.x, self.y,
                                             self.width)

    def update(self, *args, **kwargs):
        """update
        """
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                setattr(self, k, v)
        elif len(args) != 0:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass
        else:
            print()

    def to_dictionary(self):
        """Returns a dict representation
        """

        return {'id': self.id, 'x': self.x, 'size': self.width, 'y': self.y}

    def __str__(self):
        """Return the print() and str() representation of a Square.
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
