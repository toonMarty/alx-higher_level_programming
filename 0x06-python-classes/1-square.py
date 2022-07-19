#!/usr/bin/python3
"""This module contains a class that defines a
    square and instantiates size of the square
"""


class Square:
    """A class that defines a square with a size
    """

    def __init__(self, __size):
        """This method initializes by passing
            initial values to the square object

            Args:
                __size: size of square
        """
        self.__size = __size
