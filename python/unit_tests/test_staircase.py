import unittest
from io import StringIO
from unittest.mock import patch

from staircase import staircase


class PlusMinusTestCase(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_mixed_with_precision(self, mock_stdout):
        staircase(6)
        self.assertEqual(
            mock_stdout.getvalue(),
            '     #\n'
            '    ##\n'
            '   ###\n'
            '  ####\n'
            ' #####\n'
            '######\n'
        )