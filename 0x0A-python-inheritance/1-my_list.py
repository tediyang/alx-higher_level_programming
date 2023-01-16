#!/usr/bin/python3
'''Mylist module'''


class Mylist(list):
    '''Inherit from list'''
    def print_sorted(self):
        '''print sorted list'''
        print(sorted(self))
