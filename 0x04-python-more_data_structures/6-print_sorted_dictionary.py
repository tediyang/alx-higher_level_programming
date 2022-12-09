#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    new = sorted(a_dictionary)

    for i in new:
        print(f"{i}: {a_dictionary.get(i)}")
