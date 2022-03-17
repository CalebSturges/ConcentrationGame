import random
from math import floor
from enum import Enum
from collections import deque
from string import ascii_uppercase
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

  def get_unicode(self):
     #in python 3.10 would use case      
    if self.value == 1:
      return 'A'
    elif self.value < 11:
      return str(self.value)
    elif self.value == 11:
      return 'J'
    elif self.value == 12:
      return 'Q'
    elif self.value == 13:
      return 'K'
    else:
      ValueError('Not a valid rank')
 
    
  def describe(self):
    self.name, self.value

class Suit(Enum):
  spade = 0
  club = 1
  heart = 2
  diamond = 3
  def get_index(self):
     for i in range(len(list(Suit.__members__))):
       if self.name == list(Suit.__members__)[i]:
         print(i)
         print(self.name)
         return i
   
  def get_unicode(suit):
    #in python 3.10 would use case
    if suit == Suit.spade:
      return '\u2660'
    elif suit ==  Suit.club:
      return '\u2663'
    elif suit ==  Suit.heart:
      return '\u2665'
    elif suit == Suit.diamond:
      return '\u2666'
    else:
      ValueError('Not a valid suit.')

class Card:
  def get_color(self):
     if self.suit is None:
       return None
     elif self.suit.value in (0, 1):
       return 'black'
     elif self.suit.value in (2, 3):
       return 'red'
     else:
        raise ValueError('Not a valid color.')

  def get_id(self):
     return self.suit.get_index()*13+self.rank.value
 
  def get_match_id(self):
      return self.suit.value*12+self.rank.value
      
  def get_table_id(self):
    pass

  def __init__(self,  
   rank: Rank = None, suit: Suit = None, table_index = None):
      self.rank = rank
      self.suit = suit
      self.table_index = table_index

def bridge_shuffle(stack: deque, iter = 1, randomize = True):
  if iter < 1:
    return stack
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
  
  def __init__(self,  jokers=False,  shufflenum=5):
    self.jokers = jokers
    for suit in list(Suit.__members__.items()):
      for rank in list(Rank.__members__.items()):
        card = Card(rank=rank[1], suit=suit[1])
        self.stack.append(card)
 
    self.stack = bridge_shuffle(self.stack, iter = 5)
  

class Table:
  jokers=False
  matched_coordinates = {}
  def get_cardnum(self):
    suit_cards = len(Suit.__members__)*len(Rank)
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
    print((self.get_rownum(),  self.get_colnum()))
    self.table_slots = np.zeros((self.get_rownum(),  self.get_colnum()))
    self.matched_cards = np.zeros(self.get_matchnum())
    for i in range(self.get_rownum()):
      for j in range(self.get_colnum()):
        self.table_slots[i, j] = deck.stack.pop().get_id()

  def all_matches_found(self):
    return self.matched_cards.prod()==1

  def get_card(self,  pick):
    row = int(pick[1:])-1
    col = ascii_uppercase.index(pick[0])
    card_id = self.table_slots[row, col]-1
    rank_id = floor(card_id % 12)
    suit_id = floor(card_id/13)
    rank = Rank(rank_id+1)
    suit = list(Suit)[suit_id]
    return Card(rank=rank, suit=suit, table_index = (row, col))

  def update_matched(self, card_one, card_two):
    match_id = card_one.get_match_id()
    if match_id == card_two.suit.value:
      self.matched_cards[match_id] = 1
      match_string = card_one.suit.get_color() + card_one.rank.name
      self.matched_coordinates.update({match_string: (card_one.table_index, card_two.table_index)})
      return True
    return False
    
  def display_table(self, spaces=3, show_cards=None):
    print('Concentration Game')
    spaces_1 = ' ' * spaces
    spaces_2 = '  ' * spaces
    letters = list(string.ascii_uppercase)[:self.get_colnum()]
    column_ids = spaces_2.join(letters)
    swap_rows = {}
    if show_cards is not None:
      card_one, card_two = show_cards
      for row in range(self.get_rownum()):
        card_one_col = card_one.table_index[1]
        card_two_col = card_two.table_index[1]
        rank_swap = []
        suit_swap = []
        for col in range(self.get_colnum()):
          if card_one.table_index == (row, col):
            rank_swap.append('|' + card_one.rank.get_unicode() + ' '*(spaces*2-1))
            print(Suit.get_unicode(card_one.suit))
            print(card_one.suit)
            suit_swap.append('|' +' '*(spaces-2) + Suit.get_unicode(card_one.suit)+ spaces_1)
          elif card_two.table_index == (row, col):
             print(card_two.rank.get_unicode())
             rank_swap.append('|' + card_two.rank.get_unicode() + ' '*(spaces*2-1))
             print(card_two.suit)
             print(card_two)
             suit_swap.append('|' +' '*(spaces-2) + Suit.get_unicode(card_two.suit) + spaces_1)
          else:
            rank_swap.append('|' + spaces_2)
            suit_swap.append('|' + spaces_2)
                 
        swap_rows.update({str(row)+'_0':''.join(rank_swap)})
        swap_rows.update({str(row)+'_' + str(floor(spaces/2)):''.join(suit_swap)})
   
    print(spaces_1 + column_ids + spaces_1)
    for row in range(self.get_rownum()):
      print(self.get_colnum() * ('+' + '--' * spaces) + '+')
      for s in range(spaces):
        print(swap_rows.get(str(row) +'_' + str(s), self.get_colnum() * ('|' + spaces_2)) + '|')
    print(self.get_colnum() * ('+' + '--' * spaces) + '+')
