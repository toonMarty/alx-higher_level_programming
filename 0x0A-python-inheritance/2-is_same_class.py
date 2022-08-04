#!/usr/bin/python3
"""
This module contains a function is_same_class() that
returns True is object is exactly an instance of the specified class
otherwise False
"""


def is_same_class(obj, a_class):
    """
    This method checks whether an object is an
    exact instance of a class
    Args:
        obj: the object
        a_class: the class that the object should match
    Returns:
        True(bool): if object is exactly an instance of the class
        False(bool): otherwise
    """
    if type(obj) == a_class:
        return True
    else:
        return False
