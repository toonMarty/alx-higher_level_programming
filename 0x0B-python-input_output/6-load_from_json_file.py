#!/usr/bin/python3
"""
This module contains a function
load_from_json() that creates an
object from a JSON file
"""
import json


def load_from_json_file(filename):
    """
    A function that creates an object from a
    json file
    Args:
        filename: the name of the file
    Returns:
        obj: the decoded object
    """
    with open(filename, mode='r', encoding='utf-8') as f:
        x = json.load(f)
        return x
