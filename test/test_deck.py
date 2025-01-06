import unittest
from src.deck import Deck, Card
from src.hand import Hand

class DeckTestCase(unittest.TestCase):

    def setUp(self):
        self.deck = Deck()

    def tearDown(self):
        pass

    def test_number_of_cards(self):
        """
        Test that there are 52 cards in the deck.
        """
        number_of_cards = len(self.deck.cards)
        self.assertEqual(number_of_cards, 52)

    def test_unique_cards(self):
        """
        Test that each individual card has a unique value and suit combination.
        """
        unique_cards = set(str(card) for card in self.deck.cards)
        self.assertEqual(len(unique_cards), 52)


if __name__ == '__main__':
    unittest.main()

class HandTestCase(unittest.TestCase):

    def setUp(self):
        self.hand = Hand()
    
    def test_add_card(self):
        """
        Test that a card is added to a hand.
            Checks number of cards in hand has increased.
        """
        card = Card("5", "Hearts")
        self.hand.add_card(card)
        self.assertEqual(len(self.hand.cards), 1)

    def test_calculate_score(self):
        """
        Test that the score of hand is calculated correctly.
        """
        self.hand.add_card(Card("5", "Hearts"))
        self.hand.add_card(Card("10", "Diamonds"))
        ace_inputs = []
        self.assertEqual(self.hand.calculate_score(ace_inputs), 15)

    def test_calculate_score_with_ace_high(self):
        """
        Test the Ace in a a hand is treated as 11.
            Checks score reflects 11 points added.
        """
        self.hand.add_card(Card("Ace", "Hearts"))
        self.hand.add_card(Card("10", "Diamonds"))
        ace_inputs = [True]
        self.assertEqual(self.hand.calculate_score(ace_inputs), 21)

    def test_calculate_score_with_ace_low(self):
        """
        Test the Ace in a a hand is treated as 1.
            Checks score reflects 1 points added.
        """
        self.hand.add_card(Card("Ace", "Hearts"))
        self.hand.add_card(Card("10", "Diamonds"))
        ace_inputs = [False]
        self.assertEqual(self.hand.calculate_score(ace_inputs), 11)
    
    def test_calculate_score_multiple_aces(self):
        """
        Test the Ace in a a hand is treated as 11 and 1.
            Checks score reflects 11 and 1 points added.
        """
        self.hand.add_card(Card("Ace", "Hearts"))
        self.hand.add_card(Card("Ace", "Spades"))
        self.hand.add_card(Card("9", "Diamonds"))
        ace_inputs = [True, False]  # First Ace is 11, second is 1
        self.assertEqual(self.hand.calculate_score(ace_inputs), 21)

if __name__ == 'main':
    unittest.main()
