#!/usr/bin/python3
'''Square Model'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''Square class that inherits from Rectangle'''
    def __init__(self, size, x, y, id=None):
        '''Intialization'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f'[Square] ({self.id}) {self.x}/{self.y} - {self.height}'
