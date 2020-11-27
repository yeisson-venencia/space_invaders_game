from math import sqrt,pow

class Position(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, value):
        self.__y = value

    @staticmethod
    def distance(point_a, point_b):
        return sqrt(pow((point_a.x - point_b.x),2) + pow((point_a.y - point_b.y),2))