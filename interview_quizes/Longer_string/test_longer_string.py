import unittest

from longer_string import printValue


class MyTest(unittest.TestCase):

    def test_in_one(self):
        self.assertGreater(printValue('cdd','dssde') ,'dssde')

    def test_in_two(self):
        self.assertGreater(printValue('dssde','cdd') ,'dssde')

    def test_in_three(self):
        self.assertEqual(printValue('bcc','cdd') ,'bcc,cdd')
      