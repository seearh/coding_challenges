import random
import unittest
from io import StringIO
from unittest.mock import patch

from python.minimax_sum import miniMaxSum


class MiniMaxSumTestCase(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_ordered(self, mock_stdout):
        miniMaxSum([1, 3, 5, 7, 9])
        self.assertEqual(
            mock_stdout.getvalue(),
            '16 24\n'
        )

    @patch('sys.stdout', new_callable=StringIO)
    def test_unordered(self, mock_stdout):
        arr = [1, 3, 5, 7, 9]
        random.shuffle(arr)
        miniMaxSum(arr)
        self.assertEqual(
            mock_stdout.getvalue(),
            '16 24\n'
        )

    @patch('sys.stdout', new_callable=StringIO)
    def test_equal_elements(self, mock_stdout):
        miniMaxSum([3, 3, 3, 3, 3])
        self.assertEqual(
            mock_stdout.getvalue(),
            '12 12\n'
        )