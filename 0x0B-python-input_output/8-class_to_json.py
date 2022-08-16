#!/usr/bin/python3
"""
This module contains a function that returns the
dictionary description with simple data structure
"""


def class_to_json(obj):
    """
    Args:
        obj: a class instance
    Returns:
         dict: a dictionary description of the object
    """
    return obj.__dict__
