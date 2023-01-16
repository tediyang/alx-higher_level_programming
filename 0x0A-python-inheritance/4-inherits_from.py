#!/usr/bin/python3
'''inherit from module'''


def inherits_from(obj, a_class):
    '''check if obj inherits from a_class'''
    return isinstance(obj, a_class) and type(obj) == a_class
