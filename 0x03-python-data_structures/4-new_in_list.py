#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if my_list is None:
        return
    new = my_list.copy()
    new[idx] = element

    return new
