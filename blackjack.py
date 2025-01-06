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
                            ace_high_values.append(False)  # Ace is 1
                            break
                        elif user_input == 11:
                            ace_high_values.append(True)  # Ace is 11
                            break
                        else:
                            print("Invalid choice. Please enter 1 or 11.")
                    except ValueError:
                        print("Invalid input. Please enter a number.")

        score = player_hand.calculate_score(ace_high_values)
        print(f"Your score: {score}")

        if score == 21:
            print("Blackjack! You win!\nGame Over")
            play_again()
            break
        elif score > 21:
            print("Bust! You lose! \nGame Over")
            play_again()
            break

        # Check if player wants to hit or stand
        action = input("Do you want to 'hit' or 'stand'? ").strip().lower()
        if action == 'hit':
            player_hand.add_card(deck.cards.pop())
        elif action == 'stand':
            print("Final hand:", player_hand)
            print("Final score:", player_hand.calculate_score(ace_high_values))
            play_again()
            break
        else:
            print("Invalid input. Please type 'hit' or 'stand'.")


def play_again():
    play_again = input("Do you want to play again? (y/n): ")
    if play_again != 'y':
        print("Game Over")
    else:
        play()

if __name__ == '__main__':
    play()
