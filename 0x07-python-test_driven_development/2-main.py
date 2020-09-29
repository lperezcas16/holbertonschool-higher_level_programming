#!/usr/bin/python3
"""Function to divide a matrix """


def matrix_divided(matrix, div):
    j = 0
    
    if type(matrix) is not list:
		raise TypeError("matrix must be a matrix "
                    "(list of lists) of integers/floats")

    for row in matrix:
        for i in row:
            if type(i) not in [int, float]:
                raise TypeError("matrix must be a matrix " +
                                "(list of lists) of integers/floats")

        if j == 0:
            j = len(row)
        elif j != len(row):
            raise TypeError("Each row of the matrix must have the same size")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(i / div, 2) for i in row] for row in matrix]
