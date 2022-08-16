#!/usr/bin/python3
"""
This module contains a function append_write()
that writes data to a file and appends new
data
"""


def append_write(filename="", text=""):
    """
    A method that returns appends a string
    at the end of a text file
    Args:
        filename: name of the file
        text: a sequence of characters to append
    Returns:
        append_data (int): number of characters added
    """
    with open(filename, mode='a', encoding='utf-8') as f:
        append_data = f.write(text)
        return append_data
