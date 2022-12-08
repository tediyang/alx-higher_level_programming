#!/usr/bin/python3

def search_replace(my_list, search, replace):
    if len(my_list) == 0:
        return my_list

    new = my_list.copy()
    for i, n in enumerate(new):
        if n == search:
            new[i] = replace

    return new
