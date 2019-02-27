# Implement two classes, Card and Deck.
# 1 - Each instance of Card should have a suit ("Hearts", "Diamonds", "Clubs", "Spades")
# 2 - Each instance of Card should have a value ("A"..."K")
# 3 - Card's __repr__ method should display the card's value and suit (e.g. "A" of Clubs)

# 1 - Each instance of Deck should have a cards attribute with all 52 possibile instances of Card.
# 2 - Deck should have and instance method called count which returns a count of how many cards remain in the deck.
# 3 - Deck's _repr__ method should display information on how many cards are in the deck "Deck of 52 cards".
# 4 - Deck should have an instance methoed called _deal which accepts a number and removes at most that many cards from
#     the deck (it may need to remove fewer if you request more cards than are currently in the deck!) If there are no
#     cards left, this method should return a ValueError with the message "All cards have been dealt."
# 5 - Deck should have an instance method called shuffle which will shuffle a full deck of cards. If there are cards
#     missing from the deck, this method should return a ValueError with the message "Only full decks can be shuffled".
# 6 - Deck should have an instance method called deal_card which uses the _deal method to deal a single card from the
#     deck.
# 7 - Deck should have an instance method called deal_hand which accepts a number and uses the _deal method to deal a
#     list of cards from the deck.
import random

class Card:
    def __init__(self, value, suit):
        suits = ("Hearts", "Diamonds", "Clubs", "Spades")
        values = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
        if suit in suits:
            self.suit = suit
        else:
            raise ValueError("Not an acceptable suit")
        if value in values:
            self.value = value
        else:
            raise ValueError("Not an acceptable card")

    def __repr__(self):
        return "{} of {}".format(self.value, self.suit)


class Deck:
    total_cards = 52
    myHand = []

    def __init__(self):
        self.cards = ["A of Hearts", "2 of Hearts", "3 of Hearts", "4 of Hearts",
                      "5 of Hearts", "6 of Hearts", "7 of Hearts", "8 of Hearts",
                      "9 of Hearts", "10 of Hearts", "J of Hearts", "Q of Hearts", "K of Hearts",
                      "A of Spades", "2 of Spades", "3 of Spades", "4 of Spades",
                      "5 of Spades", "6 of Spades", "7 of Spades", "8 of Spades",
                      "9 of Spades", "10 of Spades", "J of Spades", "Q of Spades", "K of Spades",
                      "A of Diamonds", "2 of Diamonds", "3 of Diamonds", "4 of Diamonds",
                      "5 of Diamonds", "6 of Diamonds", "7 of Diamonds", "8 of Diamonds",
                      "9 of Diamonds", "10 of Diamonds", "J of Diamonds", "Q of Diamonds", "K of Diamonds",
                      "A of Clubs", "2 of Clubs", "3 of Clubs", "4 of Clubs",
                      "5 of Clubs", "6 of Clubs", "7 of Clubs", "8 of Clubs",
                      "9 of Clubs", "10 of Clubs", "J of Clubs", "Q of Clubs", "K of Clubs"]
        Deck.total_cards = 52

    def __repr__(self):
        return "Deck of {} cards".format(Deck.total_cards)

    def _deal(self, num):
        cards_dealt = []
        if num <= Deck.total_cards:
            for i in range(0, num):
                new_card = (self.cards.pop())
                cards_dealt.append(new_card)
                Deck.total_cards -= 1
        else:
            raise ValueError("All cards have been dealt")

        Deck.myHand.extend(cards_dealt)
        return cards_dealt

    def count(self):
        return "Deck of {}".format(Deck.total_cards)

    def deal_card(self):
        return self._deal(1)

    def deal_hand(self, num):
        if int(num) > 0:
            return self._deal(num)

    def shuffle(self):
        if Deck.total_cards == 52:
            random.shuffle(self.cards)
        else:
            raise ValueError("Only full decks can be shuffled")


my_deck = Deck()
print(my_deck)
my_deck.shuffle()
card = my_deck.deal_card()
print(card)
hand = my_deck.deal_hand(5)
print(hand)
print(Deck.myHand)
print(my_deck)
