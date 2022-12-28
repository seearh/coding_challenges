import unittest

from birthday_bar import birthday


class BirthdayBarTestCase(unittest.TestCase):
    def test_many_segments_1(self):
        self.assertEqual(
            birthday(
                [2, 2, 1, 3, 2],
                4,
                2,
            ),
            2,
        )
    
    def test_many_segments_2(self):
        self.assertEqual(
            birthday(
                [1, 2, 1, 3, 2],
                3,
                2,
            ),
            2,
        )
    
    def test_no_segments(self):
        self.assertEqual(
            birthday(
                [1, 1, 1, 1, 1, 1],
                3,
                2,
            ),
            0,
        )
    
    def test_one_segment(self):
        self.assertEqual(
            birthday(
                [4],
                4,
                1,
            ),
            1,
        )