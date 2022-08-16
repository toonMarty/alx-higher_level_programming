#!/usr/bin/python3
"""
This module contains a function
write_file() that writes into a
file and returns the number of characters
written
"""


def write_file(filename="", text=""):
    """
    A method that writes a file
    and overwrites any contents if they
    already exist
    Args
        filename: the name of the file
        text: the text to write to said file
    Returns
        write_data (int): number of characters written
    """
    with open(filename, mode='w', encoding='utf-8') as f:
        write_data = f.write(text)
        return write_data
