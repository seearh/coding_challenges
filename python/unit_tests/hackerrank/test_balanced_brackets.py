import unittest

from hackerrank.balanced_brackets import isBalanced


class BalancedBracketsTestCase(unittest.TestCase):
    def test_balanced_brackets(self):
        for s in (
            r'{[()]}', 
            r'{{[[(())]]}}',
            r'({}[])',
        ):
            with self.subTest(s=s):
                self.assertEqual(isBalanced(s), 'YES')

    def test_unbalanced_brackets(self):
        for s in (
            r'{[(])}',
            r'{][)()]}',
        ):
            with self.subTest(s=s):
                self.assertEqual(isBalanced(s), 'NO')

    def test_all_open_brackets(self):
        self.assertEqual(isBalanced('([{([[[[[(({'), 'NO')

    def test_all_closed_brackets(self):
        self.assertEqual(isBalanced(']]]))]}'), 'NO')