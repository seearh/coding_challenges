import unittest

from hackerrank.between_two_sets import getTotalX


class BetweenTwoSetsTestCase(unittest.TestCase):
    def test_between_two_sets(self):
        self.assertEqual(
            getTotalX([2, 4], [16, 32, 96]),
            3,
        )