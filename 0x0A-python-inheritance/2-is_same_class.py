#!/usr/bin/python3
'''class check module'''


def is_same_class(obj, a_class):
    '''check if they are the same class'''
    if isinstance(obj, a_class):
        return True
    return False
