import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        #self.assertEqual(True, True) --> False Positive
        #self.assertEqual('foo'.upper(), 'Foo') --> Red Light/Green Light test
        self.assertEqual('foo'.upper(), 'Foo')
    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()


