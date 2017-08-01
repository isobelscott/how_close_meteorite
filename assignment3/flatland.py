#!/usr/bin/env python

import math
import time

class Shape(object):
    """ Defines a geometric shape."""
    @staticmethod
    def ea_list(ealist):
        return str(', '.join(str(p) for p in ealist))
    
    def __init__(self, side):
        self.side = side

    def __str__(self):
        return "My name is %s and I am a %s." % (self.shape_name, self.shape_type)

    def update_side_length(self, change):
        self.side = self.side + change
        return self.side

    def add_ally(self, shape_object):
        self.__class__.allies.add(shape_object)
        return list(self.__class__.allies)
  
    def add_enemy(self, shape_object):
        self.__class__.enemies.add(shape_object)
        return list(self.__class__.enemies)

    def give_name(self, shape_name):
        self.shape_name = shape_name
        return self.shape_name


class Triangle(Shape):
    """ Contains methods specific to an equilateral triangle."""    
    shape_type = "Triangle"
    allies = set()
    enemies = set()


    def __init__(self, length):
        super().__init__(length)

    def area(self):
        self.area = ((3**0.5)/4 * self.side * self.side)
        return self.area

    def perimeter(self):
        self.perimeter = self.side * 3
        return self.perimeter
    

class Square(Shape):
    """ Contains methods specific to a square."""
    shape_type = "Square"
    allies = set()
    enemies = set()
    
    def area(self):
        area = self.side * self.side
        return area

    def perimeter(self):
        perimeter = self.side * 4
        return perimeter


class Circle(Shape):
    """ Contains methods specific to a circle with the side being the radius."""
    shape_type = "Circle"
    allies = set()
    enemies = set()
    
    def area(self):
        area = math.pi * self.side * self.side 
        return area

    def circumference(self):
        c = 2 * math.pi * self.side
        return c
        

if __name__ == '__main__':
    
    tri1 = Triangle(4.0)
    Shape.give_name(tri1, "Aaron")
    triangle_allies = Shape.add_ally(tri1,"Circle") 
    triangle_enemies = Shape.add_enemy(tri1,"Square")
    
    squ1 = Square(2.1)
    Shape.give_name(squ1, "Titus")
    square_enemies = Shape.add_enemy(squ1, "Triangle")
    square_enemies = Shape.add_enemy(squ1, "Circle")
    
    cir1 = Circle(6.2)
    Shape.give_name(cir1, "Tamora")
    circle_allies = Shape.add_ally(cir1, "Triangle")
    circle_enemies = Shape.add_enemy(cir1, "Square")

    print(tri1)
    tri1allies = Shape.ea_list(triangle_allies)
    tri1enemies = Shape.ea_list(triangle_enemies)
    print("I am friends with " + tri1allies + " and enemies with " + tri1enemies + '\n') 
    time.sleep(2)

    print(cir1)
    cir1allies = Shape.ea_list(circle_allies)
    cir1enemies = Shape.ea_list(circle_enemies)
    print("I am friends with " + cir1allies + " and enemies with " + cir1enemies + '\n')
    time.sleep(2)

    print(squ1)
    squ1allies = "no one"
    squ1enemies = Shape.ea_list(square_enemies)
    print("I am friends with " + squ1allies + " and enemies with " + squ1enemies + '\n')



