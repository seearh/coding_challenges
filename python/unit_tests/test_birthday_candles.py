import unittest

from python.birthday_candles import birthdayCakeCandles


class BirthdayCakeCandlesTestCase(unittest.TestCase):
    def test_multiple_tallest(self):
        self.assertEqual(
            birthdayCakeCandles([4, 4, 1, 3]), 2
        )
        self.assertEqual(
            birthdayCakeCandles([3, 2, 1, 3]), 2
        )

    def test_single_tallest(self):
        self.assertEqual(
            birthdayCakeCandles([1, 5, 4, 3]), 1
        )

    def test_all_same_height(self):
        self.assertEqual(
            birthdayCakeCandles([1, 1, 1, 1, 1, 1]), 6
        )
        