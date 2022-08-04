#!/usr/bin/python3
"""
This module contains a class MyList that inherits from list
"""


class MyList(list):
    """A class that inherits from list
    """
    def print_sorted(self):
        """
        This method prints a list in ascending sort order
        Returns:
             nothing
        """
        for i in range(len(self)):
            if not isinstance(self[i], int):
                raise TypeError('elements should be of type int')
        my_list = self[:]
        my_list.sort()
        print(my_list)
