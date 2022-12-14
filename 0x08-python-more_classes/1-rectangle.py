#!/usr/bin/python3
"""
A Rectangle class
"""


class Rectangle:
    """
    Rectangle data and functions here
    """

    def __init__(self, width=0, height=0):
        """
        Instantiation
        :param width: width
        :param height: height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter for width
        :param self: None
        :return: self.__width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter for height
        :param self: None
        :return: self.__height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
