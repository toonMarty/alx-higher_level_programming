#!/usr/bin/python3
"""
This module contains a class Square that inherits from
Rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class that inherits from Rectangle
    """
    def __init__(self, __size):
        """
        This method initializes a Square object based on
        the dimension, size
        Args:
            __size (int): size of the Square
        """
        self.__size = self._Rectangle__width = \
            self._Rectangle__height = __size
        Rectangle.integer_validator(self, "size", self.__size)

    def area(self):
        """
        This method returns the area of a Square instance
        Returns:
             area(int): the area of a Square object
        """
        return self.__size ** 2

    def __str__(self):
        """
        This method returns the string representation of a Square
        instance
        Returns:
             str: string representation of a Square instance as
             specified
        """
        return f'{"[Square]"} {self._Rectangle__width}/' \
               f'{self._Rectangle__height}'
