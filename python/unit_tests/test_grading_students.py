import unittest

from grading_students import gradingStudents


class GradingStudentsTestCase(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(
            gradingStudents([73, 67, 38, 33]),
            [75, 67, 40, 33]
        )