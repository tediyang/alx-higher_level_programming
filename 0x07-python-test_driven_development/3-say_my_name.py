#!/usr/bin/python3
'''Module for printing the first_name and last_name to the stdout.'''

def say_my_name(first_name, last_name=""):
    '''Print a string containing the first_name and last_name.'''

    if first_name is None:
        raise TypeError("say_my_name() missing 1 required positional argument: 'first_name'")
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')

    print(f"My name is {first_name} {last_name}")
