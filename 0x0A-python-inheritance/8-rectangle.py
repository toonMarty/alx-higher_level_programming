#!/usr/bin/python3
"""
This module contains a class Rectangle that inherits from
BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class that inherits from BaseGeometry
    """
    def __init__(self, __width, __height):
        """
        This method initializes a Rectangle instance

        Args:
            __width: width of the rectangle
            __height: height of the rectangle
        """
        self.__width = __width
        self.__height = __height
        BaseGeometry.integer_validator(self, "width", self.__width)
        BaseGeometry.integer_validator(self, "height", self.__height)
