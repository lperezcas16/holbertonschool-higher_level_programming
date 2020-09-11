#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [[cel ** 2 for cel in row]for row in matrix]
    return new_matrix
