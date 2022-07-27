#!/usr/bin/python3
"""
This is the 2-matrix_divided module

The 2-matrix_divided module supplies one function, matrix_divided()
"""


def matrix_divided(matrix, div):
    """
    This function divides elements of a matrix(list of lists)
    with a number, div.
    div can be an int or a float
    Args:
        param matrix (int, float): A compound object(list of list(s))
        param div (int, float): The number to divide each element
        of the matrix by.

    Returns:
        float: a new matrix
    """
    res = [list(x) for x in matrix]

    for i in range(len(matrix)):
        # for j in range(len(matrix[i])):
        if not isinstance(matrix[i], list):
            # if not isinstance(matrix[i][j], (int, float)):
            raise TypeError('matrix must be a matrix (list of lists) '
                            'of integers/floats')
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')

    for i in range(len(matrix)):
        if len(matrix[i]) == 0:
            raise IndexError('Cannot divide an empty matrix')

    for i in range(len(matrix)):
        if i != len(matrix) - 1:
            if len(matrix[i]) != len(matrix[i + 1]):
                raise TypeError('each row of the matrix '
                                'must have the same size')

    for i in range(len(matrix)):    # row
        for j in range(len(matrix[i])):     # column
            res[i][j] = float((matrix[i][j] / div).__format__('.2f'))
    return res
