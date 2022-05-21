import unittest

from time_conversion import timeConversion


class TimeConversionTestCase(unittest.TestCase):
    def test_12pm(self):
        self.assertEqual(
            timeConversion('12:01:00PM'),
            '12:01:00'
        )

    def test_12am(self):
        self.assertEqual(
            timeConversion('12:01:00AM'),
            '00:01:00'
        )

    def test_am(self):
        self.assertEqual(
            timeConversion('07:07:07AM'),
            '07:07:07'
        )

    def test_pm(self):
        self.assertEqual(
            timeConversion('07:07:07PM'),
            '19:07:07'
        )