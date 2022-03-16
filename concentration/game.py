from concentration import cards
import string

class Settings:
  jokers = False
  shufflenum = 5
  start_from_last_deck = False
  
  def set_settings(self):
    #gui clde goes here
    
  def __init__(self, ask_user = True):
     if ask_user:
       self.set_settings()
    
def rectangle_mesh(rownum, colnum, spaces=3):
  for _ in range(rownum):
    print(colnum * ('+' + '- ' * spaces) + '+')
    for _ in range(rownum):
      print(colnum * ('|' + '  ' * spaces) + '|')
  print(colnum * ('+' + '- ' * spaces) + '+')

def rectangle_mesh(rownum, colnum, spaces=3):
  print("Concentration Game")
  spaces_1 = ' ' * spaces
  spaces_2 = '  ' * spaces
  letters = list(string.ascii_uppercase)[:colnum]
  column_ids = spaces_2.join(letters) #[s + spaces_2 for s in letters]
  #column_ids[colnum] = letters[
  print(spaces_1 + column_ids + spaces_1)
  for _ in range(rownum):
    print(colnum * ('+' + '- ' * spaces) + '+')
    for _ in range(rownum):
      print(colnum * ('|' + spaces_2) + '|')
  print(colnum * ('+' + '- ' * spaces) + '+')

rectangle_mesh(4, 13)


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
   
