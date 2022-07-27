#!/usr/bin/python3
"""
This is the 0-add_integer module

The 0-add_integer module supplies one function, add_integer()
"""


def add_integer(a, b=98):
    """
    This function adds two integers

    Args:
        param a (int): The first integer
        param b (int): The second integer

    Returns:
        int: the sum of the two integers
    """
    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')
    if isinstance(a, float):
        return int(a) + b
    if isinstance(b, float):
        return a + int(b)

    return a + b
