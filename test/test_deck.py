import unittest
from src.deck import Deck, Card
from src.hand import Hand
from src.player import Player, Computer

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
        Test the Ace in a hand is treated as 11.
            Checks score reflects 11 points added.
        """
        self.hand.add_card(Card("Ace", "Hearts"))
        self.hand.add_card(Card("10", "Diamonds"))
        ace_inputs = [True]
        self.assertEqual(self.hand.calculate_score(ace_inputs), 21)

    def test_calculate_score_with_ace_low(self):
        """
        Test the Ace in a hand is treated as 1.
            Checks score reflects 1 points added.
        """
        self.hand.add_card(Card("Ace", "Hearts"))
        self.hand.add_card(Card("10", "Diamonds"))
        ace_inputs = [False]
        self.assertEqual(self.hand.calculate_score(ace_inputs), 11)
    
    def test_calculate_score_multiple_aces(self):
        """
        Test the Ace in a hand is treated as 11 and 1.
            Checks score reflects 11 and 1 points added.
        """
        self.hand.add_card(Card("Ace", "Hearts"))
        self.hand.add_card(Card("Ace", "Spades"))
        self.hand.add_card(Card("9", "Diamonds"))
        ace_inputs = [True, False]  # First Ace is 11, second is 1
        self.assertEqual(self.hand.calculate_score(ace_inputs), 21)

class PlayerTestCase(unittest.TestCase):
    def setUp(self):
        self.player = Player()

    def test_initial_hand_empty(self):
        """"
        Test the hand is empty upon start of round.
        """
        self.assertEqual(len(self.player.hand.cards), 0, "Player's initial hand should be empty.")

    def test_add_cards_to_hand(self):
        """
        Test when you draw cards it is added into the player's hand.
        """
        self.player.hand.add_card(Card("10", "Diamonds"))
        self.player.hand.add_card(Card("5", "Hearts"))
        self.assertEqual(len(self.player.hand.cards), 2, "Player's hand should contain 2 cards.")

class ComputerTestCase(unittest.TestCase):
    def setUp(self):
        self.computer = Computer()

    def test_computer_hits_under_18(self):
        """
        Test computer hits new card if score is under 18
        """
        self.computer.hand.add_card(Card("10", "Diamonds"))
        self.computer.hand.add_card(Card("6", "Spades"))
        deck = Deck()
        self.computer.take_turn(deck)
        self.assertEqual(len(self.computer.hand.cards), 3)

    def test_computer_stands_at_18(self):
        """
        Test computer stops drawing cards at score 18
        """
        self.computer.hand.add_card(Card("10", "Diamonds"))
        self.computer.hand.add_card(Card("8", "Spades"))
        deck = Deck()
        self.computer.take_turn(deck)
        self.assertEqual(len(self.computer.hand.cards), 2)
    
    def test_computer_stands_at_greater_than_18(self):
        """
        Test computer stops drawing cards after score exceeds 18
        """
        self.computer.hand.add_card(Card("10", "Diamonds"))
        self.computer.hand.add_card(Card("10", "Spades"))
        deck = Deck()
        self.computer.take_turn(deck)
        self.assertEqual(len(self.computer.hand.cards), 2)
    
    def test_computer_changes_ace_dynamically(self):
        """
        Test computer does not exceed score of 21 while choosing the values of the aces in the hand
        """
        self.computer.hand.add_card(Card("Ace", "Diamonds"))
        self.computer.hand.add_card(Card("Ace", "Spades"))
        self.computer.hand.add_card(Card("9", "Hearts"))
        deck = Deck()
        self.computer.take_turn(deck)
        # First Ace should be taken as 11 and second ace as 1, otherwise the score exceeds 21
        # The loop breaks at third card because score is now greater than 18
        self.assertEqual(self.computer.score, 21)


if __name__ == 'main':
    unittest.main()
