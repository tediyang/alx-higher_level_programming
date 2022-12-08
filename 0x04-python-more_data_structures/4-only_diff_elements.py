#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    if len(set_1) == 0 or len(set_2) == 0:
        return list(set_1) or list(set_2)

    uncommon = [i for i in set_1 if i not in set_2]
    uncommon.extend([i for i in set_2 if i not in set_1])
    return uncommon
