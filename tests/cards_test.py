import unittest
from concentration import cards

class TestStringMethods(unittest.TestCase):

  def enum_card(self):
    self.assertEqual(cards.Suit.spade, cards.Suit['spade'])
    self.assertEqual(cards.Suit.heart.value, cards.Suit.diamond.value)
    with self.assertRaises(ValueError)
      cards.Suit('spade')

  def shuffle_deck(self):
    self.assertEqual(cards.Deck(shufflenum=0), cards.Deck(shufflenum=0))
    self.assertUnequal(cards.Deck(shufflenum=1), cards.Deck(shufflenum=0))
    self.assertUnequal(cards.Deck(shufflenum=1), cards.Deck(shufflenum=1)
    

  def full_deck(self):
        self.assertTrue(len(cards.Deck().stack)==52)
        self.assertTrue(len(cards.Deck(jokers=True).stack)==54)

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
