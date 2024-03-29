#!/usr/bin/python3
'''Rectangle Module'''
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    '''class inherits from BaseGeometry'''
    def __init__(self, width, height):
        self.integer_validator("height", height)
        self.__height = height
        self.integer_validator("width", width)
        self.__width = width

    def area(self):
        '''returns the area of a rectangle'''
        return self.__height * self.__width

    def __str__(self):
        '''returns the class and it variables'''
        return f"[Rectangle] {self.__width}/{self.__height}"
