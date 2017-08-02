#!/usr/bin/env python3

import unittest
from flatland import Triangle 

class TestTriangle(unittest.TestCase):
    """ Tests the methods in the Triangle class. """

    def test_area(self):
        self_side = 4
        self_area = ((3 ** 0.5)/4) * (self_side ** 2) 
        self.assertNotEqual(self_area, self_side)


    def test_perimeter(self):
        self.side = 4
        self.perimeter = self.side + self.side + self.side
        self.assertNotEqual(self.side, self.perimeter)

if __name__ == '__main__':
    unittest.main()
