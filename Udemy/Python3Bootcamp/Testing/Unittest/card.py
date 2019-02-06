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
        return f"{self.value} of {self.suit}"

# print(Card("A", "Hearts"))
