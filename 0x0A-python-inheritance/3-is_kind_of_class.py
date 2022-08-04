#!/usr/bin/python3
"""
This module contains a method is_kind_of_class()
that checks whether an object is an instance of a
class or inherited from a class
"""


def is_kind_of_class(obj, a_class):
    """
    This method checks whether an object is an
    instance of a class or inherited from a class

    Args:
        obj: the object
        a_class: the class to which the object belongs
    Returns:
         True(bool): if isinstance
         False(bool): if not isinstance
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
