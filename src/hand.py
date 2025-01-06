class Hand:
    def __init__(self):
        self.cards = []
    
    def add_card(self, card):
        self.cards.append(card)

    def calculate_score(self, ace_inputs):
        total_score = 0
        ace_index = 0

        for card in self.cards:
            if card.value in ["Jack", "Queen", "King"]:
                total_score += 10
            elif card.value == "Ace":
                total_score += 11 if ace_inputs[ace_index] else 1
                ace_index += 1
            else:
                total_score += int(card.value)

        return total_score
    def __str__(self):
        return ", ".join(str(card) for card in self.cards)

if __name__ == "__main__":
    from deck import Card

    hand = Hand()
    print(f"Hand: {hand}")
    print(f"Score: {hand.calculate_score(ace_inputs=[])}")