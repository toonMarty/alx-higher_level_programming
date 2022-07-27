#!/usr/bin/python3
"""
This module contains a module that defines
a rectangle and instantiates the width and
height of the rectangle (with optional width and
height)
The module also contains setters and getters for the
width and height
"""


class Rectangle:
    """A class that defines a rectangle with setters and getters
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, __width=0, __height=0):
        """
        This method initializes a Rectangle object
        If no value is passed for width and height, an
        optional 0 is used. It also raises appropriate
        exceptions based on errors
        Args:
            __width: width of the rectangle
            __height: height of the rectangle
        """
        self.__width = __width
        self.__height = __height

        if not isinstance(__width, int):
            raise TypeError('width must be an integer')
        if __width < 0:
            raise ValueError('width must be >= 0')

        if not isinstance(__height, int):
            raise TypeError('height must be an integer')
        if __height < 0:
            raise ValueError('height must be >= 0')

        Rectangle.number_of_instances += 1

    def __str__(self):
        """This method enables printing of a
            class instance passed as an
            argument to a method
            Returns:
                str: the string representation of a class
                instance
        """
        if self.__width == 0 or self.__height == 0:
            return ''
        if isinstance(self.print_symbol, (list, tuple, dict)):
            my_list = [self.print_symbol *
                       self.__width for _ in range(self.__height)]
            return '\n'.join(map(str, my_list))

        return '\n'.join(self.print_symbol *
                         self.__width for _ in range(self.__height))

    def __repr__(self):
        """
        This method returns a string representation of a rectangle
        Returns:
             str: the string representation of a class instance
        """
        return f'Rectangle({self.__width}, {self.__height})'

    def __del__(self):
        """
        This method deletes an instance of a class
        Returns:
            nothing
        """
        Rectangle.number_of_instances -= 1
        print('Bye rectangle...')

    @property
    def width(self):
        """
        gets the width of the Rectangle
        sets the width of the Rectangle
        Returns:
             int: value of width
        """
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

        if not isinstance(self.__width, int):
            raise TypeError('width must be an integer')
        if self.__width < 0:
            raise ValueError('width must be >= 0')

    @property
    def height(self):
        """
        gets the height of the Rectangle
        sets the height of the Rectangle
        Returns:
             int: value of height
        """
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

        if not isinstance(self.__height, int):
            raise TypeError('height must be an integer')
        if self.__height < 0:
            raise ValueError('height must be >= 0')

    def area(self):
        """
        Finds the area of a rectangle
        Returns:
             int: the area of the square
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Finds the perimeter of a rectangle
        Returns:
             int: the perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0

        return (2 * self.__width) + (2 * self.__height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Finds the biggest rectangle instance based on the area
        Args:
            rect_1 (Rectangle): first rectangle object
            rect_2 (Rectangle): second rectangle object
        Returns:
             Rectangle: the biggest rectangle based on area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')

        if rect_1.area() > rect_2.area():
            return rect_1
        elif rect_2.area() > rect_1.area():
            return rect_2
        if rect_1.area() == rect_2.area():
            return rect_1
