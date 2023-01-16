#!/usr/bin/python3
'''MyInt Module'''


class MyInt(int):
    '''class inherits from int'''
    def __eq__(self, other):
        '''compares equally'''
        return int(self) != int(other)

    def __ne__(self, other):
        '''compares not equally'''
        return int(self) == int(other)
