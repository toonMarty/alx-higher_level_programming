#!/usr/bin/python3
"""
This module contains a function that adds an
attribute to an object
"""


def add_attribute(obj, name, value):
    """
    The function that adds the attributes
    Args:
        obj: the object
        name: the name of the object
        value: the value of the attribute
    Returns:
        value: the set attribute
    """
    if type(obj):
        return setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
