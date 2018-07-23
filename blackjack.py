from itertools import product
import random
class Deck(object):
    cards = list(product(['A','2','3','4','5','6','7','8','9','10','J','Q','K'],['Spade','Heart','Diamond','Club']))
    def shuffle_cards(self):
        random.shuffle(self.cards)
        print self.cards
class Player(object):
    balance=100

d = Deck() 
d.shuffle_cards()