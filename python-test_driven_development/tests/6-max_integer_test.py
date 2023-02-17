#!/usr/bin/python3
"""
Unit Test for max_integer()
"""

import unittest

max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_MaxEnd(self):
        self.assertEqual(max_integer([1, 1, 1, 2]), 2)

    def test_MaxStart(self):
        self.assertEqual(max_integer([2, 1, 1, 1]), 2)

    def test_MaxMid(self):
        self.assertEqual(max_integer([1, 2, 1]), 2)

    def test_OneNegative(self):
        self.assertEqual(max_integer([1, 1, -1, 2]), 2)

    def test_OneNegative(self):
        self.assertEqual(max_integer([-1, -1, -1, -2]), -1)

    def test_OneArg(self):
        self.assertEqual(max_integer([1]), 1)

    def test_NoArg(self):
        self.assertEqual(max_integer(), None)

if __name__=='__main__':
    unittest.main()
