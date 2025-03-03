import random
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, num_cards):
        return [self.cards.pop() for _ in range(num_cards)] if len(self.cards) >= num_cards else []

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def receive_cards(self, cards):
        self.hand.extend(cards)

    def show_hand(self):
        return f"{self.name}'s Hand: " + ", ".join(str(card) for card in self.hand)

deck = Deck()
deck.shuffle()

players = [Player("Kaushik"), Player("virat kohli"), Player("rohit")]
for player in players:
    player.receive_cards(deck.deal(5))
for player in players:
    print(player.show_hand())
