#!/usr/bin/python3
"""Basic geometry class
"""


class BaseGeometry:

    """Creates a function area
    """

    def area(self):
        """Raise exception
        """

        raise Exception("area() is not implemented")

    @staticmethod
    def integer_validator(self, name, value):
        """function that validates value
        """

        if type(value) != int:
            raise TypeError(name + "<name> must be an integer")
        if value < 0:
            raise ValueError(name + "<name> must be greater than 0")
