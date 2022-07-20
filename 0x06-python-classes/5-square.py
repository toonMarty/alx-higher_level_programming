#!/usr/bin/python3
"""This module contains a class that defines a
    square and instantiates size of the square
    with optional size=0 and a private instance
    variable. The class also has a public instance
    method that returns the area of the square
    The class has setters and getters
    The class has a method to print a square
"""


class Square:
    """A class that defines a square and prints it using #
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

    def area(self):
        """
        Finds the area of a square
        Returns:
             int: the area of the square
        """
        return self.__size * self.__size

    @property
    def size(self):
        """
        gets the size of the square
        sets the size of the square
        checks the value and raises appropriate exceptions
        Returns:
            int: value of size
        """
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value

        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')

    def my_print(self):
        """
        prints a square using the # character
        Returns:
            nothing
        """
        for i in range(self.__size):
            for j in range(self.__size):
                print('#', end='')
            print('')

        if self.__size == 0:
            print()
