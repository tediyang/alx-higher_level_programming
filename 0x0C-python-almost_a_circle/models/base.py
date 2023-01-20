#!/usr/bin/python3
'''Base Model'''
import json
import os.path


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
        if list_dictionaries is None or len(list_dictionaries) < 1:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''save json string to file'''
        list_dic = []
        filename = f'{cls.__name__}.json'
        if list_objs is not None:
            list_dic = [dic.to_dictionary() for _, dic in enumerate(list_objs)]

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(cls.to_json_string(list_dic))

    @staticmethod
    def from_json_string(json_string):
        '''convert from json string'''
        if json_string is None or len(json_string) < 1:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''create a class'''
        if cls.__name__ == 'Square':
            dummy = cls(1)
        else:
            dummy = cls(1, 2)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        '''load data from a json file'''
        filename = f'{cls.__name__}.json'

        if os.path.exists(filename) is False:
            return []

        with open(filename, 'r', encoding='utf-8') as f:
            read_file = f.read()

        conv_file = cls.from_json_string(read_file)
        conv_list = [cls.create(**dic) for _, dic in enumerate(conv_file)]

        return conv_list
