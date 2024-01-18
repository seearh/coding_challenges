import unittest

from hackerrank.number_line_jumps import kangaroo


class NumberLineJumpsTestCase(unittest.TestCase):
    def test_YES(self):
        self.assertEqual(
            kangaroo(0, 3, 4, 2),
            'YES'
        )

    def test_NO(self):
        self.assertEqual(
            kangaroo(0, 2, 5, 3),
            'NO'
        )