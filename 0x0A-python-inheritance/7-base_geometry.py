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

    def integer_validator(self, name, value):
        """function that validates value
        """

        if type(value) != int:
            raise TypeError("{:s} must be an integer".format(name))

        if value <= 0:
            raise ValueError(name + "{:s} must be greater than 0".format(name))
