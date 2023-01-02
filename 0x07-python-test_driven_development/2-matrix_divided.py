#!/usr/bin/python3
'''Module that divides values of a matrix by the given divisor'''


def matrix_divided(matrix, div):
    ''' This function accepts 2 parameters; one a matrix and the
    other a divisor value which both parameters must either be ints
    or floats'''

    if len(matrix) == 0:
        raise TypeError('matrix should not be empty')

    if div == 0:
        raise ZeroDivisionError('division by zero')

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError('div must be a number')

    for i in matrix:
        check = list(map(lambda x: True if isinstance(x, int)
            or isinstance(x, float) else False, i))
        if not all(check):
            raise TypeError('matrix must be a matrix (list of lists) of integers/floats')

    length = len(matrix[0])
    for i in matrix:
        if len(i) != length:
            raise TypeError('Each row of the matrix must have the same size')

    return list(map(lambda x: list(map(lambda i: round(i / div, 2), x)), matrix))
