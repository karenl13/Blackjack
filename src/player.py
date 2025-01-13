from src.hand import Hand

class Player:
    def __init__(self):
        self.hand = Hand()
        self.score = 0
        self.games_won = 0
        self.games_lost = 0

    def take_turn(self, deck):

        while True:
            print(f"Your hand: {self.hand}")

            # Ask for Ace value choice for each Ace in the hand
            ace_high_values = []
            for card in self.hand.cards:
                if card.value == "Ace":
                    while True:
                        try:
                            user_input = int(input(f"Would you like {card} to be 1 or 11? Enter the number: "))
                            if user_input == 1:
                                ace_high_values.append(False)  # Ace is 1
                                break
                            elif user_input == 11:
                                ace_high_values.append(True)  # Ace is 11
                                break
                            else:
                                print("Invalid choice. Please enter 1 or 11.")
                        except ValueError:
                            print("Invalid input. Please enter a number.")

            self.score = self.hand.calculate_score(ace_high_values)
            print(f"Your score: {self.score}")
            if self.score >= 21:
                break

            # Ask if player wants to hit or stand
            action = input("Do you want to 'hit' or 'stand'? (h/s)")
            if action == 'h':
                self.hand.add_card(deck.cards.pop())
            elif action == 's':
                break
            else:
                print("Invalid input. Please type 'h' or 's'.")

class Computer(Player):
    def take_turn(self, deck):
        while True:
            # Ask for Ace value choice for each Ace in the hand
            ace_high_values = []
            for card in self.hand.cards:
                if card.value == "Ace":
                    if self.score + 11 <= 21:
                        ace_high_values.append(True)  # Ace is 11
                        self.score += 11
                    else:
                        ace_high_values.append(False)  # Ace is 1
            self.score = self.hand.calculate_score(ace_high_values)
            if self.score >= 18:
                break
            else:
                self.hand.add_card(deck.cards.pop())
        


