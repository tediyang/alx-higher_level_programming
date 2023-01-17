#!/usr/bin/python3
'''read file function'''


def read_file(filename=""):
    '''prints the bytes converted to string in a file'''
    with open(filename, encoding="utf-8") as f:
        print(f.read())
