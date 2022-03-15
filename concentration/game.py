from concentration import cards

class Settings:
  jokers = False
  shufflenum = 5
  start_from_last_deck = False
  
  def set_settings(self):
    #gui clde goes here
    
  def __init__(self, ask_user = True):
     if ask_user:
       self.set_settings()
    

def game(self):
    
  #ask user for settings
  settings = Settings()
  deck = Deck()
  table = Table(deck)
  roundnum = 0
  while table.all_matches_found()=False:
   pick_two()
   pick_one, pick_two = show_two()
   update_matched(pick_one, pick_two)
   
