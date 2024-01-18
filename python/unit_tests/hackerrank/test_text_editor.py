from unittest.mock import call, patch
import unittest

from hackerrank.text_editor import TextEditor


class TextEditorTestCase(unittest.TestCase):
    @patch('builtins.print')
    def test_sequence(self, mock_print):
        self.editor = TextEditor()
        self.editor.append('abc')
        self.assertEqual(self.editor._text, 'abc')
        self.editor.print(3)
        self.editor.delete(3)
        self.assertEqual(self.editor._text, '')
        self.editor.append('xy')
        self.editor.print(2)
        self.editor.undo()
        self.editor.undo()
        self.assertEqual(self.editor._text, 'abc')
        self.editor.print(1)
        mock_print.assert_has_calls(
            [call('c'), call('y'), call('a')]
        )