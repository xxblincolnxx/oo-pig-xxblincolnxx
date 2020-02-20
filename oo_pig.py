import random

# class Hand:
#   """
#   responsibility: Creates a new hand for a particular player and tracks the score of that hand until "hold" or 1-roll.
#   collaborators: Roll, Game
#   """
#   def __init__(self):
#     self.hand_score = [] 

# class Roll:
#   """
#   responsibility: generate an instance of a dice roll and keeps a score to add to game. 
#   collaborators: Hand, Possible Roll Table
#   """
#   def __init__(self, die_object):
#     self.roll = random.randrange(die.low, die.high, 1) 
# MOVING THE FUNCTIONALITY OF THIS TO A FUNCTION UNDER GAME

class Die:
  """
  responsibility: Determines the number of potential outcomes for a dice roll
  collaborators: Game
  """
  def __init__(self, lowest_value, highest_value):
    self.low = lowest_value
    self.high = highest_value


class Player:
  """
  responsibility: Generates a player that keeps score
  collaborators: Game
  """
  def __init__(self, name):
    self.name = name
    self.score = 0

  # def sum_of_turn (self):
  #   turn_score = 0
  #   for roll in self.rolls_this_turn:
  #     total_score += roll
  #   return turn_score


class Game:
  """
  responsibility: executes game logic, 
  collaborators: Player, Dice
  """
  def __init__(self):
    self.me = Player('me')
    self.yakuza = Player('yakuza')
    self.dice = Die(1, 6)
    self.winner = 'TBD'
    self.play_game()

  # def play_game(self):  
  #   #Include a while loop w/score total < 100

  def roll_dice(self):
      return random.randint(self.dice.low, self.dice.high) 

  def human_take_turn(self):
    """
    """
    turn_score = 0
    playing = 'yes'
    while playing == 'yes':
      cont = input('Djya wanna roll da dice? [yes or no]')
      if cont == 'yes':
        roll = self.roll_dice() 
        if roll != 1: 
          turn_score += roll
          print('score this turn is:'+str(turn_score))
        else:
          print('Welp ya rolled a 1... dummy!')
          turn_score = 0
          playing = 'no'
      else:
        playing = 'no'
    return turn_score

  def bot_take_turn(self):
    """
    """
    turn_score = 0
    playing = 'yes'
    while playing == 'yes':
      input('PRESS ANY KEY')
      cont = self.bot_decides(turn_score)
      if cont == 'yes':
        roll = self.roll_dice() 
        print(f'The crook rolled a {roll}')
        if roll != 1: 
          turn_score += roll
          print(f'oh s***! his score is now: {turn_score}')
        else:
          print('LOLOLOL he gets sweet, sweet nothing')
          turn_score = 0
          playing = 'no'
      else:
        playing = 'no'
    return turn_score
  
  def bot_decides(self, turn_score):
    if turn_score < 6:
      print('Yakuza: You fool. Of course I proceed')
      return 'yes'
    #brave yakuza scenarios
    elif (self.yakuza.score + 20) < self.me.score or self.yakuza.score > (self.me.score + 20) or self.me.score + 10 > 100 or turn_score < 10:
      if random.randint(1, 100) > 20:
        print('Yakuza: You fool! Cowardice is for law-abiding street-rats!')
      else:
        print('Yakuza: I... I do not know what has come over me... I ... must pass.')
        return 'no'
    #cautious yakuza scenarios
    elif abs(self.yakuza.score - self.me.score)<10 or (self.yakuza.score < 50 and self.me.score < 50):
      if random.randint(1, 100) > 90:
        print('Yakuza: A fool? No! I am a warrior!')
        return 'yes'
      else:
        print('Yakuza: Only a fool would... **coughing**')
        return 'no' 
    else:
      print('Yakuza: Today we remove our masks and reveal the true fools! The coin decides!')
      if random.randint(1, 100) > 50:
        print('Yakuza: ... and I... I am brave!')
        return 'yes'
      else:
        print('Yakuza: ...only a cowa **coughing** ...A FOOL WOULD... I... pass.')
        return 'no'

  def play_game (self):
    while self.winner == 'TBD':
      self.me.score += self.human_take_turn()
      if self.me.score >= 100:
        print('You win! Congrats on beating corruption at its own game!')
        self.winner = 'You'
      print(f'*******************Current Scores: Society {self.me.score} / Crooks {self.yakuza.score}*******************')
      self.yakuza.score += self.bot_take_turn()
      if self.yakuza.score >=100:
        print('You let the gangster win... and he has an evil grin on his face...')
        self.winner = 'Yakuza'
      print(f'*******************Current Scores: Society {self.me.score} / Crooks {self.yakuza.score}*******************')
    print('The winner is:'+ self.winner)

Game()