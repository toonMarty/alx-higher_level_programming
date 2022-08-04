#!/usr/bin/python3
"""This module contains a method lookup() that returns
a list of available attributes and methods of an object"""


def lookup(obj):
    """
    This method returns
    a list of available attributes and methods of an object
    Args:
        obj: the object to lookup from
    Returns:
         list: list of attributes and methods
    """
    return list(dir(obj))
