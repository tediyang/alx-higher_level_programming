#!/usr/bin/python3

def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except ValueError as val:
        print("Exception: {}".format(val))
        return False
    except TypeError as typ:
        print("Exception: {}".format(typ))
        return False
