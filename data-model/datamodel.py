import collections 
from random import choice

Card = collections.namedtuple('Card',['rank','suit'])

class Frenchmark:
    ranks = [str(n) for n in range(2,11)]+list('JQKA') # store 2 to A cards

    suits = 'spades diamonds clubs hearts'.split() # 4 type of cards in card

    def __init__(self):
        self.__cards = [Card(rank,suit) for suit in self.suits
                                        for rank in self.ranks
        ] # its store 52 cards with each suits .. its tuple but store as like as dictonary

    def __len__(self):
        return len(self.__cards)

    def __getitem__(self,position): # its automatically call a spacific card for local variable position with suits when we call calss FenchDeck like tuple 
        return self.__cards[position]


if __name__ == '__main__':
    
    deck = Frenchmark()

    print("Random choice: ",choice(deck))

    for c in deck:
        print(c)

    print(Card('Q','hearts') in deck)
                        