import unittest

from between_two_sets import getTotalX


class BetweenTwoSetsTestCase(unittest.TestCase):
    def test_balanced_brackets(self):
        self.assertEqual(
            getTotalX([2, 4], [16, 32, 96]),
            3,
        )