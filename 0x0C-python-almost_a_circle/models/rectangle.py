#!/usr/bin/python3
"""Rectangle class
"""
Base = __import__('base').Base


class Rectangle(Base):

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Getter for width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter for width
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Getter for height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter for height
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def x(self):
        """Getter for x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """ Setter for x
        """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter for y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for x
        """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns area of rectangle
        """
        return self.__width * self.__height

    def display(self):
        """printed rectangle with '#'
        y is newline, x is space
        in stdout
        """
        import sys
        for i in range(self.__height):
            for j in range(self.__width - 1):
                print("{}".format('#'), end='', file=sys.stdout)
            print('#', file=sys.stdout)

    def __str__(self):
        return "[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__,
                                                self.id, self.__x, self.__y,
                                                self.__width, self.__height)
