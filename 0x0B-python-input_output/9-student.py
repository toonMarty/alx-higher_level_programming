#!/usr/bin/python3
"""
This module contains a class Student that defines a student
and a method to_json() that retrieves a dictionary representation
of a student instance
"""


class Student:
    """A class that defines a student
    """
    def __init__(self, first_name, last_name, age):
        """
        This method initializes a student instance
        Args:
            first_name: student's first_name
            last_name:  student's last_name
            age: student's age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        A method that returns the dictionary representation
        of a student instance
        Returns:
            dict: a dictionary representation of a student instance
        """
        return self.__dict__
