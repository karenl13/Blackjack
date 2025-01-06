import unittest
from src.deck import Deck, Card
from src.hand import Hand

class DeckTestCase(unittest.TestCase):

    def setUp(self):  # this method will be run before each test
        self.deck = Deck()

    def tearDown(self):  # this method will be run after each test
        pass

    def test_number_of_cards(self):  # any method beginning with 'test_' will be run by unittest
        number_of_cards = len(self.deck.cards)
        self.assertEqual(number_of_cards, 52)


if __name__ == '__main__':
    unittest.main()

class HandTestCase(unittest.TestCase):

    def setUp(self):
        self.hand = Hand()
    
    def test_add_card(self):
        card = Card("5", "Hearts")
        self.hand.add_card(card)
        self.assertEqual(len(self.hand.cards), 1)

    def test_calculate_score_no_ace(self):
        self.hand.add_card(Card("5", "Hearts"))
        self.hand.add_card(Card("10", "Diamonds"))
        self.assertEqual(self.hand.calculate_score(ace_value=True), 15)

    def test_calculate_score_with_ace_high(self):
        self.hand.add_card(Card("Ace", "Hearts"))
        self.hand.add_card(Card("10", "Diamonds"))
        self.assertEqual(self.hand.calculate_score(ace_value=True), 21)

    def test_calculate_score_with_ace_low(self):
        self.hand.add_card(Card("Ace", "Hearts"))
        self.hand.add_card(Card("10", "Diamonds"))
        self.assertEqual(self.hand.calculate_score(ace_value=False), 11)

if __name__ == 'main':
    unittest.main()
