import unittest

from diagonal_diff import diagonalDifference


class DiagonalDifferenceTestCase(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(
            diagonalDifference([
                [1, 2, 3],
                [4, 5, 6],
                [9, 8, 9],
            ]), 2
        )
        self.assertEqual(
            diagonalDifference([
                [11, 2, 4],
                [4, 5, 6],
                [10, 8, -12],
            ]), 15
        )

    def test_absolute_diff(self):
        self.assertEqual(
            diagonalDifference([
                [3, 2, 1],
                [6, 5, 4],
                [9, 8, 9],
            ]), 2
        )
        self.assertEqual(
            diagonalDifference([
                [4, 2, 11],
                [6, 5, 4],
                [-12, 8, 10],
            ]), 15
        )
        