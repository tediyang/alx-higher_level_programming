#!/usr/bin/python3
'''Base Model'''


class Base:
    '''Base class'''
    __nb_objects = 0

    def __init__(self, id=None):
        '''Initialization'''
        self.id = id
        if self.id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
