#!/bin/bash
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle:
    """Create a class Rectangle
    that inherits from BaseGeometry (7-base_geometry.py)."""

    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
