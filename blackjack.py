from src.deck import Deck
from src.hand import Hand


def play():
    print('Blackjack game:')
    deck = Deck()
    player_hand = Hand()

    player_hand.add_card(deck.cards.pop())
    player_hand.add_card(deck.cards.pop())

    while True:
        print(f"Your hand: {player_hand}")

        # Ask for Ace value choice for each Ace in the hand
        ace_high_values = []
        for card in player_hand.cards:
            if card.value == "Ace":
                while True:
                    try:
                        user_input = int(input(f"Would you like {card} to be 1 or 11? Enter the number: "))
                        if user_input == 1:
                            ace_high_values.append(False)  # False means Ace treated as 1
                            break
                        elif user_input == 11:
                            ace_high_values.append(True)  # True means Ace treated as 11
                            break
                        else:
                            print("Invalid choice. Please enter 1 or 11.")
                    except ValueError:
                        print("Invalid input. Please enter a number.")

        # Calculate the score based on player choices for Aces
        ace_high = all(ace_high_values)  # Use the collected Ace values
        print(f"Your score: {player_hand.calculate_score(ace_high_values)}")

        # Check if player wants to hit or stand
        action = input("Do you want to 'hit' or 'stand'? ").strip().lower()
        if action == 'hit':
            player_hand.add_card(deck.cards.pop())
        elif action == 'stand':
            print("Final hand:", player_hand)
            print("Final score:", player_hand.calculate_score(ace_high_values))
            break
        else:
            print("Invalid input. Please type 'hit' or 'stand'.")


if __name__ == '__main__':
    play()
