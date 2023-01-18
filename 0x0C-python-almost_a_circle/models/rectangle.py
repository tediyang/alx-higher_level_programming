#!/usr/bin/python3
'''
    Rectangle Model
'''
from models.base import Base


class Rectangle(Base):
    '''
        Rectangle class that inherits from Base
    '''
    def __init__(self, width, height, x=0, y=0, id=None):
        '''
            Initialization
        '''
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.id = id
        if self.id is None:
            Base.__init__(self, id)

    def setter_validator(self, name, value):
        '''validate the values before assignment'''
        if not isinstance(value, int):
            raise TypeError(f'{name} must be an integer')
        if name in ('width', 'height'):
            if value <= 0:
                raise ValueError(f'{name} must be > 0')
        if value < 0:
            raise ValueError(f'{name} must be >= 0')

    @property
    def width(self):
        '''
            width getter
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''
            width setter
        '''
        self.setter_validator("width", value)
        self.__width = value

    @property
    def height(self):
        '''
            height getter
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''
            height setter
        '''
        self.setter_validator("height", value)
        self.__height = value

    @property
    def x(self):
        '''
            x getter
        '''
        return self.__x

    @x.setter
    def x(self, value):
        '''
            x setter
        '''
        self.setter_validator("x", value)
        self.__x = value

    @property
    def y(self):
        '''
            y getter
        '''
        return self.__y

    @y.setter
    def y(self, value):
        '''
            y setter
        '''
        self.setter_validator("y", value)
        self.__y = value

    def area(self):
        '''
            get the area
        '''
        return self.width * self.height

    def display(self):
        for i in range(self.height):
            for j in range(self.width):
                print('#')
            print()
