#!/usr/bin/env python

import math
import copy


class Point(object):
    '''represents a point in 2-D space'''

    def __init__(self, x, y):
        '''Point constructor: takes initial x,y values'''
        self.x = x
        self.y = y

    def setXY(self, x, y):
        '''Set x and y coordinates to new values.'''
        self.x = x
        self.y = y

    def getXY(self):
        ''' return the x,y coordinates as a tuple.'''
        return (self.x, self.y)

    def distance(self, other):
        ''' compute and return the Euclidean
            distance between this point and another.'''
        d = (self.x - other.x)**2 + (self.y - other.y)**2
        return math.sqrt(d)

    def __str__(self):
        return "Point ({:.1f},{:.1f})".format(self.x, self.y)


class Shape(object):
    """ A generic shape class. """
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __str__(self):
        return "I am a {} {}.".format(self.color, self.name)

    def area(self):
        return 0.0

    def perimeter(self):
        return 0.0


class Rectangle(Shape): 
    def __init__(self, corner, width, height, color):
        Shape.__init__(self, "rectangle", color)
        self.corner = corner
        self.width = width
        self.height = height

    def perimeter(self):
        return self.width * 2 + self.height * 2

    def area(self):
        return self.width * self.height


    def move_rec(self, dx, dy):
        self.corner.x += dx
        self.corner.y += dy
        new_corner = copy.deepcopy(self.corner)
        r2 = Rectangle(new_corner, self.width, self.height, self.color)
        return r2

class Circle(Shape):
    def __init__(self, center, radius, color):
        Shape.__init__(self, "circle", color)
        self.center = center
        self.radius = radius

    def diameter(self):
        return self.radius * 2

    def area(self):
        return math.pi * self.radius**2


if __name__ == "__main__":

    r = Rectangle(Point(3,5), 5, 10, "blue")
    print(r)
    print(r.perimeter())
    print(r.area())
    
    r2 = r.move_rec(4, 6)
    print(r2)


    """
    c = Circle(Point(10,20), 15, "orange")
    print(c)
    print(c.diameter())
    print(c.area())

    """


