#!/usr/bin/python3

def print_sortrd_dictionary(a_dictionary):
    new = sorted(a_dictionary)

    for i in new:
        print(f"{i}: {a_dictionary[i]}")
