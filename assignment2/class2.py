#!/usr/bin/env python


import math


class Point(object):
    """ represents a point in 2-D space """
    
    def __init__(self, x, y):
        """ Point constructor: takes initial x,y values """
        self.x = x
        self.y = y

    def setXY(self, x, y):
        self.x = x
        self.y = y        

    def getXY(self):
        """ return the x,y coordinates as a tuple."""
        return (self.x, self.y)

    def distance(self, other):
        d = (self.x - other.x)** 2 + (self.y - other.y)** 2
        return math.sqrt(d)


class Rectangle(object):
    """ represent a rectangle. 
        attributes: width, heigh, corner.
    """

    def __init__(self, width, height, corner):
        self.width = width
        self.height = height
        self.corner = corner

    def __str__(self):
        return "Rectangle lower-left: ({:.1f}, {:.1f}) "
        "upper-right: ({:.1f}, {:.1f})".format(self.corner.x,
        self.corner.y, (self.corner.x + self.width), 
        (self.corner.y + self.height))

    def move_rectangle(self, px, py):
        px += self.corner.x
        py += self.corner.y
        new_point = (px, py)
        return new_point

    def perimeter(self):
        perimeter = (self.width*2 + self.height*2)
        return perimeter
    
    def area(self):
        area = self.width * self.height
        return area

class Circle(object):
    """ represents a circle.
        attributes: center point, diameter.
    """

    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def __str__(self):
        return "Circle ({:.1f}, {:.1f}) with radius {:.1f}".format(
                self.center.x, self.center.y, self.radius)

    def move_circle(self, dx, dy):
        dx += self.center.x
        dy += self.center.y
        new_center = (dx, dy)
        return new_center
    
    def perimeter(self):
        perimeter = self.radius * 2
        return perimeter

    def area(self):
        area = math.pi * self.radius**2
        return area

if __name__ == "__main__":

    r = Rectangle(100.0, 200.0, Point(0, 0))
    print(r)

    new_coords = r.move_rectangle(5, 3)
    print(new_coords)

    peri = r.perimeter()
    print(peri)

    area1 = r.area()
    print(area1)

    c = Circle(Point(0, 0), 400.0)
    print(c)

    peri_circle = c.perimeter() 
    print(peri_circle)

    area_circle = c.area()
    print(area_circle)

