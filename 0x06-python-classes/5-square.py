#!/usr/bin/python3
""" Class Square that defines a square by
    Private instance attribute: size
    Instantiation with optional size
    size must be an integer. Get the area 
    and print the result.
"""


class Square:
    """Class constructor"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) != int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        return self.size ** 2

    def my_print(self):
        if self.size == 0:
            print()
        else:
            for i in range(self.size):
                print('#' * self.size)
