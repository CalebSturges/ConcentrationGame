import unittest
from concentration import cards

class TestStringMethods(unittest.TestCase):

    def (self):
        self.assertEqual('foo'.upper(), 'FOO')

    def full_deck(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def empty_deck(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    def random_deck(self):
        pass

if __name__ == '__main__':
    unittest.main()
