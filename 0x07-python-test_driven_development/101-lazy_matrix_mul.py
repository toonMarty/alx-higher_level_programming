#!/usr/bin/python3
"""
This is the 101-lazy_matrix_mul module

The 101-lazy_matrix_mul module supplies one function, lazy_matrix_mul()
"""
import numpy
from numpy import matrix


def lazy_matrix_mul(m_a, m_b):
    """
    This function multiplies two matrices
    Args:
        param m_a(int, float): A compound object(list of list(s))
        param m_b(int, float): A compound object.

    Returns:
        (float, int): a new matrix product of m_a and m_b
    """
    if not isinstance(m_a, list):
        raise TypeError('m_a must be a list')
    if not isinstance(m_b, list):
        raise TypeError('m_b must be a list')
    for i in range(len(m_a)):
        if not isinstance(m_a[i], list):
            raise TypeError('m_a must be a list of lists')
    for i in range(len(m_b)):
        if not isinstance(m_b[i], list):
            raise TypeError('m_b must be a list of lists')

    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    for i in range(len(m_a)):
        if len(m_a[i]) == 0:
            raise ValueError("m_a can't be empty")
    for i in range(len(m_b)):
        if len(m_b[i]) == 0:
            raise ValueError("m_b can't be empty")

    for i in range(len(m_a)):
        for j in range(len(m_a[i])):
            if not isinstance(m_a[i][j], (int, float)):
                raise TypeError('m_a should contain only integers or floats')
    for i in range(len(m_b)):
        for j in range(len(m_b[i])):
            if not isinstance(m_b[i][j], (int, float)):
                raise TypeError('m_b should contain only integers or floats')
    for i in range(len(m_a)):
        if i != len(m_a) - 1:
            if len(m_a[i]) != len(m_a[i + 1]):
                raise TypeError('each row of m_a must be of the same size')
    for i in range(len(m_b)):
        if i != len(m_b) - 1:
            if len(m_b[i]) != len(m_b[i + 1]):
                raise TypeError('each row of m_b must be of the same size')

    res = numpy.dot(m_a, m_b)
    return res
