
from random import shuffle


class Card:
    """docstring for Cart"""

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return f'{self.value} of {self.suit}'


class Deck:
    def __init__(self):
        suits = ['hearts', 'spades', 'diamonds', 'Clubs']
        values = ['A', '1', '2', '3', '4', '5',
                  '6', '7', '9', '10', 'J', 'Q', 'K']
        self.cards = [Card(value, suit) for suit in suits for value in values]
        # print(self.cards)

    def __repr__(self):
        return f'Deck of {self.count()} cards'

    def count(self):
        return len(self.cards)

    def _deal(self, num):
        card_in = self.count()
        actual = min([card_in, num])
        if not card_in:
            raise ValueError("All card have been dealt with")
        cards = self.cards[-actual:]
        self.cards = self.cards[:-actual]
        return cards

    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(hand_size):
        return self._deal(hand_size)

    def shuffle_deck(self):
        if self.count() < 52:
            raise ValueError('Only full deck can be shuffled')
        shuffle(self.cards)
        return self


d = Deck()
d.shuffle_deck()
print(d._deal(6))
print(d.count())
print(d)
