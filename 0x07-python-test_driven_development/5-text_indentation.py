#!/usr/bin/python3
'''Text indentation function'''


def text_indentation(text):
    '''This function prints a string and add indentation when necessary'''
    if text is None:
        raise TypeError("text_indentation() missing 1 required positional argument: 'text'")

    if not isinstance(text, str):
        raise TypeError('text must be a string')

    for i, c in enumerate(text):
        if c in ['.', '?', ':']:
            print(c, end='\n')
            continue
        if c == ' ' and i != 0 and text[i - 1] in ['.', '?', ':']:
            continue
        print(c, end='')
