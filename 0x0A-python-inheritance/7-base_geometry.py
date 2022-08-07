#!/usr/bin/python3
"""
This module contains an empty class BaseGeometry
and a method area()
"""


class BaseGeometry:
    """a class that defines BaseGeometry
    """
    def area(self):
        """
        This method checks whether area has been implemented
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
        This method validates integers and raises
        appropriate error Messages
        Args:
            name: a string
            value: the value of the string
        Returns:
             nothing
        """
        if not type(value) is int and not isinstance(value, int):
            raise TypeError(name + ' must be an integer')
        if value <= 0:
            raise ValueError(name + ' must be greater than 0')
