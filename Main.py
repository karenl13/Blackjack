import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QInputDialog
from PyQt5.QtCore import Qt
from src.deck import Deck
from src.hand import Hand


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Blackjack")
        self.setGeometry(100, 100, 700, 400)

        # Initialise game elements
        self.deck = Deck()
        self.player_hand = Hand()
        self.ace_high_values = []

        # Counters for wins and losses
        self.games_won = 0
        self.games_lost = 0

        # Layouts and Widgets
        self.central_widget = QWidget()
        self.layout = QVBoxLayout(self.central_widget)

        # Player's Hand and Score
        self.player_hand_label = QLabel("Your Hand: ")
        self.player_hand_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.player_hand_label)

        self.player_score_label = QLabel("Your Score: 0")
        self.player_score_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.player_score_label)

        # Game Messages
        self.message_label = QLabel("")
        self.message_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.message_label)

        # Buttons
        self.hit_button = QPushButton("Hit")
        self.stand_button = QPushButton("Stand")
        self.play_again_button = QPushButton("Play Again")

        self.hit_button.clicked.connect(self.hit)
        self.stand_button.clicked.connect(self.stand)
        self.play_again_button.clicked.connect(self.play_again)

        self.layout.addWidget(self.hit_button)
        self.layout.addWidget(self.stand_button)
        self.layout.addWidget(self.play_again_button)

        self.setCentralWidget(self.central_widget)

        # Start the game
        self.start_game()

    def start_game(self):
        """Start the game by dealing two cards to the player."""
        self.deck = Deck()
        self.player_hand = Hand()
        self.ace_high_values = []

        # Deal two cards to the player
        self.player_hand.add_card(self.deck.cards.pop())
        self.player_hand.add_card(self.deck.cards.pop())

        self.update_ui()
    
    def play_again(self):
        """Reset the game"""       
        # Reset messages and enable buttons
        self.message_label.setText("")
        self.hit_button.setDisabled(False)
        self.stand_button.setDisabled(False)
        self.start_game()
    
    def choose_ace_value(self, card):
        """The player to choose Ace value (1 or 11) using a dialog."""
        choices = ["1","11"]
        choice, ok = QInputDialog.getItem(
            self, 
            "Choose Ace Value", 
            f"Would you like {card} to be 1 or 11?",
            choices,
        )
        if ok and choice == "11":
            return True # Ace is 11
        else:
            return False # Ace is 1

    def update_ui(self):
        """Update the hand and score display."""
        hand_str = ", ".join(str(card) for card in self.player_hand.cards)
        self.player_hand_label.setText(f"Your Hand: {hand_str}")

        # Loop through all cards in the player's hand to handle Aces
        for card in self.player_hand.cards:
            if card.value == "Ace":
                choice = self.choose_ace_value(card)  # Prompt for each Ace
                self.ace_high_values.append(choice)

        score = self.player_hand.calculate_score(self.ace_high_values)
        self.player_score_label.setText(f"Your Score: {score}")

        if score == 21:
            self.message_label.setText("Blackjack! You win!")
            self.end_game()
        elif score > 21:
            self.message_label.setText("Bust! You lose!")
            self.end_game()

    def hit(self):
        """Add a card to the player's hand."""
        self.player_hand.add_card(self.deck.cards.pop())
        self.ace_high_values = []
        self.update_ui()

    def stand(self):
        """End the player's turn."""
        self.message_label.setText("You win! Game Over.")
        self.end_game()

    def end_game(self):
        """Disable buttons to end the game."""
        self.hit_button.setDisabled(True)
        self.stand_button.setDisabled(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())
