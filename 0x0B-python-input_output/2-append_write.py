#!/usr/bin/python3
'''append to a file function'''


def append_write(filename="", text=""):
    '''append to a file'''
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
