from src.deck import Deck
from src.hand import Hand
from src.player import Player, Computer


def play():
    print('Welcome to solo blackjack! Get as close to 21 as you can')
    deck = Deck()
    player = Player()

    player.hand.add_card(deck.cards.pop())
    player.hand.add_card(deck.cards.pop())

    player.take_turn(deck)

    print(f"Your Final Score: {player.score}")
    if player.score > 21:
        print("Bust! You lose! \nGame Over")
    elif player.score == 21:
        print("Blackjack! You win!\nGame Over")
    else:
        print("Game Over. Better luck next time!")
    
    play_again(play, play_against_computer)
    

def play_against_computer():
    print('Welcome, you will be competing against a computer!')
    deck = Deck()

    player = Player()
    computer = Computer()

    player.hand.add_card(deck.cards.pop())
    player.hand.add_card(deck.cards.pop())
    computer.hand.add_card(deck.cards.pop())
    computer.hand.add_card(deck.cards.pop())

    player.take_turn(deck)
    computer.take_turn(deck)

    print(f"Your Final Score: {player.score}")
    print(f"Computer's Final Score: {computer.score}")

    if player.score > 21:
        print("You busted! computer wins!")
    elif computer.score > 21:
        print("Computer busted! You win!")
    elif player.score == 21 and computer.score != 21:
        print("Blackjack! You win!")
    elif computer.score == 21 and player.score != 21:
        print("Computer hits Blackjack! computer wins!")
    elif player.score > computer.score:
        print("You win!")
    elif computer.score > player.score:
        print("Computer wins!")
    else:
        print("It's a tie!")

    play_again(play_against_computer)

def play_again(method, switch):
    while True:
        mode = input("Do you want to (1) Play again (2) Switch modes (3) Exit (1/2/3) ")
        if mode == '1':
            method()
            break
        elif mode == '2':
            switch()
            break
        elif mode == '3':
            print('Goodbye!')
            break
        print("Invalid. Please enter '1' or '2' or '3'.")

if __name__ == '__main__':
    print('Blackjack game:')
    while True:
        mode = input("Would you like to (1) Play against computer (2) Play solo? (1/2)")
        if mode == '1':
            play_against_computer()
            break
        elif mode == '2':
            play()
            break
        print("Invalid. Please enter '1' or '2'.")
