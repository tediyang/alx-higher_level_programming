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
        '''print the shape'''
        for i in range(self.y):
            print()
        for j in range(self.height):
            print(' ' * self.x, end='')
            for k in range(self.width):
                print("#", end='')
            print()

    def update(self, *args, **kwargs):
        '''Update the values'''
        attr = ['id', 'width', 'height', 'x', 'y']

        if len(args) > 0 and args is not None:
            for i, _ in enumerate(args):
                setattr(self, attr[i], args[i])
        else:
            if len(kwargs) > 0:
                for key, value in kwargs.items():
                    setattr(self, key, value)

    def to_dictionary(self):
        '''return dictionary representation'''
        return {'x': self.x, 'y': self.y, \
'id': self.id, 'height': self.height, 'width': self.width}

    def __str__(self):
        '''
            returns the parameters
        '''
        return f'[Rectangle] ({self.id}) {self.x}/{self.y} \
- {self.width}/{self.height}'
