#!/usr/bin/python3
'''Square Module'''
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    '''class module inherits from rectangle'''
    def __init__(self, size):
        '''initialization'''
        self.integer_validator("size", size)
        self.__size = size
        Rectangle.__init__(self, size, size)

    def area(self):
        '''return the area of a square'''
        return self.__size ** 2
