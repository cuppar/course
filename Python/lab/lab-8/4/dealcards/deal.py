from .pokerdeck import Deck
class Decker:

    def __init__(self):
        self.deck = Deck()
    def deal(self):
        return self.deck.choice()
