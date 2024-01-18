import unittest
from io import StringIO
from unittest.mock import patch

from hackerrank.apples_and_oranges import countApplesAndOranges


class ApplesAndOrangesTestCase(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_example(self, mock_stdout):
        countApplesAndOranges(
            s=7, t=10, a=4, b=12,
            apples=[2, 3, -4],
            oranges=[3, -2, -4],
        )
        self.assertEqual(
            mock_stdout.getvalue(),
            '1\n'
            '2\n'
        )
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_sample(self, mock_stdout):
        countApplesAndOranges(
            s=7, t=11, a=5, b=15, 
            apples=[-2, 2, 1],
            oranges=[5, -6],
        )
        self.assertEqual(
            mock_stdout.getvalue(),
            '1\n'
            '1\n'
        )