#!/usr/bin/python3
"""This module contains a class that defines a
    square and instantiates size of the square
    with optional size=0 and a private instance
    variable. The class also has a public instance
    method that returns the area of the square
    The class has setters and getters
    The class has a method to print a square
    The class now has the spec. of printing spaces
"""


class Square:
    """A class that defines a square and prints spaces using
    """
    def __init__(self, __size=0, __position=(0, 0)):
        """This method initializes by passing
            initial values to the square object
            if no value is passed, an optional
            0 is used. It also raises appropriate
            exceptions based on errors.
            The method initializes by passing initial values
            to a tuple which holds the co-ordinates of a square

            Args:
                __size: size of square
        """
        self.__size = __size
        self.__position = __position

        for i in range(len(self.__position)):
            if not isinstance(__position[i], int) or __position[i] < 0:
                raise TypeError('position must be a tuple of 2 positive '
                                'integers')

        if len(__position) != 2:
            raise TypeError('position must be a tuple of 2 positive '
                            'integers')

    def __str__(self):
        """This method enables printing of a
            class instance passed as an
            argument to a method
            Returns:
                str: the string representation of a class
                instance
        """
        return str(self.my_print())

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

    @property
    def position(self):
        """
        gets the co-ordinates of the square
        sets the co-ordinates of the square
        checks the value and raises appropriate exceptions
        Returns:
            int: value of size
        """
        return self.__position

    @size.setter
    def size(self, value):
        for i in range(len(self.__position)):
            self.__position = value

    def area(self):
        """
        Finds the area of a square
        Returns:
             int: the area of the square
        """
        return self.__size * self.__size

    def my_print(self):
        """
        prints a square using the # character
        Returns:
            nothing
        """
        for i in range(self.__size):
            if self.__position[1] > 0:
                print(' ', end='')
            elif self.__position == (0, 0):
                print(end='')
            else:
                for m in range(len(self.__position)):
                    for n in range(len(self.__position)):
                        print(' ', end='')
            for j in range(self.__size):
                print('#', end='')
            print('')

        if self.__size == 0:
            print()
