#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new = matrix.copy()
    rows = len(new)
    for row in range(rows):
        for col in range(len(new[row])):
            new[row][col] *= new[row][col]

    return new
