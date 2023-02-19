#!/usr/bin/python3
"""
test base class
"""

import unittest
from models import base
Base = base.Base


class TestBase(unittest.TestCase):
    """
    test base class
    """

    def test_no_id(self):
        """
        test id being assigned
        """
        b = Base()
        self.assertEqual(b.id, 1)

    def test_no_id_again(self):
        """
        test id being incremented
        """
        b1 = Base()
        self.assertEqual(b1.id, 2)

    def test_set_id(self):
        """
        test passing in an id
        """
        b2 = Base(69)
        self.assertEqual(b.id, 69)
