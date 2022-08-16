#!/usr/bin/python3
"""
This module contains a function that reads
and prints contents of a file
"""


def read_file(filename=""):
    """
    A method that reads a file and
    prints the contents of a file
    Args:
        filename: the name of the file
    """
    with open(filename, encoding="utf-8") as f:
        read_data = f.read()
        print(read_data)
