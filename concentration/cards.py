import random
from enum import Enum
from collections import deque
import numpy as np

class Rank(Enum):
    ace = 1
    two = 2
    three = 3
    four = 4
    five = 5
    six = 6
    seven = 7
    eight = 8
    nine = 9
    ten = 10
    jack = 11
    queen = 12
    king = 13
    
    def describe():
        self.name, self.value

class Suit(Enum):
    spade = 0
    club = 0
    heart = 1
    diamond = 1
    def get_index(self):
       for i in range(len(Suit)):
           if self.name == Suit(i).name:
               return i

class Card:
    def __init__(self, 
    rank: Rank = None, 
    suit: Suit = None):
        self.rank = rank
        self.suit = suit
     
    def get_color(self):
        if self.suit is None:
            return None
        elif self.suit.value == 0:
            return 'black'
        elif self.suit.value == 1:
            return 'red'
        else:
            raise ValueError('Not a valid color.')
            
    def get_id(self):
        return self.suit[1].get_index()*12+self.rank[1].value
        
    def get_match_id():
        return self.suit.value*12+self.rank.value

def bridge_shuffle(stack: deque, iter = 1, randomize = True):
    cut_stack = deque()
    while len(cut_stack) < len(stack):
        cut_stack.append(stack.pop())
        
    new_stack = deque()
    while len(stack)+len(cut_stack):
        if random.uniform(0, len(stack)) > random.uniform(0, len(cut_stack)):
            new_stack.append(stack.pop())
        else:
            new_stack.append(cut_stack.pop())
    
    if iter <= 1:
        return new_stack 
    else:
        return bridge_shuffle(new_stack, iter-1)
 
class Deck:
    stack = deque()
    def len(self):
        return len(self.stack)
    
    def __init__(self, shuffle = True):
        for suit in Suit.__members__.items():
            for rank in Rank.__members__.items():
                card = Card(rank=rank, suit=suit)
                self.stack.append(card)
 
        if shuffle:
             self.stack = bridge_shuffle(self.stack, iter = 5)
            
class Table:
     Jokers = False
     card_num = len(Suit)*len(Rank)
     row_num = 4
     table_slots = np.zeros((row_num, round(card_num/row_num)))
     matched_cards = np.zeros(round(card_num/2))
     
     def __init__(self, deck):
            for i in range(self.row_num):
                for j in range(round(self.card_num/self.row_num)):
                    self.table_slots[i, j] = deck.stack.pop().get_id()
            
deck = Deck()
table = Table(deck)
