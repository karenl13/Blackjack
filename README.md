## Blackjack Tech Test

Built from the starter code provided for the BBC Software Engineering Graduate Scheme tech test.

### Run this project

- Run the game within the terminal: `python3 blackjack.py`
    #### Modes
    - Solo Mode: Play classic Blackjack, get as close to 21.
    - Computer Mode: Compete against a computer player
    #### Features
    - Change the values of the aces in your hand as you draw new cards
    - Switch modes at your command
    - At the end of the game, see how many games you won and lost.

- Run the game with a graphical interface `python3 Main.py`
    #### Modes
    - Solo mode - logic replicated from terminal version
    #### Features
    - Interactive buttons to 'Hit', 'Stand' and 'Play Again'
    - Displays the statistics of the games won and lost

### Run Unit Tests

- To run all the tests for the project `python3 -m unittest discover test`
    - Testing classes Hand, Deck, Player and Computer

