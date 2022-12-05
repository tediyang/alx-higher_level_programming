#!/usr/bin/python3

def no_c(my_string):
    if my_string is None:
        return
    new = ""
    for i in my_string:
        if i != 'c' or i != 'C':
            new += i

    return new
