class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        values = ["2", "3", "4", "5", "6", "7", "8", "9", "10","Jack", "Queen", "King", "Ace"]
        suits = ["Diamonds", "Clubs", "Hearts", "Spades"]
        self.cards = [Card(value, suit) for value in values for suit in suits]

    
if __name__ == "__main__":
    deck = Deck()
    for card in deck.cards:
        print(card)