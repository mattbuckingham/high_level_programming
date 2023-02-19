#!/usr/bin/python3
"""

"""


import unittest
from models import rectangle
from models.base import Base
Rectangle = rectangle.Rectangle

class TestRectangle(unittest.TestCase):
    """

    """

    def test_2_arg(self):
        """
        make a simple rec, test width
        """
        r = Rectangle(1, 2)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)

    def test_3_arg(self):
        """
        rec with an x value
        """
        r1 = Rectangle(1, 2, 3)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)

    def test_4_arg(self):
        """
        rec with a y value
        """
        r2 = Rectangle(1, 2, 3, 4)
        self.assertEqual(r2.y, 4)

    def test_5_arg(self):
        """

        """
        r3 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r3.id, 5)

    def test_wrong_type(self):
        """
        test
        """
        self.assertRaises(TypeError, Rectangle, ["1", 2])
        self.assertRaises(TypeError, Rectangle, [1, "2"])
        self.assertRaises(TypeError, Rectangle, [1, 2, "3"])
        self.assertRaises(TypeError, Rectangle, [1, 2, 3, "4"])

    def test_neg_val(self)
    """
    test
    """
