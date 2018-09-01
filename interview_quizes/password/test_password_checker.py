import unittest

from password_checker import pword_checker

class Test_passwords(unittest.TestCase):
    def test_1(self):
        self.assertAlmostEqual(pword_checker(), "ABd1234@1")
