#!/usr/bin/python3
"""
This module contains a method inherits_from()
that returns True if object is an instance of a class
(direct or indirect) or False otherwise
"""


def inherits_from(obj, a_class):
    """
    This method checks whether an object inherits from a specific class
    Args:
        obj: the object
        a_class: the class
    Returns:
         True(bool): if inherited from a class (directly or indirectly
         False(bool): otherwise
    """
    if not type(obj) is a_class:
        return True
    else:
        return False
