class Hand:
    def __init__(self):
        self.cards = []
    
    def add_card(self, card):
        self.cards.append(card)

    def calculate_score(self, ace_value = True):
        total_score = 0
        aces = 0

        for card in self.cards:
            if card.value in ["Jack, Queen", "King"]:
                total_score += 10
            elif card.value == "Ace":
                aces +=1
                if ace_value:
                    total_score += 11
                else:
                    total_score += 1
            else:
                total_score += int(card.value)

        return total_score
    def __str__(self):
        return ", ".join(str(card) for card in self.cards)

if __name__ == "__main__":
    from deck import Card

    hand = Hand()
    print(f"Hand: {hand}")
    print(f"Score: {hand.calculate_score(ace_value = True)}")