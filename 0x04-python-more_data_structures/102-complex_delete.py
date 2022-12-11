#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    new = a_dictionary.copy()
    for key in new.keys():
        if a_dictionary.get(key) == value:
            del a_dictionary[key]

    return a_dictionary
