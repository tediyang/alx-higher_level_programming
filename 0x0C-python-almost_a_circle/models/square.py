#!/usr/bin/python3
'''Square Model'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''Square class that inherits from Rectangle'''
    def __init__(self, size, x=0, y=0 id=None):
        '''Intialization'''
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        '''size getter'''
        self.width

    @size.setter
    def size(self, value):
        '''size setter'''
        self.width = value
        self.height = value

    def __str__(self):
        return f'[Square] ({self.id}) {self.x}/{self.y} \
- {self.height}'
