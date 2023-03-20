import unittest
from whiteboard import solution

class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(solution("Hey fellow coding temple students"), "Hey wollef gnidoc elpmet stneduts")

    def test_2(self):
        self.assertEqual(solution('This is a string of words'), 'This is a gnirts of sdrow')

    def test_3(self):
        self.assertEqual(solution('Clutch 112 is the best cohort ever'), 'hctulC 112 is the best trohoc ever')

if __name__== "__main__":
    unittest.main()