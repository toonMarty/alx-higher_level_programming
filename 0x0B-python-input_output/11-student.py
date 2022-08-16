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

    def to_json(self, attrs=None):
        """
        This method retrieves a dictionary representation of a student
        instance
        Args:
            attrs: attributes of the class instance
        Returns:
             dict: a dictionary representation of a student instance
        """
        my_dict = {}
        if isinstance(attrs, list):
            for key in self.__dict__:
                for i in range(len(attrs)):
                    if attrs[i] == key:
                        my_dict[key] = self.__dict__[key]
            return my_dict
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """
        This method replaces all attributes of the student
        instance
        Args:
            json: a dictionary containing student attributes
        Returns:
             dict: The dictionary with new attributes set
        """
        return self.to_json(self.__dict__.update(json))
