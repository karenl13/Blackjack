from src.deck import Deck
from src.hand import Hand
from src.player import Player, Computer


def play_solo(player):
    print('Solo mode: Get as close to 21 as you can')
    # Initialise deck and reset player object for new round
    deck = Deck()
    player.hand.reset_hand()
    player.score = 0

    # Add two cards to player's hand
    player.hand.add_card(deck.cards.pop())
    player.hand.add_card(deck.cards.pop())

    # Player plays a round
    player.take_turn(deck)

    # Score determines outcome
    print(f"Your Final Score: {player.score}")
    if player.score > 21:
        print("Bust! You lose! \nGame Over")
        player.games_lost += 1
    elif player.score == 21:
        print("Blackjack! You win!\nGame Over")
        player.games_won += 1
    else:
        print("Close... Game Over.")
    
    # Asks the player to play again
    play_again(player, play_solo, play_against_computer)
    

def play_against_computer(player):
    print('Versus Computer: Beat the computer')

    # Initialise deck and computer and reset player object for new round
    deck = Deck()
    player.hand.reset_hand()
    player.score = 0
    computer = Computer()

    # Add two cards each player's hand  
    player.hand.add_card(deck.cards.pop())
    player.hand.add_card(deck.cards.pop())
    computer.hand.add_card(deck.cards.pop())
    computer.hand.add_card(deck.cards.pop())

    # They sequentially take their turn
    player.take_turn(deck)
    computer.take_turn(deck)

    # Score determines outcome
    print(f"Your Final Score: {player.score}")
    print(f"Computer's Final Score: {computer.score}")
    if player.score > 21 and computer.score > 21:
        print("Both bust, it's a tie!")
    elif player.score > 21:
        print("You busted! Computer wins!")
        player.games_lost += 1
    elif player.score == 21 and computer.score != 21:
        print("Blackjack! You win!")
        player.games_won +=1
    elif computer.score > 21:
        print("Computer busted! You win!")
        player.games_won +=1
    elif computer.score == 21 and player.score != 21:
        print("Computer hits Blackjack! computer wins!")
        player.games_lost +=1
    elif player.score > computer.score:
        print("You win!")
        player.games_won +=1
    elif computer.score > player.score:
        print("Computer wins!")
        player.games_lost +=1
    else:
        print("It's a tie!")

    # Asks the player to play again
    play_again(player, play_against_computer, play_solo)

def play_again(player, method, switch):
    while True:
        mode = input("Do you want to \n(1) Play again (2) Switch modes (3) Exit? \n(1/2/3): ")
        if mode == '1':
            method(player)
            break
        elif mode == '2':
            print((f"Games Won: {player.games_won} | Games Lost: {player.games_lost}"))
            # Create new player object for new game
            new_player = Player()
            switch(new_player)
            break
        elif mode == '3':
            print('Goodbye!')
            # Print final score for player
            print((f"Games Won: {player.games_won} | Games Lost: {player.games_lost}"))
            break
        print("Invalid. Please enter '1' or '2' or '3'.")

if __name__ == '__main__':
    print('Blackjack game:')
    player = Player()
    while True:
        mode = input("Would you like to: \n(1) Play against computer (2) Play solo? \n(1/2):")
        if mode == '1':
            play_against_computer(player)
            break
        elif mode == '2':
            play_solo(player)
            break
        print("Invalid. Please enter '1' or '2'.")
