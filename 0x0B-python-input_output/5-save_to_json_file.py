#!/usr/bin/python3
"""
This module contains a function
save_to_json() that writes an object
to a text file, using a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """
    A function that writes an object to a
    text file, using a json representation
    Args:
        my_obj: the object
        filename: the text file
    Returns:
        obj: a serializable object
    """
    with open(filename, mode='w', encoding='utf-8') as f:
        return json.dump(my_obj, f)
