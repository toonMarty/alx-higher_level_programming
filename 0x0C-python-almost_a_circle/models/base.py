#!/usr/bin/python3
"""
This module contains a class Base.
This class will be the “base” of all other classes in this project.
The goal of it is to manage id attribute in all your future classes
and to avoid duplicating the same code (by extension, same bugs)
"""


class Base:
    """The Base class that manages id attributes
    """
    _nb_objects = 0  # private class attribute

    def __init__(self, id=None):
        """
        This method initializes Base class instances
        Args:
            id (int): public instance attribute identifier for
            class instances
        """
        self.id = id

        if id is not None:
            self.id = id
        else:
            Base._nb_objects += 1
            self.id = Base._nb_objects
