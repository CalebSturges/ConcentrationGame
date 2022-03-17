from concentration.cards import Rank, Suit, Card, Deck, Table
import string

class Settings:
  jokers = False
  shufflenum = 5
  start_from_last_deck = False
  
  def set_settings(self):
    pass
    #gui clde goes here
    
  def __init__(self, ask_user = True):
     if ask_user:
       self.set_settings()

def pick_cards():
  card_one = input('For the first card you want to flip give the column letter and row number (highest row is 1) like bingo - e.g. C2, G1, A4:')
  card_two = input('For the second card you want to flip give the column letter and row number:')
  print(card_one.upper())
  return card_one.upper(), card_two.upper()
  
def game():
  #ask user for settings
  settings = Settings()
  deck = Deck()
  table = Table(deck)
  table.display_table()
  roundnum = 0
  while table.all_matches_found()==False:
    roundnum+=1
    pick_one, pick_two = pick_cards()
    card_one = table.get_card(pick_one)
    card_two = table.get_card(pick_two)
    table.display_table(show_cards = (card_one, card_two))
    match = table.update_matched(card_one, card_two)
    if match:
      print('You got a match')
  print('Congrats you have won the game.')
  
