#!/usr/bin/python3
"""
This module contains a function
from_json_to_string() that returns
an object represented by a JSON string
"""
import json


def from_json_string(my_str):
    """
    A method that returns an object
    represented by a JSON string
    Args:
        my_str: the string
    Returns:
        python data structure (obj): an object represented
        by a JSON string
    """
    return json.loads(my_str)
