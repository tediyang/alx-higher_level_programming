#!/usr/bin/python3
'''BaseGeometry Module'''


class BaseGeometry:
    '''
        class BaseGeometry with 2 public instances.
        area() raises an exception.
        integer_validator() validates an integer.
    '''
    def area(self):
        '''raises an exception'''
        raise Exception('area() is not implemented')
    def integer_validator(self, name, value):
        '''accepts two parameters and validate the value arg'''
        if not isinstance(value, int):
            raise TypeError(f'{name} must be an integer')
        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')
