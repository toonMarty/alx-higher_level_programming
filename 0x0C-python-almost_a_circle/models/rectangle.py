#!/usr/bin/python3
"""
This module contains a Rectangle class
that inherits from the Base class
"""
Base = __import__('base').Base


class Rectangle(Base):
    """A class that defines a Rectangle
    """
    def __init__(self, __width, __height, __x=0, __y=0, id=None):
        """
        This method initializes Rectangle object(s)
        Args:
        __width: width of the Rectangle
        __height: height of the Rectangle
        __x: the x dimension
        __y: the y dimension
        id: the class id
        """
        super().__init__(id)
        self.__width = __width
        self.__height = __height
        self.__x = __x
        self.__y = __y

        if not isinstance(self.__width, int):
            raise TypeError('width must be an integer')
        if not isinstance(self.__height, int):
            raise TypeError('height must be an integer')
        if not isinstance(self.__x, int):
            raise TypeError('x must be an integer')
        if not isinstance(self.__y, int):
            raise TypeError('y must be an integer')
        if self.__width <= 0:
            raise ValueError('width must be > 0')
        if self.__height <= 0:
            raise ValueError('height must be > 0')
        if self.__x < 0:
            raise ValueError('x must be >= 0')
        if self.__y < 0:
            raise ValueError('y must be >= 0')

    @property
    def width(self):
        """
        gets the width of a Rectangle
        sets the width of a Rectangle
        Returns:
            self.__width: the value of the width
        """
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value
        if not isinstance(self.__width, int):
            raise TypeError('width must be an integer')
        if self.__width <= 0:
            raise ValueError('width must be > 0')

    @property
    def height(self):
        """
        gets the height of a Rectangle
        sets the height of a Rectangle
        Returns:
            self.__height: the value of the height
        """
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value
        if not isinstance(self.__height, int):
            raise TypeError('height must be an integer')
        if self.__height <= 0:
            raise ValueError('height must be > 0')

    @property
    def x(self):
        """
        gets the value of a Rectangle's x
        sets the value of a Rectangle's x
        Returns:
            self.__x: the value of x
        """
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value
        if not isinstance(self.__x, int):
            raise TypeError('x must be an integer')
        if self.__x < 0:
            raise ValueError('x must be >= 0')

    @property
    def y(self):
        """
        gets the value of a Rectangle's y
        sets the value of a Rectangle's y
        Returns:
            self.__y: the value of y
        """
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
        if not isinstance(self.__y, int):
            raise TypeError('y must be an integer')
        if self.__y < 0:
            raise ValueError('y must be >= 0')

    def area(self):
        """
        This method returns the area of a Rectangle object
        Returns:
            area (int): the area of the rectangle
        """
        return self.__width * self.__height

    def display(self):
        """
        This method displays a rectangle using the
        # character
        """
        for i in range(self.__height):
            for m in range(self.__x):
                for n in range(self.__y):
                    print(' ', end='')
            for j in range(self.__width):
                print('#', end='')
            print()

    def __str__(self):
        """
        This method returns a string representation
        of a Rectangle instance by overriding the
        str magic method
        """
        return f'[Rectangle] ({self.id}) ' \
               f'{self.__x}/{self.__y} - ' \
               f'{self.__width}/{self.__height}'

    def update(self, *args):
        self.id = args[0]
