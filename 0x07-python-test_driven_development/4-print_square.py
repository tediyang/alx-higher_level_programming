#!/usr/bin/python3
'''This module prints a square with the given size vale'''


def print_square(size):
    '''Prints a square with the provided square value'''

    if isinstance(size, float) and size < 0:
        raise TypeError('size must be an integer')
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')

    for _ in range(size):
        for _ in range(size):
            print('#', end='')
        print()
