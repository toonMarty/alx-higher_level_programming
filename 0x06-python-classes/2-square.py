#!/usr/bin/python3
"""This module contains a class that defines a
    square and instantiates size of the square
    with optional size=0 and a private instance
    variable
"""


class Square:
    """A class that defines a square with an optional size
    """
    def __init__(self, __size=0):
        """This method initializes by passing
            initial values to the square object
            if no value is passed, an optional
            0 is used. It also raises appropriate
            exceptions based on the errors

            Args:
                __size: size of square
        """
        self.__size = __size

        if not isinstance(__size, int):
            raise TypeError('size must be an integer')
        elif __size < 0:
            raise ValueError('size must be >= 0')
