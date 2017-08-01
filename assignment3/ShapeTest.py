#!/usr/bin/env python3

import unittest
from flatland import Shape
from random import randint

class TestShape(unittest.TestCase):
    """ Tests the methods in the Shape class in flatland. """
    
    #  test the staticmethod to show list as individual strings
    def test_ea_list(self):
        self.myShape = Shape(4)
        self.ealist_template = 'a, b, c, d'
        list1 = list(['a','b','c','d'])
        self.ealist_test = self.myShape.ea_list(list1)
        self.assertEqual(self.ealist_template,self.ealist_test)

    # test the side length update
    def test_update_side_length(self):
        self.side = randint(1, 50)
        self.myShape = Shape(self.side)
        self.change = randint(-20, 20)
        self.side = self.side + self.change
        self.assertTrue(Shape(self.side))

    # test that the ally has been added to the ally list
    allies = []
    def test_add_ally(self):
        self.shape_object = 'a'
        allies = TestShape.allies
        allies.append(self.shape_object)
        self.assertEqual(allies, list(self.shape_object))

if __name__ == '__main__':
    unittest.main()

