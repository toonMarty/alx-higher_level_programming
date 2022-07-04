#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        print('{:d}'.format(matrix[i]).replace(',', '', 1000000).
              replace('[', '', 1000000).
              replace(']', '', 1000000))
