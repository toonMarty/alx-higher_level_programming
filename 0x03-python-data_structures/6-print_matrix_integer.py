#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        print('{}'.format(matrix[i]).
              replace(',', '', 8).replace('[', '', 3).replace(']', '', 3))