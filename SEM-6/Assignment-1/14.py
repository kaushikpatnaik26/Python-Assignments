from dataclasses import dataclass
import random

@dataclass
class Card:
    rank: str
    suit: str

class Deck:
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    
    def __init__(self):
        self.cards = [Card(rank, suit) for rank in self.ranks for suit in self.suits]
        random.shuffle(self.cards)
    
    def deal(self, num_cards):
        return [self.cards.pop() for _ in range(min(num_cards, len(self.cards)))]
    
    def remaining_cards(self):
        return len(self.cards)
deck = Deck()
player_hand = deck.deal(5)

print("Player's hand:")
for card in player_hand:
    print(f"{card.rank} of {card.suit}")

print("Remaining cards in deck:", deck.remaining_cards())
