import unittest
from io import StringIO
from unittest.mock import patch

from hackerrank.plus_minus import plusMinus


class PlusMinusTestCase(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_mixed_with_precision(self, mock_stdout):
        plusMinus([-4, 3, -9, 0, 4, 1])
        self.assertEqual(
            mock_stdout.getvalue(),
            '0.500000\n'
            '0.333333\n'
            '0.166667\n'
        )

    @patch('sys.stdout', new_callable=StringIO)
    def test_no_zero(self, mock_stdout):
        plusMinus([100, -100, -100, 100])
        self.assertEqual(
            mock_stdout.getvalue(),
            '0.500000\n'
            '0.500000\n'
            '0.000000\n'
        )

    @patch('sys.stdout', new_callable=StringIO)
    def test_no_positives(self, mock_stdout):
        plusMinus([0, -3, 0, -13, 0, -1, -53, -100])
        self.assertEqual(
            mock_stdout.getvalue(),
            '0.000000\n'
            '0.625000\n'
            '0.375000\n'
        )

    @patch('sys.stdout', new_callable=StringIO)
    def test_no_negatives(self, mock_stdout):
        plusMinus(list(range(10)))
        self.assertEqual(
            mock_stdout.getvalue(),
            '0.900000\n'
            '0.000000\n'
            '0.100000\n'
        )