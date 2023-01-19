#!/usr/bin/python3
'''Square Model'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''Square class that inherits from Rectangle'''
    def __init__(self, size, x=0, y=0, id=None):
        '''Intialization'''
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        '''size getter'''
        return self.width

    @size.setter
    def size(self, value):
        '''size setter'''
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        '''update the parameter values'''
        params = ['id', 'size', 'x', 'y']
        if args is not None and len(args) > 0:
            for i, _ in enumerate(args):
                setattr(self, params[i], args[i])
        else:
            if len(kwargs) > 0:
                for key, value in kwargs.items():
                    setattr(self, key, value)

    def __str__(self):
        return f'[Square] ({self.id}) {self.x}/{self.y} \
- {self.width}'
