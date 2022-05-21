import unittest

from triplets import compareTriplets


class TripletsTestCase(unittest.TestCase):
    def test_with_tie(self):
        self.assertEqual(
            compareTriplets([1, 2, 3], [3, 2, 1]),
            (1, 1)
        )
        self.assertEqual(
            compareTriplets([5, 6, 7], [3, 6, 10]),
            (1, 1)
        )

    def test_no_tie(self):
        self.assertEqual(
            compareTriplets([17, 28, 30], [99, 16, 8]),
            (2, 1)
        )