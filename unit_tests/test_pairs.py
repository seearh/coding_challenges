import unittest

from pairs import pairs


class PairsTestCase(unittest.TestCase):
    def test_pairs_1(self):
        self.assertEqual(
            pairs(1, [1, 2, 3, 4]), 3
        )

    def test_pairs_2(self):
        self.assertEqual(
            pairs(2, [1, 5, 3, 4, 2]), 3
        )