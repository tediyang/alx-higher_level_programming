#!/usr/bin/python3
'''Base Model'''
import json


class Base:
    '''Base class'''
    __nb_objects = 0

    def __init__(self, id=None):
        '''Initialization'''
        self.id = id
        if self.id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''to json string'''
        if list_dictionaries is None or \
len(list_dictionaries) < 1:
            return "[]"
        return json.dumps(list_dictionaries)
