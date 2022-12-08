#!/usr/bin/python3

def common_elements(set_1, set_2):
    if len(set_1) == 0 or len(set_2) == 0:
        return []

    common = [i for i in set_1 if i in set_2]
    return common
