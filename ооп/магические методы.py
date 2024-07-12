from typing import Any


class Point:
    MAX_COORD = 100
    MIN_COORD = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_coords(self, x, y):
        if self.MIN_COORD <= x <= self.MAX_COORD:
            self.x = x
            self.y = y
    
    def __getattribute__(self, item):
        if item == 'x':
            raise ValueError('доступ')
        else:
            return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        if key == 'z':
            raise AttributeError('ytljcneg: ')
        else:
            object.__setattr__(self, key, value)

    def __getattr__(self,item):
        return False
    

    def __delattr__(self, item):
        print('delattr ' + item)
        object.__delattr__(self, item)
pt1 = Point(1,2)
pt2 = Point(10,20)

del pt1.x
print(pt1.__dict__)