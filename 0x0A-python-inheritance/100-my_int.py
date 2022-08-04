#!/usr/bin/python3
"""
This module contains a class MyInt that changes the behavior
of the __eq__ and __ne__ magic methods
"""


class MyInt(int):
    """A rebel class that defies the laws of equality and inequality
    """
    def __eq__(self, other):
        """
        This method checks for !equality
        Args:
            other: the other object
        Returns:
             True(bool): if not equal
             False(bool): if equal
        """
        return self.__int__() != other.__int__()

    def __ne__(self, other):
        """
        This method checks for equality
        Args:
            other: the other object
        Returns:
             True(bool): if equal
             False(bool): if not equal
        """
        return self.__int__() == other.__int__()
