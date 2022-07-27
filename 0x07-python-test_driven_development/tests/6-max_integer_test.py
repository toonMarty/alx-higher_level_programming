#!/usr/bin/python3
"""
This is the 6-max_integer_test module

The 6-max_integer_test module tests different cases of max_integer
"""
import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """A class that tests the max integer using various cases
    """
    def test_max_integer(self):
        """
        This method tests the function and whether the
        function returns expected values
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([-1, -3, -2, -10]), -1)

    def test_types(self):
        """
        This method tests various data types passed as
        arguments to the function, max_integer()
        """
        self.assertRaises(TypeError, max_integer, ['a', 'b', 'c'])
        self.assertRaises(TypeError, max_integer, '[1, 2, 3]')
        self.assertRaises(TypeError, max_integer, (1, 2, 3, 4))
        self.assertRaises(TypeError, max_integer, [1.0, 2.0, 3.5, 4.9])
