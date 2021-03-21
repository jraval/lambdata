# Write some code using unittest to test our enlarge() function works as desired

import unittest
from mylambdata.mymod import enlarge

class TestMyMod(unittest.TestCase):
    def test_enlarge(self):
        self.assertEqual('foo'.upper(), 'FOO')
        self.assertEqual(enlarge(9), 900)
        #self.assertEqual(enlarge(9), 90)#Red Light Test
        #enlarge(9)

if __name__ == '__main__':
    unittest.main()