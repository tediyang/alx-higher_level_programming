#!/usr/bin/python3

def number_keys(a_dictionary):
    if len(a_dictionary) == 0:
        return 0

    count = 0
    for key in a_dictionary.keys():
        count += 1
    return count
