#!/usr/bin/python3
'''convert from json string function'''
import json


def from_json_string(my_str):
    '''convert json string toobject'''
    return json.loads(my_str)
