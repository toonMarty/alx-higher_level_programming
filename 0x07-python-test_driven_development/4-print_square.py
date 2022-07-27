#!/usr/bin/python3
"""
This is the 4-print_square module

The 4-print_square module supplies one function, print_square()
"""


def print_square(size):
    """
    This function prints a square using the # character
    Args:
        param size (int): size of the square

    Returns:
        nothing
    """
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')

    if isinstance(size, float) and size < 0:
        raise TypeError('size must be an integer')

    for i in range(size):
        for j in range(size):
            print('#', end='')
        print()
