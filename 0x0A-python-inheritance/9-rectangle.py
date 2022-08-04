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
            __width(int): width of the rectangle
            __height(int): height of the rectangle
        """
        self.__width = __width
        self.__height = __height
        BaseGeometry.integer_validator(self, "width", self.__width)
        BaseGeometry.integer_validator(self, "height", self.__height)

    def __str__(self):
        """
        This method returns the string representation of a rectangle
        instance
        Returns:
             str: string representation of a Rectangle instance as
             specified
        """
        return f'{"[Rectangle]"} {self.__width}/{self.__height}'

    def area(self):
        """
        This method implements the area of a rectangle
        Returns:
            int: the area of the rectangle object
        """
        return self.__width * self.__height
