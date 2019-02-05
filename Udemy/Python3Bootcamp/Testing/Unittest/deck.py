import random

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
        return f"Deck of {Deck.total_cards} cards"

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
        return f"Deck of {Deck.total_cards}"

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
