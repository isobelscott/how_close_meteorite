#!/usr/bin/env python3

import unittest
from Shape import Shape


class TestShape(unittest.TestCase):
    """ Tests the Shape class in flatlands. """
    def setUp(self):
        self.myShape = Shape(4)
        self.ealist_template = 'a, b, c, d'
        list1 = list(['a','b','c','d'])
        print(list1)
        self.ealist_test = self.myShape.ea_list(list1)
        print(self.ealist_test)

    def test_ea_list(self):
        self.assertEqual(self.ealist_template,self.ealist_test)


if __name__ == '__main__':
    unittest.main()

