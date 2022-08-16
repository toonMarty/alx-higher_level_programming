#!/usr/bin/python3
"""
This module contains a function that
returns the JSON representation of an object
"""
import json


def to_json_string(my_obj):
    """
    A method that returns the json
    representation of an object(string)
    Args:
        my_obj: the object
    Returns:
        str: a string representation of myobj
    """
    return json.dumps(my_obj)
