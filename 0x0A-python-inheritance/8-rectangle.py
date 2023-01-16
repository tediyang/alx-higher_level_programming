#!/usr/bin/python3
'''Rectangle Module'''
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    '''class rectangle inherit from BaseGeometry'''
    def __init__(self, width, height):
        '''Initialize rectangle method'''
        self.integer_validator("height", height)
        self.__height = height
        self.integer_validator("width", width)
        self.__width = width
