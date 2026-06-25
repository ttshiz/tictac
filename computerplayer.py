import tictac
import random

class ComputerPlayer:
    """ a dedicated AI like system to play a Tic Tic Toe like game  """
    def __init__(self, ttgame):
        self.game = ttgame

    def choose_move(self):
        space = random.randint(0,8) # assuming a 3x3 game for now
        return space
        # For a more intelligent move chooser
        #try choosing the middle location since it has the most options
        # if al ready taken try to block
        # otherwise random