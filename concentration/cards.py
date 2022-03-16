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
    
  def describe(self):
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
         
  def get_unicode(self):
    #in python 3.10 would use case
    if self.name == Suit.spade:
      return '\u2660'
    elif self.name ==  Suit.club:
      return '\u2663'
    elif self.name ==  Suit.heart:
      return '\u2665'
    elif self.name == Suit.diamond:
      return '\u2666'
    else:
      ValueError('Not a valid suit.')
  
  def describe(self):
    self.name, self.value 



class Card:
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
        
  def __init__(self,  
   rank: Rank = None, suit: Suit = None):
      self.rank = rank
      self.suit = suit

def bridge_shuffle(stack: deque, iter = 1, randomize = True):
  if iter < 1:
    return deque
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
  
  def __init__(self, jokers=False, shufflenum = 5):
    self.jokers = jokers
    for suit in Suit.__members__.items():
      for rank in Rank.__members__.items():
        card = Card(rank=rank, suit=suit)
        self.stack.append(card)
 
    self.stack = bridge_shuffle(self.stack, iter = 5)
            
class Table:
  jokers=False
  def get_cardnum(self):
    suit_cards = len(Suit)*len(Rank)
    if self.jokers:
      return suit_cards+2
    else:
      return suit_cards
   
  def get_rownum(self): 
    if self.jokers:
      return 6
    else:
      return 4
      
  def get_colnum(self): 
    return round(self.get_cardnum()/self.get_rownum())
        
  def get_matchnum(self):
    return round(self.get_cardnum()/2)
    
  def __init__(self, deck):
    self.jokers = deck.jokers
    self.table_slots = np.zeros((self.get_rownum(),  self.get_colnum()))
    self.matched_cards = np.zeros(self.get_matchnum())
    for i in range(self.get_rownum()):
      for j in range(self.get_colnum()):
        self.table_slots[i, j] = deck.stack.pop().get_id()

   def all_matches_found(self):
     return self.matched_cards.prod==1
