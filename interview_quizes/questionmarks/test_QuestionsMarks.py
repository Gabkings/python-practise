import unittest

from QuestionsMarks import QsMarks

class Test_QuestionsMarks(unittest.TestCase):
    def test_string1(self):
        self.assertEqual(QsMarks("arrb6???4xxbl5???eee5"), "true")

    def test_string2(self):
        self.assertEqual(QsMarks("acc?7??sss?3rr1??????5"), "true")

    def test_string3(self):
        self.assertEqual(QsMarks("5??aaaaaaaaaaaaaaaaaaa?5?5"), "false")

    def test_string4(self):
        self.assertEqual(QsMarks("9???1???9???1???9"), "true")
    def test_string5(self):
        self.assertEqual(QsMarks("aa6?9"), "false")