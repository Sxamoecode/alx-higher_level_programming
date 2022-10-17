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

    def area(self):
        """Returns area of rectangle
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        :return: perimeter of rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """ method print the rectangle with the character #
        """
        emp = ""
        if self.__height == 0 or self.__width == 0:
            return emp

        for i in range(self.__height):
            if i == self.__height - 1:
                emp += ('#' * self.__width)
            else:
                emp += (('#' * self.__width) + '\n')
        return emp
